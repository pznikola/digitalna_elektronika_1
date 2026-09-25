# Izveštaj o ispravkama — vežbe 07

## 07-01: Str. 1–2, zad. 1 → sec:1

**Izvor:** „beskonačnim, ali parnim brojem“
**Ispravka:** Granica parnog podniza; niski nivo V_L nije automatski 0 V.
**Vrsta, provera i uticaj:** Pojašnjenje: parnost se odnosi na konačne dužine 2n pre prelaska na granicu. Izvor nema preciznu analitičku karakteristiku; dodata ograničenja grafičkog odgovora.

## 07-02: Str. 3–4, zad. 2 → sec:2

**Izvor:** Isti simboli VOH/VOL za stabilne i garantovane nivoe.
**Ispravka:** V_H/V_L za stabilne, V_OH=f(V_IL), V_OL=f(V_IH) za garantovane nivoe invertora.
**Vrsta, provera i uticaj:** Stručna dopuna: aproksimacija izvornika zadržana je, ali izričito označena. Primarni izvor MIT, slajdovi 4–7, razlikuje VMAX/VMIN i VOH/VOL. Uticaj: numeričke margine u zadacima 3–5.

## 07-03: Str. 5, zad. 3a.1 → eq:3.2

**Izvor:** (2.5 V−2.7 V)^n/3^n
**Ispravka:** (−1/3)^n(v_0−2.5 V)
**Vrsta, provera i uticaj:** Računska i dimenziona greška: iterira se faktor nagiba, ne početni napon; pogrešan izraz ima jedinicu V^n. Granica 2.5 V ostaje ista.

## 07-04: Str. 5, zad. 3a.2 → sec:3

**Izvor:** Nedosledni indeksi parnih/neparnih izlaza.
**Ispravka:** v_2n=2.7 V, v_(2n+1)=2.3 V.
**Vrsta, provera i uticaj:** f(f(x))=x. Ceo niz nema granicu za dati ulaz.

## 07-05: Str. 5–6, zad. 3b → sec:3

**Izvor:** „nagib 2“, „nagib 1/3“, „nagib 3“ za opadajuće segmente.
**Ispravka:** Nagibi −2, −1/3, −3; za regeneraciju koristi se njihov modul.
**Vrsta, provera i uticaj:** Znak nagiba određuje invertovanje. Ispod praga se parnost izlaza mora pratiti.

## 07-06: Str. 6, zad. 3c → eq:3.5

**Izvor:** MSNM0=MSNM1=2 V kao konačan rezultat.
**Ispravka:** Garantovane margine 1 V; procena prema stabilnim nivoima 2 V.
**Vrsta, provera i uticaj:** f3(3)=1, f3(2)=4; 2−1=4−3=1. Izvorna aproksimacija nije tačna za nagib 1/2.

## 07-07: Str. 7, opšti postupak → eq:4.1

**Izvor:** k<1 garantuje konvergenciju; k>1 uvek daje +∞.
**Ispravka:** Konvergencija za |k|<1; rast odstupanja za k>1 zavisi od početne tačke.
**Vrsta, provera i uticaj:** Za k=−2 izraz divergira, a k=2,x0=y* ostaje konstantan. Analiza važi samo dok tačke ostaju na segmentu. Dodati slučajevi k=−1 i k<−1 radi potpunosti.

## 07-08: Str. 8, zad. 4c → eq:4.3

**Izvor:** MSNM0=MSNM1=2 V.
**Ispravka:** Garantovane margine 1 V; procena 2 V označena.
**Vrsta, provera i uticaj:** Za bafer VOL=b3(2)=1, VOH=b3(3)=4; promenjena tačka vrednovanja u odnosu na invertor.

## 07-09: Str. 9, zad. 5 → tabela pre eq:5.1

**Izvor:** T4=(4 V,0.5 V)
**Ispravka:** T4=(3 V,0.5 V)
**Vrsta, provera i uticaj:** f3(3)=1, b3(1)=0.5; za ulaz 4 izlaz bi bio 0.25. Ispravka preneta na crtež i tabelu.

## 07-10: Str. 10, zad. 5 → sec:5

