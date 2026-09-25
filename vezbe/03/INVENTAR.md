# Inventar prenosa — vežbe 03

Izvorni brojevi blokova odnose se na Pandoc strukturu DOCX dokumenta. U glavnom `.tex` fajlu ostavljeni su odgovarajući komentari.

| Izvorna celina | Nova oznaka |
|---|---|
| Uvod (blok 29) | `sec:1` |
| Konverzije brojnih sistema (blok 31) | `sec:1.1` |
| Prelazak iz brojnog sistema sa osnovom r u brojni sistem sa osnovom p  (blok 39) | `sec:1.1.1` |
| Prelazak iz dekadnog brojnog sistema u brojni sistem sa osnovom r (blok 48) | `sec:1.1.2` |
| Prelazak iz brojnog sistema čija je osnova stepen broja dva u brojni sistem čija je osnova stepen broja 2 (blok 63) | `sec:1.1.3` |
| Predstave brojeva u digitalnim sistemima (blok 66) | `sec:1.2` |
| Znak i apsolutna vrednost (blok 69) | `sec:1.2.1` |
| Komplement maksimalne vrednosti  (blok 73) | `sec:1.2.2` |
| Komplement osnove  (blok 87) | `sec:1.2.3` |
| Zadaci sa časova vežbi (blok 99) | `sec:2` |
| Zadatak 2.1. (blok 100) | `sec:2.1` |
| Zadatak 2.2.  (blok 122) | `sec:2.2` |
| Zadatak 2.3.  (blok 134) | `sec:2.3` |
| Zadatak 2.4.  (blok 148) | `sec:2.4` |
| Zadatak 2.5.  (blok 171) | `sec:2.5` |
| Zadatak 2.6.  (blok 194) | `sec:2.6` |
| Zadatak 2.7.  (blok 227) | `sec:2.7` |
| Zadaci za samostalni rad (blok 250) | `sec:3` |
| Zadatak 3.1.  (blok 251) | `sec:3.1` |
| Zadatak 3.2.  (blok 256) | `sec:3.2` |

## Jednačine

Sve navedene izvorne oznake imaju LaTeX oznaku `eq:<izvorna oznaka>`; vidljivu numeraciju određuje LaTeX.

1.1.1.1, 1.1.1.2, 1.1.1.3, 1.1.1.4, 1.1.1.5, 1.1.1.6, 1.1.1.7, 1.1.1.8, 1.1.1.9, 1.2.1.1, 1.2.2.1, 1.2.2.2, 1.2.2.3, 1.2.2.4, 1.2.2.5, 1.2.3.1, 1.2.3.2, 1.2.3.3, 1.2.3.4, 1.2.3.5, 2.1.1, 2.1.2, 2.1.3, 2.1.4, 2.1.5, 2.1.6, 2.1.7, 2.2.1, 2.2.2, 2.2.3, 2.2.4, 2.3.1, 2.3.2, 2.3.3, 2.3.4, 2.3.5, 2.3.6, 2.3.7, 2.3.8, 2.3.9, 2.3.10, 2.3.11, 2.3.12, 2.3.13, 2.3.14, 2.4.1, 2.4.2, 2.4.3, 2.4.4, 2.4.5, 2.4.6, 2.4.7, 2.4.8, 2.4.9, 2.4.10, 2.4.11, 2.4.12, 2.4.13, 2.4.14, 2.4.15, 2.4.16, 2.4.17, 2.4.18, 2.4.19, 2.4.20, 2.4.21, 2.4.22, 2.4.23, 2.4.24, 2.4.25, 2.4.26, 2.4.27, 2.4.28, 2.4.29, 2.4.30, 2.4.31, 2.5.1, 2.5.2, 2.5.3, 2.5.4, 2.5.5, 2.5.6, 2.5.7, 2.5.8, 2.5.9, 2.5.10, 2.5.11, 2.5.12, 2.5.13, 2.5.14, 2.5.15, 2.5.16, 2.5.17, 2.5.18, 2.5.19, 2.5.20, 2.5.21, 2.5.22, 2.5.23, 2.5.24, 2.5.25, 2.5.26, 2.5.27, 2.5.28, 2.5.29, 2.5.30, 2.5.31, 2.6.1, 2.6.2, 2.6.3, 2.6.4, 2.6.5, 2.6.6, 2.6.7, 2.6.8, 2.6.9, 2.6.10, 2.7.1, 2.7.2, 2.7.3, 2.7.4, 2.7.5, 2.7.6, 2.7.8, 2.7.9, 2.7.10, 2.7.11, 2.7.12, 3.2.1, 3.2.2, 3.2.3

## Prenos

Svi sadržinski blokovi od uvoda do kraja uključeni su; izvorna naslovna strana i statični sadržaj zamenjeni su novom naslovnom stranom i automatskim sadržajem. Izmene blokova i računskih tabela opisane su u izveštaju.

## Obuhvat zadataka i tabela

Preneto je sedam zadataka sa časova (izvor 2.1–2.7 → `sec:2.1`–`sec:2.7`) i dva zadatka za samostalni rad (3.1–3.2 → `sec:3.1`–`sec:3.2`), ukupno devet. Preneta su postojeća rešenja; samostalnim zadacima nisu dodata nova rešenja. Izvor nema sadržinske ilustracije.

Tabele korišćene samo za poravnanje numerisanih formula postale su okruženja `equation`. Postupci deljenja i množenja pri konverziji, periodični zapisi, pregledi predstava i tabele zadatih primera ostali su izmenjivi matematički sadržaj. Njihovo poreklo određuju komentari blokova u `.tex` fajlu.

Izvorni blokovi tabela (uključujući Word raspored formula): 35, 41, 43, 45, 52, 55, 57, 60, 62, 71, 75, 77, 80, 83, 86, 89, 91, 93, 95, 98, 107, 109, 111, 116, 119, 121, 124, 128, 130, 132, 141, 145, 147, 155, 157, 159, 161, 163, 165, 167, 169, 178, 180, 182, 184, 186, 188, 190, 192, 202, 204, 209, 211, 214, 216, 219, 221, 224, 226, 234, 236, 238, 240, 242, 244, 246, 249, 258, 260, 263. Svaki ima komentar porekla u glavnom LaTeX fajlu.

## Ponovna provera 25. 9. 2026.

Trenutni dokument ima 134 numerisane jednačine, dve sadržinske računske tabele (blokovi 109 i 111), devet zadataka i nema sadržinskih ilustracija. Naslovna tabela sa kontaktima nije računska tabela. Dodate su stabilne oznake `eq:zapis`, `eq:13-375` i `eq:2.7.13` za tri već postojeće jednačine. Prethodna formulacija o „pregledima predstava i tabelama zadatih primera“ odnosi se na izmenjive matematičke izraze, ne na dodatna okruženja `tabular`. Mesta izvora i sva rešenja sačuvani su. Dokazi svih formula povezani su preko `code/pregled_formula.json`; pregled svih 17 konačnih stranica evidentiran je u zajedničkom registru.
