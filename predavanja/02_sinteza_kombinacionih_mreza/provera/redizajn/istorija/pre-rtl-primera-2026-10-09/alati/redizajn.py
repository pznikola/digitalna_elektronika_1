#!/usr/bin/env python3
"""Beleške i provere redizajna. Nijedna komanda ne daje sadržinsku potvrdu."""
from __future__ import annotations

import argparse
import copy
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from zajednicko import ROOT, CATEGORIES, catalog_row, lectures, read_json, write_json, sha256, pdf_pages, run

TOOLS = Path(__file__).resolve().parent
CATS = (*CATEGORIES, "pokrivenost", "beleske")
FORBIDDEN = re.compile(r"\\pause\b|allowframebreaks|\\(?:only|uncover|onslide|visible|invisible|alt|temporal)\s*<|\bshrink\b|\\(?:begin\{frame\}|item)\s*<")
REFERENCE = re.compile(r"\\(?:input|include|includegraphics|lstinputlisting|verbatiminput|VerbatimInput|pgfplotstableread)(?:\[[^\]]*\])?\{([^{}]+)\}")


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def active(folder):
    path = Path(folder) / "provera/redizajn/manifest.json"
    if not path.exists():
        return False
    if read_json(path).get("phase") != "redizajn":
        raise ValueError(f"Nepoznata faza u {path}; odbijeno vraćanje na stare potvrde.")
    return True


def safe_path(base, relative):
    path = (Path(base) / relative).resolve()
    if not path.is_relative_to(Path(base).resolve()):
        raise ValueError(f"Putanja izlazi iz dozvoljenog foldera: {relative}")
    return path


def tex_source(path):
    return re.sub(r"(?<!\\)%[^\n]*", "", Path(path).read_text(encoding="utf-8"))


def read_trace(path):
    return [(sid, int(page)) for sid, page in (line.split() for line in path.read_text().splitlines() if line.strip())]


def tool_versions():
    return {"lualatex": run(["lualatex", "--version"]).splitlines()[0],
            "latexmk": run(["latexmk", "-v"]).strip(),
            "python": sys.version, "pdfinfo": subprocess.run(
                ["pdfinfo", "-v"], capture_output=True, text=True, check=True).stderr.strip()}


def input_files(folder, fls):
    """Stvarni INPUT-i uključuju pakete i fontove, a ne sve zajedničke teme."""
    folder = Path(folder).resolve()
    files = set()
    for line in Path(fls).read_text().splitlines():
        if not line.startswith("INPUT "):
            continue
        path = (folder / line[6:]).resolve()
        if path.is_relative_to(folder / "build"):
            continue
        if not path.is_file():
            raise ValueError(f"Nedostaje korišćena zavisnost: {path}")
        files.add(path)
    return files


def hashes(paths):
    return {str(p.resolve()): sha256(p) for p in sorted(set(paths))}


def changed_files(record):
    return [name for name, value in record.items() if not Path(name).is_file() or sha256(name) != value]


def validate_catalog(folder, data):
    row = catalog_row(folder)
    ids = [s["id"] for s in data["slides"]]
    if (data["source_pdf"] != row[1] or data["expected_slides"] != row[4]
            or ids != [f"{row[0]}-s{n:03}" for n in range(1, row[4] + 1)]):
        raise ValueError("Original, broj ili stabilni ID-jevi ne odgovaraju katalogu.")
    return row


def presentation_data(folder, original, manifest):
    """Izvorna mapa ostaje neizmenjena; samo evidentirane podele daju nastavke."""
    splits = manifest.get("approved_splits")
    if splits is None:
        return original
    approval = safe_path(folder, splits["approval_path"])
    if not approval.is_file() or sha256(approval) != splits["approval_sha256"]:
        raise ValueError("Nedostaje ili je promenjeno odobrenje podele slajdova.")
    decision = read_json(approval)
    continuations = splits["continuations"]
    source_ids = [s["id"] for s in original["slides"]]
    if (not continuations or not set(continuations).issubset(source_ids)
            or list(continuations) != [sid for sid in source_ids if sid in continuations]
            or decision.get("source_ids") != list(continuations)
            or decision.get("lecture") != manifest["lecture"]
            or decision.get("action") != "split_into_two"
            or not decision.get("user_message", "").strip()):
        raise ValueError("Podele ne odgovaraju izvornim slajdovima i korisnikovoj odluci.")
    data = copy.deepcopy(original)
    data["original_slides"] = copy.deepcopy(original["slides"])
    data["slides"] = []
    for source in original["slides"]:
        data["slides"].append(copy.deepcopy(source))
        if source["id"] in continuations:
            sid = source["id"] + "b"
            path = continuations[source["id"]]
            if (not isinstance(path, str) or not path.startswith("slajdovi/")
                    or Path(path).name != f"s{source['source_number']:03}b_nastavak.tex"):
                raise ValueError(f"{sid}: neispravna putanja nastavka.")
            safe_path(folder, path)
            part = copy.deepcopy(source)
            part.update(id=sid, frame_label=sid, tex=path, split_part=2)
            data["slides"].append(part)
    for page, slide in enumerate(data["slides"], 1):
        slide["output_page"] = page
    data["expected_slides"] = len(data["slides"])
    return data


