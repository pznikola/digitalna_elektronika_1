#!/usr/bin/env python3
"""Nezavisne provere rekonstruisanih predavanja; dopuniti tokom rekonstrukcije."""
from math import isclose, exp, log
n=0
def same(a,b):
 global n
 assert isclose(a,b,rel_tol=1e-9,abs_tol=1e-12),(a,b)
 n+=1
def check(ok):
 global n
 assert ok
 n+=1
# Diode with series resistor, forward model and reverse recovery current.
for vh,vl,r in [(5.,-5.,1000.),(3.3,-1.,470.),(12.,-2.,2200.)]:
 for vd in (.3,.6,.7):
  ih=(vh-vd)/r;il=(vl-vd)/r
  same(vh-ih*r,vd);same(vl-il*r,vd)
  check(ih>0 and il<0)
# KCL and normal active current gain, independent beta/IB sweep.
for beta in (20.,50.,100.,200.):
 for ib in (1e-6,10e-6,100e-6):
  ic=beta*ib;ie=ic+ib
  same(ie,(beta+1)*ib)
  same(ie-ic,ib)
# Model voltage identity; original text confuses BC and CE near saturation.
for vbe,vce in [(.6,2.),(.7,.1),(.7,.2)]:
 vbc=vbe-vce
 same(vbe-vbc,vce)
 same(-vbe,-(vbc+vce))
same(.7-.1,.6)
# Load-limited IC versus available beta*IB at the saturation boundary.
for vcc,rc,beta in [(5.,1000.,100.),(3.3,2200.,50.),(12.,4700.,200.)]:
 ic=(vcc-.1)/rc;ib_boundary=ic/beta
 same(beta*ib_boundary,ic)
 check(beta*(2*ib_boundary)>ic)

# S009: matched RC voltage divider, checked at nonzero complex frequencies.
for rb,rbe,cb in [(1000.,4000.,1e-9),(4700.,1000.,2e-9),(2200.,2200.,1e-9)]:
 cbe=rb*cb/rbe
 for omega in (0.,1e3,1e5,1e7):
  z1=rb/(1+1j*omega*rb*cb);z2=rbe/(1+1j*omega*rbe*cbe)
  h=z2/(z1+z2)
  same(h.real,rbe/(rb+rbe));same(h.imag,0.)
# S011–020: KCL-derived transfer, numerical slope, both discrete saturation
# boundaries and all three forms of VM, without correcting source slides.
for vcc,rb,rc,beta in [(5.,10000.,1000.,100.),(3.3,47000.,2200.,200.),(12.,22000.,1000.,50.)]:
 vbe,vbes,vces,vgamma=.6,.7,.1,.5
 gain=beta*rc/rb
 transfer=lambda vi:vcc-rc*beta*((vi-vbe)/rb)
 check((0-vbe)/rb<0);check((0-vbes)/rb<0)
 same(vcc-rc*0,vcc)
 for vi in (.65,.7,.8):
  ib=(vi-vbe)/rb;ic=beta*ib;vo=vcc-rc*ic
  same(vi-rb*ib-vbe,0.)
  same(vo,transfer(vi))
  same(vo,vcc-gain*(vi-vbe))
 same((transfer(.9)-transfer(.8))/.1,-gain)
 check(transfer(vgamma)>vcc)
 vi1=rb/(beta*rc)*(vcc-vces)+vbe
 vi2=rb/(beta*rc)*(vcc-vces)+vbes
 same(transfer(vi1),vces)
 same(beta*(vi2-vbes)/rb,(vcc-vces)/rc)
 same(vi2-vi1,vbes-vbe)
 vm=(vcc+gain*vbe)/(1+gain)
 same(transfer(vm),vm)
 same(vm,vbe*(vcc/vbe+gain)/(1+gain))
 same(vm,vbe*((vcc/vbe-1)/(1+gain)+1))
 same((vm-vces)+(vcc-vm),vcc-vces)
 same((vgamma-vces)+(vi1-vgamma)+(vcc-vi1),vcc-vces)
# S021–027: fanout and signed IOH from independent KCL balances.
for vcc,rb,rc,beta in [(5.,10000.,1000.,100.),(3.3,47000.,2200.,200.),(12.,22000.,1000.,50.)]:
 vbes,vces=.7,.1
 vohmin=.8*vcc
 iih=(vcc-vbes)/rb
 ioh=(vohmin-vcc)/rc
 same(vcc+rc*ioh,vohmin);check(ioh<0)
 iol=beta*(vohmin-vbes)/rb-(vcc-vces)/rc
 same((vcc-vces)/rc+iol,beta*(vohmin-vbes)/rb)
 vih=vbes+rb*(vcc-vces)/(beta*rc)
 same(beta*(vih-vbes)/rb-(vcc-vces)/rc,0)
 nh=abs(ioh)/iih
 same(nh,rb/rc*(vcc-vohmin)/(vcc-vbes))
 check(nh<rb/rc)
