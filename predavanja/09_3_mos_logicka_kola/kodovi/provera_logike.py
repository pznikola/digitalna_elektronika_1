#!/usr/bin/env python3
"""Nezavisne računske provere svih obrađenih MOS tema; ne zamenjuju vizuelni pregled."""
from math import isclose, sqrt, log, exp, prod, floor
from itertools import product
n=0

def same(a,b):
 global n
 assert isclose(a,b,rel_tol=1e-9,abs_tol=1e-12),(a,b)
 n+=1

def check(ok):
 global n
 assert ok
 n+=1

# S004: zbir komponenti kapacitivnosti kanala i dva preklapanja.
for w,l,cox,c0 in [(1,1,1,.1),(4,2,.3,.02),(2,.5,.7,.04)]:
 for parts,total in [((cox*w*l,0,0),cox*w*l),((0,cox*w*l/2,cox*w*l/2),cox*w*l),((0,2*cox*w*l/3,0),2*cox*w*l/3)]:
  same(sum(parts),total);same(sum(parts)+2*c0*w,total+2*c0*w)
# S010: Milerovo preslikavanje iz jednakog prenetog naelektrisanja.
for v in (1.,3.3,5.):
 same(.2*(v-(-v)),(.2*2)*v)
# S011–012: otpornosti i kapacitivnosti skalirane nezavisno.
for r in (1.,2.,4.,9.):
 optimum=sqrt(r)
 delay=lambda b:.69/2*(1+r/b)*((b+.5*b)+(1+.5))
 for b in (.5,1.,2.,3.,4.,8.):
  rn=1.;rp=r/b;cdp=b;cdn=1.;cgp=.5*b;cgn=.5
  same(.69/2*(rn+rp)*(cdp+cdn+cgp+cgn),delay(b))
  check(delay(optimum)<=delay(b)+1e-12)
 same((1+r/optimum)-r*(1+optimum)/optimum**2,0.)
# S016–018: proizvod RC ostaje isti; AM–GM za sve stepenaste odnose.
for k in (.25,1.,4.,16.):
 same((3/k)*(.2*k),3*.2)
for stages in (2,3,4,5):
 for fanout in (16.,64.,256.):
  f=fanout**(1/stages)
  same(prod([f]*stages),fanout)
  caps=[f**i for i in range(stages+1)]
  same(caps[-1],fanout)
  for i in range(1,stages):same(caps[i],sqrt(caps[i-1]*caps[i+1]))
  # Dve dimenzije se pomeraju uz očuvan proizvod odnosa.
  for q in (.3,.8,1.4,3.):
   ratios=[f*q,f/q]+[f]*(stages-2)
   same(prod(ratios),fanout);check(sum(ratios)>=stages*f)
# S020: jedinstven koren f(log f−1)=gamma i stacionarna tačka po N.
lo,hi=2.,5.
for _ in range(70):
 mid=(lo+hi)/2
 if mid*(log(mid)-1)<1:lo=mid
 else:hi=mid
f=(lo+hi)/2
same(f,exp(1+1/f));same(round(f,1),3.6)
for fanout in (64.,256.,1024.):
 stages=log(fanout)/log(f)
 same(1+fanout**(1/stages)-fanout**(1/stages)*log(fanout)/stages,0.)
 delay=lambda m:m*(1+fanout**(1/m))
 for q in (.7,.9,1.1,1.5):check(delay(stages)<delay(stages*q))
# S021–023: normalizovane širine, ukupni fanout i kašnjenje za faktor četiri.
same(floor(3.6+.5),4);same(floor(3.6**2+.5),13)
for stages in (1,3,5):
 caps=[4**i for i in range(stages+1)]
 same(stages+sum(caps[i+1]/caps[i] for i in range(stages)),5*stages)