def presentation_structure_errors(data, trace=None, page_count=None):
    from provera import structure_errors
    if "original_slides" not in data:
        return structure_errors(data, data["expected_slides"], trace, page_count)
    # Ponovljene izvorne lokacije su dozvoljene samo u prethodno potvrđenoj podeli.
    original = dict(data, slides=data["original_slides"])
    errors = structure_errors(original, len(original["slides"]))
    slides = data["slides"]
    for field in ("id", "tex", "frame_label"):
        values = [s[field] for s in slides]
        if len(values) != len(set(values)):
            errors.append(f"Duplirana vrednost: {field}")
    if [s["output_page"] for s in slides] != list(range(1, data["expected_slides"] + 1)):
        errors.append("Nepotpun ili promenjen redosled izlaznih strana.")
    if page_count is not None and page_count != data["expected_slides"]:
        errors.append(f"PDF ima {page_count}, očekivano {data['expected_slides']} strana")
    if trace is not None and trace != [(s["id"], s["output_page"]) for s in slides]:
        errors.append("Redosled oznaka u kompajliranom PDF-u ne odgovara odobrenoj podeli.")
    return errors


def context(folder):
    folder = Path(folder).resolve()
    if not active(folder):
        raise ValueError("Beleške zahtevaju eksplicitan manifest redizajna. Prvo odobrenje početka i init.")
    manifest = read_json(folder / "provera/redizajn/manifest.json")
    data = read_json(folder / "provera/mapa.json")
    row = validate_catalog(folder, data)
    if manifest.get("schema_version") != 1 or manifest.get("selected_style") != "B":
        raise ValueError("Nepodržana šema manifesta ili neusvojen stil.")
    data = presentation_data(folder, data, manifest)
    ids = [s["id"] for s in data["slides"]]
    if ids != manifest["slide_ids"] or manifest["lecture"] != row[0]:
        raise ValueError("Promenjen izvorni niz stabilnih ID-jeva ili broj slajdova.")
    original = safe_path(ROOT, data["source_pdf"])
    if sha256(original) != data["source_sha256"] or data["source_sha256"] != manifest["source_sha256"]:
        raise ValueError("Promenjen originalni PDF.")
    theme = safe_path(ROOT / "_zajednicko", manifest["theme"])
    tm = theme / "manifest.json"
    if sha256(tm) != manifest["theme_manifest_sha256"]:
        raise ValueError("Promenjen manifest korišćene verzije teme; potrebna je evidentirana dorada.")
    for name, value in read_json(tm)["sources"].items():
        path = safe_path(theme, name)
        if not path.is_file() or sha256(path) != value:
            raise ValueError(f"Promenjen ili nedostajući resurs teme: {path}")
    return folder, manifest, data, theme


def closure(folder, start):
    """Statički prepoznatljive lokalne zavisnosti; ostale INPUT-e tretiramo kao zajedničke."""
    folder = Path(folder).resolve()
    result, pending = set(), [Path(start).resolve()]
    while pending:
        path = pending.pop()
        if path in result:
            continue
        if not path.is_file():
            raise ValueError(f"Nedostaje resurs: {path}")
        result.add(path)
        if path.suffix not in (".tex", ".sty"):
            continue
        for name in REFERENCE.findall(tex_source(path)):
            if "\\" in name or "#" in name:
                continue  # dinamički ulazi ostaju u stvarnom .fls spisku
            candidates = [base / (name + ext) for base in (folder, path.parent)
                          for ext in ("", ".tex", ".pdf", ".png", ".jpg", ".csv", ".dat")]
            found = next((p.resolve() for p in candidates if p.is_file()), None)
            if found is None:
                raise ValueError(f"Nedostaje uključeni resurs {name} iz {path}")
            pending.append(found)
    return result


