# Inventar prenosa — vežbe 04

Izvorni brojevi blokova odnose se na Pandoc strukturu DOCX dokumenta. U glavnom `.tex` fajlu ostavljeni su odgovarajući komentari.

| Izvorna celina | Nova oznaka |
|---|---|
| Uvod (blok 31) | `sec:1` |
| Sabiranje i oduzimanje neoznačenih brojeva (blok 32) | `sec:1.1` |
| Aritmetičke operacije u predstavi znak i apsolutna vrednost (blok 43) | `sec:1.2` |
| Sabiranje i oduzimanje brojeva u komplementu osnove (blok 46) | `sec:1.3` |
| Sabiranje i oduzimanje brojeva u komplementu maksimalne vrednosti (blok 51) | `sec:1.4` |
| Množenje neoznačenih brojeva (blok 55) | `sec:1.5` |
| Množenje označenih brojeva (blok 58) | `sec:1.6` |
| Deljenje neoznačenih brojeva (blok 60) | `sec:1.7` |
| Zadaci sa časova vežbi (blok 62) | `sec:2` |
| Zadatak 2.1. (blok 63) | `sec:2.1` |
| Zadatak 2.2. (blok 73) | `sec:2.2` |
| Zadatak 2.3. (blok 80) | `sec:2.3` |
| Zadatak 2.4 (blok 90) | `sec:2.4` |
| Zadatak 2.5 (blok 100) | `sec:2.5` |
| Zadatak 2.6.  (blok 111) | `sec:2.6` |
| Zadaci za samostalni rad (blok 117) | `sec:3` |
| Zadatak 3.1.  (blok 118) | `sec:3.1` |
| Zadatak 3.2.  (blok 123) | `sec:3.2` |
| Zadatak 3.3.  (blok 132) | `sec:3.3` |
| Zadatak 3.4.  (blok 143) | `sec:3.4` |
| Zadatak 3.5. (blok 176) | `sec:3.5` |
| Zadatak 3.6. (blok 181) | `sec:3.6` |

## Jednačine

Sve navedene izvorne oznake imaju LaTeX oznaku `eq:<izvorna oznaka>`; vidljivu numeraciju određuje LaTeX.

1.1.1, 1.2.1, 3.3.1, 3.4.1, 3.4.2, 3.4.3, 3.4.4, 3.4.5, 3.4.6, 3.4.7, 3.4.8, 3.4.9, 3.4.10, 3.4.11, 3.4.14, 3.4.15, 3.4.18

## Prenos

Svi sadržinski blokovi od uvoda do kraja uključeni su; izvorna naslovna strana i statični sadržaj zamenjeni su novom naslovnom stranom i automatskim sadržajem. Izmene blokova i računskih tabela opisane su u izveštaju.

## Obuhvat zadataka, slika i tabela

Šest zadataka sa časova (2.1–2.6) i šest za samostalni rad (3.1–3.6) daju ukupno dvanaest zadataka. Oznake su `sec:2.1`–`sec:2.6` i `sec:3.1`–`sec:3.6`. Preneta su postojeća rešenja samostalnih zadataka 3.3 i 3.4; nova rešenja ostalim samostalnim zadacima nisu dodata.

| Izvorna ilustracija | Nova oznaka | Izvor crteža u `Images/` |
|---|---|---|
| Slika 3.3.1 | `fig:comp2` | `Zadatak_3/komparator2.tex` |
| Slika 3.3.2 | `fig:comp4` | `Zadatak_3/komparator4.tex` |
| Slika 3.3.3 | `fig:max` | `Zadatak_3/maksimum.tex` |
| Slika 3.4.1 (tri Karnoove karte) | `fig:kmap` | `Zadatak_4/karno.tex` |
| Slika 3.4.2 | `fig:adder` | `Zadatak_4/sabirac.tex` |
| Slika 3.4.3 | `fig:mux4` | `Zadatak_4/mux4.tex` |
| Prva slika 3.4.4 — proizvod X | `fig:x` | `Zadatak_4/proizvod.tex` |
| Druga slika 3.4.4 — izlaz Y | `fig:y` | `Zadatak_4/kompletna.tex` |

Duplirana oznaka 3.4.4 iz izvora zamenjena je jedinstvenim automatskim brojevima. Tabela 3.4.1 odgovara `tab:adder`, a pregled 3(A+1) odgovara `tab:triS`. Aritmetičke tabele ostaju uz odgovarajuća rešenja; svih 62 računska primera sa međukoracima povezano je sa `code/rezultati.json`.

Jednačine 3.4.12, 3.4.13, 3.4.16 i 3.4.17, ručno rekonstruisane iz složenijih Word zapisa, takođe imaju oznake `eq:<izvorna oznaka>`. Tri formule koje su u DOCX bile WMF slike prenete su kao izmenjiva matematika u zadatku 3.2, uključujući zadate iskaze koje student treba da proveri.

Izvorni blokovi tabela (uključujući Word raspored formula): 34, 35, 39, 40, 49, 53, 70, 72, 79, 87, 89, 97, 99, 108, 110, 116, 136, 145, 148, 152, 154, 158, 160, 164, 168, 170. Svaki ima komentar porekla u glavnom LaTeX fajlu.

## Ponovna provera 25. 9. 2026.

Provereno je 12 zadataka, 35 numerisanih jednačina, 22 sadržinske tabele (četiri simbolička prikaza postupaka u uvodu, 16 tabela konkretnih računskih postupaka i dve funkcionalne tabele) i osam ilustracija. Ilustracija `karno` sadrži tri zasebne karte, ukupno 48 ćelija i 11 implicanata. Naslovna tabela sa kontaktima evidentira se odvojeno.

Šesnaest postupaka ima nove oznake `tab:postupak-1`–`tab:postupak-16`, nazive i ponovljena zaglavlja nastavaka. Njihov sadržaj i redosled ostali su isti. Ranije nenazvane numerisane formule dobile su oznake `eq:racun-1`–`eq:racun-14`. U proverama se prati svih 54 komplementnih/neoznačenih operacija, osam ZA izraza (pet objavljenih rezultata), šest množenja i tri deljenja sa ukupno 26 koraka. Rešenja samostalnih pottačaka nisu dopisana. Matematika i konkretne veze dokumentovane su u `code/PREGLED_DOKAZA.md` i `code/pregled_izvora.json`. Pregledano je svih 27 konačnih stranica.


### Dopuna prikaza posle korisničkog pregleda

Broj zadataka, 35 numerisanih jednačina, 22 sadržinske tabele i osam ilustracija nisu promenjeni. Tabele `tab:postupak-8`–`tab:postupak-16` sada sadrže pisani račun, umesto prethodnog sažetog pregleda po koracima. Šest množenja obuhvata oba izvorna postupka; tri deljenja imaju 18 oduzimanja i 15 dopisivanja, uz grupisanje početnog prefiksa kao u originalu. Sve vrednosti, početne cifre i konačni rezultati su obuhvaćeni. U prvoj tabeli odeljka 1.4 vraćena je strelica kružnog prenosa. U `fig:kmap` dodata je ispuna postojećih grupa; u `fig:adder` direktne veze i zamenjen raspored ulaza desnog I kola. Detalji i razlog su u nalazima 04-A13–A16. Prethodni brojevi koraka i opisi sažetih tabela odnose se na raniju verziju.

Dopuna 04-A17: u Slici 7 (`fig:x`) D₁ je prebačen sa dijagonalnog voda na horizontalni odvod iste vertikale S, uz tačku spoja. Broj slika i funkcija nisu promenjeni.
