#!/usr/bin/env python3
"""Extract PDF listings verbatim, then simulate the extracted RTL with Icarus."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

from hdl_runtime import ROOT, invoke
from simulacija import simulate


def extract(output):
    records = []
    for n in ['01', '02', '04', '05']:
        main = next((ROOT / n).glob(n + '_*.tex'))
        text = re.sub(r'(?<!\\)%[^\n]*', '', main.read_text())
        paths = re.findall(r'\\inputminted\[[^]]*\]\{systemverilog\}\{([^}]+)\}', text)
        assert paths, ('no listings', n)
        assert len(paths) == len(set(paths)), ('duplicate listing', n)
        results = {}
        for mode in ['-raw', '-layout']:
            copied = subprocess.run(['pdftotext', mode, str(main.with_suffix('.pdf')), '-'],
                                    capture_output=True, text=True, check=True).stdout
            blocks = re.findall(r'module\s+[A-Za-z_]\w*\b.*?endmodule', copied, re.S)
            assert len(blocks) == len(paths), ('extracted listing count', n, mode)
            results[mode] = blocks
        for index, relative in enumerate(paths):
            source = main.parent / relative
            original = source.read_text().rstrip('\n')
            modules = re.findall(r'^module\s+([A-Za-z_]\w*)\b', original, re.M)
            assert len(modules) == 1, ('one complete module per listing', source)
            top = 'tb_' + modules[0]
            assert (source.parent / (top + '.sv')).is_file(), ('missing listing testbench', source, top)
            for mode, blocks in results.items():
                assert blocks[index] == original, ('PDF copy differs from source', source, mode)
            case = output / (n + '_' + str(index))
            case.mkdir(parents=True, exist_ok=True)
            for dependency in source.parent.glob('*.sv'):
                shutil.copy2(dependency, case / dependency.name)
            # The tested design is the PDF text, including indentation and comments.
            extracted = results['-raw'][index] + '\n'
            (case / source.name).write_text(extracted)
            records.append(dict(source=str(source.relative_to(ROOT)), directory=case.name, top=top,
                                raw_exact=True, layout_exact=True,
                                copied_text_sha256=hashlib.sha256(extracted.encode()).hexdigest()))
    (output / 'text.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inside', action='store_true')
    args = parser.parse_args()
    if args.inside:
        output = Path('/out')
        records = json.loads((output / 'text.json').read_text())
        for record in records:
            case = output / record['directory']
            simulate(case, record['top'], case / 'simulation', 'iverilog')
            record['copied_rtl_simulation'] = 'pass'
        (output / 'result.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    else:
        output = ROOT / 'PROVERA/_build/pdf_copy'
        output.mkdir(parents=True, exist_ok=True)
        extract(output)
        invoke(__file__, ['--inside'], output)
        records = json.loads((output / 'result.json').read_text())
        (ROOT / 'PROVERA/_build/pdf_copy.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
        print(f'PDF copy: {len(records)} exact listings (-raw and -layout), extracted RTL simulations passed.')


if __name__ == '__main__':
    main()