def validate_sources(folder, data):
    errors = presentation_structure_errors(data)
    main = folder / (folder.name + ".tex")
    text = tex_source(main)
    if re.findall(r"\\input\{(slajdovi/[^}]+)\}", text) != [s["tex"] for s in data["slides"]]:
        errors.append("Glavni izvor ne uključuje tačan niz slajdova.")
    for path in closure(folder, main):
        if path.suffix in (".tex", ".sty") and path.is_relative_to(folder) and FORBIDDEN.search(tex_source(path)):
            errors.append(f"Zabranjeno deljenje, overlay ili smanjivanje: {path}")
    for slide in data["slides"]:
        text = tex_source(safe_path(folder, slide["tex"]))
        if re.findall(r"\\slajdid\{([^}]+)\}", text) != [slide["id"]]:
            errors.append(f"{slide['id']}: netačna ili duplirana oznaka izvora.")
        if len(re.findall(r"\\begin\{frame\}", text)) != 1:
            errors.append(f"{slide['id']}: očekivan je tačno jedan frame.")
    if errors:
        raise ValueError("\n".join(errors))


def validate_pdf(folder, data):
    pdf = folder / "build" / f"{folder.name}.pdf"
    errors = presentation_structure_errors(data, read_trace(pdf.with_suffix(".slide-map.tsv")), pdf_pages(pdf))
    if errors:
        raise ValueError("\n".join(errors))
    return pdf


def log_errors(pdf):
    log = pdf.with_suffix(".log").read_text(encoding="utf-8", errors="replace")
    return [line for line in log.splitlines() if re.search(
        r"Overfull \\[hv]box|Missing character:|undefined references|(?:Reference|Citation) .* undefined|Label .* multiply defined|LaTeX Font Warning:|Rerun to get cross-references right|^!", line)]


def compile_tex(folder, main, config):
    output = folder / "build"
    output.mkdir(exist_ok=True)
    env = os.environ.copy()
    env.setdefault("TEXMFVAR", str(output / "texmf-var"))
    env.setdefault("SOURCE_DATE_EPOCH", "1790208000")
    env.setdefault("FORCE_SOURCE_DATE", "1")
    command = ["latexmk", "-r", str(config), "-lualatex", "-recorder", "-outdir=build", main.name]
    state = output / f"{main.stem}.state.json"
    if state.exists():
        old = read_json(state)
        if "inputs" in old and (changed_files(old["inputs"]) or changed_files(old["outputs"])
                                or old["tools"] != tool_versions()):
            # Ne potpisuj stari PDF ako latexmk ne prepozna promenu fonta/alata/config-a.
            command.insert(1, "-g")
    log = output / f"{main.stem}.build.log"
    with log.open("w") as stream:
        result = subprocess.run(command, cwd=folder, env=env, stdout=stream, stderr=subprocess.STDOUT)
    if result.returncode:
        raise ValueError(f"Kompilacija nije uspela: {log}\n" + "\n".join(log.read_text(errors="replace").splitlines()[-25:]))
    return command


def save_receipt(folder, name, command, extra=()):
    pdf = folder / "build" / f"{name}.pdf"
    inputs = input_files(folder, pdf.with_suffix(".fls")) | set(extra)
    inputs |= {folder / "provera/mapa.json", folder / "provera/redizajn/manifest.json"}
    splits = read_json(folder / "provera/redizajn/manifest.json").get("approved_splits")
    if splits:
        inputs.add(safe_path(folder, splits["approval_path"]))
    inputs |= {TOOLS / name for name in ("redizajn.py", "zajednicko.py", "izgradnja.py", "provera.py", "uporedni_pregled.py")}
    inputs |= {p for p in (folder / "kodovi").rglob("*") if p.is_file() and "__pycache__" not in p.parts}
    trace = pdf.with_suffix(".notes-map.tsv" if name.endswith("_beleske") else ".slide-map.tsv")
    record = {"inputs": hashes(inputs), "outputs": hashes([pdf, trace, pdf.with_suffix('.log')]),
              "tools": tool_versions(), "command": command}
    write_json(pdf.with_suffix(".state.json"), record)
    ledger = folder / "provera/redizajn/izgradnja.json"
    records = read_json(ledger) if ledger.exists() else {}
    records[name] = record
    write_json(ledger, records)
    return record


