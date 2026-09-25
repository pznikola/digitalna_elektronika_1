#!/usr/bin/env python3
"""Exercise inventory identity and invalidation in an isolated synthetic fixture.

Fixture attestations are test data, never human approval of working documents.
No working source, PDF or human review record is changed.
"""
import contextlib
import io
import json
import shutil
import tempfile
from pathlib import Path

import audit


def main():
    root, here, exercises = audit.ROOT, audit.HERE, audit.EXERCISES
    results = []
    with tempfile.TemporaryDirectory(prefix='de1-registry-fixture-') as temp:
        fixture = Path(temp)
        paths = set(audit.dependencies('03')) | set(audit.evidence_dependencies('03'))
        main_source = next((root / '03').glob('*.tex'))
        for suffix in ['.pdf', '.synctex.gz']:
            paths.add(str(main_source.with_suffix(suffix).relative_to(root)))
        paths.add('PROVERA/registar.json')
        for relative in paths:
            target = fixture / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / relative, target)
        audit.ROOT, audit.HERE, audit.EXERCISES = fixture, fixture / 'PROVERA', ['03']
        try:
            pdf = fixture / main_source.relative_to(root).with_suffix('.pdf')
            # Synthetic baseline: this only tests the decision mechanism.
            import re
            import subprocess
            info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True, check=True).stdout
            count = int(re.search(r'Pages:\s*(\d+)', info)[1])
            sample = {'03': {'sources': audit.dependencies('03'),
                             'evidence_sources': audit.evidence_dependencies('03'),
                             'pdf_sha256': audit.sha(pdf), 'pages': list(range(1, count + 1)),
                             'evidence': ['03/code/PREGLED_DOKAZA.md']}}
            attestation = audit.HERE / 'rucni_pregled.json'
            attestation.write_text(json.dumps(sample))

            def run():
                before = attestation.read_bytes()
                with contextlib.redirect_stdout(io.StringIO()):
                    result = audit.report()
                assert attestation.read_bytes() == before, 'audit modified human approval'
                return result, json.loads((audit.HERE / 'registar.json').read_text())

            ok, first = run()
            assert ok, 'synthetic unchanged fixture rejected'
            ok, second = run()
            assert ok and first['items'] == second['items'], 'IDs or locations are unstable'
            assert len({u['id'] for u in second['items']}) == len(second['items'])
            results.append({'case': 'stable IDs and idempotent inventory', 'passed': True})
            source = fixture / main_source.relative_to(root)
            original_source = source.read_bytes()
            source.write_bytes(b'% synthetic line shift\n' + original_source)
            ok, shifted = run()
            assert not ok and {u['id'] for u in shifted['items']} == {u['id'] for u in first['items']}, 'line shift changed IDs'
            source.write_bytes(original_source)
            assert run()[0]
            results.append({'case': 'stable IDs after source line shift', 'passed': True})
            for relative in [str(main_source.relative_to(root)), '03/code/PREGLED_DOKAZA.md',
                             'PROVERA/logic.py', str(pdf.relative_to(fixture))]:
                target = fixture / relative
                original = target.read_bytes()
                target.write_bytes(original + b'\n% registry fault fixture\n')
                ok, record = run()
                assert not ok and all(u['status'] == 'neprovereno' for u in record['items']), relative
                target.write_bytes(original)
                assert run()[0], 'restored fixture did not recover'
                results.append({'case': 'invalidation: ' + relative, 'passed': True})
            sample['03']['pages'].pop()
            attestation.write_text(json.dumps(sample))
            assert not run()[0], 'missing page approval accepted'
            results.append({'case': 'missing visual page approval', 'passed': True})
        finally:
            audit.ROOT, audit.HERE, audit.EXERCISES = root, here, exercises
    output = here / '_build' / 'registry.json'
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
    print(f'Registar: {len(results)} provera stabilnosti i poništavanja potvrde uspešno završeno.')


if __name__ == '__main__':
    main()
