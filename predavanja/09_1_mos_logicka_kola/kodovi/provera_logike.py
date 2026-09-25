"""Nezavisne računske provere; ilustrativni parametri nisu novi podaci slajdova.
Greške izvornika se potvrđuju kao protivprimeri, ne ispravljaju u prezentaciji.
Pokretanje: python3 kodovi/provera_logike.py (samo standardna biblioteka).
"""
from fractions import Fraction as F
from math import sqrt, isclose
from itertools import product

checks = 0

def eq(a, b):
    global checks
    assert isclose(a, b, rel_tol=2e-8, abs_tol=2e-8), (a, b)
    checks += 1

def bisect(f, lo, hi):
    assert f(lo) * f(hi) <= 0
    for _ in range(100):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2

def derivative(f, x):
    h = 1e-5
    return (f(x+h)-f(x-h))/(2*h)

# S10–11: NMOS vodi za 1, PMOS za 0; redne i paralelne veze.
for a, b in product((False, True), repeat=2):
    eq(not (a and b), (not a) or (not b))
    eq(not (a or b), (not a) and (not b))
# S3–8: jednakost na granici dugog kanala i algebra kratkog kanala.
for k, u, le in product((.2, 1., 2.), (.3, 1., 3.), (.1, 1., 10.)):
    eq(k/2*(2*u*u-u*u), k/2*u*u)
    eq(k/2/(1+u/le)*u*u, k/2*le/(le+u)*u*u)
    eq(u/(1+u/le), u*le/(le+u))
# S19,21: ravnoteža struja i izvod za jedinično pojačanje.
for vdd, k, r, vt in product((3., 5.), (1., 2.), (2., 4.), (.4, .8)):
    vi = vt+1/(k*r); vo=vdd-1/(2*k*r)
    eq((vdd-vo)/r, k/2*(vi-vt)**2)
    eq(derivative(lambda x: vdd-r*k/2*(x-vt)**2, vi), -1)
    vo=sqrt(2*vdd/(3*k*r)); vi=vt+2*vo-1/(k*r)
    eq((vdd-vo)/r,k/2*(2*vo*(vi-vt)-vo*vo))
    eq(-k*vo/(1/r+k*(vi-vt-vo)), -1)
# S24: koren početne ravnoteže naspram eksplicitne kvadratne jednačine.
for vdd, vt, k, r, le in product((1.2, 5.), (.2, .4), (.5, 2.), (1., 3.), (.1, 2.)):
    root=bisect(lambda v: (vdd-v)/r-k/2*le/(le+v-vt)*(v-vt)**2, vt, vdd)
    a=k*le/2+1/r; b=(le-vdd+vt)/r; c=-le*(vdd-vt)/r
    eq(root, vt+(-b+sqrt(b*b-4*a*c))/(2*a))
# S32–33: tačni integrali polinoma daju 5/6 i 7/9.
v=F(1); endpoint_linear=(v*v+(v/2)**2)/2
endpoint_const=(v+v/2)/2
eq(endpoint_linear/endpoint_const, F(5,6))
integral_const=2*(v*v/2-(v/2)**2/2)
integral_linear=2*(v**3/3-(v/2)**3/3)
eq(integral_const,F(3,4)); eq(integral_linear/integral_const,F(7,9))
# S39–42: faktorizacija aktivnog opterećenja i zamena rešenja VIL.
for kl, kd, d in product((.1,.2), (1.,2.), (.2,.5)):
    vdd=5.; vt=.7; vc=vdd+vt+d
    vo=vdd+d*(1-sqrt(kd/(kd-kl)))
    vi=vt+d*kl/kd*sqrt(kd/(kd-kl))
    eq(kl*(2*(vc-vo-vt)*(vdd-vo)-(vdd-vo)**2),kl*(vdd-vo)*(vdd+2*d-vo))
    eq(kl*(vdd-vo)*(vdd+2*d-vo),kd*(vi-vt)**2)
    eq(kl*(vdd+d-vo),kd*(vi-vt))
# S47: zajedničko skaliranje širina čuva odnos k.
for w1,w2,factor in product((1.,3.),(2.,5.),(.5,10.)):
    eq(w1/w2, factor*w1/(factor*w2))
# S52: izvod linearnog rešenja, uključujući izuzetak kl=kd.
for kl,kd in product((.1,1.),(1.,2.)):
    eq(derivative(lambda vi: 5-.7-sqrt(kd/kl)*(vi-.6),1.),-sqrt(kd/kl))
# S56: implicitni VOH sa efektom polarizacije osnove, nezavisna provera korena.
for vdd,gamma in product((1.2,5.),(.2,.5)):
    vt=.4; phi=.6
    vo=bisect(lambda x: x-vdd+vt+gamma*(sqrt(phi+x)-sqrt(phi)),0,vdd-vt)
    eq(vo,vdd-vt-gamma*(sqrt(phi+vo)-sqrt(phi)))
    assert 0 < vo < vdd-vt
# Protivprimeri grešaka originala (s14,44–47,51,53–55).
vdd=5.; vt=1.; kr=1.
wrong=vt+sqrt(2*vdd/kr); correct=vt+(-1+sqrt(1+2*kr*vdd))/kr
assert not isclose(wrong,correct)
eq(vdd-(correct-vt),kr/2*(correct-vt)**2)
# d[vo*(2vi-2vt-vo)]/dvi za vo'=-1 iznosi 4vo-2vi+2vt.
vi,vo,vt=2.,.5,.7
actual=derivative(lambda t:(vo-t)*(2*(vi+t)-2*vt-(vo-t)),0)
eq(actual,4*vo-2*vi+2*vt)
assert not isclose(actual,2*vo-2*vi+2*vt)
vc,vdd,vtl=7.,5.,.7; delta=vc-vdd-vtl
eq(vdd+2*delta,2*vc-vdd-2*vtl)
assert not isclose(vdd+2*delta,2*vc-vdd-vtl)
# S45 i 54: štampani koreni ne zadovoljavaju početnu ravnotežu struja.
kl,kd,vtd=.2,1.,.7
for a,b in ((vc-vtl,vc-vdd-vtl),(vdd-vtl,0.)):
    root=sqrt(1+kd/kl*(1-b*b/(a*a)))
    vo=kl/kd*a*(1+root); vi=vtd+kl/kd*a*root
    load=kl*((a-vo)**2-b*b)
    drive=kd*vo*(2*vi-2*vtd-vo)
    assert not isclose(load,drive)
# S51: posle zamene VI koeficijent je kl²/kd, umesto štampanog kl.
assert not isclose(kl*kl/kd,kl)
# S55: VOH=VDD-VTl mora se pojaviti i u imeniocu.
assert not isclose(vdd-vtd,vdd-vtl-vtd)
print(f'MOS: {checks} nezavisnih računskih poređenja; protivprimeri grešaka originala potvrđeni.')