def current_receipt(folder, name):
    record = read_json(folder / "build" / f"{name}.state.json")
    changed = changed_files(record["inputs"]) + changed_files(record["outputs"])
    if changed or record["tools"] != tool_versions():
        raise ValueError("Zastarela izgradnja: " + (", ".join(changed[:3]) or "verzije alata"))
    return record


def build_slides(folder):
    folder, manifest, data, theme = context(folder)
    validate_sources(folder, data)
    command = compile_tex(folder, folder / f"{folder.name}.tex", theme / "latexmkrc")
    pdf = validate_pdf(folder, data)
    inputs = input_files(folder, pdf.with_suffix(".fls"))
    if theme / "stil.sty" not in inputs:
        raise ValueError("Prezentacija ne koristi izabranu verziju teme.")
    alien = [p for p in inputs if p.is_relative_to(ROOT / "_zajednicko") and not p.is_relative_to(theme)]
    if alien:
        raise ValueError("Prezentacija koristi drugu zajedničku temu: " + str(alien[0]))
    save_receipt(folder, folder.name, command, [theme / "manifest.json", theme / "latexmkrc"])
    print(f"PDF redizajna: {pdf}")


def note_path(slide):
    # Slajdovi imaju nazive sNNN_naslov.tex; beleške imaju stabilno ime sNNN.tex.
    suffix = "b" if slide.get("split_part") == 2 else ""
    return f"beleske/s{slide['source_number']:03}{suffix}.tex"


def notes_entries(folder, manifest, data):
    entries = manifest["notes"]
    if list(entries) != [s["id"] for s in data["slides"]]:
        raise ValueError("Pogrešan redosled ili skup ID-jeva beležaka.")
    for slide in data["slides"]:
        sid = slide["id"]
        item = entries[sid]
        expected = note_path(slide)
        if item["path"] != expected:
            raise ValueError(f"{sid}: beleške moraju biti u {expected}")
        text = tex_source(safe_path(folder, expected))
        if re.findall(r"\\BeleskeID\{([^}]+)\}", text) != [sid]:
            raise ValueError(f"{sid}: pogrešan ID beležaka.")
        if FORBIDDEN.search(text):
            raise ValueError(f"{sid}: Beamer overlay u beleškama.")
        if not item["title"].strip():
            raise ValueError(f"{sid}: nedostaje naslov beležaka.")
    if {p.name for p in (folder / "beleske").glob("s*.tex")} != {Path(note_path(s)).name for s in data["slides"]}:
        raise ValueError("Izvori beležaka imaju nedostajući ili suvišan slajd.")
    return entries


def tex_escape(text):
    return "".join({"\\": r"\textbackslash{}", "_": r"\_", "%": r"\%", "&": r"\&", "#": r"\#",
                    "{": r"\{", "}": r"\}", "$": r"\$", "^": r"\textasciicircum{}", "~": r"\textasciitilde{}"}.get(c, c) for c in text)


def notes_document(folder, manifest, data):
    # Preambulum bezbedno ispisuje i ID sa donjom crtom (09_1).
    lines = ["% Generisano: uređuj beleske/sNNN.tex i naslove u manifestu.",
             r"\documentclass[11pt,a4paper]{article}",
             r"\input{" + os.path.relpath(TOOLS / "beleske-v1.tex", folder) + "}",
             r"\newcommand{\BeleskePrezentacija}{build/" + folder.name + ".pdf}",
             r"\begin{document}"]
    for slide in data["slides"]:
        entry = manifest["notes"][slide["id"]]
        lines.append(r"\BeleskaSlajda{" + slide["id"] + "}{" + str(slide["output_page"]) + "}{" + tex_escape(entry["title"]) + "}{" + entry["path"] + "}")
    lines.append(r"\end{document}")
    return "\n".join(lines) + "\n"


def notes_trace_errors(trace, ids, page_count):
    errors = []
    if [p for _, p in trace] != list(range(1, page_count + 1)):
        errors.append("Nepotpun zapis strana beležaka.")
    groups = [sid for i, (sid, _) in enumerate(trace) if i == 0 or sid != trace[i - 1][0]]
    if groups != ids:
        errors.append("Pogrešan ID, redosled ili nekompletni blokovi beležaka.")
    return errors


