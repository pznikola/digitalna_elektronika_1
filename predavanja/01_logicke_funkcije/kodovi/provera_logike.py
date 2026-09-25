#!/usr/bin/env python3
"""Nezavisna provera prepisanih funkcionalnih tabela i prikazanih identiteta."""
import itertools
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FUNCTIONS = {
    16: lambda x, y: x and y,
    17: lambda x, y: x or y,
    18: lambda x, y: x != y,
    19: lambda x, y: not (x and y),
    20: lambda x, y: not (x or y),
    21: lambda x, y: x == y,
}


def main():
    for slide, function in FUNCTIONS.items():
        source = (ROOT / f"tabele/s{slide:03}_funkcionalna_tabela.tex").read_text()
        rows = re.findall(r"([01])&([01])&([01])\\\\", source)
        assert len(rows) == 4, (slide, rows)
        assert [(int(x), int(y)) for x, y, _ in rows] == list(itertools.product((0, 1), repeat=2))
        for x, y, z in rows:
            assert int(z) == int(function(bool(int(x)), bool(int(y)))), (slide, x, y, z)
    for x, y, z in itertools.product((False, True), repeat=3):
        assert (x and (y or z)) == ((x and y) or (x and z))
        assert (x or (y and z)) == ((x or y) and (x or z))
        assert (not (x and y)) == ((not x) or (not y))
        assert (not (x or y)) == ((not x) and (not y))
        assert ((x != y) != z) == (x != (y != z))
        assert (not ((x and y) and z)) == (not (x and y and z))
    assert any((not (x and y and z)) != (not ((not (x and y)) and z))
               for x, y, z in itertools.product((False, True), repeat=3))
    for x1, x2, x3, x4 in itertools.product((False, True), repeat=4):
        original = (x1 and x2) or (x3 and x4)
        nand_network = not ((not (x1 and x2)) and (not (x3 and x4)))
        assert original == nand_network
    print("Provereno: 24 reda tabela, Bulovi identiteti, neekvivalentna NI kaskada i NI realizacija sa slajda 37.")


if __name__ == "__main__":
    main()