same(4*4*4,64)
# S026–030: funkcije nezavisno iz provođenja MOS prekidača i dimenzije.
for a,b in product((False,True),repeat=2):
 nor_pun=(not a) and (not b);nor_pdn=a or b
 nand_pun=(not a) or (not b);nand_pdn=a and b
 check(nor_pun!=nor_pdn);check(nand_pun!=nand_pdn)
 check(nor_pun==(not(a or b)));check(nand_pun==(not(a and b)))
# Normirana otpornost Rn=1/W, Rp=2/W; najgore uključeno stanje daje 1.
same(2/4+2/4,1.);same(1/1,1.);same(1/2+1/2,1.);same(2/2,1.)
same(4+4+1+1,10);same(2+2+2+2,8);same((10-8)/10,.2)
# S031–034: dualne mreže, svih 16 kombinacija i najgore putanje otpornosti.
for a,b,c,d in product((False,True),repeat=4):
 pdn=d or ((not a) and (b or c))
 pun=(not d) and (a or ((not b) and (not c)))
 check(pun!=pdn);check(pun==(not(d or ((not a) and (b or c)))))
same(2/4+2/4,1.);same(2/8+2/8+2/4,1.)
same(1/1,1.);same(1/2+1/2,1.)
# S036–039: ulazne kapacitivnosti, karakteristične konstante i skaliranje.
for w in (.5,1.,4.):
 cg=.2;req=3/w
 cin=(w+2*w)*cg
 same(cin,3*w*cg)
 tau=.69*req*cin
 same(tau,.69*3*3*cg)
 same(.69*req*(2*w+2*w)*cg/tau,4/3)
 same(.69*req*(w+4*w)*cg/tau,5/3)
 for fanout in (1,4,16):
  same(.69*req*(.8*cin+fanout*cin),tau*(fanout+.8))
# S035: najveći broj kola sam za sebe ne određuje najveće kašnjenje.
check(len([10,10])<len([1,1,1]) and sum([10,10])>sum([1,1,1]))
# S041–044: minimum susednog para, normalizacija i jednaki napori.
for tau1,tau2 in [(4/3,1.),(1.,5/3),(2.,3.)]:
 for cin,cout in [(1.,16.),(2.,64.),(.5,9.)]:
  cmid=sqrt(tau2/tau1*cin*cout)
  same(tau1/cin-tau2*cout/cmid**2,0.)
  same(tau1*cmid/cin,tau2*cout/cmid)
  delay=lambda cm:tau1*(cm/cin+.75)+tau2*(cout/cm+.5)
  for q in (.8,1.2):check(delay(cmid)<delay(cmid*q))
for le,gamma,p in [(1.,.5,.5),(4/3,.75,1.),(5/3,.9,1.5)]:
 same(le*gamma,p)
 same(le*(4+gamma),le*4+p)
# S045: par običnih izlaza, tabela provodjenja i kratkospojne kombinacije.
for out1,out2 in product((False,True),repeat=2):
 tn1,tp1,tn2,tp2=not out1,out1,not out2,out2
 conflict=(tn1 and tp2) or (tn2 and tp1)
 check(conflict==(out1!=out2))
 check((tn1!=tp1) and (tn2!=tp2))
# S046–050: trostatički izlaz, otvoreni drejn i jedan prolazni prekidač.
for a,e in product((False,True),repeat=2):
 tristate=(not a) if e else 'Z'
 check((tristate=='Z')==(not e))
 if e:check(tristate==(not a))
for a in (False,True):
 od=0 if a else 'Z'
 check((od=='Z')==(not a))
for states in product((False,True),repeat=4):
 # Četiri izlaza OD i jedan zajednički pull-up.
 output=not any(states)
 check(output==all(not x for x in states))
for a,b in product((False,True),repeat=2):
 ptl=b if a else 'Z'
 check((ptl=='Z')==(not a))
 if a:check(ptl==b)

