"""Zajednički I/O za inventar, izgradnju i proveru predavanja."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NS = {"x": "http://www.w3.org/1999/xhtml"}
CATEGORIES = ("tekst", "formule", "tabele", "kod", "crtezi", "citljivost")
CATALOG = [
    ("01", "01 Logicke funkcije.pdf", "01_logicke_funkcije", 19, 37),
    ("02", "02 Sinteza kombinacionih mreza.pdf", "02_sinteza_kombinacionih_mreza", 27, 54),
    ("03", "03 Kola srednjeg stepena integracije.pdf", "03_kola_srednjeg_stepena_integracije", 11, 21),
    ("04", "04 Brojni sistemi.pdf", "04_brojni_sistemi", 20, 39),
    ("05", "05 Aritmeticke operacije.pdf", "05_aritmeticke_operacije", 28, 55),
    ("06", "06 Kodovi.pdf", "06_kodovi", 15, 30),
    ("07", "07 Uvod u HDL.pdf", "07_uvod_u_hdl", 16, 31),
    ("08", "08 Elementi analize logickih kola.pdf", "08_elementi_analize_logickih_kola", 34, 67),
    ("09_1", "09 1 MOS logicka kola.pdf", "09_1_mos_logicka_kola", 29, 57),
    ("09_2", "09 2 MOS logicka kola.pdf", "09_2_mos_logicka_kola", 31, 62),
    ("09_3", "09 3 MOS logicka kola.pdf", "09_3_mos_logicka_kola", 36, 71),
    ("10", "10 Logička kola sa bipolarnim tranzistorima.pdf", "10_logicka_kola_sa_bipolarnim_tranzistorima", 48, 96),
]


def run(args, cwd=None):
    return subprocess.check_output([str(a) for a in args], cwd=cwd, text=True)


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def lectures(selection=""):
    result = [ROOT / row[2] for row in CATALOG if not selection or row[2] == selection]
    if not result:
        raise ValueError(f"Nepoznato predavanje: {selection}")
    return result


def catalog_row(folder):
    return next(row for row in CATALOG if row[2] == Path(folder).name)


def pdf_pages(pdf):
    text = run(["pdfinfo", pdf])
    return int(re.search(r"^Pages:\s+(\d+)", text, re.M).group(1))


def pdf_words(pdf):
    xml = run(["pdftotext", "-bbox-layout", pdf, "-"])
    root = ET.fromstring(xml)
    result = []
    for page in root.findall(".//x:page", NS):
        lines = []
        for line in page.findall(".//x:line", NS):
            words = [dict(text=w.text or "", **{k: float(v) for k, v in w.attrib.items()})
                     for w in line.findall("x:word", NS)]
            lines.append(words)
        result.append({"width": float(page.get("width")),
                       "height": float(page.get("height")), "lines": lines})
    return result


def source_slides(pages):
    """Spoljne oznake slajdova, ne podnožja i ne prisustvo tekstualnog sloja."""
    result = []
    for page_number, page in enumerate(pages, 1):
        if (page["width"], page["height"]) != (540, 720):
            raise ValueError(f"Neočekivana geometrija PDF strane {page_number}")
        for position, marker_y, y0 in (("gornji", 343.9, 68.7), ("donji", 657.1, 381.9)):
            markers = [w["text"] for line in page["lines"] for w in line
                       if abs(w["xMin"] - 30) < .3 and abs(w["yMin"] - marker_y) < 1
                       and w["text"].isdigit()]
            if not markers:
                continue
            if len(markers) != 1:
                raise ValueError(f"Nejednoznačan slajd: strana {page_number}, {position}")
            lines = []
            for line in page["lines"]:
                # Podnožje je ispod y0 + 246; isečak za vizuelni pregled ga zadržava.
                words = [w for w in line if 30 <= w["xMin"] < 510 and y0 <= w["yMin"] < y0 + 246]
                if words:
                    lines.append({"text": " ".join(w["text"] for w in words),
                                  "bbox_pt": [min(w["xMin"] for w in words), min(w["yMin"] for w in words),
                                              max(w["xMax"] for w in words), max(w["yMax"] for w in words)]})
            result.append({"pdf_page": page_number, "position": position,
                           "source_number": int(markers[0]), "bbox_pt": [30, y0, 510, y0 + 270],
                           "source_lines": lines})
    return result


def normalize_text(value):
    # NFC namerno ne menja matematičku tipografiju ni oznake negacije.
    value = unicodedata.normalize("NFC", value)
    for a, b in {"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl"}.items():
        value = value.replace(a, b)
    return " ".join(value.split())


def dependency_digest(folder):
    """Promena bilo kog izvora ili zajedničkog stila traži novu izgradnju."""
    folder = Path(folder)
    files = [p for base in (folder, ROOT / "_zajednicko") for p in base.rglob("*")
             if p.is_file() and "build" not in p.relative_to(base).parts
             and p.suffix in (".tex", ".sty", ".vhd", ".v", ".sv", ".abl", ".jed", ".txt", ".csv", ".dat", ".png", ".jpg", ".pdf")]
    files.append(folder / "provera/mapa.json")
    h = hashlib.sha256()
    for path in sorted(files):
        h.update(str(path.relative_to(ROOT)).encode("utf-8"))
        h.update(path.read_bytes())
    return h.hexdigest()