**Izvor:** VIH=2 V, VIL=3 V
**Ispravka:** VIL=2 V, VIH=3 V
**Vrsta, provera i uticaj:** Zamenjene oznake; moduli nagiba prelaze 1 na ulazu 2 i padaju ispod 1 na ulazu 3. Ranije margine 2 V nisu saglasne sa ispisanim pragovima.

## 07-11: Str. 10, zad. 5 → eq:5.2

**Izvor:** MSNM0=MSNM1=2 V.
**Ispravka:** Garantovane margine 1.5 V; procena 2 V posebno.
**Vrsta, provera i uticaj:** h(3)=0.5, h(2)=4.5; 2−0.5=4.5−3=1.5.

## Jezik i prelom

Ispravljeni su „obzirom“, „izazima“, „proizodača“, „karakteristikeprenosa“, termin „regenerabilnost“, slaganje roda/broja i interpunkcija (str. 1–10). Oštećena dijakritika u pdftotext izlazu nije greška izvornog PDF-a. Izrazi sa apsolutnom vrednošću nagiba u izvorniku vizuelno su potvrđeni; ne prijavljuju se kao izvorna greška. Tabele imaju diskretne razdelnike između redova, bez dodatne tanke linije uz booktabs pravila.

## Provere i reference

`make check` proverava racionalne segmente, kontinuitet, nagibe, kompoziciju, iteracije i margine, uključujući granične tačke.

[MIT 6.012, Lecture 11, slajdovi 4–7](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-spring-2009/b96efcfa398f43f970ae4f36ac43456b_MIT6_012S09_lec11.pdf): primarni nastavni izvor za razliku između krajnjih napona i garantovanih nivoa, nagib −1 i aproksimaciju VOH≈VMAX, VOL≈VMIN.

## Završna provera crteža

Razmaknute su oznake osa i numeričkih podeoka, povećan je razmak između prikaza četiri iteracije i sprečen je prelom kratke napomene preko stranica. Vodovi između invertora i mesta unošenja šuma povezani su sa imenovanim priključcima simbola.

## Ponovni pregled — 25. 9. 2026.

Pregledani su ceo izvornik od 10 stranica i konačni LaTeX/PDF. Raniji nalazi iznad ponovo su potvrđeni; potpuni [dokazi i obuhvat](code/PREGLED_DOKAZA.md), [otisci formula/crteža](code/pregled_izvora.json) i [tačni tekstualni zapisi pre/posle](../PROVERA/nalazi_07_tekst.json) dopunjuju istoriju.

### 07-A01 — presek nije dovoljan za stabilnost

**Mesto:** zadatak 1, pasus pre `eq:1.2`. **Pre:** „preseci van dijagonale određuju par stabilnih nivoa“ bez uslova. **Posle:** iskaz vezan za prikazanu karakteristiku; dodati uslovi |f′(VL)f′(VH)|<1 za dvociklus i |f′(VS)|<1 za fiksnu tačku. **Vrsta:** stručna dopuna. Izvod kompozicije daje proizvod nagiba; par preseka sa proizvodom >1 je nestabilan. Zadatak 3, kolo 1, daje upravo protivprimer (proizvod 4). Granica zadatka 1 nije promenjena. Ponovna provera obuhvatila sve parne fiksne tačke komadnih funkcija i njihove multiplikatore.

### 07-A02 — lokalno slabljenje i garancija konačnog šuma

**Mesto:** zadatak 2, pasusi uz `eq:2.1`–`eq:2.8`. **Pre:** ulazi „moraju ostati u oblastima malog pojačanja“; vrsta/domen šuma i stabilizovan prethodni lanac nisu bili izričiti. **Posle:** statički šum, prethodno stabilni nivoi za SSNM, konvencionalne granice za S karakteristiku, dovoljni uslovi invarijantnosti intervala i domen napajanja. **Vrsta:** stručno pojašnjenje pretpostavki. |f′|<1 je lokalni uslov, a konačna amplituda zahteva poređenje granica intervala. Ne daje se neosnovana garancija o impulsima ili ulazima izvan poznate krive. Sve postojeće nejednakosti i numeričke margine ostaju iste. Potvrđeno dedukcijom i zamenom stvarnih krajnjih vrednosti; MIT Lecture 11, slajdovi 4–7.

