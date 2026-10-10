# Stručna pitanja — predavanje 04

Datum: **2026-10-02**. Korisnik je odobrio tri ispravke; preostala pitanja su **s009 i s035**, za koja je tražio pojašnjenje. Predlozi i odluke ostaju u tehničkoj evidenciji, izvan nastavnih beležaka.

[PLAN_PREDAVANJA.md §1.1](../../../../PLAN_PREDAVANJA.md) propisuje: „Promene formula, vrednosti, topologije kola, stručnih tvrdnji ili uslova zahtevaju korisnikovo izričito odobrenje.“ Stvarna poruka i obim odluke su u [odluke.md](odluke.md).

## Otvorena pitanja

| Slajd | Izvorni zapis i problem | Predložena stručna ispravka |
|---|---|---|
| s009 | Iz CV/rⁿ < 1 naveden je n ≥ logᵣ CV. Taj slabiji uslov ne garantuje dovoljno cifara kada je CV = rᵐ: za CV = 8, r = 2 dopušta n = 3, dok je 8₁₀ = 1000₂ i zahteva 4 cifre. | **n > logᵣ CV, za CV > 0**. Najmanji broj cifara je ⌊logᵣ CV⌋ + 1. Za CV = 0 koristi se jedna cifra; logaritam nule nije definisan. |
| s035 | Druga formula je 2ⁿ − invertovani zapis + 1. Za n = 4 i početnu vrednost 3, invertovani zapis je 1100₂ = 12; izraz daje 16 − 12 + 1 = 5, pa ne vraća početnu vrednost. | Oduzimati ceo drugi komplement: **2ⁿ − (invertovani zapis + 1)**, odnosno **16 − (12 + 1) = 3**. U drugoj formuli dodati zagrade oko invertovanog zapisa i jedinice. Prva formula za prvi komplement ostaje ista. |

Slabiji uslov s009 jeste nužan za ispravan broj cifara, ali nije dovoljan; stroga nejednakost daje tačan kriterijum. S035 treba da pokaže da ponovljeno komplementiranje vraća početni kod. U fiksnoj širini kodiranje i prenos posmatraju se modulo 2ⁿ; za primer sa 3 nema graničnog prenosa.

Korisnik je zatražio objašnjenje oba pitanja; odobrenje njihove promene još nije dato. Nisu menjani ni slajdovi ni formule u beleškama.

## Odobreno i primenjeno

| Slajd | Primena korisnikove odluke |
|---|---|
| s006 | Oba decimalna niza imaju tačan početak **0.346938775510204081632653061224489795…**, uz postojeći celobrojni deo 167 gde postoji. |
| s016 | Prva dva dvostruka indeksa su **b₍ₙ₋₁₎,₍ₖ₋₁₎** i **b₍ₙ₋₁₎,₍ₖ₋₂₎**, odnosno LaTeX `b_{(n-1),(k-1)}` i `b_{(n-1),(k-2)}`. |
| s034 | Naziv je **„komplement 10-tke“**; **1000 − 123 = 877** ostaje. |

Pogođeni projekcioni slajdovi i A4 prikazi beležaka pregledaju se ponovo, uz obnovu potvrda i `notes`, `review`, `check`. `Check` ostaje NEZAVRŠENO samo za s009/formule i s035/formule. Posle odluke o ta dva pitanja izvršiti njihove odobrene dorade i pregled, pa tek uz uspešnu završnu proveru postaviti `ceka_odobrenje`. Odobrenje stručnih ispravki nije prihvatanje cele 04 niti dozvola za 05.
