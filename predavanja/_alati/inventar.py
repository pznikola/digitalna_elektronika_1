#!/usr/bin/env python3
"""Formira početni inventar; postojeći inventar nikad ne prepisuje."""
import argparse
import re
import unicodedata
from zajednicko import ROOT, CATALOG, CATEGORIES, pdf_words, source_slides, sha256, write_json, read_json


def slug(text):
    text = text.lower().replace("đ", "dj")
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    words = re.sub(r"[^a-z0-9]+", "_", text).strip("_").split("_")
    return "_".join(words[:7])[:65].strip("_") or "sadrzaj_za_pregled"


def initialize():
    for key, pdf_name, name, expected_pages, expected_slides in CATALOG:
        folder = ROOT / name
        pdf = ROOT / pdf_name
        target = folder / "provera/mapa.json"
        if target.exists():
            if read_json(target)["source_sha256"] != sha256(pdf):
                raise ValueError(f"Promenjen original: {pdf_name}")
            print(f"Sačuvan postojeći inventar: {name}")
            continue
        pages = pdf_words(pdf)
        slides = source_slides(pages)
        assert len(pages) == expected_pages, pdf_name
        assert [s["source_number"] for s in slides] == list(range(1, expected_slides + 1)), pdf_name
        for sub in ("slajdovi", "slike/tikz", "slike/izvorne", "tabele", "kodovi", "podaci", "provera"):
            path = folder / sub
            path.mkdir(parents=True, exist_ok=True)
            (path / ".gitkeep").touch()
        for slide in slides:
            n = slide["source_number"]
            sid = f"{key}-s{n:03}"
            text = "\n".join(line["text"] for line in slide["source_lines"])
            hint = slide["source_lines"][0]["text"] if slide["source_lines"] else "slikovni_sadrzaj"
            slide.update(id=sid, frame_label=sid, output_page=n,
                         tex=f"slajdovi/s{n:03}_{slug(hint)}.tex", source_text=text,
                         inventory_confirmed=False,
                         inventory={"tekstualni_sloj": text,
                                    "napomena": "Automatsko izdvajanje; formule, slike, tabele i kod obavezno proveriti na originalu."})
        write_json(target, {"schema_version": 1, "lecture_id": key, "source_pdf": pdf_name,
                            "source_sha256": sha256(pdf), "source_pages": expected_pages,
                            "expected_slides": expected_slides, "slides": slides})
        write_json(folder / "provera/pregled.json", {
            "schema_version": 1,
            "slides": {s["id"]: {"categories": {c: "ceka" for c in CATEGORIES},
                                   "notes": "Rekonstrukcija i pregled nisu završeni.",
                                   "source_render_sha256": None, "new_render_sha256": None}
                       for s in slides}})
        inputs = "\n".join(r"\input{" + s["tex"] + "}" for s in slides)
        (folder / f"{name}.tex").write_text(
            "% Jedan izvorni slajd = jedan frame = jedna PDF strana.\n"
            "\\documentclass[aspectratio=169,11pt]{beamer}\n"
            "\\usepackage{../_zajednicko/stil}\n"
            "\\usepackage{../_zajednicko/dijagrami}\n"
            "\\begin{document}\n" + inputs + "\n\\end{document}\n", encoding="utf-8")
        (folder / "README.md").write_text(
            f"# {name}\n\nIzvor: `../{pdf_name}` ({expected_pages} PDF strana, {expected_slides} slajdova).\n\n"
            "Originalni materijal: Digitalna elektronika 1, 2021/22, Katedra za elektroniku, "
            "prof. dr Lazar Saranovac; oznake su prenete iz originala.\n\n"
            f"Izgradnja: `make -C predavanja LECTURE={name} all` iz korena repozitorijuma.\n\n"
            "`provera/mapa.json` sadrži izvorne lokacije; `provera/pregled.json` stvarni status pregleda. "
            "Inventar nije potvrda da je sadržaj rekonstruisan. Nedostajući `.tex` fajlovi označavaju preostali rad; "
            "nisu zamenjeni praznim slajdovima ili slikama originala.\n", encoding="utf-8")
        (folder / "provera/izvestaj.md").write_text(
            f"# Status prenosa — {key}\n\nInventarisano: {expected_slides} slajdova.\n\n"
            "Rekonstrukcija i vizuelna provera nisu završene. Merodavni statusi su u `pregled.json`.\n",
            encoding="utf-8")
        (folder / "provera/uocene_greske.md").write_text(
            "# Uočene greške originala\n\n"
            "Ovaj izveštaj popunjava se pri sadržinskom pregledu. Prazan izveštaj ne potvrđuje ispravnost originala.\n\n"
            "Za svaki nalaz navesti slajd, originalni zapis, razlog sumnje i predlog ispravke. "
            "Originalni sadržaj ostaje sačuvan u prezentaciji.\n", encoding="utf-8")
        print(f"{name}: {len(slides)} slajdova")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    initialize()
