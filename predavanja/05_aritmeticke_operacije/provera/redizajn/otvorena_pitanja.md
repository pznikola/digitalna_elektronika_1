# Otvorena stručna pitanja — predavanje 05

Datum: 2026-10-02. Ovo su predlozi; izvorni zapisi još nisu promenjeni. Prema [planu](../../../../PLAN_PREDAVANJA.md#11-šta-mora-ostati-očuvano), stručne izmene zahtevaju korisnikovo izričito odobrenje. Pitanja iz nastavnih primera s007, s011, s038 i s040 nisu greške i ostaju na slajdovima.

## 1. s014 — red prenosa u osnovi 7

Original: `001000`; predlog: `011000`. Sabiranje od najmanje težine daje prenose 0,0,0,1,1,0 u smeru računanja. Rezultat `404.63₇` ostaje isti.

## 2. s024 — vrednost dodatka

Tekst kaže `100000`, račun prikazuje `10000`. Za četiri bita dodatak je 2⁴ = `10000₂`. Predlog: uskladiti tekst sa postojećim računom.

## 3. s026 — izlazni prenosi

Uz zbir maksimalnih pozitivnih vrednosti stoji `c_(n−1)=1`, a uz zbir minimalnih negativnih `c_(n−1)=0`. Po indeksiranju s013, predlog je 0 odnosno 1. Za n=4: 7+7=14, bez izlaznog prenosa; 8+8=16, sa prenosom. Oba slučaja imaju označeno prekoračenje, koje nije isto što i izlazni prenos.

## 4. s053/s054 — neuspešno probno oduzimanje

Original: `R=<0`, uz uspešnu granu `R>=0`. Predlog: neuspešna grana `R<0`, uspešna `R≥0`. Nulti ostatak je uspešno oduzimanje i daje bit količnika 1. Primer 74:8 ostaje isti, ali npr. 8:8 pokazuje zašto se grane ne smeju preklapati.

## 5. s050–s052 — binarna tačka proizvoda i greška odsecanja

Za n-bitne operande sa n−1 razlomljenih bita, celobrojni proizvod ima 2n−2 razlomljenih pozicija, dakle binarnu tačku iza DVA najviša bita. Original stavlja tačku posle samo jednog, što menja skalu za faktor 2. Kontraprimer n=4: `0.100 × 0.100 = 0.010000` (1/4); sirovi osmobitni proizvod je `00.010000`, dok `0.0010000` predstavlja 1/8.

Predlog za usklađenu obradu:

- s050/s052: sirovi zapis `c_(2n−1)c_(2n−2).c_(2n−3)…c₀`; kada rezultat pripada [−1,1), ukloniti ponovljeni najviši znak, sačuvati n bita `c_(2n−2).c_(2n−3)…c_(n−1)` i odbaciti n−1 bita `c_(n−2)…c₀`. Izuzetak (−1)·(−1)=1 ostaje vidljiv.
- s051: za n=4 prikazati `c₀.c₋₁…c₋₆`, odbaciti tri bita i uskladiti maksimum sa `0.000111 = 7/64`; opšti maksimum `(2^(n−1)−1)/2^(2n−2)`.
- Sve povezane indekse i dopune u beleškama uskladiti sa istom skalom; sačuvati sva izvođenja i načine zaokruživanja.

Alternativa koja takođe zahteva odluku: zadržati s051 kao samostalan primer kvantizacije proizvoljnog osmobitnog ulaza, izričito ga razdvojiti od preciznosti proizvoda dva četvorobitna operanda, pa sačuvati 15/128 kao granicu za taj zaseban primer.

## 6. s052 — zaokruživanje naviše

Original propisuje dodatak `r=1/2^(n−1)` bez uslova. Ako je rezultat već tačno predstavljiv, dodatak menja ispravan rezultat: uz korak 1/8, vrednost 1/4 postaje 3/8.

Predlog: dodati jedan korak samo kada odbačeni deo nije nula; inače `r=0`. Za najbližu vrednost razdvojiti bit odluke od numeričkog dodatka: prvi odbačeni bit odlučuje o koraku, uz zasebno pravilo za tačnu polovinu. Sve postojeće vrste zaokruživanja ostaju prikazane.

## Nastavak

Izgled i nesporne beleške obrađuju se dok se čeka odluka. Nerešena pitanja sprečavaju status `ceka_odobrenje` i završnu potvrdu sadržaja pogođenih slajdova. Početak 06 nije odobren.
