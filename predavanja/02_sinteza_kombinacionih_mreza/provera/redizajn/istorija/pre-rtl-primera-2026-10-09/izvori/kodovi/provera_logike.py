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
    # Odobrena formula na slajdu 22 je proizvod zbirova iz funkcionalne tabele.
    slide_22 = (ROOT / "slajdovi/s022_mreza_ili_i.tex").read_text()
    # Raspored po redovima i boja formule ne menjaju pet uređenih činilaca.
    assert re.findall(r"\(([^()]+)\)", slide_22) == [
        "C+B+A", r"C+B+\bar A", r"C+\bar B+A",
        r"\bar C+B+A", r"\bar C+\bar B+\bar A",
    ]
    for c, b, a in itertools.product((0, 1), repeat=3):
        shown = (c or b or a) and (c or b or not a) and (c or not b or a) and (not c or b or a) and (not c or not b or not a)
        assert bool(shown) == ((a + b + c) == 2)
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
    # Karte 52/53 i usklađene formule čine drugi primer hazarda.
    map_ones = {0, 1, 3, 7}
    assert r"F=\bar C\bar B+BA" in (ROOT / "slajdovi/s052_karte_funkcije_sa_hazardom.tex").read_text()
    assert r"\implicant{1}{3}" in (ROOT / "slike/tikz/s053_zajednicka_povrsina.tex").read_text()
    for c, b, a in itertools.product((0, 1), repeat=3):
        index = 4*c + 2*b + a
        f = ((not c) and (not b)) or (b and a)
        assert (index in map_ones) == bool(f)
        assert bool(f) == bool(f or ((not c) and a))
    # Prelaz B:1→0, C=A=1, samo invertor kasni: pre/sredina/posle (slajdovi 50–51).
    outputs = [((1 and inv_b) or (b and 1)) for b, inv_b in [(1, 0), (0, 0), (0, 1)]]
    assert outputs == [1, 0, 1]
    # Isti hazard za kartirani primer pri C=0, A=1.
    mapped_outputs = [((1 and inv_b) or (b and 1)) for b, inv_b in [(1, 0), (0, 0), (0, 1)]]
    assert mapped_outputs == [1, 0, 1]
    print("Provereni: tabela 8 redova, SOP/POS za 16 ulaza, obe konsenzus jednakosti i oba primera gliča.")


if __name__ == "__main__":
    main()
