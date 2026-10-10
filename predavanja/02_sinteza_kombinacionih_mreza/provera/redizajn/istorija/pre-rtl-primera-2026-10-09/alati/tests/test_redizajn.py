"""Regresije pokrivenosti, beležaka i potvrda; bez menjanja nastavnih predavanja."""
import copy
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import redizajn as rd
from izgradnja import clean
from zajednicko import write_json


class CoverageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        for name in ("slajdovi", "beleske"):
            (self.folder / name).mkdir()
            (self.folder / name / "s001.tex").write_text("% element: 09_1-s001:e1\nVažno objašnjenje.")
        self.slide = {"id": "09_1-s001", "tex": "slajdovi/s001.tex", "source_number": 1}
        self.data = {"slides": [self.slide]}
        self.inventory = {"09_1-s001": {"confirmed": True, "elements": [{
            "id": "09_1-s001:e1", "description": "Objašnjenje", "source": "PDF 1, gornji, pasus 2",
            "origin": "original", "must_remain_visible": False}]}}
        self.coverage = {"09_1-s001": [{"element": "09_1-s001:e1", "slide": None,
            "notes": {"path": "beleske/s001.tex", "anchor": "% element: 09_1-s001:e1"},
            "change": "Objašnjenje premešteno u beleške istog slajda", "status": "provereno"}]}

    def errors(self):
        return rd.coverage_errors(self.folder, self.data, self.inventory, self.coverage)

    def test_explanation_moved_to_same_slide_notes_passes(self):
        self.assertEqual(self.errors(), [])

    def test_omitted_element_fails(self):
        self.coverage["09_1-s001"] = []
        self.assertTrue(self.errors())

    def test_duplicate_element_fails(self):
        self.coverage["09_1-s001"] *= 2
        self.assertTrue(self.errors())

    def test_required_visible_content_cannot_only_be_in_notes(self):
        self.inventory["09_1-s001"]["elements"][0]["must_remain_visible"] = True
        self.assertTrue(self.errors())

    def test_destination_in_another_slides_notes_fails(self):
        (self.folder / "beleske/s002.tex").write_text("% element: 09_1-s001:e1")
        self.coverage["09_1-s001"][0]["notes"]["path"] = "beleske/s002.tex"
        self.assertTrue(self.errors())

    def test_missing_anchor_fails(self):
        (self.folder / "beleske/s001.tex").write_text("Nešto drugo.")
        self.assertTrue(self.errors())

    def test_unconfirmed_inventory_or_element_fails(self):
        self.inventory["09_1-s001"]["confirmed"] = False
        self.assertTrue(self.errors())
        self.inventory["09_1-s001"]["confirmed"] = True
        self.coverage["09_1-s001"][0]["status"] = "ceka"
        self.assertTrue(self.errors())

    def test_missing_included_resource_is_not_silently_ignored(self):
        (self.folder / "slajdovi/s001.tex").write_text(r"\includegraphics{slike/nedostaje.pdf}")
        with self.assertRaisesRegex(ValueError, "Nedostaje"):
            self.errors()


