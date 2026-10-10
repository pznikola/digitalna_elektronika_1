# Otvorena stručna pitanja — 09_3

Pregled 2026-10-03. Naredni predlozi **nisu primenjeni**. Raspored i potpune beleške pripremljeni su za korisnikov pregled, ali ove izvorne tvrdnje/oznake sprečavaju završnu sadržinsku potvrdu. Prema `PLAN_PREDAVANJA.md` §1.1 i §6, izmene formula, uslova i stručnih tvrdnji zahtevaju izričitu odluku korisnika. Dovoljno je odgovoriti po oznakama P01–P13. Moguće je prihvatiti predlog, dati drugačiju formulaciju ili izričito zadržati izvorni zapis uz dogovoreno objašnjenje.

| Predlog | Slajdovi | Odluka koja se traži |
|---|---|---|
| P01 | s011–s013 | Usloviti vezu sa pokretljivošću i tvrdnje o tehnološki nezavisnom optimumu. |
| P02 | s017–s019, s021/s022 | Razdvojiti oznake fanouta i veličine stepena. |
| P03 | s021/s022 | Navesti pretpostavke γ=1 i jednakog završnog fanouta. |
| P04 | s021/s022 | Najbliži neparni N označiti kao heuristiku i porediti stvarna kašnjenja. |
| P05 | s020 | Precizirati značenje „nema zatvorenu formu“. |
| P06 | s028/s029 | „Ekvivalentna širina“ → „ekvivalentni geometrijski faktor W/L“. |
| P07 | s035 | Kritičnu putanju definisati ukupnim kašnjenjem. |
| P08 | s037 | Uskladiti krajnju kapacitivnost sa definicijom W na s036. |
| P09 | s043 | Ispraviti oznake i poslednji indeks u izrazu D. |
| P10 | s051 | Oznaku VGTn zameniti pragom VTn i precizirati konačno stanje. |
| P11 | s062 | Uvodni VI=−12 V zameniti sa VI=+12 V. |
| P12 | s066 | Uskladiti izlaznu jednačinu sa izlaznim invertorom. |
| P13 | s071 | Precizirati ograničenje standardne domino logike. |

## P01 — Model odnosa P/N i jedinični invertor

Na s009 korišćen je model kratkog kanala, dok s011 prelazi na `r≈IDnsat/IDpsat=μn/μp` bez dodatnih pretpostavki. Iz izvedene funkcije sledi **β=√r**; poslednja zamena pokretljivostima nije opšta. Čak i u kvadratnom modelu jednakih dimenzija odnos struja zavisi od odnosa `(VDD−VTn)²/(VDD−|VTp|)²`. Korekcije λ i modeli kratkog kanala mogu ga dodatno menjati.

Predlog: zadržati izvedeni optimum β=√r, a vezu sa μ usloviti odgovarajućim modelom, približno jednakim apsolutnim pragovima i zanemarljivom razlikom korekcija. Na s013 odnos 2:1 nazvati izabranim referentnim kompromisom; minimalno dinamičko kašnjenje i statički prag VDD/2 ne garantovati za svaku tehnologiju. Sam s012 razlikuje dinamički i statički optimum.

## P02 — Fanout i normirana veličina

Na s017/s018 `f_i` je odnos susednih kapacitivnosti, a s019/s021/s022 koristi `f_i` za ukupnu normiranu veličinu, sa `f_1=1` i odnosima `f_(i+1)/f_i`. Predlog: veličine nazvati `k_i`, fanout `h_i=C_(G,i+1)/C_(G,i)=k_(i+1)/k_i`, a jedinstveni idealni faktor ostaviti `f`. Svi postojeći međukoraci ostaju, uz dosledne oznake. Krajnje opterećenje `k_(N+1)=F` nije dodatni invertor.

## P03 — Pretpostavke približnog kašnjenja

Opšti zbir sa s019 ima `tp0/γ`; na s021 faktor izostaje. Predlog: na s021 eksplicitno navesti γ=1 ili vratiti opšti faktor. Na s022 `tp=5Ntp0` važi za γ=1 i **svih N fanouta jednakih 4**, uključujući završni CL. Ako je CL fiksiran i N zaokružen, poslednji fanout nije automatski 4. Predlog: prikazati uslov `F=4^N`; u ostalim slučajevima računati zbir sa stvarnim završnim opterećenjem.

## P04 — Neparan broj stepena

Najbliži neparan broj kontinualnom optimumu nije uvek najbolji diskretni izbor. Za F=10, γ=1, procena `ln(10)/ln(3.6)≈1.798` bira N=1. Međutim, za geometrijski dimenzionisane kandidate `t(1)/tp0=11`, a `t(3)/tp0=3(1+10^(1/3))≈9.463`. N=3 je brži. Predlog: nazvati postojeće zaokruživanje praktičnom procenom, uporediti susedne dopuštene neparne brojeve sa f=F^(1/N) i konačno proveriti stvarne celobrojne dimenzije i CL.

## P05 — Zatvorena forma

