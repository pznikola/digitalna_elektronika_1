# Inventar prenosa — vežbe 05

Izvorni brojevi blokova odnose se na Pandoc strukturu DOCX dokumenta. U glavnom `.tex` fajlu ostavljeni su odgovarajući komentari.

| Izvorna celina | Nova oznaka |
|---|---|
| Uvod (blok 22) | `sec:1` |
| Kodovi (blok 23) | `sec:1.1` |
| Težinski kodovi (blok 27) | `sec:1.1.1` |
| Netežinski kodovi (blok 38) | `sec:1.1.2` |
| Kodovi sa mogućnošću detekcije greške (blok 63) | `sec:1.1.3` |
| Zadaci sa časova vežbi (blok 103) | `sec:2` |
| Zadatak 2.1. (blok 104) | `sec:2.1` |
| Zadatak 2.2. (blok 116) | `sec:2.2` |
| Zadatak 2.3. (blok 122) | `sec:2.3` |
| Zadatak 2.4 (blok 133) | `sec:2.4` |
| Zadatak 2.5 (blok 141) | `sec:2.5` |
| Zadatak 2.6.  (blok 149) | `sec:2.6` |

## Jednačine

Sve navedene izvorne oznake imaju LaTeX oznaku `eq:<izvorna oznaka>`; vidljivu numeraciju određuje LaTeX.

1.1.3.1, 1.1.3.2, 1.1.3.3, 1.1.3.4, 1.1.3.5, 2.6.1

## Prenos

Svi sadržinski blokovi od uvoda do kraja uključeni su; izvorna naslovna strana i statični sadržaj zamenjeni su novom naslovnom stranom i automatskim sadržajem. Izmene blokova i računskih tabela opisane su u izveštaju.

## Obuhvat zadataka, slika i tabela

Svih šest zadataka 2.1–2.6 preneto je redom (`sec:2.1`–`sec:2.6`), sa postojećim rešenjima. Izvorni sadržaj pominje samostalni rad, ali takvi zadaci ne postoje u telu DOCX fajla; zastarela stavka sadržaja nije preneta.

| Izvor | Nova oznaka / mesto |
|---|---|
| Tabela 1.1.1.1 — BCD8421 | `tab:bcd` |
| Tabela 1.1.1.2 — BCD2421 | `tab:2421`; osa, upareni redovi i komplementarnost |
| Tabela 1.1.2.1 — više 3 | `tab:excess` |
| Tabela 1.1.2.2 — konstrukcija Grejovog koda | `tab:graybuild`; sva četiri koraka n=1,2,3,4 |
| Algoritamske tabele za Grejovo kodovanje/dekodovanje (blokovi 54 i 57) | Opšta pravila uz istovetne komentare blokova |
| Tabela 1.1.2.3 — decimalni Grejov kod | `tab:graybcd` |
| Tabela 1.1.3.1 — Hamingova rastojanja | `tab:distances` |
| Tabela 1.1.3.2 — parnost | `tab:parity3` |
| Kanal prenosa (blok 65) | `fig:channel`, `Images/Uvod/kanal.tex` |
| Prva slika 1.1.3.1 — Hamingovo rastojanje | `fig:cube`, `Images/Uvod/kocke.tex` |
| Druga slika 1.1.3.1 — Hamingov kod | `fig:venn`, `Images/Uvod/ven.tex` |
| Slika 2.6.1 — primer greške | `fig:venn-task`, `Images/Zadatak_6/ven.tex` |

Duplirana izvorna oznaka 1.1.3.1 više ne dovodi do dvosmislenih referenci. Računske tabele zadataka, raspored informacionih i kontrolnih bita, sindromi, susedi broja 23 i postojeći primer proširenog Hamingovog koda ostaju uz svoje izvorne blokove. Tabele koje su služile samo kao raspored jednačina zamenjene su matematičkim okruženjima.

Izvorni blokovi tabela (uključujući Word raspored formula): 30, 35, 42, 50, 54, 57, 61, 68, 73, 76, 81, 86, 88, 90, 93, 95, 97, 99, 112, 114, 121, 132, 147, 161. Svaki ima komentar porekla u glavnom LaTeX fajlu.
