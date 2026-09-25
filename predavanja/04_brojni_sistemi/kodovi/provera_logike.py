#!/usr/bin/env python3
"""Nezavisne računske provere izvornih primera i prenetih ćelija tabela."""
from fractions import Fraction
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def fractional_digits(value, radix, length):
    result = []
    for _ in range(length):
        value *= radix
        digit = value.numerator // value.denominator
        result.append(digit)
        value -= digit
    return ''.join(str(d) for d in result)


def main():
    for radix in range(2, 17):
        for k in range(1, 7):
            assert sum((radix-1)*Fraction(radix)**i for i in range(-k, 0)) == 1-Fraction(radix)**(-k) < 1
    assert 3*7**2+2*7+6+Fraction(2,7)+Fraction(3,49) == 167+Fraction(17,49)
    assert fractional_digits(Fraction(17,49), 10, 36) == '346938775510204081632653061224489795'
    # Original završava zaokruženom cifrom 9 pre znaka nastavka; ne popravljamo je.
    assert fractional_digits(Fraction(17,49), 10, 32) != '34693877551020408163265306122449'
    assert fractional_digits(Fraction(1,5), 2, 9) == '001100110'
    for filename, base, expected_count in [('s013_celobrojna_vrednost.tex',10,5),('s015_deljenje_u_osnovi_sedam.tex',7,7)]:
        source = (ROOT/'tabele'/filename).read_text()
        source = re.sub(r'\\textcolor\{DEcrvena\}\{([^{}]+)\}',r'\1',source)
        rows = re.findall(r'(\d+):2\s*&\s*(\d+)\s*&\s*(\d+)\\\\',source)
        assert len(rows)==expected_count
        for value, quotient, remainder in rows:
            assert divmod(int(value,base),2)==(int(quotient,base),int(remainder))
    source=(ROOT/'tabele/s013_razlomljena_vrednost.tex').read_text()
    rows=re.findall(r'([01]\.\d) x 2&([01]\.\d)&([01])\\\\',source)
    assert len(rows)==9
    for value,result,integer in rows:
        assert Fraction(value)*2==Fraction(result)
        assert int(Fraction(result))==int(integer)
    for base in (8,16):
        source=(ROOT/f'tabele/s018_{base}_u_binarni.tex').read_text()
        rows=re.findall(r'([0-9A-F]) & ([01]+)\\\\',source)
        assert len(rows)==base
        assert all(int(a,base)==int(b,2) for a,b in rows)
    for n in range(29,33):
        rows=re.findall(r'([01]{4})&(\d+)&\$(-?\d+)\$\\\\',(ROOT/f'tabele/s{n:03}_kodovi.tex').read_text())
        assert len(rows)==16
        for code,unsigned,value in rows:
            u=int(unsigned); assert int(code,2)==u
            expected={29:u if u<8 else -(u-8),30:u-8,31:u if u<8 else u-15,32:u if u<8 else u-16}[n]
            assert int(value)==expected
            if n==29 and u==8 or n==31 and u==15: assert value=='-0'
    rows=re.findall(r'\$(-?\d+)\$&([01]{4})&([01]{4})\\\\',(ROOT/'tabele/s037_drugi_komplement_i_ofset.tex').read_text())
    assert len(rows)==16
    for value,twos,offset in rows:
        v=int(value); assert int(twos,2)%16==v%16 and int(offset,2)==v+8
        assert int(twos,2)^8==int(offset,2)
    assert int('236',7)==int('1111101',2)==125
    assert int('1AC3',16)==int('1101011000011',2)
    assert int('10100010010101101',2)==int('144AD',16)
    assert int('1A',16)+Fraction(int('3C',16),256)==int('11010',2)+Fraction(int('001111',2),64)
    assert int('101100',2)+Fraction(int('1011011',2),128)==int('2C',16)+Fraction(int('B6',16),256)
    assert int('01101000',2)==int('68',16)==104
    assert 999-123==876 and 1000-123==877
    assert -1+Fraction(1,4)==Fraction(-3,4)
    for value in range(8,16):
        assert -(16-value)==-(value>>3)*8+(value&7)
    # Kontraprimeri nepreciznim zapisima originala, slajdovi 9 i 35.
    assert 3>=3 and not Fraction(8,2**3)<1
    assert (15+1-(15-3)+1)%16 != 3
    assert (15+1-((15-3)+1))%16 == 3
    print('Proverene sve ćelije tabela, prelazi između osnova, 32 decimale, komplementi i fiksna tačka; neskladi originala na slajdovima 6, 9 i 35 izdvojeni.')


if __name__=='__main__':
    main()