### 07-A03 — krajnje fiksne tačke prvog bafera

**Mesto:** zadatak 4b. **Pre:** „Prvo kolo privlači tačke sredini“. **Posle:** privlači unutrašnje tačke, dok tačni ulazi 0 i 5 V ostaju na nestabilnim krajnjim fiksnim tačkama. **Vrsta:** stručna korekcija preširokog iskaza. Direktno b₁(0)=0,b₁(5)=5, uz jednostrane nagibe 2. Rezultat za 2.7 V ostaje 2.5 V; usklađeno sa istim izuzetkom već navedenim kod invertora. Ponovna provera iz stvarnih segmenata nalazi sva tri fiksna korena.

### 07-A04 — mesto unošenja šuma kod kompozicije

**Mesto:** početak rešenja zadatka 5, rezultati `eq:5.2`. **Pre:** „margine ... kaskade“ bez izričitog razgraničenja unutrašnje veze. **Posle:** jedan stepen je ceo par invertor–bafer; šum je na međuvezi kopija, unutrašnja veza idealna. **Vrsta:** potrebna pretpostavka. Kompozicija b(f(x)) nije model b(f(x)+e₁)+e₂ sa dva nezavisna poremećaja. Rezultat 1.5 V važi pod sada navedenim uslovom. Ne uvode se nove proizvoljne amplitude unutrašnjeg šuma. Tačna kompozicija, svi prelomi i margine ponovo izvedeni racionalno.

### 07-A05 — obnova pomoćnih projekcija iz originala

**Mesta:** originalne slike 3.1,4.1,5.1,5.3 → `Zadatak_3/karakteristike`, `Zadatak_4/karakteristike`, `Zadatak_5/karakteristike`, `Zadatak_5/rezultat`. **Pre:** krive su imale tačne koordinate, ali su nedostajale isprekidane projekcije originalnih preloma. **Posle:** vraćene diskretne projekcije na ose, bez promene krivih. **Vrsta:** grafički propust konverzije. Olakšano je očitavanje tačaka na kojima se zasnivaju jednačine. Svaka koordinata crteža poredi se sa stvarnim segmentima; svih pet izmenjenih izvoza (uključujući lanac iz naredne stavke) regenerisano.

### 07-A06 — oznaka napona na izlazu četvrtog bloka

**Mesto:** `Images/Zadatak_4/lanac.tex`, slika `fig:4.2`. **Pre:** y₄,…,yₙ uz jednu istu žicu. **Posle:** y₄ na toj žici, a odvojene tri tačke označavaju nastavak lanca. **Vrsta:** grafička dvosmislenost. Naponi različitih stepena uopšte nisu jednaki. Sve četiri blokovske veze praćene su od izlaza do narednog ulaza; matematička rekurzija nije promenjena.

### 07-A07 — čitljivost oznaka i imenovanje tabele

**Mesta:** `fig:1.4`, `fig:5.3`, tabela pre `eq:5.1`. **Pre:** oznake (VL,VH)/(VH,VL) dodirivale su odraženu krivu; tri poslednje strelice imale su praktično nultu dužinu i zaklanjale presek. Tabela nije imala broj/naslov. **Posle:** oznake pomerene van krivih; očuvana dva razlučiva koraka približavanja; oznake T₁–T₄ imaju belu podlogu prema pomoćnim linijama; tabela dobila `tab:prelomi` i naslov. **Vrsta:** formatiranje/grafika. Ne menja se geometrijski postupak ni rezultat. Svi konačni crteži provereni na PDF stranama; svaka od 14 stranica pregledana nakon završnih izmena.

### Ograničenje 07-L01 — preciznost prvog zadatka

Izvornik i dalje nema dovoljno podataka za tačnu numeričku graničnu vrednost. Potvrđen je grafički zaključak i doslednost četiri prikaza, ali numerički parametri pomoćne Bézier krive nisu proglašeni zadatim tehnološkim modelom. Ograničenje je vidljivo u studentskom tekstu i zasebno u dokazima.