def build_notes(folder, compile_slides=True):
    folder, manifest, data, theme = context(folder)
    notes_entries(folder, manifest, data)
    if compile_slides:
        build_slides(folder)
    current_receipt(folder, folder.name)
    main = folder / f"{folder.name}_beleske.tex"
    document = notes_document(folder, manifest, data)
    if not main.exists() or main.read_text() != document:
        main.write_text(document, encoding="utf-8")
    command = compile_tex(folder, main, theme / "latexmkrc")
    pdf = folder / "build" / f"{main.stem}.pdf"
    errors = notes_trace_errors(read_trace(pdf.with_suffix(".notes-map.tsv")), manifest["slide_ids"], pdf_pages(pdf))
    if errors:
        raise ValueError("\n".join(errors))
    # Projekcioni PDF je generisani ulaz; eksplicitno ga veži uz PDF beležaka.
    save_receipt(folder, main.stem, command, [folder / "build" / f"{folder.name}.pdf", theme / "latexmkrc"])
    print(f"PDF beležaka: {pdf}")


def baseline(folder, manifest):
    pre = folder / "build/redizajn/pre"
    index = pre / "snapshot.json"
    if not index.exists() or sha256(index) != manifest["baseline_sha256"]:
        raise ValueError("Nedostaje ili je promenjen početni prikaz; ne može se zameniti novim.")
    record = read_json(index)
    for relative, value in record["files"].items():
        path = safe_path(pre, relative)
        if not path.is_file() or sha256(path) != value:
            raise ValueError(f"Nedostaje ili je promenjen početni resurs: {relative}")
    return pre, record


def init(folder, theme_name, decision):
    """Priprema samo izabrano predavanje; radi se tek posle stvarnog odobrenja početka."""
    from izgradnja import build
    from uporedni_pregled import render_pdf
    folder = Path(folder).resolve()
    dest = folder / "provera/redizajn"
    pre = folder / "build/redizajn/pre"
    if dest.exists() or pre.exists() or (folder / "beleske").exists():
        raise ValueError("Redizajn/početni prikaz/beleške već postoje; nastavi postojeće stanje, bez prepisivanja.")
    if not decision.strip():
        raise ValueError("Nedostaje stvarna korisnikova odluka o početku.")
    data = read_json(folder / "provera/mapa.json")
    validate_catalog(folder, data)
    validate_sources(folder, data)
    theme = safe_path(ROOT / "_zajednicko", theme_name)
    theme_hash = sha256(theme / "manifest.json")
    build(folder)
    pdf = validate_pdf(folder, data)
    deps = input_files(folder, pdf.with_suffix(".fls"))
    deps |= {folder / "provera/mapa.json", ROOT / data["source_pdf"], ROOT / "_zajednicko/latexmkrc"}
    # Čuvaj i kod/podatke koji služe računskoj proveri iako ih TeX ne uključuje.
    deps |= {p.resolve() for p in (folder / "kodovi").rglob("*") if p.is_file()}
    pre.mkdir(parents=True)
    shutil.copy2(pdf, pre / "prezentacija.pdf")
    shutil.copy2(pdf.with_suffix(".slide-map.tsv"), pre / "prezentacija.slide-map.tsv")
    for path in deps:
        if path.is_relative_to(ROOT):
            target = pre / "izvori" / path.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
    render_pdf(pre / "prezentacija.pdf", pre / "slajdovi", 1280)
    record = {"created": now(), "dependencies": hashes(deps), "tools": tool_versions(),
              "command": ["make", "-C", "predavanja", "LECTURE=" + folder.name, "all"],
              "files": {str(p.relative_to(pre)): sha256(p) for p in sorted(pre.rglob("*")) if p.is_file()}}
    write_json(pre / "snapshot.json", record)
    manifest = {"schema_version": 1, "phase": "redizajn", "lecture": data["slides"][0]["id"].split("-s")[0],
                "selected_style": "B", "theme": theme_name, "theme_manifest_sha256": theme_hash,
                "source_sha256": data["source_sha256"], "slide_ids": [s["id"] for s in data["slides"]],
                "baseline_sha256": sha256(pre / "snapshot.json"), "created": now(),
                "build_record": "provera/redizajn/izgradnja.json",
                "notes": {s["id"]: {"path": note_path(s), "title": s.get("title") or s["id"]} for s in data["slides"]}}
    write_json(dest / "manifest.json", manifest)
    write_json(dest / "inventar.json", {"slides": {s["id"]: {"confirmed": False, "elements": []} for s in data["slides"]}})
    write_json(dest / "pokrivenost.json", {"slides": {s["id"]: [] for s in data["slides"]}})
    write_json(dest / "pregled.json", {"slides": {s["id"]: {"categories": {k: "ceka" for k in CATS}, "date": "", "reviewer": "", "notes": ""} for s in data["slides"]}})
    (dest / "odluke.md").write_text("# Odluke\n\nDatum evidentiranja: " + now() + "\n\nKorisnikova poruka o početku:\n\n> " + decision.replace("\n", "\n> ") + "\n\nOdobrenje rezultata: nema. Prelazak na sledeće: nije odobren.\n")
    (dest / "izvestaj.md").write_text("# Izveštaj redizajna\n\nStatus: u_radu. Sačuvan početni prikaz; inventar, redizajn i pregledi čekaju.\n\nSledeći korak: pregled originala i popis svakog sadržajnog elementa prema PLAN_PREDAVANJA.md.\n")
    (folder / "beleske").mkdir()
    for sid, item in manifest["notes"].items():
        (folder / item["path"]).write_text(r"\BeleskeID{" + sid + "}\n% Napisati beleške posle analize originala; ovaj fajl nije potvrđen.\n")
    (folder / f"{folder.name}_beleske.tex").write_text(notes_document(folder, manifest, data))
    print(f"Sačuvan početni prikaz i otvorena evidencija: {dest}; nijedna potvrda nije automatski data.")


