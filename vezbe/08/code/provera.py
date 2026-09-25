#!/usr/bin/env python3
"""Nezavisne numeričke, simboličke i iscrpne prekidačke provere."""
from math import sqrt,isclose
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import re
import sympy as s
count=0
def check(v,msg=''):
 global count
 assert v,msg
 count+=1
def near(a,b,tol=1e-8):check(abs(a-b)<tol,(a,b))
def root(f,a,b):
 check(f(a)*f(b)<0)
 for _ in range(100):
  c=(a+b)/2
  if f(a)*f(c)<=0:b=c
  else:a=c
 return (a+b)/2
# MOS model continuity, cutoff and positive currents across representative biases.
for B,E,u in product([.0002,.00086],[.3,.6,2.4],[.05,.2,.8]):
 lin=lambda d:B*(u*d-d*d/2)/(1+d/E)
 sat=B*u*u/(2*(1+u/E))
 near(lin(u),sat);near(lin(0),0);check(all(lin(u*i/10)>=0 for i in range(11)))
B=.00086;R=20000;D=1.2;T=.4;al=1/(B*R)
vlow=root(lambda y:(D-y)/R-B*((D-T)*y-y*y/2),0,D-T)
near(vlow,.08556683435028978)
vil=T+al;vih=T-al+sqrt(8*D*al/3);ol=sqrt(2*D*al/3);oh=D-al/2
near((D-oh)/R,B*(vil-T)**2/2);near((D-ol)/R,B*((vih-T)*ol-ol**2/2));near((T-vih+2*ol)*B,1/R)
check(oh>vil-T);check(ol<vih-T);near(vil-ol,.24247398847684412);near(oh-vih,.3977386746281066)
vs=root(lambda x:(D-x)/R-B*(x-T)**2/2,T,D);near(vs,.6523495330888067)
th=lambda y:.4+.2*(sqrt(y+.88)-sqrt(.88));VH=root(lambda y:y-1.2+th(y),0,1.2)
near(VH,.7335643265972611);near(th(.1),.41037326833929616);near(1.2+th(1.2),1.700827471644182)
# Units: L=100 nm=1e-5 cm, mobility cm²/(Vs), velocity cm/s.
v=8e6;L=1e-5;mu=270;cox=1.6e-6;u2=1.2-.1-th(.1)
KR=(v*L/mu)*(1+.1/.6)*u2*u2/((u2+.6)*((VH-.4)*.1-.1**2/2))
near(KR,4.495578303655942);i1=KR*mu*cox/(1+.1/.6)*((VH-.4)*.1-.1**2/2);i2=L*v*cox*u2*u2/(u2+.6);near(i1,i2,1e-14)
check(.1<VH-.4 and 1.1>u2);check(not isclose(KR,1.7,rel_tol=.01))
# Symbolic depletion-load equations, with threshold held constant as stated.
K,t,u,d,y=s.symbols('K t u d y',positive=True)
Fhigh=K*u*u-2*t*d+d*d
check(s.simplify(Fhigh.subs({u:t/s.sqrt(K*(K+1)),d:t*(1-s.sqrt(K/(K+1)))}))==0)
check(s.simplify((s.diff(Fhigh,u)+s.diff(Fhigh,d)).subs(d,t-K*u))==0)
Flow=K*(2*u*y-y*y)
check(s.simplify((s.diff(Flow,u)-s.diff(Flow,y)).subs(u,2*y))==0)
check(s.simplify(Flow.subs(u,2*y)-3*K*y*y)==0)
for ratio,want in [(4,.6112880845167364),(1,.537965311633131)]:
 f=lambda x:(x-.4)**2/(x-.4+.6)-ratio*(.8-x)**2/(.8-x+2.4)
 x=root(f,.4,.8);near(x,want);near(f(x),0,1e-14);check(.4<x<.8 and x>=x-.4 and x<=x+.4)
# Independent PDN/PUN descriptions from the transistor networks.
def series(*xs):return all(xs)
def parallel(*xs):return any(xs)
for a,b,c,d in product([False,True],repeat=4):
 pd5=parallel(series(not a,not b),series(not c,not d));pu5=series(parallel(a,b),parallel(c,d));check((not pd5)==pu5==((a or b)and(c or d)))
 pd5b=series(parallel(a,b),parallel(c,d));pu5b=parallel(series(not a,not b),series(not c,not d));check(pd5b!=pu5b);check(not(not pd5b)==pu5)
 pd6=parallel(a,series(b,parallel(c,d)));pu6=series(not a,parallel(not b,series(not c,not d)));check(pd6!=pu6);check(pu6==((not a and not b)or(not a and not c and not d)))
 P=(not c)or((not a)and(not d))or(c and(a or d));original=(not(a and b))and((not P)or not(c and d));pd8=(a and b)or(c and d);check(original==(not pd8));check(pd8==parallel(series(a,b),series(c,d)))
# Worst conducting paths, inverse normalized resistance.
for widths,target in [([F(1)],F(1)),([F(2),F(2)],F(1)),([F(4),F(4)],F(2)),([F(4),F(8),F(8)],F(2))]:check(1/sum(1/w for w in widths)==target)
# TG multiplexer model propagates values, including Z, without Boolean arithmetic on Z.
def mux(sel,hi,lo):return hi if sel else lo
truth=[]
for a,b,c,d in product([0,1],repeat=4):
 y=mux(a,mux(b,c,d),mux(c,d,b));formula=(a and((not b and d)or(b and c)))or(not a and((c and d)or(not c and b)));check(y==formula);truth.append(y)
check(truth[5]==1)
expected=[0,'D',1,'D','D','D',0,1]
for j,(a,b,c) in enumerate(product([0,1],repeat=3)):
 for d in [0,1,'Z']:
  actual=mux(a,mux(b,c,d),mux(c,d,b));check(actual==(d if expected[j]=='D' else expected[j]))
for a,b,c in product([0,1],repeat=3):check(mux(a,c,mux(b,c,0))==mux(c,mux(a,1,b),0)==((a or b)and c))
# Event-driven dynamic node: no recharge during evaluation, including C falling.
events=sorted({0,1,1.5,2,3,4,5,6,7,7.5,8,9,10,11});Y=1;trace=[]
for t in events:
 clk=int(any(start<=t<start+1 for start in [1,3,5,7,9]));a=0;b=int(t>=1.5);c=int(t<7.5)
 if not clk:Y=1
 elif c and(a or b):Y=0
 trace.append((t,Y))
check(trace==[(0,1),(1,1),(1.5,0),(2,1),(3,0),(4,1),(5,0),(6,1),(7,0),(7.5,0),(8,1),(9,1),(10,1),(11,1)])
base=Path(__file__).resolve().parents[1];tex=(base/'08_mos.tex').read_text();labels=re.findall(r'\\label\{([^}]+)\}',tex);refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',tex)
check(len(set(labels))==len(labels));check(set(refs)<=set(labels));check(len(re.findall(r'\\section\{Zadatak',tex))==10)
from audit_math import run
run(base,check)
print(f'08: {count} uspešnih provera MOS modela, stvarnih veza, formula, tabela i vremenskih dijagrama.')
