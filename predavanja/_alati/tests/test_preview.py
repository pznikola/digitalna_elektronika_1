"""Radni pregled mora koristiti isti preambulum kao završna prezentacija."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import izgradnja
from zajednicko import sha256


class PreviewTests(unittest.TestCase):
    def test_custom_packages_and_original_numbers_survive_preview(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / 'lecture'
            (folder / 'provera').mkdir(parents=True)
            (folder / 'slajdovi').mkdir()
            original = root / 'original.pdf'
            original.write_bytes(b'original')
            preamble = '\\documentclass{beamer}\n\\usepackage{colortbl}\n'
            (folder / 'lecture.tex').write_text(preamble + '\\begin{document}\n\\end{document}\n')
            (folder / 'slajdovi/s002.tex').write_text('frame')
            (folder / 'provera/mapa.json').write_text(json.dumps({
                'source_pdf': 'original.pdf', 'source_sha256': sha256(original),
                'slides': [{'tex': 'slajdovi/s001.tex', 'source_number': 1},
                           {'tex': 'slajdovi/s002.tex', 'source_number': 2}]}))

            def compile_stub(*args, **kwargs):
                (folder / 'build/radni_pregled.pdf').write_bytes(b'compiled')
                return SimpleNamespace(returncode=0)

            with patch.object(izgradnja, 'ROOT', root), \
                    patch.object(izgradnja, 'dependency_digest', return_value='digest'), \
                    patch.object(izgradnja.subprocess, 'run', side_effect=compile_stub):
                izgradnja.build(folder, preview=True)
            result = (folder / 'build/radni_pregled.tex').read_text()
            self.assertTrue(result.startswith(preamble))
            self.assertIn('\\setcounter{framenumber}{1}', result)
            self.assertIn('\\input{slajdovi/s002.tex}', result)
            self.assertNotIn('slajdovi/s001.tex', result)


if __name__ == '__main__':
    unittest.main()