# S029–032: RC charge/discharge, derivative/KCL and inverse event times.
for vcc,rb,rc,beta,cap in [(5.,10000.,1000.,100.,1e-9),(3.3,47000.,2200.,200.,2e-9),(12.,22000.,1000.,50.,5e-10)]:
 tau=rc*cap;vol=.1;vh=.8*vcc;ib=(vh-.6)/rb;asym=vcc-rc*beta*ib
 check(asym<vol)
 charge=lambda t:vcc+(vol-vcc)*exp(-t/tau)
 discharge=lambda t:asym+(vcc-asym)*exp(-t/tau)
 same(charge(0),vol);same(discharge(0),vcc)
 for x in (.1,.5,1.,2.):
  t=x*tau
  dc=(vcc-vol)/tau*exp(-x)
  same(cap*dc,(vcc-charge(t))/rc)
  dd=-(vcc-asym)/tau*exp(-x)
  same(cap*dd,(vcc-discharge(t))/rc-beta*ib)
 saturation=tau*log((vcc-asym)/(vol-asym))
 same(discharge(saturation),vol)
 midpoint=(vcc+vol)/2
 tphl=tau*log((vcc-asym)/(midpoint-asym))
 same(discharge(tphl),midpoint);check(0<tphl<saturation)
 high=.9*vcc+.1*vol;low=.1*vcc+.9*vol
 t90=tau*log((vcc-asym)/(high-asym));t10=tau*log((vcc-asym)/(low-asym))
 same(t10-t90,tau*log((high-asym)/(low-asym)))
 check(not isclose((t10-t90)/tau,log(9),rel_tol=.01))
# S033: Thevenin transformation checked directly against nodal KCL.
for rb,rn,vn in [(10000.,4700.,5.),(4700.,10000.,3.),(2200.,2200.,2.)]:
 rt=rb*rn/(rb+rn)
 for vi in (0.,1.,3.,5.):
  et=(vi/rb-vn/rn)/(1/rb+1/rn)
  same(et,vi*rn/(rb+rn)-vn*rb/(rb+rn))
  same((vi-et)/rb,(et+vn)/rn)
 vil=(1+rb/rn)*.5+rb/rn*vn
 same(vil*rn/(rb+rn)-vn*rb/(rb+rn),.5)
# S034–036: wired low dominates, floating all-off is Z, not logic 1.
from itertools import product
mismatches=0
for a,b in product((False,True),repeat=2):
 same(int(not(a or b)),int((not a) and (not b)))
for a,b,c,d in product((False,True),repeat=4):
 outputs=(not a,not(b and c),c or d)
 wire_with_rc=all(outputs)
 original_formula=(not a) and not(b and c) and (c and d)
 mismatches+=wire_with_rc!=original_formula
 without_rc='Z' if all(outputs) else 0
 check((without_rc=='Z')==wire_with_rc)
check(mismatches>0)
# S039–042: two-input diode logic from piecewise voltage constraints.
for vd in (.3,.6,.7):
 for a,b in product((0.,5.),repeat=2):
  vor=max(0.,a-vd,b-vd)
  vand=min(5.,a+vd,b+vd)
  same(int(vor>2.5),int(a>2.5 or b>2.5))
  same(int(vand>2.5),int(a>2.5 and b>2.5))
  check(vor>=0 and vand<=5)
  if a>b:same(vor,a-vd);check(b-vor<0)
# S046–049: affine DTL model, noise margins, base current and dynamics.
for vcc,vd,vgt,vgd,vbes,vces,rd,rb,rc,beta in [(5.,.6,.5,.5,.7,.1,4000.,1000.,1600.,50.),(5.,.7,.5,.5,.7,.1,4000.,2200.,1000.,100.),(3.3,.6,.45,.45,.7,.1,2200.,4700.,1000.,50.)]:
 vil=vd+vgt;vih=2*vd+vbes-vgd
 a=(vcc-vces)/(vil-vih)
 same(a,-(vcc-vces)/(vd+vbes-vgd-vgt))
 transfer=lambda vi:a*(vi-vil)+vcc
 same(transfer(vil),vcc);same(transfer(vih),vces)
 vm=(vcc-a*vil)/(1-a)
 same(transfer(vm),vm);check(vil<vm<vih)
 same(vil-vces,vd+vgt-vces)
 same(vcc-vih,vcc-2*vd-vbes+vgd)
 same((vm-vces)+(vcc-vm),vcc-vces)
 ib=(vcc-2*vd-vbes)/rd-vbes/rb
 same((vcc-2*vd-vbes)/rd,ib+vbes/rb)
 iol=beta*ib-(vcc-vces)/rc
 same(beta*ib,(vcc-vces)/rc+iol);check(iol>0)
 asym=vces-rc*iol
 same(asym,vcc-rc*beta*ib)
 tau=rc*1e-9
 endtime=tau*log(1+(vcc-vces)/(rc*iol))
 same(asym+(vcc-asym)*exp(-endtime/tau),vces)
