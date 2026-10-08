#!/usr/bin/env python3
"""Quartus elaboration and Questa batch simulation in disposable project copies."""
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    output = ROOT / 'PROVERA/_build/vendor'
    output.mkdir(parents=True, exist_ok=True)
    proof = []
    versions = {}
    for executable, option in [('quartus_sh', '--version'), ('vsim', '-version')]:
        if shutil.which(executable):
            p = subprocess.run([executable, option], capture_output=True, text=True, timeout=60)
            versions[executable] = (p.stdout + p.stderr).strip()
        else:
            versions[executable] = 'unavailable'
    with tempfile.TemporaryDirectory(prefix='de1-sv-vendor-') as td:
        for i, source in enumerate(sorted(ROOT.glob('[0-9][0-9]/code/**/zadatak.sv'))):
            work = Path(td) / str(i)
            work.mkdir()
            for p in source.parent.iterdir():
                if p.is_file() and p.suffix in ['.sv', '.tcl', '.do']:
                    shutil.copy2(p, work / p.name)
            # Compile commands come from the actual student GUI script.
            commands = [line for line in (work / 'run_tb_gui.do').read_text().splitlines()
                        if line.startswith(('vlib ', 'vmap ', 'vlog '))]
            commands += ['vsim work_sv.tb_zadatak', 'run -all', 'quit -code 0']
            (work / 'batch.do').write_text('onerror {quit -code 1}\n' + '\n'.join(commands) + '\n')
            for engine, command in [('quartus', ['quartus_sh', '-t', 'make_project.tcl']),
                                    ('questa', ['vsim', '-c', '-onfinish', 'stop', '-do', 'batch.do'])]:
                label = str(source.parent.relative_to(ROOT)).replace('/', '_') + '_' + engine
                log = output / (label + '.log')
                try:
                    p = subprocess.run(command, cwd=work, capture_output=True, text=True, timeout=300)
                    text = p.stdout + p.stderr
                    result = 'pass' if p.returncode == 0 and (engine != 'questa' or 'PASS:' in text) else 'fail'
                    if re.search(r'Unable to checkout|license.*(?:not found|fail|error)|cannot find.*license|Unable to check.?out', text, re.I):
                        result = 'license-unavailable'
                except (FileNotFoundError, subprocess.TimeoutExpired) as error:
                    text, result = str(error), 'unavailable'
                log.write_text(text)
                proof.append(dict(path=str(source.parent.relative_to(ROOT)), engine=engine,
                                  result=result, log=str(log.relative_to(ROOT))))
                print(proof[-1], flush=True)
    (ROOT / 'PROVERA/_build/vendor.json').write_text(json.dumps(dict(versions=versions, checks=proof), indent=2) + '\n')
    if any(p['result'] == 'fail' for p in proof):
        raise SystemExit('Vendor HDL checks failed; inspect logs')


if __name__ == '__main__':
    main()
