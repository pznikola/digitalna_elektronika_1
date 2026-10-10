# Otvorena stručna pitanja — predavanje 10

Status: `u_radu`. Ovi predlozi **nisu primenjeni**. Potrebno je korisnikovo izričito odobrenje stručnih promena prema [planu](../../../../PLAN_PREDAVANJA.md). Prezentacija i beleške su radna verzija za pregled, ne konačno nastavno izdanje.

Za odluku je dovoljno navesti oznake P01–P19 i prihvatanje ili željenu alternativu. Odobrenje ovih ispravki odvojeno je od prihvatanja cele prezentacije.

| Predlog | Slajdovi | Pitanje |
|---|---|---|
| P01 | s006 | Zasićeni model: naziv napona |
| P02 | s014 | Struja u aktivnoj karakteristici |
| P03 | s030 | Asimptota kolektorske struje |
| P04 | s032 | Dimenzija gotove RC formule |
| P05 | s034 | Oznaka donjeg baznog otpornika |
| P06 | s035, s036 | Funkcija mreže otvorenih kolektora |
| P07 | s038 | Plivajući ulaz |
| P08 | s058 | Granica neopterećenog totem-pole izlaza |
| P09 | s059 | Znak pada na D4 |
| P10 | s060 | Otpornik u IIL |
| P11 | s065, s066 | Model početnog zasićenog intervala |
| P12 | s066 | Indeks struje u modelu pražnjenja |
| P13 | s078 | Trostatička NOR tabela |
| P14 | s083 | Oznake izlaza u objašnjenju |
| P15 | s084 | Struja u simetričnoj tački |
| P16 | s085 | Koji tranzistor je zakočen |
| P17 | s090 | Ukupni i promenljivi izlazni napon |
| P18 | s092 | Punjenje ECL izlaza |
| P19 | s093 | Dva različita tranzistora T3 |

## P01 — Zasićeni model: naziv napona

Slajdovi: 10-s006, PDF strana 3, donji.

Problem: Opis navodi spoj baza–kolektor uz VCES=0.1 V. Šema prikazuje kolektor–emitor.

Predlog: Zameniti naziv sa „kolektor–emitor“; VBC=VBES−VCES=0.6 V u ovom modelu.


## P02 — Struja u aktivnoj karakteristici

Slajdovi: 10-s014, PDF strana 7, donji.

Problem: U međukoraku je VO=VCC−RC IR, dok dalje stoji RC betaF IB.

Predlog: Zameniti IR sa IC u spornom međukoraku.


## P03 — Asimptota kolektorske struje

Slajdovi: 10-s030, PDF strana 15, donji.

Problem: Izraz za vo(∞) sadrži iRC(t), iako se računa stacionarna granica.

Predlog: Pisati iRC(∞)=betaF IB i koristiti tu vrednost u asimptoti.


## P04 — Dimenzija gotove RC formule

Slajdovi: 10-s032, PDF strana 16, donji.

Problem: U odbačenom gotovom izrazu piše tf=2.2, bez vremenske konstante.

Predlog: Dopuniti zapis tf≈2.2τ, uz očuvano upozorenje da taj izraz nije primenljiv na razmatrani proces.


## P05 — Oznaka donjeg baznog otpornika

Slajdovi: 10-s034, PDF strana 17, donji.

Problem: U šemi sa zajedničkim RC oba bazna otpornika su RBB, iako je donji ulaz VIA i tranzistor TA.

Predlog: Donji označiti RBA; topologiju ne menjati.


## P06 — Funkcija mreže otvorenih kolektora

Slajdovi: 10-s035, PDF strana 18, gornji, 10-s036, PDF strana 18, donji.

Problem: Donji simbol je ILI, a izlazni proizvod sadrži faktor CD.

Predlog: Pisati (bar A)(overline BC)(C+D); zadržati nacrtani ILI simbol.


## P07 — Plivajući ulaz

Slajdovi: 10-s038, PDF strana 19, donji.

Problem: Izvorno objašnjenje kaže „Na ulazu nema napona“. Plivajući ulaz nema definisan DC nivo.

Predlog: Pisati „Napon ulaza nije jednoznačno određen“ i zadržati preporuku terminacije.


## P08 — Granica neopterećenog totem-pole izlaza

Slajdovi: 10-s058, PDF strana 29, donji.

Problem: U lancu uslova ponovljeno je IC→0; naredni zaključak o bazi zahteva IB→0.

