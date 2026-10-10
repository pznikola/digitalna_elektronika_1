"""Nezavisni dokazi nastavnih dopuna 06; ne odobrava greške originala."""
from fractions import Fraction
from pathlib import Path
from itertools import combinations
import struct
import provera_logike

ROOT = Path(__file__).resolve().parents[1]

def crc_remainder(word, generator=0b11001):
    while word.bit_length() >= generator.bit_length():
        word ^= generator << (word.bit_length() - generator.bit_length())
    return word

def main():
    provera_logike.main()
    assert (255 + 1) & 255 == 0 and 127 + 1 == 128
    assert ord('1') == 0x31 and ord('P') + 0x20 == ord('p')
    # Konverzija preko količnika/ostatka radi za svaku vrednost jednog bajta.
    for value in range(256):
        rest=value;digits=[]
        while rest:
            rest,d=divmod(rest,10);digits.append(d)
        assert sum(d*10**i for i,d in enumerate(digits)) == value
        bcd=0
        for shift in reversed(range(8)):
            for pos in [0,4,8]:
                if (bcd>>pos)&15 >= 5:
                    bcd+=3<<pos
            bcd=(bcd<<1)|((value>>shift)&1)
        assert sum(((bcd>>pos)&15)*10**(pos//4) for pos in [0,4,8])==value
    for d in range(5,10):
        prepared=(d+3)<<1
        assert prepared>>4==1 and prepared&15==2*d-10
    assert 43+81==124 and (43+81)%100==24
    assert 19+57==76 and 76-100==-24
    assert Fraction(13)+Fraction(1,4)==Fraction(53,4)
    assert Fraction(1)+Fraction(1,4)+Fraction(1,32)==Fraction(41,32)
    assert Fraction(41,32)*2**7==164
    assert struct.unpack('>f', (1).to_bytes(4,'big'))[0] == float(Fraction(1,2**149))
    # Hornerovi prefiksi, a ne samo krajnji rezultat.
    value=0;states=[]
    for b in '11110011':
        value=value*2+int(b);states.append(value)
    assert states==[1,3,7,15,30,60,121,243]
    # Isto tumačenje tri trenutka očitavanja kao na osam tragova s018/s019.
    events=[3.12,1.96,2.22,1.6];times=[1.78,2.58,3.5]
    for states,expected in [([(1,0),(0,1),(0,1),(0,1)],['1001','1111','0111']),
                            ([(1,0),(1,1),(0,0),(0,0)],['1100','1100','0100'])]:
        observed=[''.join(str(after if t>=event else before) for (before,after),event in zip(states,events)) for t in times]
        assert observed==expected
    for b in [0,1]:
        for p in [0,1]:assert ((b^p)^p)==b
    for message in range(256):
        crc=crc_remainder(message<<4)
        assert crc<16 and crc_remainder((message<<4)|crc)==0
    word=0b111001100000;bits=f'{word:012b}';window=int(bits[:5],2);before=[];after=[]
    for i in range(7):
        before.append(f'{window:05b}')
        window^=0b11001 if window&16 else 0
        after.append(f'{window:05b}')
        window=(window<<1)|int(bits[5+i])
    assert before==['11100','01011','10111','11100','01010','10100','11010']
    assert after==['00101','01011','01110','00101','01010','01101','00011']
    assert window==6
    assert all(v in (ROOT/'beleske/s025.tex').read_text() for v in before+after)
    # Polinomski proizvod: sva tri reda i sva poništavanja.
    q=sum(1<<i for i in [7,5,4,2,1]);product=(q<<4)^(q<<3)^q
    assert product==(word^6) and crc_remainder(product)==0
    assert ((0b10011^0b10110).bit_count())==2
    assert 2**3<9+3+1 and 2**4>=9+4+1 and 2**4-4-1==11
    assert 1^2^3==0  # kontraprimer neograničenom zaključku s029, van beležaka
    hot=[1<<i for i in range(8)];therm=[(1<<i)-1 for i in range(8)]
    assert min((a^b).bit_count() for a,b in combinations(hot,2))==2
    assert min((a^b).bit_count() for a,b in combinations(therm,2))==1
    print('Dopune beležaka: 256 konverzija /10 i Shift-Add-3, BCD korekcije, oba FP primera i 2^-149, osam Hornerovih prefiksa, šest vremenskih očitavanja, EXOR, 256 CRC poruka i 14 međurezultata, polinomsko množenje, rastojanja kodova i broj sindroma: PROVERENO. Osam grupa izvornih stručnih pitanja i dalje zahteva korisnikovu odluku.')

if __name__=='__main__':main()
