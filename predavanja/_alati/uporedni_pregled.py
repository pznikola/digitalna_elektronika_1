#!/usr/bin/env python3
"""Renderuje originalne i nove slajdove; nikad ne potvrđuje sadržaj automatski."""
import argparse
import difflib
import html
import subprocess
from pathlib import Path
from PIL import Image
from zajednicko import ROOT, lectures, read_json, write_json, sha256, normalize_text, run, pdf_pages

RENDER_VERSION = 1


def render_pdf(pdf, output, width):
    output.mkdir(parents=True, exist_ok=True)
    stamp = output / "render.json"
    expected = {"sha256": sha256(pdf), "width": width, "version": RENDER_VERSION, "pages": pdf_pages(pdf)}
    cached = read_json(stamp) if stamp.exists() else {}
    if all(cached.get(k) == v for k, v in expected.items()):
        images = sorted(output.glob("p-*.png"), key=lambda p: int(p.stem.split("-")[-1]))
        if (len(images) == expected["pages"]
                and [int(p.stem.split("-")[-1]) for p in images] == list(range(1, expected["pages"] + 1))
                and cached.get("images") == {p.name: sha256(p) for p in images}):
            return images
    for path in output.glob("p-*.png"):
        path.unlink()
    subprocess.run(["pdftoppm", "-png", "-scale-to-x", str(width), "-scale-to-y", "-1",
                    str(pdf), str(output / "p")], check=True, stdout=subprocess.DEVNULL)
    images = sorted(output.glob("p-*.png"), key=lambda p: int(p.stem.split("-")[-1]))
    if len(images) != expected["pages"]:
        raise ValueError(f"Nepotpun prikaz PDF-a: {pdf}")
    write_json(stamp, dict(expected, images={p.name: sha256(p) for p in images}))
    return images


def compiled_map(folder, name):
    path = folder / "build" / f"{name}.slide-map.tsv"
    if not path.exists():
        return {}
    pairs = [line.split() for line in path.read_text().splitlines() if line.strip()]
    return {sid: int(page) for sid, page in pairs}


def generate(folder):
    data = read_json(folder / "provera/mapa.json")
    original = ROOT / data["source_pdf"]
    if sha256(original) != data["source_sha256"]:
        raise ValueError(f"Promenjen original: {original}")
    dest = folder / "build/pregled"
    dest.mkdir(parents=True, exist_ok=True)
    pages = render_pdf(original, dest / "pdf_strane", 1440)
    old_dir = dest / "original"
    old_dir.mkdir(exist_ok=True)
    for slide in data["slides"]:
        target = old_dir / f"{slide['id']}.png"
        with Image.open(pages[slide["pdf_page"] - 1]) as page:
            factor = page.width / 540
            box = tuple(round(v * factor) for v in slide["bbox_pt"])
            page.crop(box).save(target)
    full = folder / "build" / f"{folder.name}.pdf"
    draft = folder / "build/radni_pregled.pdf"
    pdf = full if full.exists() else draft if draft.exists() else None
    new_images, output_map, new_text = [], {}, []
    if pdf:
        new_images = render_pdf(pdf, dest / "novi", 1280)
        output_map = compiled_map(folder, pdf.stem)
        new_text = run(["pdftotext", "-layout", pdf, "-"]).split("\f")
    hashes, cards = {}, []
    for slide in data["slides"]:
        sid = slide["id"]
        new_page = output_map.get(sid)
        new_path = new_images[new_page - 1] if new_page and new_page <= len(new_images) else None
        old_path = old_dir / f"{sid}.png"
        hashes[sid] = {"source_render_sha256": sha256(old_path),
                       "new_render_sha256": sha256(new_path) if new_path else None}
        new_img = (f'<a href="{new_path.relative_to(dest)}"><img loading="lazy" src="{new_path.relative_to(dest)}" alt="Novi {sid}"></a>'
                   if new_path else '<p class="missing">Slajd još nije rekonstruisan.</p>')
        source_text = normalize_text(slide["source_text"])
        target_text = ""
        if new_page and new_page <= len(new_text):
            lines = new_text[new_page - 1].strip().splitlines()
            if lines and lines[-1].strip() == str(slide["source_number"]):
                lines.pop()
            target_text = normalize_text("\n".join(lines))
        diff = "\n".join(difflib.unified_diff(source_text.split(), target_text.split(),
                                             fromfile="original", tofile="novi", lineterm=""))
        cards.append(f'''<section id="{sid}"><h2>{sid} — PDF strana {slide['pdf_page']}, {slide['position']}</h2>
<p><code>{html.escape(slide['tex'])}</code></p><div class="pair">
<a href="original/{sid}.png"><img loading="lazy" src="original/{sid}.png" alt="Original {sid}"></a>{new_img}</div>
<details><summary>Tekstualne razlike — pomoć pri pregledu, nisu automatska ocena</summary><pre>{html.escape(diff)}</pre></details></section>''')
    write_json(dest / "otisci.json", hashes)
    (dest / "index.html").write_text('''<!doctype html><html lang="sr-Latn"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Provera prenosa</title>
<style>body{font:16px system-ui;margin:24px;background:#f3f5f8;color:#182536}section{background:white;padding:16px;margin:24px 0}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:16px}.pair img{width:100%;border:1px solid #ccc}pre{white-space:pre-wrap}
.missing{color:#af3447}h1,h2{color:#194f78}@media(max-width:900px){.pair{grid-template-columns:1fr}}</style>
<h1>Original / nova prezentacija</h1><p>Pregledati svaki slajd. Klik na sliku otvara punu veličinu.
Ovaj dokument ne potvrđuje vernost prenosa. Radni prikaz može sadržati samo deo prezentacije.</p>'''
                                               + "\n".join(cards) + "</html>\n", encoding="utf-8")
    print(f"Pregled: {dest / 'index.html'}")
    return hashes


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lecture", default="")
    args = parser.parse_args()
    for folder in lectures(args.lecture):
        generate(folder)
