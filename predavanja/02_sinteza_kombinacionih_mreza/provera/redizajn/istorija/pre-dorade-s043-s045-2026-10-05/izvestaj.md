# Predavanje 02 — dorada s040–s042

**Status: `ceka_odobrenje` · 2026-10-04.** Svi aktuelni nalozi primenjeni i pregledani; provere prolaze, nema otvorenih stručnih pitanja. Korisnik nije odobrio gotovu prezentaciju.

## Obuhvat i verzija

Originalni PDF ostaje neizmenjen: 27 strana i 54 izvorna slajda. Prezentacija i PDF beležaka imaju po **60 strana**, sa ranije odobrenim nastavcima s002b/s009b/s015b/s023b/s024b/s032b. Broj, redosled i stabilni ID-jevi nisu menjani ovom doradom. Stil B, zamrznuta tema etf-v1, fontovi, LuaLaTeX, odnos 16:9, autorstvo i školska godina 2021/22 ostaju očuvani. Naslov s041 „Algoritam minimizacije“ usklađen je sa pratećim PDF-om. Funkcije, vrednosti, topologije i odobrena zaglavlja nisu promenjeni.

## Izmene i pokrivenost

| ID / PDF strana | Rezultat |
|---|---|
| s040 / 46 | Dve gornje desne karte bliže znaku jednakosti. Donje grupe 0/4 i 0/1/4/5 označene otvorenim tamnocrvenim konturama preko gornje i donje ivice, uz svetlu podlogu. Dodate strelice uklonjene su po poslednjem nalogu. |
| s041 / 47 | Potpuniji izvorni tok: unos funkcije iz tabele/specifikacije, oba numerisana koraka, izvorni crveni naglasak „što manjim brojem površina što višeg reda“, uslov i garancija minimalnosti I/ILI realizacije i dostupnost pravih/komplementnih ulaza. |
| s042 / 48 | Potpunije izvorno objašnjenje proizvoljne vrednosti b/X, izbora 1 ili 0 za oba oblika ili obrnutog izbora radi sažimanja, objedinjavanja proizvoda površinama, stalnih literala/komplemenata i izostavljanja promenljivih koje se menjaju. Izvorni podvučeni naglasci sada su tamnocrveni. |

Pokriveno je **222/222 elemenata: 163 izvorne grupe i 59 dopuna**. **110 elemenata** ima odredište u beleškama. Izvorna objašnjenja minimalnosti s041 i izbora vrednosti s042 sada su potpuno vidljiva; njihove izvorne celine više ne zahtevaju dodatno odredište u beleškama. [Mapa pokrivenosti](pokrivenost.md), [evidencija beležaka](evidencija_beleski.json) i [odluke](odluke.md) čuvaju poreklo izvan nastavnog PDF-a.

Beleške s041 zadržavaju dodatnu vezu broja/redova površina sa članovima/literalima, dopušteno preklapanje, proveru celog pokrivanja i ograničenja kriterijuma. Uklonjeno je nepotrebno ponavljanje uslova i pretpostavke sada prikazanih na slajdu. Nastavni tekst beležaka s040 i s042 bajtno je nepromenjen: indeksiranje/grupe i konkretni algebarski primeri ostaju dodatno nastavno objašnjenje. Nema uredničke evidencije ili korisnikovih odluka u PDF-u beležaka. Izvorni jezički zapisi preformulisani su bez stručne izmene: „Da bi dobili“ u „Za funkciju…“, „kako logička nula“ u „kao logičku nulu“ i „što minimalnija“ u „što jednostavnija“.

## Pregled i provere

Stvarno su pregledani originali, početni prikazi, lokalni izvori, konačni slajdovi i cele A4 beleške **s040/s041/s042**. Provereni su svi indeksi, grupe, konture preko ivica, oznake, formule u beleškama, potpunost izvornog sadržaja, razmaci i čitljivost.

[Poređenje prikaza](poredjenje_dorade_s040_s042.json) dokazuje pikselnu jednakost **ostalih 57 celih slajdova i A4 strana**, uz očuvane važeće potvrde. Tri pogođene potvrde obnovljene su posle stvarnog pregleda. Originalni PDF i istorijska mapa ostaju neizmenjeni. Dodatno su provereni parovi susednih indeksa i algebarski primeri sažimanja u beleškama s042.

Izvršeno sa izlaznim kodom 0:

```bash
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza notes
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza review
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza check
```

**`check`: PROVERENO.** Strukturne i postojeće računske provere prolaze. Oba konačna LaTeX loga nemaju prekoračenja prostora, upozorenja ili grešaka. Potvrđeno je 60 slajdova i 60 A4 strana, tačan redosled i povezivanje ID-jeva. Alati i zajednička tema nisu menjani.

[Notes log](../../build/redizajn/dorada-s040-s042-2026-10-04/notes.log), [review log](../../build/redizajn/dorada-s040-s042-2026-10-04/review.log), [check log](../../build/redizajn/dorada-s040-s042-2026-10-04/check.log).

## Arhiva, isporuka i nastavak

Neposredno prethodna verzija sa 60 slajdova sačuvana je u `istorija/pre-oznaka-susedstva-s040-2026-10-04/izvori-i-evidencija.tar.gz`, sa [tadašnjim izveštajem](istorija/pre-oznaka-susedstva-s040-2026-10-04/izvestaj.md). Prethodni prikazi su u `build/redizajn/pre-oznaka-susedstva-s040-2026-10-04/`; ranije dorade i tadašnji otisci ostaju istorija.

- [Prezentacija — 60 slajdova](../../build/02_sinteza_kombinacionih_mreza.pdf), pogođene strane 46–48.
- [PDF beležaka — 60 A4 strana](../../build/02_sinteza_kombinacionih_mreza_beleske.pdf).
- [Uporedni pregled](../../build/redizajn/pregled/index.html).

Generisani PDF/PNG/HTML i logovi u `build/` ne verzionišu se i obnavljaju gornjim komandama. Sledeći korak je korisnikov pregled ove verzije 02; gotov rezultat nije odobren. Ranije dozvole za druga predavanja su odvojene i nisu menjane.

## SHA-256 pregledane verzije

| Resurs | Otisak |
|---|---|
| Originalni PDF | `f631914c9f32a0472f4fa3af11115abaadb9316dfcf6f1528cd91ef4d28868f4` |
| Izvorna mapa | `b2c8e07fa123a40da68c8b89b1b1c6ce88112e90c7417792cdec341d60136ca2` |
| Manifest | `b01aa603f6dce15bfb20d7447e59bdb2898847455610b1fd7d07a8520b126fe4` |
| Prezentacioni PDF | `8a6019633b96c638821fcfc9b30b6e3ee02f7f05dd34c04a909c60ccb0bfe5f6` |
| PDF beležaka | `3a618ab78e82e690eb61080c4485843d2aa7bd723ef5b2307cc8e28ec971795f` |
| Zapis izgradnje | `9e15b4fb79915664f9a7d7f0ed0153cf52117e5511bad06d3f20dc21ca518f7d` |
| Potvrde pregleda | `bd04f72a95d7d73effab044962f7239462bce331a4f28ae3e49f51de966136cd` |
| Evidencija beležaka | `aa1ae3f159b07fa3573ca379841cae841d357b0e1e82c24d9bd1fd5db70025fa` |
| Poređenje prikaza | `990420ce350830c50823dbd5fc0f907acc54428467736c709ef63c5a00c6c146` |
| Arhiva prethodne isporuke | `ed77a993afe4c5f713d31fc4ac4419ae3e2fd83eafeaf20a09e20352fcc94a12` |
