import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from zajednicko import CATEGORIES, source_slides, normalize_text
from provera import structure_errors, review_errors


def sample_slides():
    return [{"id": f"01-s{n:03}", "tex": f"slajdovi/s{n:03}.tex", "frame_label": f"01-s{n:03}",
             "source_number": n, "output_page": n, "pdf_page": (n + 1) // 2,
             "position": "gornji" if n % 2 else "donji", "inventory_confirmed": True}
            for n in range(1, 4)]


def page(*numbers):
    return {"width": 540., "height": 720., "lines": [
        [{"text": str(n), "xMin": 30., "yMin": 343.9 if i == 0 else 657.1,
          "xMax": 40., "yMax": 353.9 if i == 0 else 667.1}]
        for i, n in enumerate(numbers)]}


class StructureTests(unittest.TestCase):
    def test_two_slides_and_single_last_page(self):
        slides = source_slides([page(1, 2), page(3)])
        self.assertEqual([s["source_number"] for s in slides], [1, 2, 3])
        self.assertEqual([s["position"] for s in slides], ["gornji", "donji", "gornji"])

    def test_missing_footer_and_image_only_slide_are_preserved(self):
        slides = source_slides([page(53, 54)])
        self.assertEqual(len(slides), 2)
        self.assertEqual(slides[1]["source_number"], 54)
        self.assertEqual(slides[1]["source_lines"], [])

    def test_nonstandard_geometry_is_not_silently_split(self):
        p = page(1, 2)
        p["width"] = 720.
        with self.assertRaises(ValueError):
            source_slides([p])

    def test_complete_bijection(self):
        slides = sample_slides()
        trace = [(s["id"], s["output_page"]) for s in slides]
        self.assertEqual(structure_errors({"slides": slides}, 3, trace, 3), [])

    def test_missing_slide_fails(self):
        self.assertTrue(structure_errors({"slides": sample_slides()[:-1]}, 3))

    def test_duplicate_slide_fails(self):
        slides = sample_slides()
        slides[1] = copy.deepcopy(slides[0])
        self.assertTrue(structure_errors({"slides": slides}, 3))

    def test_changed_order_fails(self):
        self.assertTrue(structure_errors({"slides": list(reversed(sample_slides()))}, 3))

    def test_extra_overlay_page_fails(self):
        slides = sample_slides()
        trace = [(s["id"], s["output_page"]) for s in slides]
        trace.insert(1, (slides[0]["id"], 2))
        self.assertTrue(structure_errors({"slides": slides}, 3, trace, 4))

    def test_wrong_source_location_fails(self):
        slides = sample_slides()
        slides[1]["position"] = "gornji"
        self.assertTrue(structure_errors({"slides": slides}, 3))


class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.slide = sample_slides()[0]
        self.current = {"source_render_sha256": "a" * 64, "new_render_sha256": "b" * 64}
        self.review = dict(self.current, categories={k: "provereno" for k in CATEGORIES},
                           notes="Provereni svi elementi prema originalu.")

    def test_current_review_passes(self):
        self.assertEqual(review_errors(self.slide, self.review, self.current), [])

    def test_changed_new_render_invalidates_review(self):
        self.current["new_render_sha256"] = "c" * 64
        self.assertTrue(review_errors(self.slide, self.review, self.current))

    def test_changed_source_render_invalidates_review(self):
        self.current["source_render_sha256"] = "c" * 64
        self.assertTrue(review_errors(self.slide, self.review, self.current))

    def test_unreviewed_and_missing_categories_fail(self):
        self.review["categories"]["tekst"] = "ceka"
        self.assertTrue(review_errors(self.slide, self.review, self.current))
        self.review["categories"].pop("tekst")
        self.assertTrue(review_errors(self.slide, self.review, self.current))

    def test_inventory_requires_confirmation(self):
        self.slide["inventory_confirmed"] = False
        self.assertTrue(review_errors(self.slide, self.review, self.current))

    def test_readability_cannot_be_not_applicable(self):
        self.review["categories"]["citljivost"] = "nije_primenljivo"
        self.assertTrue(review_errors(self.slide, self.review, self.current))

    def test_present_content_cannot_be_not_applicable(self):
        self.slide["inventory"] = {"kategorije": ["tabele"]}
        self.review["categories"]["tabele"] = "nije_primenljivo"
        self.assertTrue(review_errors(self.slide, self.review, self.current))

    def test_normalization_preserves_mathematics(self):
        self.assertEqual(normalize_text("  A\n +\t B  "), "A + B")
        self.assertNotEqual(normalize_text("x̄ = 1"), normalize_text("x = 1"))
        self.assertNotEqual(normalize_text("A + B"), normalize_text("A B"))
        self.assertNotEqual(normalize_text("x₁"), normalize_text("x1"))


if __name__ == "__main__":
    unittest.main()
