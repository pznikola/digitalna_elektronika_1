# Pregled vektorskih šema — 09_2

Datum: 2026-10-03. Svaki originalni isečak, početni i novi slajd pregledani su pojedinačno. Topologija je upoređena sa izvornim vezama; nije odobreno menjanje topologije.

| Slajdovi | Provera i rezultat crtanja |
|---|---|
| s002–s010 | TD je NMOS sa indukovanim, TL sa ugrađenim kanalom. Sors i gejt TL su na izlazu; drejn TL na VDD. Spoj izlaza ima tačku. Vodovi su kratki, oznake odvojene od simbola. |
| s011, s016–s022 | P sors na VDD, gejt na masu; N gejt na VI, sors na masu; zajednički drejnovi na VO. Očuvane osnove i presek s011. |
| s023–s037, s048 | P i N gejtovi na VI, zajednički drejnovi na VO, izvori na napajanju/masi. Osnove u s023 ostaju posebno prikazane. S048 zadržava širine P=2/N=1. |
| s010/s022/s037 | Kvalitativne karakteristike zadržavaju naponske nivoe, pragove, nagibe i vertikalnu oblast; oznake VIL/VIH/VDD su razdvojene. Grafici nisu predstavljeni kao merenja. |
| s049 | Obe izvorne zaštitne diode i njihovi polariteti ostaju na ulazu prema VDD i masi; vodovi zaobilaze simbole. Tvrdnja o preciznim granicama napona ostaje P09. |
| s050/s051 | Očuvani TN, TP, RW1/RW2, RS1/RS2, CP/CN i tri mala talasna prikaza. Mirrored PNP omogućava vod prema bazi bez prelaska preko simbola. Čvor baze TN ostaje između RS1/RS2; P10 predlaže samo popravku teksta, ne prevezivanje kola. |
| s055 | Oba stanja punjenja/pražnjenja, kapacitivnost CL, ulazni nivoi i smerovi promene VO ostaju vidljivi. Dve realizacije su razdvojene po visini. |
| s058/s059 | Strelica iSC odvojena od izlaznog napona i simbola. Vremenske oznake tS iznad, tSC ispod talasnih oblika; linije nivoa imaju odvojene natpise. Očuvani oba impulsa i sve pomoćne vertikale. |

Tropriključne šeme koriste postojeće native CircuitikZ/Razavi simbole; depletion TL koristi symbol nmosd. Četvoropriključne nastavne ilustracije i fizički preseci čuvaju izvornu konvenciju. Sve su uređivi vektori. Font oznaka je 9–10 pt u konačnoj veličini, boja nastavnog isticanja tamnocrvena; veze su tamne, spojevi označeni tačkama, ukrštanja bez spoja nemaju tačku.

## Izmenjeni izvori