class NotesAndEvidenceTests(unittest.TestCase):
    def test_catalog_prevents_renaming_stable_ids(self):
        data = {"source_pdf": "original.pdf", "expected_slides": 1, "slides": [{"id": "01-s001"}]}
        with patch.object(rd, "catalog_row", return_value=("01", "original.pdf", "demo", 1, 1)):
            rd.validate_catalog(Path("demo"), data)
            data["slides"][0]["id"] = "01-novi001"
            with self.assertRaisesRegex(ValueError, "stabilni ID"):
                rd.validate_catalog(Path("demo"), data)

    def test_multi_page_notes_keep_one_contiguous_block_per_id(self):
        self.assertEqual(rd.notes_trace_errors([("09_1-s001", 1), ("09_1-s001", 2), ("09_1-s002", 3)],
                                              ["09_1-s001", "09_1-s002"], 3), [])

    def test_missing_swapped_duplicate_and_wrong_id_notes_fail(self):
        for trace in ([('a', 1)], [('b', 1), ('a', 2)], [('a', 1), ('b', 2), ('a', 3)],
                      [('a', 1), ('wrong', 2)], [('a', 1), ('b', 3)]):
            with self.subTest(trace=trace):
                self.assertTrue(rd.notes_trace_errors(trace, ["a", "b"], len(trace)))

    def test_changed_notes_source_or_render_invalidates_confirmation(self):
        current = {"notes_sources_sha256": "a", "notes_render_sha256": "b", "coverage_sha256": "c"}
        review = {"categories": {k: "provereno" for k in rd.CATS}, "evidence": copy.deepcopy(current),
                  "date": "2026-09-25", "reviewer": "Test", "notes": "Test potvrda"}
        slide = {"id": "a"}
        self.assertEqual(rd.review_errors(slide, review, current), [])
        for key in current:
            changed = dict(current, **{key: "changed"})
            self.assertTrue(rd.review_errors(slide, review, changed))

    def test_notes_and_coverage_cannot_be_not_applicable(self):
        review = {"categories": {k: "provereno" for k in rd.CATS}, "evidence": {"hash": "a"},
                  "date": "2026-09-25", "reviewer": "Test", "notes": "Test potvrda"}
        for key in ("beleske", "pokrivenost", "citljivost"):
            changed = copy.deepcopy(review)
            changed["categories"][key] = "nije_primenljivo"
            self.assertTrue(rd.review_errors({"id": "a"}, changed, {"hash": "a"}))

    def test_wrong_manifest_phase_cannot_fall_back_to_reconstruction(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            write_json(folder / "provera/redizajn/manifest.json", {"phase": "typo"})
            with self.assertRaisesRegex(ValueError, "Nepoznata faza"):
                rd.active(folder)


    def test_clean_cannot_remove_only_baseline(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            (folder / "build/redizajn/pre").mkdir(parents=True)
            with self.assertRaisesRegex(ValueError, "početni prikaz"):
                clean(folder)
            self.assertTrue((folder / "build/redizajn/pre").exists())

    def test_fls_dependencies_ignore_unused_theme_but_detect_used_resource(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            used = root / "etf-v1/stil.sty"
            unused = root / "etf-v2/stil.sty"
            used.parent.mkdir(); unused.parent.mkdir()
            used.write_text("used"); unused.write_text("unused")
            fls = root / "demo.fls"
            fls.write_text("INPUT etf-v1/stil.sty\n")
            before = rd.hashes(rd.input_files(root, fls))
            unused.write_text("new unused")
            self.assertEqual(rd.changed_files(before), [])
            used.write_text("changed")
            self.assertEqual(rd.changed_files(before), [str(used)])
            used.unlink()
            with self.assertRaisesRegex(ValueError, "Nedostaje"):
                rd.input_files(root, fls)


class ApprovedSplitTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.original = {"expected_slides": 2, "slides": [
            {"id": f"02-s{n:03}", "frame_label": f"02-s{n:03}",
             "tex": f"slajdovi/s{n:03}_izvor.tex", "source_number": n, "output_page": n,
             "pdf_page": 1, "position": "gornji" if n == 1 else "donji"}
            for n in (1, 2)]}
        approval = self.folder / "odobrenje.json"
        write_json(approval, {"lecture": "02", "action": "split_into_two",
                             "source_ids": ["02-s001"], "user_message": "Podeli s001 na dva slajda."})
        self.manifest = {"lecture": "02", "approved_splits": {
            "approval_path": "odobrenje.json", "approval_sha256": rd.sha256(approval),
            "continuations": {"02-s001": "slajdovi/s001b_nastavak.tex"}}}

    def test_expansion_keeps_original_map_and_source_locations(self):
        before = copy.deepcopy(self.original)
        data = rd.presentation_data(self.folder, self.original, self.manifest)
        self.assertEqual(self.original, before)
        self.assertEqual([s["id"] for s in data["slides"]], ["02-s001", "02-s001b", "02-s002"])
        self.assertEqual([s["source_number"] for s in data["slides"]], [1, 1, 2])
        self.assertEqual([s["output_page"] for s in data["slides"]], [1, 2, 3])
        self.assertEqual(data["original_slides"], before["slides"])
        self.assertEqual(rd.note_path(data["slides"][1]), "beleske/s001b.tex")
        trace = [(s["id"], s["output_page"]) for s in data["slides"]]
        self.assertEqual(rd.presentation_structure_errors(data, trace, 3), [])
        for wrong in (trace[:-1], list(reversed(trace)), trace + [trace[-1]]):
            self.assertTrue(rd.presentation_structure_errors(data, wrong, len(wrong)))
        self.assertTrue(rd.presentation_structure_errors(data, trace, 2))

    def test_no_approval_does_not_enable_split(self):
        self.assertIs(rd.presentation_data(self.folder, self.original, {}), self.original)
        (self.folder / "odobrenje.json").unlink()
        with self.assertRaisesRegex(ValueError, "odobrenje"):
            rd.presentation_data(self.folder, self.original, self.manifest)

    def test_changed_approval_or_unauthorized_source_fails(self):
        approval = self.folder / "odobrenje.json"
        approval.write_text(approval.read_text() + " ")
        with self.assertRaisesRegex(ValueError, "odobrenje"):
            rd.presentation_data(self.folder, self.original, self.manifest)
        self.manifest["approved_splits"]["approval_sha256"] = rd.sha256(approval)
        self.manifest["approved_splits"]["continuations"] = {"02-s002": "slajdovi/s002b_nastavak.tex"}
        with self.assertRaisesRegex(ValueError, "odluci"):
            rd.presentation_data(self.folder, self.original, self.manifest)

    def test_split_cannot_replace_or_reorder_originals(self):
        broken = copy.deepcopy(self.original)
        broken["slides"].reverse()
        data = rd.presentation_data(self.folder, broken, self.manifest)
        self.assertTrue(rd.presentation_structure_errors(data))
        self.manifest["approved_splits"]["continuations"]["02-s001"] = "slajdovi/s002_izvor.tex"
        with self.assertRaisesRegex(ValueError, "putanja"):
            rd.presentation_data(self.folder, self.original, self.manifest)



if __name__ == "__main__":
    unittest.main()
