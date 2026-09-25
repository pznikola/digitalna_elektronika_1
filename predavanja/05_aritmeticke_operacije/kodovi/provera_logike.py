#!/usr/bin/env python3
"""Nezavisna provera šema komparatora na slajdovima 2–11."""
from itertools import product
from pathlib import Path
from fractions import Fraction
import re


def compare2(a, b, incoming=(False, False, True), bottom_up=False):
    a1, a0, b1, b0 = a >> 1, a & 1, b >> 1, b & 1
    p1, q1 = bool(a1 and not b1), bool(not a1 and b1)
    p0, q0 = bool(a0 and not b0), bool(not a0 and b0)
    e1, e0 = not (p1 or q1), not (p0 or q0)
    greater, less, equal = p1 or (e1 and p0), q1 or (e1 and q0), e1 and e0
    ip, iq, ie = incoming
    if bottom_up:
        return greater or (equal and ip), less or (equal and iq), equal and ie
    return ip or (ie and greater), iq or (ie and less), ie and equal


def tree(high, low, bottom_up=False):
    return compare2(2*high[0]+low[0], 2*high[1]+low[1], bottom_up=bottom_up)


def main():
    for a,b in product(range(4), repeat=2):
        expected=(a>b,a<b,a==b)
        assert compare2(a,b)==expected
        assert compare2(a,b,bottom_up=True)==expected
    for a,b in product(range(16),repeat=2):
        expected=(a>b,a<b,a==b)
        high,low=compare2(a>>2,b>>2),compare2(a&3,b&3)
        assert compare2(a&3,b&3,high)==expected  # slajd 5
        assert tree(high,low)==expected  # slajd 6
        assert compare2(a>>2,b>>2,low,True)==expected  # slajd 9
        assert tree(high,low,True)==expected  # slajd 10
    wrong=[]
    for a,b in product(range(64),repeat=2):
        expected=(a>b,a<b,a==b)
        h=compare2((a>>3)&3,(b>>3)&3,(bool(a&32),bool(b&32),False))
        l=compare2(a&3,b&3,(bool(a&4),bool(b&4),False))
        if tree(h,l)!=expected: wrong.append((a,b))
        h=compare2(a>>4,b>>4,(bool(a&8),bool(b&8),False),True)
        l=compare2((a>>1)&3,(b>>1)&3,(bool(a&1),bool(b&1),False),True)
        assert tree(h,l,True)==expected  # slajd 11
    assert (0,1) in wrong
    print(f'Komparatori: 16 dvobitnih i 256 četvorobitnih parova; slajd 11 svih 4096 parova. Izvorno pitanje na slajdu 7: {len(wrong)} neslaganja; primer A=0, B=1.')