def coverage_errors(folder, data, inventory, coverage, require_confirmed=True):
    errors = []
    ids = {s["id"] for s in data["slides"]}
    if set(inventory) != ids or set(coverage) != ids:
        errors.append("Skup ID-jeva inventara/pokrivenosti ne odgovara slajdovima.")
    for slide in data["slides"]:
        sid = slide["id"]
        inv = inventory.get(sid, {})
        elements = inv.get("elements", [])
        rows = coverage.get(sid, [])
        if not elements or (require_confirmed and inv.get("confirmed") is not True):
            errors.append(f"{sid}: nedostaje nezavisan, potvrđen inventar redizajna.")
        element_ids = [e["id"] for e in elements]
        row_ids = [r["element"] for r in rows]
        if len(set(element_ids)) != len(element_ids) or len(set(row_ids)) != len(row_ids) or set(row_ids) != set(element_ids):
            errors.append(f"{sid}: izostavljen, dupliran ili nepoznat sadržajni element.")
        lookup = {r["element"]: r for r in rows}
        allowed = {"slide": closure(folder, folder / slide["tex"]),
                   "notes": closure(folder, folder / note_path(slide))}
        for element in elements:
            eid = element["id"]
            row = lookup.get(eid, {})
            if (not eid.startswith(sid + ":") or not element.get("description", "").strip()
                    or not element.get("source", "").strip() or element.get("origin") not in ("original", "postojeca_dopuna", "dopuna")
                    or not isinstance(element.get("must_remain_visible"), bool)):
                errors.append(f"{eid}: nepotpun element inventara.")
            if not row.get("slide") and not row.get("notes"):
                errors.append(f"{eid}: sadržaj nema odredište.")
            if element.get("must_remain_visible") and not row.get("slide"):
                errors.append(f"{eid}: ključni sadržaj mora ostati vidljiv na slajdu.")
            if require_confirmed and row.get("status") != "provereno":
                errors.append(f"{eid}: pokrivenost nije proverena.")
            if not row.get("change", "").strip():
                errors.append(f"{eid}: nedostaje opis promene.")
            for kind in ("slide", "notes"):
                target = row.get(kind)
                if not target:
                    continue
                path = safe_path(folder, target["path"])
                anchor = target.get("anchor", "")
                if path not in allowed[kind] or not anchor or not path.is_file() or anchor not in path.read_text():
                    errors.append(f"{eid}: nepostojeće odredište ili veza sa pogrešnim slajdom/beleškama ({kind}).")
    return errors


def coverage_markdown(folder, data, inventory, coverage):
    def cell(value):
        return str(value).replace("|", "\\|").replace("\n", " ")
    lines = ["# Mapa pokrivenosti", "", "Generisano iz inventar.json i pokrivenost.json; nije automatska potvrda sadržaja.", "",
             "| Element | Original / poreklo | Sadržaj | Slajd | Beleške | Promena / provera |", "|---|---|---|---|---|---|"]
    for slide in data["slides"]:
        rows = {r["element"]: r for r in coverage.get(slide["id"], [])}
        for e in inventory.get(slide["id"], {}).get("elements", []):
            r = rows.get(e["id"], {})
            values = [e["id"], e.get("source", "") + " / " + e.get("origin", ""), e.get("description", ""),
                      r.get("slide") or "—", r.get("notes") or "—", r.get("change", "") + " / " + r.get("status", "ceka")]
            lines.append("| " + " | ".join(cell(v) for v in values) + " |")
    (folder / "provera/redizajn/pokrivenost.md").write_text("\n".join(lines) + "\n")