# S052: original terminal currents in reverse-active operation; KCL.
for beta in (.2,.5,1.,2.,4.):
 for ib in (1e-6,10e-6,100e-6):
  ie=-beta*ib;ic=-(beta+1)*ib
  same(ic,ie-ib)
  same(-ie,beta*ib);same(-ic,(beta+1)*ib)
# S057–061: NAND behavior and terminal current budgets.
for a,b in product((False,True),repeat=2):
 input_forward=not(a and b)
 output_low=not input_forward
 same(int(not output_low),int(not(a and b)))
for vcc in (3.3,5.,5.5):
 vg,vd,vc,vbe,vbes=.5,.6,.1,.6,.7
 voh=vcc-vg-vd;vol=vc;vil=-vc+vg;vih=-vc+vbe+vbes
 same(voh-vih,vcc-vg-vd+vc-vbe-vbes)
 same(vil-vol,-vc+vg-vc)
 check(not isclose(vcc-vg+vd,voh)) # original +VD4 error
 for beta in (.2,1.,4.):
  ib=(vcc-vd-2*vbes)/4000
  for inputs in (2,3,4):
   each=beta*ib/inputs
   same(inputs*each,beta*ib)
for beta in (20.,50.,100.):
 vcc,vc,vbes,rc2,re2=5.,.1,.7,1600.,1000.
 ic2=(vcc-vc-vbes)/rc2;ib2=ic2/beta;ie2=ic2+ib2
 ib3=ie2-vbes/re2;iol=beta*ib3
 same(iol,(beta+1)*(vcc-vc-vbes)/rc2-beta*vbes/re2)
# S058/062: follower KVL, branch currents and both inequality directions.
for beta in (20.,50.,100.):
 rb=1600.;vcc=5.;vbe=.6;vd=.6;vc=.1;avail=vcc-vbe-vd
 for gain in (0.,.5,.9,1.1,2.,5.):
  rc=gain*rb/beta
  threshold=avail+(vbe-vc)/(1-gain)
  for vo in (0.,1.,2.,3.):
   ib=(avail-vo)/rb;ic=beta*ib;ie=ib+ic
   vce=vcc-rc*ic-(vo+vd)
   same(vce,vbe+(1-gain)*(avail-vo))
   same(ib,ie/(beta+1));same(ic,beta/(beta+1)*ie)
   check((vce>vc)==(vo<threshold if gain<1 else vo>threshold))

# S063–066: independent capacitor KCL and exponential/linear delay checks.
for beta in (20.,50.,100.):
 for rb,rc,c in [(1600.,130.,15e-12),(760.,50.,30e-12),(20000.,500.,10e-12)]:
  vcc,vbe,vd,vces,vl=5.,.7,.6,.1,.1
  active_inf=vcc-vbe-vd;ta=c*rb/(beta+1)
  sat_inf=vcc-vces-vd-rc*(vbe-vces)/(rb+rc);ts=c*rb*rc/(rb+rc)
  for t in (0.,.25*ta,ta,2*ta):
   vo=active_inf+(vl-active_inf)*exp(-t/ta)
   derivative=(active_inf-vl)/ta*exp(-t/ta)
   ib=(vcc-vbe-vd-vo)/rb
   same(c*derivative,(beta+1)*ib)
  for t in (0.,ts,2*ts):
   vo=sat_inf+(vl-sat_inf)*exp(-t/ts)
   derivative=(sat_inf-vl)/ts*exp(-t/ts)
   ib=(vcc-vbe-vd-vo)/rb;ic=(vcc-vces-vd-vo)/rc
   same(c*derivative,ib+ic)
  if beta*rc>rb:
   ib=(vbe-vces)/(beta*rc-rb);ic=beta*ib
   same(rb*ib+vbe,rc*ic+vces)
   threshold=vcc-rb*ib-vbe-vd
   t_original=ta*log((active_inf-vl)/(active_inf-threshold))
   same(t_original,ta*log((rc*beta-rb)/rb*(vcc-vbe-vd-vl)/(vbe-vces)))
   t_saturated=ts*log((sat_inf-vl)/(sat_inf-threshold))
   check(not isclose(t_original,t_saturated,rel_tol=1e-3,abs_tol=1e-15))
for c,iol,voh,vol in [(15e-12,.008,3.5,.2),(30e-12,.016,4.,.1)]:
 delay=c*(voh-vol)/(2*iol)
 same(voh-iol/c*delay,(vol+voh)/2)
