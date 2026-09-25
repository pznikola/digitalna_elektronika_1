#!/usr/bin/env python3
"""Nezavisne provere modela; poznate greške izvora potvrđuju se kontraprimerom.
Ne menjaju tekst prezentacije. SI jedinice; struje se porede i u normiranom obliku.
"""
from math import isclose, sqrt

broj = 0

def isto(a, b):
    global broj
    assert isclose(a, b, rel_tol=1e-8, abs_tol=1e-12), (a, b)
    broj += 1

def uslov(a):
    global broj
    assert a
    broj += 1

def omski(k, vg, vd, vt):
    return k * ((vg-vt)*vd-vd*vd/2)

def zas(k, vg, vt):
    return k*(vg-vt)**2/2

def nagib(fn, x, y):
    h=1e-5
    return -(fn(x+h,y)-fn(x-h,y))/(fn(x,y+h)-fn(x,y-h))

# S007–009: ugrađeni kanal, jednakost struja i jedinično pojačanje.
for kl in (.05, .1, .2):
    kd=1.; vtl=-1.; vtn=.7; vdd=5.
    vo=-vtl*sqrt(kl/(3*kd)); vi=vtn+2*vo
    f=lambda i,o: omski(kd,i,o,vtn)-zas(kl,0,vtl)
    isto(f(vi,vo),0); isto(nagib(f,vi,vo),-1)
    approx=kl/kd*vtl**2/(2*(vdd-vtn))
    exact=vdd-vtn-sqrt((vdd-vtn)**2-kl/kd*vtl**2)
    uslov(0<approx<=exact and abs(approx/exact-1)<.01)
    beta=kd/kl
    uslov((vo<vtn)==(beta>(-vtl/vtn)**2/3))
    # S004: ispravan fizički koren i pogrešan koren štampan u izvoru.
    vi=vtn-vtl*kl/kd/sqrt(1+kl/kd)
    vo=vdd+vtl*(1-1/sqrt(1+kl/kd))
    f=lambda i,o: omski(kl,0,vdd-o,vtl)-zas(kd,i,vtn)
    isto(f(vi,vo),0); isto(nagib(f,vi,vo),-1)
    wrong=vdd+vtl*(1+1/sqrt(1+kl/kd))
    uslov(vdd-wrong>-vtl) # van pretpostavljene omske oblasti TL
    uslov(abs(nagib(f,vi,wrong)+1)>.1)

# S018,020–022: pseudo NMOS; izlazni nivo i prag, beta i skaliranje W.
for kp in (.02,.05,.1):
    kn=1.; vd=5.; tn=1.; tp=-1.
    vo=(vd+tp)*sqrt(kp/(3*kn)); vi=tn+2*vo
    f=lambda i,o: omski(kn,i,o,tn)-zas(kp,-vd,tp)
    isto(f(vi,vo),0); isto(nagib(f,vi,vo),-1)
    approx=.5*kp/kn*(vd-tn)
    isto(approx,.5*kp/kn*(-vd-tp)**2/(vd-tn))
    uslov((approx<tn)==(kn/kp>(vd-tn)/(2*tn)))
    uslov((vo<tn)==(kn/kp>((vd-tn)/tn)**2/3))
    for factor in (.1,2.,10.): isto(kp/kn,factor*kp/(factor*kn))
    # S018: VOIL je dobar; VIL ima kp umesto kn ispod korena.
    vo=-tp+(vd+tp)*sqrt(kn/(kn+kp))
    vi=tn+(vd+tp)*kp/kn*sqrt(kn/(kp+kn))
    f=lambda i,o: omski(kp,vd,vd-o,-tp)-zas(kn,i,tn)
    isto(f(vi,vo),0); isto(nagib(f,vi,vo),-1)
    wrong=tn+(vd+tp)*kp/kn*sqrt(kp/(kp+kn))
    uslov(abs(f(wrong,vo))>.001)

