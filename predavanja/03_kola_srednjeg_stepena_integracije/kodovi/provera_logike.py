#!/usr/bin/env python3
"""Nezavisne računske provere tabela i funkcionalnih blokova sa slajdova."""
import itertools
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def encoder(bits, enabled=True):
    i3, i2, i1, i0 = bits
    p3 = enabled and i3
    p2 = enabled and not i3 and i2
    p1 = enabled and not i3 and not i2 and i1
    p0 = enabled and not i3 and not i2 and not i1 and i0
    a1, a0 = p3 or p2, p3 or p1
    gs = p3 or p2 or p1 or p0
    eo = enabled and not gs
    return bool(a1), bool(a0), bool(gs), bool(eo)


def main():
    for number, output_count in ((16, 2), (17, 3)):
        filename = "s016_koder_prioriteta.tex" if number == 16 else "s017_koder_prioriteta_gs.tex"
        rows = re.findall(r"([01X](?:&[01X]){" + str(3 + output_count) + r"})\\\\",
                          (ROOT / "tabele" / filename).read_text())
        assert len(rows) == 5, (number, rows)
        for bits in itertools.product((0, 1), repeat=4):
            matches = [row.split("&") for row in rows
                       if all(c == "X" or int(c) == bit for c, bit in zip(row.split("&")[:4], bits))]
            assert len(matches) == 1, (number, bits)
            expected = encoder(bits)[:output_count]
            assert tuple(map(int, matches[0][4:])) == expected
            i3, i2, i1, i0 = bits
            assert expected[:2] == (bool(i3 or i2), bool(i3 or (not i2 and i1)))
            assert encoder(bits, False) == (False, False, False, False)
    for s1, s0 in itertools.product((0, 1), repeat=2):
        decoded = ((not s1) and (not s0), (not s1) and s0, s1 and (not s0), s1 and s0)
        assert sum(decoded) == 1 and decoded[2*s1 + s0]
        assert bool(decoded[0] or decoded[3]) == bool((1, 0, 0, 1)[2*s1 + s0])
        assert bool(decoded[0] or decoded[3]) == (s1 == s0)
    for address in range(64):
        row, column, low = address >> 4, (address >> 2) & 3, address & 3
        assert 16*row + 4*column + low == address
    for mask in range(1 << 16):
        enabled = True
        groups, low1, low0 = [], False, False
        for group in range(3, -1, -1):
            bits = tuple((mask >> (4*group + i)) & 1 for i in range(3, -1, -1))
            a1, a0, gs, enabled = encoder(bits, enabled)
            groups.append(gs)
            low1, low0 = low1 or a1, low0 or a0
        high1, high0, gs, _ = encoder(groups)
        decoded = 8*high1 + 4*high0 + 2*low1 + low0
        assert gs == bool(mask)
        assert decoded == max(0, mask.bit_length() - 1), mask
        assert enabled == (mask == 0)
    # Slajd 4 pogrešno tvrdi da kaskada dva NI realizuje NI3.
    assert any((not (a and b and c)) != (not (a and (not (b and c))))
               for a, b, c in itertools.product((0, 1), repeat=3))
    print("Proverene obe tabele za svih 16 ulaza, dekoder/MUX, 64 adrese i svih 65536 stanja proširenog kodera; nesklad NI na slajdu 4 evidentiran.")


if __name__ == "__main__":
    main()