# S068/070: Darlington base loading and Schottky clamp terminal currents.
for beta in (20.,50.,100.):
 vcc,rc,re,vbe,vg=5.,760.,4000.,.7,.5
 load=(vcc-vbe-vg)/(rc+beta*re)
 same(load*(rc+beta*re),vcc-vbe-vg)
 for ib,ids in [(1e-4,0.),(1e-4,1e-6),(1e-4,1e-5)]:
  ibi=ib-ids;ici=beta*ibi;ic=ici-ids
  same(ic,beta*ib-(beta+1)*ids)
  same(ici,ic+ids)
  check(ic<=beta*ib)

# S076/078/093: independent output-state logic, contention, ECL OR/NOR.
for a,b in product((False,True),repeat=2):
 check((a!=b)==(int(a)+int(b)==1))
 collector1_low=a or b; collector2_low=not collector1_low
 same(int(not collector1_low),int(not(a or b)))
 same(int(not collector2_low),int(a or b))
# S082–089: ideal tail-current KCL and KVL, both transfer extremes, midpoint,
# noise margins and emitter-follower shift. No assumption that IE2=IE at midpoint.
for vcc,rc,ie in [(0.,220.,.002),(5.,245.,.002),(-.2,300.,.002)]:
 vbe,vg,vces=.7,.5,.1
 voh=vcc;vol=vcc-rc*ie;vr=(voh+vol)/2
 vil=vg-vbe+vr;vih=vbe-vg+vr
 same(vr,vcc-rc*ie/2)
 same(voh-vih,vil-vol)
 same(voh-(vbe-vg)-(voh-vih),vr)
 same(vol+(vbe-vg)+(vil-vol),vr)
 check(vol<vil and vih<voh)
 for fraction in (0.,.25,.5,.75,1.):
  i1=ie*fraction;i2=ie-i1
  o1=vcc-rc*i1;o2=vcc-rc*i2
  same(i1+i2,ie);same(o1+o2,2*vcc-rc*ie)
  same(o1-(o1-vbe),vbe)
  same(o2-(o2-vbe),vbe)
 same(vcc-rc*ie/2,(voh+vol)/2)
 check(not isclose(vcc-rc*(ie/2)/2,(voh+vol)/2)) # S084 IE2/2 error
 vb2=vr;ve2=vb2-vbe;vc2=vcc-rc*ie
 same(vc2-ve2,vbe-rc*ie/2);check(vc2-ve2>vces)
 sat_vi=vcc-rc*ie-vces+vbe
 same(vcc-rc*ie-(sat_vi-vbe),vces)
 same(sat_vi-vbe+vces,vol)
 # S090: supply perturbations and source formula's missing quiescent current.
 for delta in (-.1,0.,.1):
  baseline=vcc-rc*ie-vbe
  shifted=vcc+delta-rc*ie-vbe
  same(shifted-baseline,delta)
  rie=10000.;di=delta/rie
  changed=vcc-rc*(ie+di)-vbe
  same(changed-baseline,-rc*delta/rie)
  check(not isclose(changed,vcc-rc*di-vbe))
 # S092: the stated exponential model reaches its midpoint at the log delay;
 # the rising-event label tpHL in the source does not change the mathematics.
 voh-=vbe;vol-=vbe;mid=(voh+vol)/2;c=15e-12;rb=50000.;vee=-5.2
 fall=c*rb*log((voh-vee)/(mid-vee))
 same(vee+(voh-vee)*exp(-fall/(c*rb)),mid)
 beta=100.;tau=c*rc/beta
 rise=tau*log((vol-vcc)/(mid-vcc))
 same(vcc+(vol-vcc)*exp(-rise/tau),mid)
# S094/S095: corresponding PECL and NECL voltage specifications must differ
# by the same 5 V common-mode shift, preserving all blank cells and columns.
import re
from pathlib import Path
lecture=Path(__file__).resolve().parents[1]
a=(lecture/'tabele/s094_pecl_dc_karakteristike.tex').read_text().splitlines()
b=(lecture/'tabele/s095_necl_dc_karakteristike.tex').read_text().splitlines()
for symbol in ('OH','OL','IH','IL'):
 token='V_{\\mathrm{'+symbol+'}}'
 aa=next(line for line in a if token in line).split('&')[2:11]
 bb=next(line for line in b if token in line).split('&')[2:11]
 for x,y in zip(aa,bb):
  if not x.strip() or not y.strip():check(not x.strip() and not y.strip())
  else:same(float(re.search(r'-?\d+',x).group()),float(re.search(r'-?\d+',y).group())+5000)
print(f'10: {n} nezavisnih računskih provera prošlo (modeli, logika, dinamika i PECL/NECL pomeraj).')