Predlog: Drugo IC→0 zameniti sa IB→0.


## P09 — Znak pada na D4

Slajdovi: 10-s059, PDF strana 30, gornji.

Problem: Prvi član za VOH ima +VD4; ostatak iste jednakosti i KVL zahtevaju −VD4.

Predlog: Zameniti +VD4 sa −VD4 u prvom članu.


## P10 — Otpornik u IIL

Slajdovi: 10-s060, PDF strana 30, donji.

Problem: Imenilac je RBE1, dok je odgovarajući otpornik u šemi RB1.

Predlog: Pisati RB1.


## P11 — Model početnog zasićenog intervala

Slajdovi: 10-s065, PDF strana 33, gornji, 10-s066, PDF strana 33, donji.

Problem: Za izlazak iz zasićenja na s065 korišćeni su aktivna konstanta C RB/(betaF+1) i aktivna asimptota. S066 koristi tu τ2 i bez dodatnog uslova tvrdi da je 50% u zasićenju.

Predlog: Koristiti zasićeni model sa s064 do granice režima; potom aktivni model. Razdvojiti slučajeve gde srednji nivo prethodi ili sledi granici. Detaljno izvođenje u beleškama obnoviti tek po odobrenju.


## P12 — Indeks struje u modelu pražnjenja

Slajdovi: 10-s066, PDF strana 33, donji.

Problem: Ekvivalent pražnjenja označen je betaF IB4, a kapacitivnost prazni T3.

Predlog: Pisati betaF IB3 u ekvivalentnom modelu.


## P13 — Trostatička NOR tabela

Slajdovi: 10-s078, PDF strana 39, donji.

Problem: Simbol ima negaciju izlaza, a u redu OE=1 tabela navodi A+B.

Predlog: Zameniti Y sa overline(A+B); OE=0, Z ostaju.


## P14 — Oznake izlaza u objašnjenju

Slajdovi: 10-s083, PDF strana 42, gornji.

Problem: U tekstu su VI1/VI2, a šema i formule imaju VO1/VO2.

Predlog: U objašnjenju koristiti VO1/VO2.


## P15 — Struja u simetričnoj tački

Slajdovi: 10-s084, PDF strana 42, donji.

Problem: Izraz deli IE2 sa2, iako kroz T2 već prolazi polovina ukupne struje IE.

Predlog: Oba IE2/2 zameniti sa IE/2, ili koristiti IE2 bez dodatnog deljenja.


## P16 — Koji tranzistor je zakočen

Slajdovi: 10-s085, PDF strana 43, gornji.

Problem: Opis tvrdi da T1 vodi i da je T1 zakočen u istom stanju.

Predlog: Drugi T1 zameniti sa T2.


## P17 — Ukupni i promenljivi izlazni napon

Slajdovi: 10-s090, PDF strana 45, donji.

Problem: U izrazima VO+ΔVO pri smetnji VEE izostavljena je početna IC. Kada je smetnja nula, izraz ne vraća početni VO.

Predlog: Za ukupan napon koristiti IC+ΔIC; za samu promenu ΔVO=−RCΔIC≈−RCΔIE. Znak veze ΔIE/ΔVEE navesti uz definisanu referencu i model izvora.


## P18 — Punjenje ECL izlaza

Slajdovi: 10-s092, PDF strana 46, donji.

Problem: U punjenju je ponovljeno tpHL i asimptota VCC, dok aktivni bafer uvodi VBE.

Predlog: Koristiti tpLH i asimptotu VCC−VBE u istom aproksimativnom modelu, uz konzistentan granični izlazni nivo.


## P19 — Dva različita tranzistora T3

Slajdovi: 10-s093, PDF strana 47, gornji.

Problem: Levi izlazni bafer i tranzistor reference imaju istu oznaku T3.

Predlog: Preimenovati tranzistor reference u T5, uz dosledne vezane oznake gde su potrebne.

## Dokaz i ograničenje provera

Nedoumice su proverene prema pojedinačnim originalnim isečcima, šemama i jednačinama. Istorijski nalazi su ponovo upoređeni sa originalom. Postojeći `kodovi/provera_logike.py` potvrđuje 1018 računskih slučajeva, uključujući razlike izvornih spornih izraza i predloženih fizičkih modela; njegov prolaz ne potvrđuje pogrešan izvorni zapis. Originalni PDF ostaje neizmenjen.