def check_arithmetic():
    root=Path(__file__).resolve().parents[1]
    for n, columns in [(15,4),(16,5)]:
        path=next((root/'tabele').glob(f's{n:03d}_*.tex'))
        rows=[tuple(map(int,m)) for m in re.findall(r'(?<![0-9])'+r'&'.join([r'([01])']*columns)+r'\\\\',path.read_text())]
        assert len(rows)==2**(columns-2), (n, rows)
        for row in rows:
            total=sum(row[:-2]); assert row[-2:]==(total//2,total%2)
    for cin,a,b in product(range(2),repeat=3):
        carry=(a and b) or (cin and (a^b))
        parity=(cin and a and b) or ((not carry) and (cin or a or b))
        assert parity == ((a+b+cin)%2)
    assert Fraction('326.23')+Fraction('95.9')==Fraction('422.13')
    assert Fraction('326.23')-Fraction('95.9')==Fraction('230.33')
    a,b=int('32623',7),int('04540',7)
    assert a+b==int('40463',7) and a-b==int('25053',7)
    carries=[0]; c=0
    for x,y in zip(reversed('32623'),reversed('04540')):
        c=(int(x)+int(y)+c)//7; carries.append(c)
    assert ''.join(map(str,reversed(carries)))=='011000'  # izvor s14: 001000
    assert int('0101',2)+int('1101',2)==int('10010',2)
    assert (5+13)%16==2 and min(5+13,15)==15
    assert 12-5==int('0111',2) and (5-12)%16==int('1001',2)
    for radix in range(2,37):
        assert (radix-1)+(radix-1)+1==radix+(radix-1)
        assert 0-1-(radix-1)==-radix
    print('Aritmetika 12–20: 12 redova tabela, 8 stanja alternativne sume, decimalni i binarni primeri, granice za osnove 2–36. Izvorna greška prenosa s14 sačuvana (001000; račun 011000).')


def check_later_arithmetic():
    root=Path(__file__).resolve().parents[1]
    # Sve kombinacije znakova u četvorobitnom sabiranju i oduzimanju.
    signed=lambda x,n: x-(1<<n) if x&(1<<(n-1)) else x
    for a,b,sub in product(range(16),range(16),range(2)):
        bv=b^(15 if sub else 0); carry=sub; into_sign=None
        for i in range(4):
            if i==3: into_sign=carry
            carry=(((a>>i)&1)+((bv>>i)&1)+carry)//2
        result=signed(a,4)+(-signed(b,4) if sub else signed(b,4))
        assert bool(into_sign^carry)==(not -8<=result<=7)
    assert (7+7)//16==0 and (8+8)//16==1  # izvor s26 je obrnut
    for value in range(16):
        extended=value|240 if value&8 else value
        assert signed(extended,8)==signed(value,4)
    for value in range(256):
        assert ((value<<1)&255)==(value*2)%256
        assert value>>1==value//2
        assert signed(value,8)>>1==signed(value,8)//2
        for delta,target in [(1,0),(-1,1)]:
            pos=next((i for i in range(8) if ((value>>i)&1)==target),7)
            assert value^((1<<(pos+1))-1)==(value+delta)%256
    # Čitaj stvarne ćelije novih TikZ tabela, ne kopiju očekivanog računa.
    def product_rows(filename):
        text=(root/'tabele'/filename).read_text()
        cells={}
        for x,y,val in re.findall(r'\\node\[text=[^\]]+\] at \(([\d.]+),(-[\d.]+)\) \{\$([01+\-x])\$\};',text):
            cells[(int(float(x)),int(-float(y)))]=val
        return [''.join(cells.get((col,row),'') for col in range(11)) for row in range(1,5)]
    expected={
        's037_prosireni.tex':['000101','+001010','+000000','001111'],
        's038_mnozenje.tex':['000101','+001010','+000000','001111'],
        's039_mnozenje.tex':['111101','+111010','+000000','1110111'],
        's040_mnozenje.tex':['000011','+000000','+001100','001111'],
        's041_oduzimanje.tex':['000011','+000000','-001100','110111'],
        's041_negativni_proizvod.tex':['000011','+000000','+110100','110111'],
        's042_mnozenje.tex':['111101','+000000','+001100','1001001']}
    for filename,rows in expected.items(): assert product_rows(filename)==rows, filename
    assert signed(int('110111',2),6)==-3*3
    assert int('1001001',2)%64==(-3)*(-3)
    # Namerno netačni izvorni primeri s38/s40 imaju rezultat 15 umesto -9.
    assert int('001111',2)!=-3*3
    # Boothova teleskopska jednakost, nezavisno od realizacije registra R.
    for n in range(2,9):
        for a in range(1<<n):
            digits=[0]+[(a>>i)&1 for i in range(n)]
            assert sum((digits[i]-digits[i+1])*(1<<i) for i in range(n))==signed(a,n)
    R=0; a=6; b=2; prev=0; states=[0]
    for i in range(4):
        current=a&1; R+=(prev-current)*b*16
        states.append(R%256);R//=2;states.append(R%256)
        prev=current;a//=2
    assert R==12
    text=(root/'tabele/s047_booth_iteracije.tex').read_text()
    displayed=[int(v.replace(' ',''),2) for v in re.findall(r'[01]{4} [01]{4}',text)]
    assert displayed==states+[12],(displayed,states)
    for n in range(2,9):
        assert Fraction((1<<n)-1,1<<(2*n-1)) < Fraction(1,1<<(n-1))
    assert Fraction(15,128)==Fraction('0.1171875')
    assert divmod(74,8)==(9,2)
    for n in [53,54]:
        text=(root/f'tabele/s{n:03d}_deljenje.tex').read_text()
        cells={(int(float(x))-2,int(-float(y))):digit
               for x,y,digit in re.findall(r'\\node\[text=[^\]]+\] at \(([\d.]+),(-[\d.]+)\) \{\\strut ([01])\};',text)}
        value=lambda row,cols:int(''.join(cells[(c,row)] for c in cols),2)
        assert divmod(value(0,range(1,8)),value(0,range(9,13))) == (
            value(0,range(14,18)),value(11 if n==53 else 10,range(4,8)))
    print('Aritmetika 26–55: 512 ADD/SUB stanja i OVF, 16 ekstenzija znaka, 256 pomeranja i INC/DEC, ćelije sedam tabela proizvoda, Boothova jednakost za širine 2–8 i svih 10 prikazanih stanja primera, greška odsecanja i 74:8=9 ostatak 2.')

if __name__=='__main__':
    main()
    check_arithmetic()
    check_later_arithmetic()