- [s002_invertor_ugradjeni_kanal.tex](../../slike/tikz/s002_invertor_ugradjeni_kanal.tex)
- [s003_invertor_ugradjeni_kanal.tex](../../slike/tikz/s003_invertor_ugradjeni_kanal.tex)
- [s004_invertor_ugradjeni_kanal.tex](../../slike/tikz/s004_invertor_ugradjeni_kanal.tex)
- [s005_invertor_ugradjeni_kanal.tex](../../slike/tikz/s005_invertor_ugradjeni_kanal.tex)
- [s006_invertor_ugradjeni_kanal.tex](../../slike/tikz/s006_invertor_ugradjeni_kanal.tex)
- [s007_invertor_ugradjeni_kanal.tex](../../slike/tikz/s007_invertor_ugradjeni_kanal.tex)
- [s008_invertor_ugradjeni_kanal.tex](../../slike/tikz/s008_invertor_ugradjeni_kanal.tex)
- [s009_invertor_ugradjeni_kanal.tex](../../slike/tikz/s009_invertor_ugradjeni_kanal.tex)
- [s010_invertor_ugradjeni_kanal.tex](../../slike/tikz/s010_invertor_ugradjeni_kanal.tex)
- [s011_presek_pseudo_nmos.tex](../../slike/tikz/s011_presek_pseudo_nmos.tex)
- [s011_pseudo_nmos.tex](../../slike/tikz/s011_pseudo_nmos.tex)
- [s011_pseudo_nmos_osnove.tex](../../slike/tikz/s011_pseudo_nmos_osnove.tex)
- [s016_pseudo_nmos.tex](../../slike/tikz/s016_pseudo_nmos.tex)
- [s017_pseudo_nmos.tex](../../slike/tikz/s017_pseudo_nmos.tex)
- [s018_pseudo_nmos.tex](../../slike/tikz/s018_pseudo_nmos.tex)
- [s019_pseudo_nmos.tex](../../slike/tikz/s019_pseudo_nmos.tex)
- [s020_pseudo_nmos.tex](../../slike/tikz/s020_pseudo_nmos.tex)
- [s021_pseudo_nmos.tex](../../slike/tikz/s021_pseudo_nmos.tex)
- [s022_pseudo_nmos.tex](../../slike/tikz/s022_pseudo_nmos.tex)
- [s023_cmos_invertor.tex](../../slike/tikz/s023_cmos_invertor.tex)
- [s023_cmos_osnove.tex](../../slike/tikz/s023_cmos_osnove.tex)
- [s023_presek_cmos.tex](../../slike/tikz/s023_presek_cmos.tex)
- [s024_cmos_invertor.tex](../../slike/tikz/s024_cmos_invertor.tex)
- [s025_cmos_invertor.tex](../../slike/tikz/s025_cmos_invertor.tex)
- [s026_cmos_invertor.tex](../../slike/tikz/s026_cmos_invertor.tex)
- [s027_cmos_invertor.tex](../../slike/tikz/s027_cmos_invertor.tex)
- [s028_cmos_invertor.tex](../../slike/tikz/s028_cmos_invertor.tex)
- [s029_cmos_invertor.tex](../../slike/tikz/s029_cmos_invertor.tex)
- [s030_cmos_invertor.tex](../../slike/tikz/s030_cmos_invertor.tex)
- [s031_cmos_invertor.tex](../../slike/tikz/s031_cmos_invertor.tex)
- [s032_cmos_invertor.tex](../../slike/tikz/s032_cmos_invertor.tex)
- [s033_cmos_invertor.tex](../../slike/tikz/s033_cmos_invertor.tex)
- [s034_cmos_invertor.tex](../../slike/tikz/s034_cmos_invertor.tex)
- [s035_cmos_invertor.tex](../../slike/tikz/s035_cmos_invertor.tex)
- [s036_cmos_invertor.tex](../../slike/tikz/s036_cmos_invertor.tex)
- [s037_cmos_invertor.tex](../../slike/tikz/s037_cmos_invertor.tex)
- [s037_pet_oblasti_cmos.tex](../../slike/tikz/s037_pet_oblasti_cmos.tex)
- [s048_cmos_invertor.tex](../../slike/tikz/s048_cmos_invertor.tex)
- [s049_esd_diode.tex](../../slike/tikz/s049_esd_diode.tex)
- [s050_parazitni_tranzistori_presek.tex](../../slike/tikz/s050_parazitni_tranzistori_presek.tex)
- [s050_parazitno_kolo.tex](../../slike/tikz/s050_parazitno_kolo.tex)
- [s051_pozitivna_povratna_sprega.tex](../../slike/tikz/s051_pozitivna_povratna_sprega.tex)
- [s055_punjenje_praznjenje.tex](../../slike/tikz/s055_punjenje_praznjenje.tex)
- [s058_impulsi_struje.tex](../../slike/tikz/s058_impulsi_struje.tex)
- [s058_struja_kratkog_spoja.tex](../../slike/tikz/s058_struja_kratkog_spoja.tex)
- [s059_impulsi_struje.tex](../../slike/tikz/s059_impulsi_struje.tex)
- [s059_struja_kratkog_spoja.tex](../../slike/tikz/s059_struja_kratkog_spoja.tex)
