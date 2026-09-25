#!/usr/bin/env python3
"""Nezavisne iscrpne provere primera; očekivane greške originala su izričite."""
import itertools
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    source = (ROOT / "tabele/s011_funkcionalna_tabela.tex").read_text()
    rows = re.findall(r"([01])&([01])&([01])&([01])\\\\", source)
    assert len(rows) == 8
    assert [tuple(map(int, row[:3])) for row in rows] == list(itertools.product((0, 1), repeat=3))
    for c, b, a, f in (map(int, row) for row in rows):
        expected = (a + b + c) == 2
        sop = ((not c) and b and a) or (c and (not b) and a) or (c and b and (not a))
        pos = (c or b or a) and (c or b or not a) and (c or not b or a) and (not c or b or a) and (not c or not b or not a)
        assert bool(f) == expected == bool(sop) == bool(pos)
    # Izvorni slajd 22 ponavlja četvrti maxterm na prvom mestu.
    mismatches = []
    for c, b, a in itertools.product((0, 1), repeat=3):
        shown = (not c or b or a) and (c or b or not a) and (c or not b or a) and (not c or b or a) and (not c or not b or not a)
        if bool(shown) != ((a + b + c) == 2):
            mismatches.append((c, b, a))
    assert mismatches == [(0, 0, 0)]
    # Nezavisan popis sa originalne karte 43/44; b na indeksu 1.
    ones, dont_care = {0, 4, 5, 8, 10}, {1}
    for d, c, b, a in itertools.product((0, 1), repeat=4):
        index = 8*d + 4*c + 2*b + a
        sop = ((not d) and (not b)) or (d and (not c) and (not a))
        pos = (d or not b) and (not d or not c) and (not d or not a)
        assert bool(sop) == bool(pos)
        if index not in dont_care:
            assert bool(sop) == (index in ones)
    # Konsenzus CA ne menja funkciju C barB + BA.
    for c, b, a in itertools.product((0, 1), repeat=3):
        f = (c and not b) or (b and a)
        assert bool(f) == bool(f or (c and a))
    # Karte 52/53 prikazuju barC barB + BA, iako formula navodi C barB + BA.
    source_ones = {0, 1, 3, 7}
    map_mismatches = []
    for c, b, a in itertools.product((0, 1), repeat=3):
        index = 4*c + 2*b + a
        assert (index in source_ones) == bool(((not c) and (not b)) or (b and a))
        if (index in source_ones) != bool((c and not b) or (b and a)):
            map_mismatches.append(index)
    assert map_mismatches == [0, 1, 4, 5]
    # Prelaz B:1→0, C=A=1, samo invertor kasni: pre/sredina/posle.
    outputs = [((1 and inv_b) or (b and 1)) for b, inv_b in [(1, 0), (0, 0), (0, 1)]]
    assert outputs == [1, 0, 1]
    print("Provereni: tabela 8 redova, SOP/POS za 16 ulaza, konsenzus i glič; potvrđena dva dokumentovana nesklada originala.")


if __name__ == "__main__":
    main()
