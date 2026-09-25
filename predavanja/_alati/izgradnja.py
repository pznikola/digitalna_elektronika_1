#!/usr/bin/env python3
"""Izgradnja kompletnog PDF-a; nezavršena predavanja ne dobijaju lažan konačan PDF."""
import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path
from zajednicko import ROOT, lectures, read_json, write_json, dependency_digest, sha256


def build(folder, preview=False):
    folder = Path(folder)
    data = read_json(folder / "provera/mapa.json")
    if sha256(ROOT / data["source_pdf"]) != data["source_sha256"]:
        raise ValueError(f"Original je promenjen: {data['source_pdf']}")
    missing = [s for s in data["slides"] if not (folder / s["tex"]).is_file()]
    output = folder / "build"
    output.mkdir(exist_ok=True)
    main = folder.name + ".tex"
    name = folder.name
    if preview:
        ready = [s for s in data["slides"] if (folder / s["tex"]).is_file()]
        if not ready:
            raise ValueError(f"{folder.name}: nijedan slajd još nije rekonstruisan")
        name = "radni_pregled"
        main = "build/radni_pregled.tex"
        source = (folder / (folder.name + ".tex")).read_text(encoding="utf-8")
        preamble, marker, _ = source.partition(r"\begin{document}")
        if not marker:
            raise ValueError(f"Nedostaje početak dokumenta: {folder.name}.tex")
        content = [preamble, marker]
        for s in ready:
            content.extend([r"\setcounter{framenumber}{" + str(s["source_number"] - 1) + "}",
                            r"\input{" + s["tex"] + "}"])
        content.append(r"\end{document}")
        (folder / main).write_text("\n".join(content) + "\n", encoding="utf-8")
    elif missing:
        raise ValueError(f"{folder.name}: nedostaje {len(missing)}/{data['expected_slides']} slajdova; "
                         f"prvi: {missing[0]['tex']}. Za radni prikaz postoji make preview.")
    env = os.environ.copy()
    env.setdefault("TEXMFVAR", str(output / "texmf-var"))
    env.setdefault("SOURCE_DATE_EPOCH", "1790208000")
    env.setdefault("FORCE_SOURCE_DATE", "1")
    command = ["latexmk", "-r", "../_zajednicko/latexmkrc", "-lualatex", "-outdir=build", main]
    log = output / f"{name}.build.log"
    with log.open("w", encoding="utf-8") as stream:
        result = subprocess.run(command, cwd=folder, env=env, stdout=stream, stderr=subprocess.STDOUT)
    if result.returncode:
        tail = "\n".join(log.read_text(encoding="utf-8", errors="replace").splitlines()[-28:])
        raise ValueError(f"Kompilacija nije uspela: {log}\n{tail}")
    write_json(output / f"{name}.state.json", {"dependencies": dependency_digest(folder),
                                              "pdf_sha256": sha256(output / f"{name}.pdf"),
                                              "preview": preview})
    print(f"{'RADNI PREGLED' if preview else 'PDF'}: {output / (name + '.pdf')}")


def clean(folder):
    path = Path(folder) / "build"
    if path.is_symlink():
        raise ValueError(f"Odbijeno čišćenje simboličkog linka: {path}")
    if path.exists():
        shutil.rmtree(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lecture", default="")
    parser.add_argument("--preview", action="store_true")
    parser.add_argument("--clean", action="store_true")
    args = parser.parse_args()
    failed = False
    try:
        folders = lectures(args.lecture)
    except ValueError as exc:
        parser.error(str(exc))
    for folder in folders:
        try:
            clean(folder) if args.clean else build(folder, args.preview)
        except (ValueError, OSError, subprocess.SubprocessError) as exc:
            print(exc, file=sys.stderr)
            failed = True
    sys.exit(1 if failed else 0)