def review_errors(slide, review, current):
    sid = slide["id"]
    errors = []
    if set(review.get("categories", {})) != set(CATS):
        errors.append(f"{sid}: nepotpune kategorije redizajna.")
    required = {"citljivost", "pokrivenost", "beleske"} | set(slide.get("inventory", {}).get("kategorije", []))
    for category, status in review.get("categories", {}).items():
        if status not in ("provereno", "nije_primenljivo") or (category in required and status != "provereno"):
            errors.append(f"{sid}/{category}: pregled nije potvrđen.")
    for key, value in current.items():
        if not value or review.get("evidence", {}).get(key) != value:
            errors.append(f"{sid}: zastarela ili nedostajuća potvrda {key}.")
    for key in ("date", "reviewer", "notes"):
        if not review.get(key, "").strip():
            errors.append(f"{sid}: nedostaje {key} pregleda.")
    return errors


def generate(folder):
    from uporedni_pregled import render_pdf
    from PIL import Image
    folder, manifest, data, theme = context(folder)
    notes_entries(folder, manifest, data)
    presentation = current_receipt(folder, folder.name)
    notes_record = current_receipt(folder, folder.name + "_beleske")
    pdf = validate_pdf(folder, data)
    notes_pdf = folder / "build" / f"{folder.name}_beleske.pdf"
    trace = read_trace(notes_pdf.with_suffix(".notes-map.tsv"))
    problems = notes_trace_errors(trace, manifest["slide_ids"], pdf_pages(notes_pdf))
    if problems:
        raise ValueError("\n".join(problems))
    pre, _ = baseline(folder, manifest)
    if read_trace(pre / "prezentacija.slide-map.tsv") != [(s["id"], s["output_page"]) for s in data.get("original_slides", data["slides"])]:
        raise ValueError("Početni prikaz ne odgovara stabilnim ID-jevima.")
    dest = folder / "build/redizajn/pregled"
    dest.mkdir(parents=True, exist_ok=True)
    original = render_pdf(ROOT / data["source_pdf"], dest / "pdf_strane", 1440)
    before = render_pdf(pre / "prezentacija.pdf", dest / "pre", 1280)
    after = render_pdf(pdf, dest / "novi", 1280)
    notes_images = render_pdf(notes_pdf, dest / "beleske", 1280)
    (dest / "original").mkdir(exist_ok=True)
    inventory = read_json(folder / "provera/redizajn/inventar.json")["slides"]
    coverage = read_json(folder / "provera/redizajn/pokrivenost.json")["slides"]
    coverage_markdown(folder, data, inventory, coverage)
    slide_deps = {s["id"]: closure(folder, folder / s["tex"]) for s in data["slides"]}
    note_deps = {s["id"]: closure(folder, folder / manifest["notes"][s["id"]]["path"]) for s in data["slides"]}
    all_local = set().union(*slide_deps.values(), *note_deps.values())
    common = {Path(p) for record in (presentation, notes_record) for p in record["inputs"]} - all_local
    # Celovita mapa/manifest/generisani dokument/PDF ne poništavaju nepogođene slajdove.
    common -= {folder / "provera/mapa.json", folder / "provera/redizajn/manifest.json",
               folder / f"{folder.name}_beleske.tex", pdf}
    shared = digest({"inputs": hashes(common), "tools": presentation["tools"], "theme": manifest["theme_manifest_sha256"]})
    evidence, cards = {}, []
    def img(path, label):
        relative = html.escape(str(path.relative_to(dest)), quote=True)
        return f'<figure><figcaption>{html.escape(label)}</figcaption><a href="{relative}"><img loading="lazy" src="{relative}" alt="{html.escape(label)}"></a></figure>'
    for slide in data["slides"]:
        sid, page = slide["id"], slide["output_page"]
        baseline_page = slide["source_number"]
        source = dest / "original" / f"{sid}.png"
        with Image.open(original[slide["pdf_page"] - 1]) as image:
            factor = image.width / 540
            image.crop(tuple(round(v * factor) for v in slide["bbox_pt"])).save(source)
        note_pages = [p for key, p in trace if key == sid]
        rendered_notes = [notes_images[p - 1] for p in note_pages]
        evidence[sid] = {
            "source_render_sha256": sha256(source), "baseline_render_sha256": sha256(before[baseline_page - 1]),
            "new_render_sha256": sha256(after[page - 1]), "notes_render_sha256": digest([sha256(p) for p in rendered_notes]),
            "slide_sources_sha256": digest(hashes(slide_deps[sid])), "notes_sources_sha256": digest(hashes(note_deps[sid])),
            "shared_sha256": shared, "mapping_sha256": digest({"slide": slide, "notes": manifest["notes"][sid]}),
            "coverage_sha256": digest({"inventory": inventory.get(sid), "coverage": coverage.get(sid)})}
        cards.append(f'<section id="{sid}"><h2>{sid}</h2><div class="grid">' + img(source, "Original") +
                     img(before[baseline_page - 1], "Pre redizajna") + img(after[page - 1], "Novi slajd") + '</div><details open><summary>Beleške istog slajda</summary><div class="notes">' +
                     "".join(img(p, f"{sid} — beleške, strana {n}") for n, p in zip(note_pages, rendered_notes)) + '</div></details></section>')
    write_json(dest / "otisci.json", evidence)
    (dest / "index.html").write_text('''<!doctype html><html lang="sr-Latn"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Pregled redizajna i beležaka</title>
<style>body{font:16px system-ui;margin:24px;background:#f3f5f8;color:#202b36}section{background:white;padding:16px;margin:24px 0}figure{margin:0}figcaption{margin:8px 0}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}img{width:100%;border:1px solid #ddd}.notes{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;max-width:1000px}summary{padding:16px 0;cursor:pointer}@media(max-width:900px){.grid,.notes{grid-template-columns:1fr}}</style>
<h1>Original / pre redizajna / novi slajd / beleške</h1>
<p>Pregledati svaki slajd, šemu i sve strane beležaka. Klik otvara punu veličinu. Ovaj pregled ne daje automatsku potvrdu.</p>
<p><a href="../../''' + folder.name + '.pdf">Prezentacija</a> · <a href="../../' + folder.name + '_beleske.pdf">Beleške PDF</a></p>' + "\n".join(cards) + '</html>\n', encoding="utf-8")
    print(f"Pregled redizajna: {dest / 'index.html'}")
    return evidence