# S051–056: NMOS passes zero, high level loses one threshold; series
# source/drain cascade loses one threshold, gate-driven cascade accumulates it.
for vdd,vt in [(3.3,.6),(5.,.8),(12.,1.)]:
 high=min(vdd,vdd-vt)
 same(high,vdd-vt)
 series=vdd
 for _ in range(3):series=min(series,vdd-vt)
 same(series,high)
 gate=vdd
 for _ in range(3):gate=min(vdd,gate-vt)
 same(gate,vdd-3*vt)
 check(gate<series)
for a,b,c in product((False,True),repeat=3):
 mux=b if a else c
 check(mux==((a and b) or (not a and c)))
for a,b in product((False,True),repeat=2):
 same(int(b if a else False),int(a and b))
 same(int(b if a else a),int(a and b))
 same(int(True if a else b),int(a or b))
 same(int(a if a else b),int(a or b))
# S057: independent decoded one-hot MUX versus two series selection switches.
for data in product((False,True),repeat=4):
 for s1,s0 in product((False,True),repeat=2):
  idx=2*int(s1)+int(s0)
  paths=[((s0 if i%2 else not s0) and (s1 if i>=2 else not s1)) for i in range(4)]
  same(sum(paths),1)
  check(any(paths[i] and data[i] for i in range(4))==data[idx])
# S058: two adjacent slices select their neighbor or their own bit.
for a_hi,a_i,a_lo,a_low in product((False,True),repeat=4):
 for right,nop,left in [(1,0,0),(0,1,0),(0,0,1)]:
  out_i=(right and a_hi) or (nop and a_i) or (left and a_lo)
  out_lo=(right and a_i) or (nop and a_lo) or (left and a_low)
  check((out_i,out_lo)==((a_hi,a_i) if right else (a_i,a_lo) if nop else (a_lo,a_low)))
# S059: preserve the source's interrupted vertical data columns. Top
# segments carry A3; below each gap column c carries Ac. This is arithmetic
# right shift with sign extension, including the four original A3 junctions.
for word in range(16):
 bits=[bool(word&(1<<i)) for i in range(4)]
 for shift in range(4):
  out=[]
  for row in range(4):
   selected=[col for col in range(4) if (row+col+1)%4==shift]
   same(len(selected),1)
   col=selected[0]
   out.append(bits[col] if row>=3-col else bits[3])
  value=sum(int(b)<<(3-r) for r,b in enumerate(out))
  signed=word if word<8 else word-16
  same(value,(signed>>shift)&15)
# S060–066: both MOS conduct at active ±15V controls for |Vi|<=12V,
# threshold magnitude below 3V. Inactive controls block both devices.
for vi in (-12.,-6.,0.,6.,12.):
 for vt in (.5,1.,2.):
  check(15-vi>vt and vi+15>vt)
  check(-15-vi<vt and vi-15<vt)
  rn=1/(15-vi-vt);rp=1/(15+vi-vt)
  req=rn*rp/(rn+rp)
  check(0<req<min(rn,rp))
for s,a,b in product((False,True),repeat=3):
 before=(s and a) or (not s and b)
 y=not before
 check((not y)==((s and a) or (not s and b)))
# S067: solve the question independently; answer is deliberately not added
# to the slide. B=0 passes A; B=1 makes the left branch a usual inverter.
for a,b in product((False,True),repeat=2):
 result=a if not b else not a
 check(result==(a!=b))
# S068–071: precharge and monotone evaluation, with optional output inverter.
for path in (False,True):
 dynamic_precharge=True
 dynamic_evaluate=not path
 domino_precharge=not dynamic_precharge
 domino_evaluate=not dynamic_evaluate
 check(not domino_precharge)
 check(domino_evaluate==path)
 check(int(dynamic_evaluate)<=int(dynamic_precharge))
# Two bare dynamic inverters can discharge the second node before the first
# falls; one may not assume a discharged dynamic node recharges in evaluate.
second=1.
for _ in range(3):second*=.6
check(second<.5)
print(f'09_3: {n} nezavisnih računskih provera prošlo.')
