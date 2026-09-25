#!/usr/bin/env python3
"""Strogi kriterijumi prihvatanja: nepotpuno predavanje vraća nenulti izlazni kod."""
import argparse
import re
import subprocess
import sys
from pathlib import Path
from zajednicko import (ROOT, CATEGORIES, lectures, catalog_row, read_json, sha256,
                        pdf_pages, dependency_digest)
from izgradnja import build
from uporedni_pregled import generate


def structure_errors(data, expected, trace=None, page_count=None):
    slides = data["slides"]
    errors = []
    for field in ("id", "tex", "frame_label"):
        values = [s[field] for s in slides]
        if len(values) != len(set(values)):
            errors.append(f"Duplirana vrednost: {field}")
    if len(slides) != expected:
        errors.append(f"Broj slajdova {len(slides)} != {expected}")
    for field in ("source_number", "output_page"):
        if [s[field] for s in slides] != list(range(1, expected + 1)):
            errors.append(f"Nepotpun ili promenjen redosled: {field}")
    locations = [(s["pdf_page"], s["position"]) for s in slides]
    expected_locations = [((n + 1) // 2, "gornji" if n % 2 else "donji") for n in range(1, expected + 1)]
    if locations != expected_locations:
        errors.append("Neispravno mapiranje originalnih strana i položaja")
    if page_count is not None and page_count != expected:
        errors.append(f"PDF ima {page_count}, očekivano {expected} strana")
    if trace is not None and trace != [(s["id"], s["output_page"]) for s in slides]:
        errors.append("Redosled oznaka u kompajliranom PDF-u ne odgovara inventaru")
    return errors


def review_errors(slide, review, current):
    errors = []
    sid = slide["id"]
    if not slide.get("inventory_confirmed"):
        errors.append(f"{sid}: inventar sadržaja nije potvrđen")
    if set(review.get("categories", {})) != set(CATEGORIES):
        errors.append(f"{sid}: nepotpune kategorije pregleda")
    for category, status in review.get("categories", {}).items():
        if status not in ("provereno", "nije_primenljivo"):
            errors.append(f"{sid}/{category}: {status}")
        if category == "citljivost" and status == "nije_primenljivo":
            errors.append(f"{sid}: čitljivost mora biti proverena")
        if category in slide.get("inventory", {}).get("kategorije", []) and status == "nije_primenljivo":
            errors.append(f"{sid}/{category}: sadržaj je u inventaru, pregled je obavezan")
    for key in ("source_render_sha256", "new_render_sha256"):
        if not current.get(key) or review.get(key) != current.get(key):
            errors.append(f"{sid}: nedostaje ili je zastarela potvrda {key}")
    if not review.get("notes", "").strip():
        errors.append(f"{sid}: nedostaje beleška pregleda")
    return errors


def check(folder, compile_pdf=True):
    data = read_json(folder / "provera/mapa.json")
    expected = catalog_row(folder)[4]
    errors = structure_errors(data, expected)
    if sha256(ROOT / data["source_pdf"]) != data["source_sha256"]:
        errors.append("Promenjen originalni PDF")
    main = folder / (folder.name + ".tex")
    main_text = main.read_text(encoding="utf-8")
    includes = re.findall(r"\\input\{(slajdovi/[^}]+)\}", main_text)
    if includes != [s["tex"] for s in data["slides"]]:
        errors.append("Glavni .tex ne uključuje tačan niz slajdova")
    missing = []
    for slide in data["slides"]:
        path = folder / slide["tex"]
        if not path.exists():
            missing.append(slide["id"])
            continue
        content = path.read_text(encoding="utf-8")
        if re.search(r"\\pause\b|allowframebreaks|\\(?:only|uncover|onslide)\s*<|shrink\s*[=,\]]", content):
            errors.append(f"{slide['id']}: zabranjeno deljenje ili smanjivanje slajda")
        if r"\slajdid{" + slide["id"] + "}" not in content:
            errors.append(f"{slide['id']}: nedostaje oznaka za kompilaciju")
    if missing:
        errors.append(f"Nedostaje {len(missing)}/{expected} slajdova: " + ", ".join(missing[:8]))
    if not errors and compile_pdf:
        try:
            build(folder)
        except ValueError as exc:
            errors.append(str(exc))
    logic_check = folder / "kodovi/provera_logike.py"
    if not errors and logic_check.exists():
        result = subprocess.run([sys.executable, str(logic_check)], capture_output=True, text=True)
        if result.returncode:
            errors.append("Računska provera: " + result.stdout + result.stderr)
    pdf = folder / "build" / f"{folder.name}.pdf"
    if not errors and pdf.exists():
        trace_path = pdf.with_suffix(".slide-map.tsv")
        trace = [(p[0], int(p[1])) for line in trace_path.read_text().splitlines() if (p := line.split())]
        errors.extend(structure_errors(data, expected, trace, pdf_pages(pdf)))
        state = read_json(pdf.with_suffix(".state.json"))
        if state["dependencies"] != dependency_digest(folder) or state["pdf_sha256"] != sha256(pdf):
            errors.append("PDF nije izgrađen iz aktuelnih izvora")
        log = pdf.with_suffix(".log").read_text(encoding="utf-8", errors="replace")
        for line in log.splitlines():
            if re.search(r"Overfull \\[hv]box|Missing character:|undefined references|Reference .* undefined", line):
                errors.append(line)
        current = generate(folder)
        reviews = read_json(folder / "provera/pregled.json")["slides"]
        if set(reviews) != {s["id"] for s in data["slides"]}:
            errors.append("Skup oznaka pregleda ne odgovara inventaru")
        for slide in data["slides"]:
            errors.extend(review_errors(slide, reviews.get(slide["id"], {}), current[slide["id"]]))
    elif not errors:
        errors.append("Konačan PDF nije izgrađen")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lecture", default="")
    args = parser.parse_args()
    failures = 0
    for folder in lectures(args.lecture):
        try:
            errors = check(folder)
        except (ValueError, OSError, KeyError) as exc:
            errors = [str(exc)]
        print(f"{folder.name}: {'NEZAVRŠENO' if errors else 'PROVERENO'}")
        for error in errors[:12]:
            print(f"  - {error}")
        if len(errors) > 12:
            print(f"  ... još {len(errors) - 12} nalaza")
        failures += bool(errors)
    sys.exit(1 if failures else 0)
