#!/usr/bin/env python3
"""Racionalne provere izlomljenih karakteristika i granica iteracija."""
from fractions import Fraction as Q
from pathlib import Path
import re
count=0
def check(ok,msg=""):
 global count
 assert ok,msg
 count+=1
F=[[(Q(0),Q(1),Q(-2),Q(5)),(Q(1),Q(4),Q(-1,3),Q(10,3)),(Q(4),Q(5),Q(-2),Q(10))],[(Q(0),Q(5),Q(-1),Q(5))],[(Q(0),Q(2),Q(-1,2),Q(5)),(Q(2),Q(3),Q(-3),Q(10)),(Q(3),Q(5),Q(-1,2),Q(5,2))]]
B=[[(a,b,-k,5-c) for a,b,k,c in segments] for segments in F]
H=[(Q(0),Q(2),Q(-1,4),Q(5)),(Q(2),Q(7,3),Q(-3,2),Q(15,2)),(Q(7,3),Q(8,3),Q(-9),Q(25)),(Q(8,3),Q(3),Q(-3,2),Q(5)),(Q(3),Q(5),Q(-1,4),Q(5,4))]
def val(segments,x):
 for a,b,k,c in segments:
  if a<=x<=b:return k*x+c
 raise ValueError(x)
for curve in F+B+[H]:
 for i,(a,b,k,c) in enumerate(curve):
  check(0<=k*a+c<=5 and 0<=k*b+c<=5)
  if i:check(val(curve,a)==k*a+c)
for i in range(601):
 x=Q(i,120)
 check(val(H,x)==val(B[2],val(F[2],x)))
 check(val(F[1],val(F[1],x))==x)
 check(val(B[1],x)==x)
for curve,expected in [(F[0],Q(5,2)),(F[1],Q(27,10)),(F[2],Q(5)),(B[0],Q(5,2)),(B[1],Q(27,10)),(B[2],Q(5))]:
 x=Q(27,10)
 for k in range(100):x=val(curve,x)
 check(abs(x-expected)<Q(1,10**20))
for curve in [F[2],B[2],H]:
 check(val(curve,Q(5,2))==Q(5,2))
 check(val(curve,0) in [0,5] and val(curve,5) in [0,5])
for curve,lo,hi,margin in [(F[2],1,4,1),(B[2],1,4,1),(H,Q(1,2),Q(9,2),Q(3,2))]:
 a,b=(3,2) if curve!=B[2] else (2,3)
 check(val(curve,a)==lo and val(curve,b)==hi)
 check(2-lo==hi-3==margin)
for k,c,x0 in [(Q(-1,3),Q(10,3),Q(27,10)),(Q(1,3),Q(5,3),Q(27,10)),(Q(2),Q(-5),Q(3))]:
 x=x0
 for n in range(1,9):
  x=k*x+c
  check(x==k**n*x0+c*(k**n-1)/(k-1))
root=Path(__file__).resolve().parents[1];tex=(root/'07_staticke_karakteristike.tex').read_text()
labels=re.findall(r'\\label\{([^}]+)\}',tex);refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',tex)
check(len(labels)==len(set(labels)));check(set(refs)<=set(labels));check(len(re.findall(r'\\section\{Zadatak',tex))==5)
from audit_math import run
run(root,check,F,B,H,val)
print(f'07: {count} provera prošlo (racionalni segmenti, kompozicija, iteracije, margine).')
