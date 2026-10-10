"""Nezavisni računski dokazi predloga; ne ispravljaju nastavni izvor."""
import math
n = 0

def ok(condition):
    global n
    assert condition
    n += 1

def close(a, b):
    ok(math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9))

# NMOS: fizička grana, oblasti i kontraprimer nedostajućeg uslova napajanja.
vdd, vtn, vtl, kd, kl = 2.4, 1, -1, 1, 1
vil = vtn - vtl * kl / kd / math.sqrt(1 + kl / kd)
voil = vdd + vtl * (1 - 1 / math.sqrt(1 + kl / kd))
vih = vtn - 2 * vtl * math.sqrt(kl / (3 * kd))
voih = -vtl * math.sqrt(kl / (3 * kd))
ok(kd / kl > (-vtl / vtn) ** 2 / 3)
ok(voil < vih)
ok(voil >= vil - vtn)
ok(0 <= vdd - voil <= -vtl)
ok(voih <= vih - vtn)
ok(vdd - voih >= -vtl)
ok(vih <= vdd)
# Pseudo NMOS: ispravan bilans, pozitivan član izvoda, negativan izvorni koeficijent.
vdd, vtn, vtp, kn, kp = 5, 1, -1, 4, 1
vo = -vtp + (vdd + vtp) * math.sqrt(kn / (kp + kn))
vi = vtn + (kp / kn) * (vo + vtp)
ip = kp / 2 * (2 * (vo - vdd) * (-vdd - vtp) - (vo - vdd) ** 2)
in_ = kn / 2 * (vi - vtn) ** 2
close(ip, in_)
close(2 * kp * (vo + vtp), 2 * kn * (vi - vtn))
vi_bad = vtn + (vdd + vtp) * kp / kn * math.sqrt(kp / (kp + kn))
ok(not math.isclose(ip, kn / 2 * (vi_bad - vtn) ** 2))
close(ip, 1.6)
close(kn / 2 * (vi_bad - vtn) ** 2, .4)
# CMOS: deljenje svih članova sa kp.
vo = .2
full = (2 * kn * vo + kp * vdd + kp * vtp + kn * vtn) / (kp + kn)
normalized = (2 * kn / kp * vo + vdd + vtp + kn / kp * vtn) / (1 + kn / kp)
bad = (2 * kn / kp * vo + vdd + vtp + kp / kn * vtn) / (1 + kn / kp)
close(full, normalized)
close(full, 1.92)
close(bad, 1.17)
# Predznak linearne PMOS struje pod pozitivnom konvencijom.
vsg, vtpos, vsd_sat, speed = 4, 1, 1, 2
negative_form = -speed * (-vsg + vtpos + vsd_sat / 2)
positive_form = speed * (vsg - vtpos - vsd_sat / 2)
close(negative_form, positive_form)
# Pri stalnoj f snaga raste kvadratno; pri f proporcionalnoj VDD kubno.
close((2 * vdd) ** 2 / vdd ** 2, 4)
close((2 * vdd) ** 3 / vdd ** 3, 8)
# Domen minimuma pojednostavljene funkcije EDP i promena znaka izvoda.
for vte in [.2, .5, 1]:
    der = lambda v: v * v * (2 * v - 3 * vte) / (v - vte) ** 2
    close(der(1.5 * vte), 0)
    ok(der(1.4 * vte) < 0 < der(1.6 * vte))
print(f"09_2: {n} dopunskih računskih provera prošlo; predlozi ostaju neodobreni.")
