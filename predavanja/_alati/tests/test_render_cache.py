import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from uporedni_pregled import render_pdf


class RenderCacheTests(unittest.TestCase):
    def test_missing_corrupt_and_extra_pages_force_regeneration(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pdf = root / "source.pdf"
            pdf.write_bytes(b"controlled-pdf")
            output = root / "render"

            def fake_render(*args, **kwargs):
                for n in (1, 2):
                    (output / f"p-{n}.png").write_bytes(f"controlled-render-{n}".encode())

            with patch("uporedni_pregled.pdf_pages", return_value=2), patch(
                    "uporedni_pregled.subprocess.run", side_effect=fake_render) as renderer:
                render_pdf(pdf, output, 1280)
                self.assertEqual(renderer.call_count, 1)
                render_pdf(pdf, output, 1280)
                self.assertEqual(renderer.call_count, 1)
                (output / "p-2.png").unlink()
                render_pdf(pdf, output, 1280)
                self.assertEqual(renderer.call_count, 2)
                (output / "p-1.png").write_bytes(b"corrupted-render")
                render_pdf(pdf, output, 1280)
                self.assertEqual(renderer.call_count, 3)
                (output / "p-3.png").write_bytes(b"unexpected-page")
                pages = render_pdf(pdf, output, 1280)
                self.assertEqual(renderer.call_count, 4)
                self.assertEqual([p.name for p in pages], ["p-1.png", "p-2.png"])
                self.assertFalse((output / "p-3.png").exists())
                pdf.write_bytes(b"changed-pdf")
                render_pdf(pdf, output, 1280)
                self.assertEqual(renderer.call_count, 5)


if __name__ == "__main__":
    unittest.main()
