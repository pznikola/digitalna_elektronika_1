#!/usr/bin/env python3
"""Nezavisna aritmetička i iscrpna logička provera vežbi 04."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
records=json.loads((root/'code/rezultati.json').read_text())
tex=(root/'04_aritmeticke_operacije.tex').read_text()
checks=0
def check(ok,msg=''):
    global checks
    assert ok,msg
    checks+=1

def unsigned(s,r):
    a,_,b=s.partition('.')
    return F(int(a+b,r),r**len(b))
def signed(s,r,rep):
    n=len(s.replace('.',''));k=len(s.partition('.')[2]);u=int(s.replace('.',''),r)
    return F(u-(r**n-(rep=='KMV') if 2*u>=r**n else 0),r**k)
def raw(s,r):return int(s.replace('.',''),r)

for rec in records:
    kind=rec['kind']
    if kind in ['signed','unsigned']:
        r=rec['base'];n=rec['n'];k=rec['k'];c=rec['carry'];R=r**n
        if kind=='unsigned':
            a=int(unsigned(rec['a'],r)*r**k);b=int(unsigned(rec['b'],r)*r**k)
            exact=a-b-rec['cin'] if rec['sub'] else a+b+rec['cin']
            result=rec['result'];check((-1 if result.startswith('-') else 1)*unsigned(result.lstrip('-'),r)==F(exact,r**k),rec)
            check(c[0]==rec['cin'])
        else:
            a=raw(rec['u'],r);b=raw(rec['v'],r)
            check(signed(rec['u'],r,rec['rep'])==signed(rec['a'],r,rec['rep']),rec)
            rhs=signed(rec['b'],r,rec['rep'])*(-1 if rec['sub'] else 1)
            check(signed(rec['v'],r,rec['rep'])==rhs,rec)
            exact=(signed(rec['a'],r,rec['rep'])+rhs)*r**k
            lo=-(R//2) if rec['rep']=='KO' else -((R-2)//2)
            hi=(R-1)//2 if rec['rep']=='KO' else -lo
            check(rec['of']==int(not lo<=exact<=hi),rec)
            modulus=R if rec['rep']=='KO' else R-1
            check((raw(rec['result'],r)-exact)%modulus==0,rec)
            if not rec['of']:check(signed(rec['result'],r,rec['rep'])==exact/r**k,rec)
        # Verify every column of the displayed carry/borrow vector.
        for i in range(n):
            ai=a//r**i%r;bi=b//r**i%r;wi=raw(rec['low'],r)//r**i%r
            if kind=='unsigned' and rec['sub']:check(ai-bi-c[i]==wi-r*c[i+1],rec)
            else:check(ai+bi+c[i]==wi+r*c[i+1],rec)
    elif kind=='sm':
        s=rec['result'];check((-1 if s[0]=='1' else 1)*int(s[1:],2)==rec['value'])
    elif kind=='multiply':
        a=signed(rec['a'],2,'KO') if rec['signed'] else unsigned(rec['a'],2)
        b=signed(rec['b'],2,'KO') if rec['signed'] else unsigned(rec['b'],2)
        result=signed(rec['result'],2,'KO') if rec['signed'] else unsigned(rec['result'],2)
        check(a*b==result,rec)
        check(sum(rec['partials'])==a*b*2**rec['k'],rec)
        check(len(rec['result'].replace('.',''))==10)
        bits=raw(rec['b'],2);x=a*2**len(rec['a'].partition('.')[2])
        for i,p in enumerate(rec['partials']):check(p==x*((bits>>i)&1)*2**i*(-1 if rec['signed'] and i==4 else 1),rec)
    elif kind=='divide':
        a=int(rec['a'],2);b=int(rec['b'],2);q=int(rec['q'],2);rem=int(rec['rem'],2)
        check(a==b*q+rem and 0<=rem<b,rec)
    check(rec.get('result',rec.get('q')) in tex,rec)
# Basic boundary condition: sum equal to radix must carry; equal operands do not borrow.
for r in [2,7,8,10,16]:
    for x,y,c in product(range(r),range(r),range(2)):
        check((x+y+c)//r==int(x+y+c>=r))
        check(((x-y-c)%r)+r*(-int(x-y-c<0))==x-y-c)
# Complete truth table, minimized SOP and XOR implementation.
for A,B in product(range(4),repeat=2):
    a1,a0=(A>>1)&1,A&1;b1,b0=(B>>1)&1,B&1;c0=a0&b0;p1=a1^b1
    s0=a0^b0;s1=p1^c0;s2=(a1&b1)|(p1&c0)
    sop=(a1 and not a0 and not b1) or (a1 and not b1 and not b0) or (not a1 and not a0 and b1) or (not a1 and b1 and not b0) or (not a1 and a0 and not b1 and b0) or (a1 and a0 and b1 and b0)
    check(4*s2+2*s1+s0==A+B)
    check(s1==sop)
    D2=(a1<<3)|(a0<<2)|((1-a1)<<1)|(1-a0)
    check(D2==3*(A+1))
    X=[A+1,2*(A+1),D2,4*(A+1)][B]
    Y=(2*X if A>B else X) if A!=B else 0
    expected=(A+1)*(B+1)*(2 if A>B else 1) if A!=B else 0
    check(Y==expected and Y<=24)
for A,B in product(range(16),repeat=2):
    ah,al=A>>2,A&3;bh,bl=B>>2,B&3
    G=ah>bh or (ah==bh and al>bl);E=ah==bh and al==bl;L=not(G or E)
    check((G,E,L)==(A>B,A==B,A<B))
for A,B,C in product(range(16),repeat=3):
    X=A;Y=C>>1;Z=B<<1;M=X if X>Y else Y
    output=Z if (Z&16 or (Z&15)>M) else M
    check(output==max(A,2*B,C//2))
# Five-digit self-study operands are valid and sign extension preserves their value.
for rec in [x for x in records if x['kind']=='signed']:
    for operand in [rec['a'],rec['b']]:
        r=rec['base'];rep=rec['rep'];k=len(operand.partition('.')[2]);n=len(operand.replace('.',''));v=signed(operand,r,rep)
        scaled=int(v*r**k);u=scaled if scaled>=0 else r**5-(rep=='KMV')+scaled
        check(F(u-(r**5-(rep=='KMV') if u*2>=r**5 else 0),r**k)==v)
labels=re.findall(r'\\label\{([^}]+)\}',tex);check(len(labels)==len(set(labels)))
for ref in re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',tex):check(ref in labels,ref)
from audit_math import run
checks += run(records)
print(f'Vežbe 04: {checks} provera uspešno završeno.')