# S028,034,036–040: simetrični CMOS i dimenzionisanje dugog kanala.
for vd in (3.3,5.,9.):
    tn=.7; tp=-tn
    vil=(3*vd+2*tn)/8; voil=(7*vd+2*tn)/8
    vih=(5*vd-2*tn)/8; voih=(vd-2*tn)/8
    f=lambda i,o: omski(1.,vd-i,vd-o,tn)-zas(1.,i,tn)
    isto(f(vil,voil),0); isto(nagib(f,vil,voil),-1)
    g=lambda i,o: zas(1.,vd-i,tn)-omski(1.,i,o,tn)
    isto(g(vih,voih),0); isto(nagib(g,vih,voih),-1)
    isto(vil,vd-vih); isto(voil,vd-voih)
    for r in (.5,1.,2.):
        vs=(tn+r*(vd+tp))/(1+r)
        isto(zas(r*r,vs-vd,tp),zas(1.,vs,tn))
        isto(r,(vs-tn)/(vd-vs+tp))
        isto(2.5*r*r,2.5*((vs-tn)/(vd-vs+tp))**2)

# S041–043: model zasićenja brzine, nezavisno poređenje struja.
for vs in (1.5,2.5,3.5):
    vd=5.; tn=.6; tp=-.6; mun=2.; mup=1.; an=1.; ap=2.
    x=vs-tn; y=vd-vs+tp
    ratio=(1+ap/y)/(1+an/x)*x/y
    ip=mup*ratio*y*y/(1+y/ap)
    inn=mun*x*x/(1+x/an)
    isto(ip,inn)
    ratio2=(mun/mup)*(1+y/ap)/(1+x/an)*(x/y)**2
    isto(ratio,ratio2)
for scale in (1e5,1e6):
    x=1.9; ratio=(x+2*scale)/(x+scale)
    uslov(abs(ratio-2)<2e-5) # dugi kanal
# S044: linearni model sa pozitivnim i negativnim predznacima.
for r in (.5,1.,2.):
    vd=5.; tn=.6; tp=-.6; dsn=.2; dsp=-.4
    vs=(tn+dsn/2+r*(vd+tp+dsp/2))/(1+r)
    isto(r*(-1)*(vs-vd-tp-dsp/2),vs-tn-dsn/2)
# S045: pretpostavka jednakih L i |vsat| daje OBRNUT odnos pokretljivosti.
mun=2.; mup=1.; dsn=1/mun; dsp=-1/mup
isto(dsn/abs(dsp),mup/mun)
uslov(not isclose(dsn/abs(dsp),mun/mup))

# S048,053: zaokruživanje širine i procena trajanja baterije.
isto(2.376*10,23.76); isto(round(2.376*10),24)
isto(10**9*1e-9,1.); isto(1./(10**9*1e-9),1.)
# S055–061: integral RC punjenja, disipacija, PDP i EDP.
for c in (1e-12,10e-12):
    for vd in (1.,3.3,5.):
        # Integral V dq iz izvora; integral u dq u kondenzatoru.
        q=c*vd
        ev=vd*q; ec=q*q/(2*c); ep=ev-ec; en=ec
        isto(ev,c*vd*vd); isto(ep,en); isto(ep+en,c*vd*vd)
        f=1e8; delay=1/(2*f)
        pdyn=(ep+en)*f; pdp=pdyn*delay
        isto(pdp,ec); isto(pdp*delay,c*vd*vd*delay/2)
# S058–059: interval provodjenja iz dve granice rampe i povrsina dva trougla.
for vd in (3.3,5.):
    vt=.7; ts=1e-9; isc=.001; f=1e8
    on=ts*vt/vd; off=ts*(vd-vt)/vd; tsc=off-on; tr=.8*ts
    isto(tsc,(vd-2*vt)/vd*tr/.8)
    charge=2*(.5*isc*tsc)
    isto(vd*charge,isc*(vd-2*vt)*tr/.8)
    isto(vd*charge*f,isc*(vd-2*vt)*tr/.8*f)
# S062: EDP ~ V^3/(V-VTe), minimum na 3VTe/2 u oblasti V>VTe.
for vte in (.2,.5,1.):
    vopt=1.5*vte
    e=lambda v:v**3/(v-vte)
    for factor in (.7,.8,.9,1.1,1.2,2.,10.):
        uslov(e(vopt)<e(vopt*factor))
    h=1e-5*vte
    uslov(abs((e(vopt+h)-e(vopt-h))/(2*h))<1e-7)
print(f'09_2: {broj} računskih provera prošlo; kontraprimeri grešaka izvora potvrđeni.')
