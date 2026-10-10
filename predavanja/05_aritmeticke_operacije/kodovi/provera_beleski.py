"""Nezavisna računska provera nastavnih dopuna u beleškama predavanja 05."""
from fractions import Fraction
from itertools import product


def signed(word, width):
    return word - (1 << width) if word & (1 << (width - 1)) else word


def check_notes():
    # Decimalni međukoraci, bez računanja binarnim floating-point brojevima.
    assert Fraction('326.23') + Fraction('95.9') == Fraction('422.13')
    assert Fraction('326.23') - Fraction('95.9') == Fraction('230.33')
    assert signed(0b11001, 5) == -7
    assert signed(0b1001, 4) == -7
    assert signed(0b110111, 6) == -9
    assert signed(0b001001, 6) == 9
    # Kružni prenos prvog komplementa: svi reprezentabilni zbirni rezultati.
    width = 4
    modulus = (1 << width) - 1
    encode = lambda x: x if x >= 0 else modulus + x
    for a, b in product(range(-7, 8), repeat=2):
        if -7 <= a + b <= 7:
            total = encode(a) + encode(b)
            word = (total & modulus) + (total >> width)
            expected = encode(a + b)
            assert word == expected or (a + b == 0 and word == modulus)
    assert ((0b1101 + 0b0011) & modulus) + ((0b1101 + 0b0011) >> 4) == 1
    # ASR i njegova razlika prema deljenju sa zaokruživanjem prema nuli.
    assert signed(0b1001, 4) // 2 == signed(0b1100, 4) == -4
    for word in range(256):
        value = signed(word, 8)
        overflow = not -128 <= value * 2 <= 127
        assert overflow == (((word >> 7) ^ (word >> 6)) & 1 == 1)
    # Boothov primer u tabeli koristi dva zasebna registra, b=2, a=6.
    a, b, previous, result = 6, 2, 0, 0
    states = []
    for _ in range(4):
        current = a & 1
        result += (previous - current) * b * 16
        states.append(result)
        result //= 2
        states.append(result)
        previous, a = current, a // 2
    assert states == [0, 0, -32, -16, -16, -8, 24, 12]
    coefficients = [((0b001110 >> (i - 1)) & 1 if i else 0)
                    - ((0b001110 >> i) & 1) for i in range(6)]
    assert sum(coefficient * (1 << i) for i, coefficient in enumerate(coefficients)) == 14
    # Granica odsecanja proizvoljnog zapisa: uvek floor, i za negativne vrednosti.
    step = Fraction(1, 8)
    assert (Fraction(-1, 16) // step) * step == Fraction(-1, 8)
    for raw in range(-128, 128):
        value = Fraction(raw, 128)
        truncated = (value // step) * step
        assert 0 <= value - truncated <= Fraction(15, 128) < step
    assert divmod(74, 8) == (9, 2)
    assert Fraction(74, 8) == Fraction('9.25')
    assert -8 // -1 == 8 > 7
    print('Beleške 05: tačni decimalni koraci, komplementni zapisi, kružni prenos, '
          '256 ASL uslova, ASR negativnog neparnog broja, sve Boothove iteracije, '
          '256 odsecanja i deljenje 74:8.')


if __name__ == '__main__':
    check_notes()
