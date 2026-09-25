"""Izmena ABEL/JEDEC izvora mora poništiti stanje izgradnje."""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import zajednicko


class DependencyTests(unittest.TestCase):
    def test_hdl_and_fuse_files_invalidate_build_but_review_does_not(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);folder=root/'lecture'
            (root/'_zajednicko').mkdir()
            (folder/'provera').mkdir(parents=True)
            (folder/'kodovi').mkdir()
            (folder/'provera/mapa.json').write_text('{}')
            with patch.object(zajednicko,'ROOT',root):
                previous=zajednicko.dependency_digest(folder)
                for suffix in ['abl','jed']:
                    source=folder/'kodovi'/('example.'+suffix)
                    source.write_text('before')
                    baseline=zajednicko.dependency_digest(folder)
                    self.assertNotEqual(previous,baseline)
                    source.write_text('after')
                    previous=zajednicko.dependency_digest(folder)
                    self.assertNotEqual(previous,baseline)
                (folder/'provera/pregled.json').write_text('{"status":"ceka"}')
                self.assertEqual(previous,zajednicko.dependency_digest(folder))

if __name__=='__main__':unittest.main()
