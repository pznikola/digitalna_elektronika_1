#!/usr/bin/env python3
"""Nezavisne provere vežbi 03. Sve konverzije koriste tačne razlomke."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import re

DIGITS='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
checks=0
def check(ok):
    global checks
    assert ok
    checks+=1

def value(text,base):
    whole,_,frac=text.upper().partition('.')
    assert all(DIGITS.index(c)<base for c in whole+frac)
    return F(int(whole or '0',base))+sum((F(DIGITS.index(c),base**i) for i,c in enumerate(frac,1)),F())

def digits(v,base,n):
    result=''
    for _ in range(n):
        v,d=divmod(v,base);result=DIGITS[d]+result
    assert v==0
    return result

for text,base,expected in [('1001.0101',2,'9.3125'),('137.21',8,'95.265625'),('1E0.2A',16,'480.1640625')]:
    check(value(text,base)==F(expected))
for a,r,b in [('13.375',10,'1101.011'),('614.24',8,'110001100.010100'),('A3B.4F',16,'101000111011.01001111')]:
    check(value(a,r)==value(b,2))
check(value('254.61',7)==137+F(43,49))
period='111000001010011100101'
check(F(int(period,2),2**len(period)-1)==F(43,49))
check(137+F(43,49)-value('10001001.1110000',2)==F(1,392))
check(3*9**2-int('51',7)*9+int('144',7)==0)
# Znak i apsolutna vrednost, uključujući obe nule.
for word,expected in [('0001011',11),('1000101',-5),('1001001',-9),('0000000',0),('0011111',31),('1011101',-29),('101110',-14),('010100',20),('1000000',0),('1000001',-1)]:
    check((-1 if word[0]=='1' else 1)*int(word[1:],2)==expected)
check(74>2**6-1)
# Tablice 2.4 i 2.5: kodiranje negativnih apsolutnih vrednosti.
fixtures={10:[('1952','8047','8048'),('4399','5600','5601'),('34','9965','9966'),('0','9999','0000'),('1','9998','9999')],16:[('F24','F0DB','F0DC'),('1E','FFE1','FFE2'),('0','FFFF','0000'),('1','FFFE','FFFF')],8:[('42','7735','7736'),('0','7777','0000'),('1','7776','7777')],2:[('0101','1010','1011'),('11','1100','1101'),('0','1111','0000'),('1','1110','1111')]}
for r,items in fixtures.items():
    for v,kmv,ko in items:
        check(digits(r**4-1-int(v,r),r,4)==kmv)
        check(digits((-int(v,r))%r**4,r,4)==ko)
for v,r in [('B2A4',16),('7377',8),('1011',2)]:check(int(v,r)>r**4//2)
check(value('77.77',8)-value('24.70',8)==value('53.07',8))
check(value('100.00',8)-value('24.70',8)==value('53.10',8))
check(value('53.07',8)+F(1,64)==value('53.10',8))
for r in [2,8,10,16]:
    for n in range(1,5):
        R=r**n
        for v in sorted({-R//2,-R//2+1,-1,0,R//2-1}):
            u=v%R;decoded=u if u<R//2 else u-R
            check(decoded==v)
# Ekstenzije i spoljni minus zadatka 2.6.
check((-45)%10000==9955)
check(9999-9954==45)
check(int('0036',8)==int('36',8))
check(int('1110',2)-16==int('10',2)-4)
check(int('1110',2)-15==int('10',2)-3)
for v,word in [(-18,'11101110'),(-120,'10001000'),(0,'00000000'),(1,'00000001'),(-128,'10000000'),(127,'01111111')]:check(format(v%256,'08b')==word)
check(not -128<=128<=127)
for word,expected in [('101','000011'),('011','111101'),('111','000001'),('001','111111'),('000','000000'),('100','000100')]:
    u=int(word,2);v=u if u<4 else u-8
    check(format((-v)%64,'06b')==expected)
# Zadaci za samostalni rad: proverena rešivost; rešenja nisu dodata tekstu.
for text,base in [('73.75',10),('1001110.101101',2),('14.D8F',16),('82.25',10),('1011010.11010111',2),('52.751',8)]:check(value(text,base)>=0)
check(2*7**2+2==2*50)
check(3**2-(4+2)*3+(2*4+1)==0)
check(value('10',2)+value('21',3)+value('32',4)+value('43',5)==value('114',6))
# Provera svih prenetih oznaka i obe ključne ispravke u samom dokumentu.
tex=next(Path(__file__).resolve().parents[1].glob('03_*.tex')).read_text()
labels=re.findall(r'\\label\{([^}]+)\}',tex)
check(len(labels)==len(set(labels)))
for ref in re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',tex):check(ref in labels)
check('(1101.011)_2' in tex)
check('8048' in tex and '(01111111)_2' in tex)
from audit_math import run
checks += run()
print(f'Vežbe 03: {checks} provera uspešno završeno.')
