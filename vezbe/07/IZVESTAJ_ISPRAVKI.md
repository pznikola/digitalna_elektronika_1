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