Iz `f ln(f)−f=γ` dobija se `f=exp(1+W₀(γ/e))`. Lambertova W funkcija je specijalna funkcija, ne elementarna. Predlog: umesto apsolutnog „nema zatvorenu formu“ napisati „nema jednostavan izraz u elementarnim funkcijama; rešavamo numerički“. Numeričko f≈3.6 za γ≈1 ostaje. Ovaj predlog je terminološko preciziranje; ne zahteva da se specijalna funkcija uvede studentima.

## P06 — Ekvivalentni geometrijski faktor

Za dva identična redna kanala izraz `W/(1+1)` računa normirani W/L, ne fizičku širinu. Predlog: promeniti samo stručni naziv; sačuvati Wp=4 za NILI i Wn=2 za NI, sve šeme i postojeće izvođenje. Brojne vrednosti se ne menjaju.

## P07 — Kritična putanja

Najveći broj kola ne garantuje najveće kašnjenje: dva kola po 10 vremenskih jedinica sporija su od tri kola po 1. Predlog: „Kritična putanja je putanja sa najvećim ukupnim kašnjenjem od ulaza do izlaza, uz tipove kola i njihova opterećenja.“ Šema označene putanje ostaje.

## P08 — Krajnje CL

S036 definiše W kao širinu N tranzistora i `Cin=3WCg`. Ako je to i dalje W na s037, krajnji uslov treba da bude `3CgW_(N+1)=CL`. Alternativa: eksplicitno redefinisati W kao ukupnu gejtsku širinu P+N, tako da postojeći krajnji izraz bude dosledan. Odnosi susednih širina ostaju isti jer se zajednički faktor 3 skraćuje.

## P09 — Završni izraz za D

Nacrtani niz je NI → invertor → NILI. Predlog:

```text
D = LE_NAND FO_i + P_NAND
  + LE_inv FO_(i+1) + P_inv
  + LE_NOR FO_(i+2) + P_NOR.
```

Izvorni `P_i`, `LE_OR`, `P_OR` i ponovljeni poslednji `FO_(i+1)` nisu dosledni prethodnom proširenom izrazu. Puna normalizacija ostaje; menjaju se ove oznake i indeks.

## P10 — Konačno stanje prolaznog nMOS

`VGTn` u `VGS=VGTn` nije prethodno definisana oznaka; na istom slajdu prag je `VTn`. Predlog: `VGS→VTn`, `I→0`, uz dostignuto `VY≈VA−VTn`. Tokom punjenja tranzistor je u zasićenju; krajnji idealizovani trenutak je granica uslova provođenja, pa ga treba razlikovati od provođenja konačne struje. Predlog ne menja gubitak nivoa ni dve postojeće šeme.

## P11 — Pozitivan ulaz

Uvod s062 navodi −12 V, dok šema, tok struje, opis P tranzistora i završni VO koriste +12 V. Predlog: promeniti **samo uvodni znak** u +12 V. Oba izvorna podatka trenutno su sačuvana za proveru.

## P12 — Izlaz selektora posle invertora

Unutrašnji selektorski čvor je `X=SA+S̄B`; fizički izlaz prikazanog invertora je `¬X`. Trenutna oznaka na tom izlazu je `Ȳ=SA+S̄B`, što izjednačava izlaz sa neinvertovanim X. Za S=1,A=1 unutrašnji čvor je 1, fizički izlaz 0, a desna strana ispisane jednačine 1.

Predlog: označiti fizički izlaz `Y=overline(SA+S̄B)`, a unutrašnji čvor `X=SA+S̄B` u objašnjenju. Ako želiš da se izlaz i dalje zove Ȳ, desna strana njegove jednačine mora biti komplement selektorske funkcije. Ne uklanja se invertor niti menjaju ulazi i kontrole.

## P13 — Ograničenje domino logike

Izlazni invertor invertuje dinamički čvor. Konačna funkcija je funkcija provođenja PDN: za rednu PDN A/B konačni izlaz je AB, dok dinamički čvor daje komplement AB. Zato tvrdnja „sve funkcije moraju biti invertovane“ ne opisuje jasno ograničenje ukupne realizacije.

Predlog: „Standardna domino kaskada zahteva monotono rastuće signale u fazi izračunavanja i realizuje neinvertujuće funkcije svojih raspoloživih ulaza.“ Sačuvati prikaz pripreme, izračunavanja, obe šeme i vremenske dijagrame. Ne uvoditi prećutnu tvrdnju da proizvoljna inverzija u domino kaskadi ostaje ispravna.

## Razjašnjeno bez stručne izmene originala

- S040 ima plus ispred γinv; potvrđen je i na originalnom renderu.
- S044 koristi drugi skup parazitnih pretpostavki: Pi=LEiγi daje γinv=0.5, γNAND=0.75, γNOR=0.9. To nije samo po sebi greška; razlika je objašnjena u beleškama.
- S046 ima **dva dodatna nMOS**, kao u originalu. Nije zamenjena uobičajenom komplementarnom varijantom.
- S059 zadržava sve gornje veze na A3 i prekide kolona: za 64 kombinacije daje aritmetičko pomeranje udesno sa proširenjem znaka.
- S067 ostaje zadatak Y=? na slajdu; izvođenje XOR odgovora nalazi se samo u beleškama predavača.
