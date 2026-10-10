#!/usr/bin/env python3
"""Freeze the originals and test that the nineteen new benches detect bad designs."""
import argparse
import json
from pathlib import Path
import re
import shutil
import tempfile

from hdl_runtime import ROOT, invoke
from simulacija import simulate
from zadatak4_check import original_source_sha


def inventory():
    frozen = json.loads((ROOT / 'PROVERA/dokazi/dopuna_originals.json').read_text())
    for group in ['vhdl', 'existing_sv']:
        for name, expected in frozen[group].items():
            assert original_source_sha(name) == expected, ('changed original', name)
    # Task 02/4 was frozen during that earlier addition. Its historical hash
    # remains in dopuna_originals.json; zadatak4_check.py checks the new scope.
    assert len(frozen['new_examples']) == 19
    for name in frozen['new_examples']:
        folder = ROOT / name
        for file in ['zadatak.sv', 'tb_zadatak.sv', 'Makefile']:
            assert (folder / file).is_file(), ('incomplete example', name, file)
        for rtl in folder.glob('*.sv'):
            if not rtl.name.startswith('tb_'):
                assert not re.search(r'\b(timeunit|timeprecision)\b|`timescale', rtl.read_text()), ('RTL timing declaration', rtl)
        make = (folder / 'Makefile').read_text()
        relative = re.search(r'^PROVERA := (.*)$', make, re.M)[1]
        assert (folder / relative).resolve() == ROOT / 'PROVERA', ('wrong Make helper path', name)
    return frozen


def negative(output):
    cases = [
        ('01/code/Zadatak_1/c', '~(I4 & I5)', '(I4 & I5)', 'NI output polarity'),
        ('02/code/Zadatak_3/d/and', 'Y[8*i+j]', 'Y[8*j+i]', '6/64 output index'),
        ('04/code/Samostalni/Zadatak_3/b', 'Z[4] | G2', 'G2', 'maximum high bit'),
        ('04/code/Samostalni/Zadatak_4/b_y', '{6{E_n}} & T', 'T', 'equal operands mask'),
        ('05/code/BCD_sabirac', 'C_out = K', 'C_out = Z[4]', 'decimal carry'),
        ('05/code/Parnost', 'PARNA = {D, P}', 'PARNA = {P, D}', 'parity bit placement'),
        ('05/code/Haming/korektor', 'R[1] ^ R[3] ^ R[5] ^ R[7]', 'R[1] ^ R[3] ^ R[6] ^ R[7]', 'syndrome group'),
    ]
    results = []
    with tempfile.TemporaryDirectory(prefix='de1-dopuna-negative-') as td:
        work = Path(td)
        for index, (relative, old, new, label) in enumerate(cases):
            folder = work / str(index)
            shutil.copytree(ROOT / relative, folder, ignore=shutil.ignore_patterns('.build'))
            rtl = folder / 'zadatak.sv'
            text = rtl.read_text()
            assert text.count(old) == 1, (label, 'mutation no longer matches')
            rtl.write_text(text.replace(old, new))
            try:
                simulate(folder, 'tb_zadatak', folder / 'simulation', 'iverilog', True)
            except RuntimeError as exc:
                assert 'FATAL:' in str(exc), (label, 'failure was not a testbench assertion', str(exc))
            else:
                raise AssertionError((label, 'testbench accepted the wrong design'))
            results.append(dict(example=relative, mutation=label, detected=True))
    Path(output).write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
    print(f'Dopuna negative: {len(results)} wrong designs rejected.', flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inside', action='store_true')
    args = parser.parse_args()
    frozen = inventory()
    if args.inside:
        negative('/out/dopuna_negative.json')
    else:
        invoke(__file__, ['--inside'], ROOT / 'PROVERA/_build')
        print(f'Dopuna inventory: 19 examples; {len(frozen["vhdl"])} VHDL and '
              f'{len(frozen["existing_sv"])} previous SV programs preserved '
              '(three historical comments removed).')


if __name__ == '__main__':
    main()
