# Stručna pitanja — predavanje 04

Datum: **2026-10-02**. Korisnik je odobrio ispravke s006, s016 i s034, a zatim usklađivanje jednačina s034/s035. Preostalo pitanje je samo **s009**, za koje je zatraženo pojašnjenje. Predlozi i odluke ostaju u tehničkoj evidenciji, izvan nastavnih beležaka.

[PLAN_PREDAVANJA.md §1.1](../../../../PLAN_PREDAVANJA.md) propisuje: „Promene formula, vrednosti, topologije kola, stručnih tvrdnji ili uslova zahtevaju korisnikovo izričito odobrenje.“ Stvarna poruka i obim odluke su u [odluke.md](odluke.md).

## Otvorena pitanja

| Slajd | Izvorni zapis i problem | Predložena stručna ispravka |
|---|---|---|
| s009 | Iz CV/rⁿ < 1 naveden je n ≥ logᵣ CV. Taj slabiji uslov ne garantuje dovoljno cifara kada je CV = rᵐ: za CV = 8, r = 2 dopušta n = 3, dok je 8₁₀ = 1000₂ i zahteva 4 cifre. | **n > logᵣ CV, za CV > 0**. Najmanji broj cifara je ⌊logᵣ CV⌋ + 1. Za CV = 0 koristi se jedna cifra; logaritam nule nije definisan. |

Slabiji uslov s009 jeste nužan za ispravan broj cifara, ali nije dovoljan; stroga nejednakost daje tačan kriterijum. S035 je sada ispravljeno: ponovljeno komplementiranje vraća početni kod. U fiksnoj širini kodiranje i prenos posmatraju se modulo 2ⁿ.

Korisnik je zatražio objašnjenje s009; njegova stručna izmena još nije odobrena. S009 i pripadajuće beleške nisu menjani.

## Odobreno i primenjeno

| Slajd | Primena korisnikove odluke |
|---|---|
| s006 | Oba decimalna niza imaju tačan početak **0.346938775510204081632653061224489795…**, uz postojeći celobrojni deo 167 gde postoji. |
| s016 | Prva dva dvostruka indeksa su **b₍ₙ₋₁₎,₍ₖ₋₁₎** i **b₍ₙ₋₁₎,₍ₖ₋₂₎**, odnosno LaTeX `b_{(n-1),(k-1)}` i `b_{(n-1),(k-2)}`. |
| s034 | Naziv je **„komplement 10-tke“**; **1000 − 123 = 877** ostaje. Binarna jednačina piše se **M − B + 1 = invertovani B + 1**, gde je M = 2ⁿ − 1, u skladu sa opštom formulom. |
| s035 | Druga jednačina je **M − (invertovani B + 1) + 1 = B**: oduzima se ceo prethodni kod, pa se dodaje jedinica. Prva jednačina za prvi komplement ostaje ista. Korisnik je izričito odobrio ovu promenu. |

Pogođeni projekcioni slajdovi i A4 prikazi beležaka pregledaju se ponovo, uz obnovu potvrda i `notes`, `review`, `check`. `Check` ostaje NEZAVRŠENO samo za s009/formule. Posle odluke o tom pitanju izvršiti odobrenu doradu i pregled, pa tek uz uspešnu završnu proveru postaviti `ceka_odobrenje`. Odobrenje stručnih ispravki nije prihvatanje cele 04 niti dozvola za 05.
