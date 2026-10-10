#!/usr/bin/env python3
"""Nezavisne računske provere izvornih primera i prenetih ćelija tabela."""
from fractions import Fraction
from pathlib import Path
import ast
import operator
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


def verify_complement_equations(s034, s035):
    """Proveri stvarne binarne jednačine za sve kodove širine 1–12 bita."""
    word = r'b_{n-1}b_{n-2}b_{n-3}\ldots b_1b_0'
    inverted = (r'\overline{b_{n-1}}\,\overline{b_{n-2}}\,'
                r'\overline{b_{n-3}}\ldots\overline{b_1}\,\overline{b_0}')
    formulas = [equation for source in (s034, s035)
                for equation in re.findall(r'\\\[(.*?)\\\]', source, re.S)
                if r'111\ldots11' in equation]
    assert len(formulas) == 3
    parsed = []
    for equation in formulas:
        equation = equation.replace(inverted, 'I').replace(word, 'B')
        equation = equation.replace(r'111\ldots11', 'M')
        equation = equation.replace(r'\left', '').replace(r'\right', '')
        left, right = equation.split('=')
        parsed.append((ast.parse(left.strip(), mode='eval').body,
                       ast.parse(right.strip(), mode='eval').body))

    def value(node, variables):
        if isinstance(node, ast.Name) and node.id in variables:
            return variables[node.id]
        if isinstance(node, ast.Constant) and type(node.value) is int:
            return node.value
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub)):
            a, b = value(node.left, variables), value(node.right, variables)
            return a+b if isinstance(node.op, ast.Add) else a-b
        raise AssertionError('Nepodržan zapis binarne jednačine')

    for n in range(1, 13):
        maximum = 2**n-1
        for code in range(2**n):
            variables = {'M': maximum, 'B': code, 'I': code ^ maximum}
            for left, right in parsed:
                assert value(left, variables) == value(right, variables), (n, code)
            complement = (variables['I']+1) % 2**n
            assert ((complement ^ maximum)+1) % 2**n == code


def verify_digit_count_condition():
    source = (ROOT/'slajdovi/s009_konacnost_celobrojnog_zapisa.tex').read_text()
    comparison = re.search(r'n\s*(>|\\geq)\s*\\log_r CV_\{10\}', source)
    assert comparison is not None
    # Monotonost logaritma daje ekvivalentno poređenje celobrojnih stepena;
    # time nema greške zaokruživanja logaritma baš na granici r**m.
    compare = {'>': operator.gt, r'\geq': operator.ge}[comparison.group(1)]
    assert r'CV_{10}>0' in source
    assert r'Za $CV_{10}=0$ dovoljan je zapis jednom cifrom: $0$.' in source
    cases = 0
    for radix in range(2, 17):
        values = set(range(1000))
        values.update(radix**m+delta for m in range(1, 13) for delta in (-1, 0, 1))
        for number in values:
            quotient, digits = number, 0
            while quotient:
                quotient //= radix
                digits += 1
            digits = max(1, digits)
            if number == 0:
                assert digits == 1
                cases += 1
                continue
            for width in range(1, digits+2):
                assert compare(radix**width, number) == (width >= digits), (radix, number, width)
                cases += 1
    return cases


def main():
    for radix in range(2, 17):
        for k in range(1, 7):
            assert sum((radix-1)*Fraction(radix)**i for i in range(-k, 0)) == 1-Fraction(radix)**(-k) < 1
    assert 3*7**2+2*7+6+Fraction(2,7)+Fraction(3,49) == 167+Fraction(17,49)
    assert fractional_digits(Fraction(17,49), 10, 36) == '346938775510204081632653061224489795'
    # Odobreni tačan početak proverava se u oba stvarna izraza s006.
    s006 = (ROOT/'slajdovi/s006_primer_prelaska_iz_osnove_sedam.tex').read_text()
    decimal_prefixes = re.findall(r'(?:0|167)\.([0-9]+)\\ldots', s006)
    assert len(decimal_prefixes) == 2
    assert all(prefix == fractional_digits(Fraction(17,49), 10, len(prefix)) for prefix in decimal_prefixes)
    s016 = (ROOT/'slajdovi/s016_kompatibilni_brojni_sistemi.tex').read_text()
    assert 'b_{(n-1),(k-1)}q^{kn-1}' in s016
    assert 'b_{(n-1),(k-2)}q^{kn-2}' in s016
    s034 = (ROOT/'slajdovi/s034_komplement_osnove.tex').read_text()
    assert 'Prikaz $-123$ u komplementu 10-tke:' in s034
    s035 = (ROOT/'slajdovi/s035_ponovljeno_komplementiranje.tex').read_text()
    verify_complement_equations(s034, s035)
    digit_count_cases = verify_digit_count_condition()
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
    print('Proverene sve ćelije tabela, prelazi između osnova, oba stvarna decimalna niza, dvostruki indeksi, tri binarne jednačine s034/s035 kroz 8190 kodova, strogi uslov s009 kroz', digit_count_cases, 'slučajeva uključujući nulu i granične stepene, naziv komplementa i fiksna tačka; nema otvorenih stručnih nesklada.')


if __name__=='__main__':
    main()
