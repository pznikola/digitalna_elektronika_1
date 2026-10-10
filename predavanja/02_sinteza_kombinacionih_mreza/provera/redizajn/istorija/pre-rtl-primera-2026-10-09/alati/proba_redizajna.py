#!/usr/bin/env python3
"""Integraciona proba na dva izmišljena slajda; nikad ne otvara nastavna predavanja."""
import re
import shutil
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import patch

import izgradnja
import provera
import redizajn as rd
import uporedni_pregled
import zajednicko
from zajednicko import ROOT, read_json, write_json, sha256, pdf_pages


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def run_demo():
    root = Path(__file__).resolve().parent / "build/proba_redizajna"
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True)
    shared = root / "_zajednicko"
    shared.mkdir()
    shutil.copytree(ROOT / "_zajednicko/etf-v1", shared / "etf-v1", ignore=shutil.ignore_patterns("build", "__pycache__"))
    shutil.copy2(ROOT / "_zajednicko/latexmkrc", shared / "latexmkrc")
    folder = root / "demo"
    folder.mkdir()
    (folder / "slajdovi").mkdir()
    # Original ima uobičajenu geometriju dve polovine; ovo nije gradivo predavanja 01.
    original_tex = root / "original.tex"
    original_tex.write_text(r"""\documentclass{article}
\usepackage[paperwidth=540bp,paperheight=720bp,margin=30bp]{geometry}
\usepackage{fontspec}\setmainfont{Latin Modern Sans}
\pagestyle{empty}\begin{document}\noindent
\vspace*{40bp}\par\textbf{DEMO: Logička funkcija}\par
Izlaz je jedan kada su oba ulaza jedan.\par $y=ab$.
\vspace{220bp}\par\textbf{DEMO: Negacija}\par
Izlaz ima suprotnu logičku vrednost.\par $y=\overline{a}$.
\end{document}
""")
    rd.compile_tex(root, original_tex, shared / "latexmkrc")
    shutil.copy2(root / "build/original.pdf", root / "original.pdf")
    preamble = r"""\documentclass[aspectratio=169,11pt]{beamer}
\newcommand{\ETFTemaPutanja}{../_zajednicko/etf-v1}
\makeatletter\edef\input@path{{\ETFTemaPutanja/}}\makeatother
\usepackage{stil,dijagrami}
\ETFPodnozje{Samostalna proba infrastrukture}
\begin{document}
"""
    (folder / "demo.tex").write_text(preamble + "\\input{slajdovi/s001_primer.tex}\n\\input{slajdovi/s002_primer.tex}\n\\end{document}\n")
    # Donja crta namerno proverava ponašanje ID-ja poput 09_1.
    slides = []
    for n, title, formula, explanation in [(1, "Logička funkcija", "y=ab", "Izlaz je jedan kada su oba ulaza jedan."),
                                          (2, "Negacija", r"y=\overline{a}", "Izlaz ima suprotnu logičku vrednost.")]:
        sid = f"DEMO_1-s{n:03}"
        source = f"slajdovi/s{n:03}_primer.tex"
        (folder / source).write_text(r"\slajdid{" + sid + "}\n" + r"\begin{frame}{" + title + "}\n" +
                                    f"% element: {sid}:formula\n\\[{formula}\\]\n" +
                                    f"% element: {sid}:objasnjenje\n{explanation}\n" + r"\end{frame}" + "\n")
        slides.append({"id": sid, "tex": source, "frame_label": sid, "title": title, "source_number": n,
                       "output_page": n, "pdf_page": 1, "position": "gornji" if n == 1 else "donji",
                       "bbox_pt": [30, 68.7 if n == 1 else 381.9, 510, 338.7 if n == 1 else 651.9],
                       "inventory": {"kategorije": ["tekst", "formule"]}, "inventory_confirmed": True})
    data = {"expected_slides": 2, "source_pdf": "original.pdf", "source_sha256": sha256(root / "original.pdf"), "slides": slides}
    write_json(folder / "provera/mapa.json", data)
    legacy_reviews = {"slides": {s["id"]: {"notes": "Istorijski test zapis — ne sme se menjati"} for s in slides}}
    write_json(folder / "provera/pregled.json", legacy_reviews)
    with ExitStack() as stack:
        for module in (zajednicko, izgradnja, provera, uporedni_pregled, rd):
            stack.enter_context(patch.object(module, "ROOT", root))
        stack.enter_context(patch.object(rd, "catalog_row", return_value=("DEMO_1", "original.pdf", "demo", 1, 2)))
        rd.init(folder, "etf-v1", "AUTOMATSKI TEST: izmišljeni primer, nije korisnikovo odobrenje predavanja.")
        inv, cov = {}, {}
        for s in slides:
            sid = s["id"]
            inv[sid] = {"confirmed": True, "elements": []}
            cov[sid] = []
            for key, visible in (("formula", True), ("objasnjenje", False)):
                eid = sid + ":" + key
                inv[sid]["elements"].append({"id": eid, "description": "Demonstraciona " + key,
                                            "source": f"PDF 1, {s['position']}", "origin": "original", "must_remain_visible": visible})
                target = {"path": s["tex"] if visible else f"beleske/s{s['source_number']:03}.tex", "anchor": "% element: " + eid}
                cov[sid].append({"element": eid, "slide": target if visible else None, "notes": None if visible else target,
                                 "change": "Očuvano" if visible else "Premešteno u beleške", "status": "provereno"})
            slide_path = folder / s["tex"]
            content = slide_path.read_text()
            content = re.sub(r"% element: [^\n]+:objasnjenje\n[^\n]+\n", "", content)
            slide_path.write_text(content)
            explanation = "Izlaz je jedan kada su oba ulaza jedan." if s["source_number"] == 1 else "Izlaz ima suprotnu logičku vrednost."
            notes = r"\BeleskeID{" + sid + "}\n" + r"\section*{Objašnjenje iz originala}" + "\n" + f"% element: {sid}:objasnjenje\n{explanation}\n"
            notes += r"\section*{Dopunsko objašnjenje}" + "\nSamostalni primer za proveru beležaka. Ovaj materijal ne pripada nastavnom predavanju.\n"
            if s["source_number"] == 1:
                notes += "\n\\newpage\n\\section*{Nastavak objašnjenja}\nProvera višestraničnih beležaka: ID u zaglavlju ostaje vezan za prvi slajd.\n"
                notes += r"\[ y(1,1)=1,\qquad y(0,1)=0. \]" + "\n"
            (folder / f"beleske/s{s['source_number']:03}.tex").write_text(notes)
        write_json(folder / "provera/redizajn/inventar.json", {"slides": inv})
        write_json(folder / "provera/redizajn/pokrivenost.json", {"slides": cov})
        # Iste javne funkcije koje pozivaju all/review/check otkrivaju novi režim.
        izgradnja.build(folder)
        current = uporedni_pregled.generate(folder)
        require(pdf_pages(folder / "build/demo.pdf") == 2, "Broj slajdova je promenjen")
        require(pdf_pages(folder / "build/demo_beleske.pdf") == 3, "Višestranične beleške nisu povezane")
        errors = provera.check(folder, compile_pdf=False)
        require(any("pregled" in e or "potvrda" in e for e in errors), "Nepregledan materijal je lažno prošao")
        require(not rd.log_errors(folder / "build/demo.pdf"), "Loš prikaz slajdova")
        require(not rd.log_errors(folder / "build/demo_beleske.pdf"), "Loš prikaz beležaka")
        # Test potvrde se čuvaju samo u ignorisanom test folderu i jasno su označene.
        reviews = {s["id"]: {"categories": {k: "provereno" for k in rd.CATS}, "evidence": current[s["id"]],
                               "date": "2026-09-25", "reviewer": "AUTOMATSKI TEST", "notes": "TEST podaci, nisu potvrda nastavnog predavanja."} for s in slides}
        write_json(folder / "provera/redizajn/pregled.json", {"slides": reviews})
        require(provera.check(folder, compile_pdf=False) == [], "Kontrolisani kompletan primer nije prošao")
        note = folder / "beleske/s001.tex"
        saved = note.read_text()
        note.write_text(saved + "% Izmena izvora bez promene izgleda.\n")
        try:
            rd.current_receipt(folder, "demo_beleske")
        except ValueError:
            pass
        else:
            raise AssertionError("Promenjene beleške nisu poništile izgradnju")
        rd.build_notes(folder)
        changed = rd.generate(folder)
        a, b = [s["id"] for s in slides]
        require(changed[a]["notes_render_sha256"] == current[a]["notes_render_sha256"], "Komentar menja prikaz")
        require(rd.review_errors(slides[0], reviews[a], changed[a]), "Izmena samo izvora nije poništila potvrdu")
        require(changed[b] == current[b], "Promena beleške prvog slajda poništila je nepogođeni drugi slajd")
        note.write_text(saved)
        unused = shared / "etf-v2"
        unused.mkdir(); (unused / "stil.sty").write_text("Nekorišćena nova tema")
        rd.build_notes(folder)
        require(rd.generate(folder) == current, "Nekorišćena tema poništila je pregled")
        note.write_text(saved.replace(a, b))
        try:
            rd.notes_entries(folder, read_json(folder / "provera/redizajn/manifest.json"), data)
        except ValueError:
            pass
        else:
            raise AssertionError("Pogrešan ID beležaka nije otkriven")
        note.write_text(saved)
        used = shared / "etf-v1/stil.sty"
        used_bytes = used.read_bytes()
        used.write_bytes(used_bytes + b"\n% changed\n")
        try:
            rd.context(folder)
        except ValueError:
            pass
        else:
            raise AssertionError("Promena korišćene teme nije otkrivena")
        used.write_bytes(used_bytes)
        missing = folder / "build/redizajn/pre/prezentacija.pdf"
        backup = missing.read_bytes(); missing.unlink()
        try:
            rd.generate(folder)
        except ValueError:
            pass
        else:
            raise AssertionError("Nedostajući početni prikaz nije otkriven")
        missing.write_bytes(backup)
        require(provera.check(folder, compile_pdf=False) == [], "Završno stanje provere ne prolazi")
        require(read_json(folder / "provera/pregled.json") == legacy_reviews, "Stare potvrde su promenjene")
        html_text = (folder / "build/redizajn/pregled/index.html").read_text()
        for url in re.findall(r'(?:href|src)="([^"]+)"', html_text):
            require((folder / "build/redizajn/pregled" / url).is_file(), "Neispravan link: " + url)
        write_json(root / "rezultat.json", {"status": "proslo", "slides": 2, "notes_pages": 3,
                   "historical_reviews_unchanged": True, "unreviewed_rejected": True,
                   "notes_source_change_invalidates_only_affected_slide": True,
                   "unused_theme_ignored": True, "used_theme_change_rejected": True,
                   "wrong_notes_id_rejected": True, "missing_baseline_rejected": True,
                   "pdf_sha256": sha256(folder / "build/demo.pdf"), "notes_sha256": sha256(folder / "build/demo_beleske.pdf")})
    print(f"INTEGRACIONA PROBA PROLAZI: {root / 'rezultat.json'}")
    return folder


if __name__ == "__main__":
    run_demo()