def check(folder, compile_pdf=True):
    folder, manifest, data, _ = context(folder)
    validate_sources(folder, data)
    notes_entries(folder, manifest, data)
    if compile_pdf:
        build_notes(folder)
    current = generate(folder)
    inventory = read_json(folder / "provera/redizajn/inventar.json")["slides"]
    coverage = read_json(folder / "provera/redizajn/pokrivenost.json")["slides"]
    errors = coverage_errors(folder, data, inventory, coverage)
    reviews = read_json(folder / "provera/redizajn/pregled.json")["slides"]
    if set(reviews) != set(manifest["slide_ids"]):
        errors.append("Nove potvrde ne sadrže tačan skup ID-jeva.")
    for slide in data["slides"]:
        errors.extend(review_errors(slide, reviews.get(slide["id"], {}), current[slide["id"]]))
    for name in (folder.name, folder.name + "_beleske"):
        errors.extend(log_errors(folder / "build" / f"{name}.pdf"))
    logic = folder / "kodovi/provera_logike.py"
    if logic.exists():
        result = subprocess.run([sys.executable, str(logic)], cwd=folder, capture_output=True, text=True)
        if result.returncode:
            errors.append("Računska provera: " + result.stdout + result.stderr)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("notes", "init"))
    parser.add_argument("--lecture", required=True)
    parser.add_argument("--theme", default="etf-v1")
    parser.add_argument("--decision-file", type=Path, help="UTF-8 fajl sa stvarnom porukom koja odobrava početak")
    args = parser.parse_args()
    if not args.lecture.strip():
        parser.error("Obavezan je izbor jednog predavanja.")
    try:
        folder, = lectures(args.lecture)
        if args.action == "init":
            if not args.decision_file:
                parser.error("init zahteva --decision-file sa stvarnim odobrenjem početka.")
            init(folder, args.theme, args.decision_file.read_text())
        else:
            build_notes(folder)
    except (ValueError, OSError, KeyError, subprocess.SubprocessError) as exc:
        print(exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
