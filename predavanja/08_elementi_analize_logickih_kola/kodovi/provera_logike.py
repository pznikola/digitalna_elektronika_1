#!/usr/bin/env python3
"""Nezavisne računske provere; izvorne greške se ne prepravljaju."""
from math import exp, log, isclose
from fractions import Fraction as F


def close(a, b):
    assert isclose(a, b, rel_tol=1e-10, abs_tol=1e-10), (a, b)


def step(t, initial, final, tau):
    return final + (initial-final)*exp(-t/tau)


def main():
    # Raspodela napona pre/posle promene opterećenja (7–8).
    assert F(1000, 1000+1) == F(1000, 1001)
    assert F(1, 1+1) == F(1, 2)
    # Margine: tipične granice iz kataloških tabela (12, 14, 28, 31).
    vil, vih, vol, voh = F(8,10), F(2), F(4,10), F(3)
    nml, nmh = vil-vol, voh-vih
    assert min(nml, nmh) == F(4,10)
    assert nml+nmh == voh-vol-(vih-vil)
    assert abs(F(4,1000)/F(-1,10000)) == 40
    assert abs(F(-4,10000)/F(20,1000000)) == 20
    assert F(4,1000)/F(-1,10000) < 0  # nedostatak apsolutne vrednosti (32)
    # RC: ODE, kontinuitet, stacionarno stanje i promena početnog trenutka.
    cases = 0
    for r in (10., 1000., 47000.):
        for c in (1e-9, 1e-6):
            tau = r*c
            for initial, final in ((0., 5.), (.3, 3.3), (5., 0.)):
                close(step(0, initial, final, tau), initial)
                close(step(100*tau, initial, final, tau), final)
                for q in (.1, 1., 3., 5.):
                    t = q*tau
                    u = step(t, initial, final, tau)
                    du = -(initial-final)*exp(-t/tau)/tau
                    close(tau*du + u, final)
                    t1 = .07*tau
                    u1 = step(t1, initial, final, tau)
                    close(step(t-t1, u1, final, tau), u)
                    # CR: napon C je komplement izlaznom naponu R.
                    ur = (final-initial)*exp(-t/tau)
                    close(ur + u, final)
                    cases += 1
    # Slajdovi 49–50: tačke 10/90/50% i 5 tau.
    t10, t90 = -log(.9), -log(.1)
    close(step(t10, 0, 1, 1), .1)
    close(step(t90, 0, 1, 1), .9)
    close(t90-t10, log(9))
    close(step(log(2), 0, 1, 1), .5)
    assert round(log(9), 1) == 2.2 and round(log(2), 2) == .69
    assert round(100*(1-exp(-5)), 1) == 99.3
    # Impuls: superpozicija i rešavanje po intervalima moraju dati isto.
    for low, high in ((0., 5.), (.3, 3.3), (-1., 2.)):
        for tau in (.05, 1., 20.):
            t1, t2 = .2, .8
            u2 = step(t2-t1, low, high, tau)
            for t in (.8, 1., 2., 10.):
                superposition = step(t-t1, low, high, tau) - (high-low)*(1-exp(-(t-t2)/tau))
                intervals = step(t-t2, u2, low, tau)
                final_formula = low+(high-low)*(1-exp(-(t2-t1)/tau))*exp(-(t-t2)/tau)
                close(superposition, intervals)
                close(intervals, final_formula)
    # Nenulta logička nula otkriva oba pogrešna međukoraka slajda 59.
    low, high, t1, t2, t, tau = .3, 3.3, .2, .8, 1., 1.
    correct = step(t-t2, step(t2-t1, low, high, tau), low, tau)
    wrong_plus = high-(high+low)+(high-low)*(exp(-(t-t2)/tau)-exp(-(t-t1)/tau))
    assert not isclose(correct, wrong_plus)
    assert not isclose(correct, 2*step(t-t1, low, high, tau))
    # RL: L di/dt + Ri = U, tau = L/R (64–66).
    for r, inductance in ((100., .01), (470., .2)):
        tau = inductance/r
        for t in (0., tau, 3*tau):
            ur = step(t, .3, 3.3, tau)
            di = (3.3-.3)*exp(-t/tau)/(r*tau)
            close(inductance*di+ur, 3.3)
    # Kompenzacija: poređenje kapacitivnog i otpornog razdelnika (67).
    for r1, r2, c2 in ((2, 3, 5), (10, 1, 7), (1, 100, 2)):
        c1 = F(c2*r2, r1)
        assert c1/(c1+c2) == F(r2, r1+r2)
        assert c1*r1 == c2*r2
        assert (c1/2)/(c1/2+c2) < F(r2, r1+r2)
        assert (c1*2)/(c1*2+c2) > F(r2, r1+r2)
    print(f'08: {cases} RC/CR stanja, impulsni i RL odzivi, margine i kompenzacija — prolaze; izvorne greške odvojeno evidentirane.')


if __name__ == '__main__':
    main()
