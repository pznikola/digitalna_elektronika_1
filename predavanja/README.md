# Predavanja — LaTeX Beamer

Plan i pravila sadržinskog prenosa: [PREDAVANJA.md](../PREDAVANJA.md).

Izvori obuhvataju 12 PDF-ova, 314 PDF strana i **620 originalnih slajdova**.
Originali ostaju neizmenjeni u ovom folderu. Materijal u `vezbe` se ne menja.

## Status

Završeno je svih **12 prezentacija sa ukupno 620 slajdova**. Svaki slajd ima
sadržinski i vizuelni pregled, vezan kontrolnim sumama za originalni i novi prikaz.
[Završni izveštaj](IZVESTAJ.md) opisuje rezultate provera i evidenciju grešaka originala.

| Predavanje | Rekonstruisano i pregledano | Završna provera |
|---|---:|---|
| 01 Logičke funkcije | 37/37 | prolazi |
| 02 Sinteza kombinacionih mreža | 54/54 | prolazi |
| 03 Kola srednjeg stepena integracije | 21/21 | prolazi |
| 04 Brojni sistemi | 39/39 | prolazi |
| 05 Aritmetičke operacije | 55/55 | prolazi |
| 06 Kodovi | 30/30 | prolazi |
| 07 Uvod u HDL | 31/31 | prolazi |
| 08 Elementi analize logičkih kola | 67/67 | prolazi |
| 09_1 MOS logička kola, 1. deo | 57/57 | prolazi |
| 09_2 MOS logička kola, 2. deo | 62/62 | prolazi |
| 09_3 MOS logička kola, 3. deo | 71/71 | prolazi |
| 10 Logička kola sa bipolarnim tranzistorima | 96/96 | prolazi |
| **Ukupno** | **620/620** | **prolazi** |

`provera/pregled.json` svakog predavanja sadrži potvrde po slajdu i kategoriji.
Promena pregledanog prikaza poništava raniju potvrdu.

`make all` odbija nepotpuno predavanje; `make check` odbija i neprovereno predavanje.
Nedostajući slajdovi se ne zamenjuju praznim okvirima ili slikama originalnih slajdova.

## Komande

Pokrenuti iz korena repozitorijuma:

```sh
make -C predavanja all
make -C predavanja LECTURE=01_logicke_funkcije all
make -C predavanja check
make -C predavanja review
make -C predavanja test
make -C predavanja clean
```

Za rekonstrukciju u toku postoji poseban radni prikaz:

```sh
make -C predavanja LECTURE=01_logicke_funkcije preview
make -C predavanja LECTURE=01_logicke_funkcije review
```

Konačan PDF: `<predavanje>/build/<predavanje>.pdf`.
Radni PDF: `<predavanje>/build/radni_pregled.pdf`; sadrži samo prenete slajdove i
zadržava njihovu izvornu numeraciju. Ne predstavlja konačnu prezentaciju.
Uporedni pregled: `<predavanje>/build/pregled/index.html`.

`make inventory` stvara samo inventare koji ne postoje. Ne prepisuje postojeće
inventare ili potvrde pregleda i odbija promenjen original.
`make clean` uklanja samo `build` podfoldere poznatih predavanja.

## Organizacija i rad

Svaki slajd je zaseban fajl u `slajdovi`, eksplicitno uključen u glavni `.tex`.
Oznaka `\slajdid{01-s001}` se zapisuje pri slanju stvarne strane u PDF, pa provera
može da otkrije dodatne overlay strane, duplikate i promenjen redosled.
Izvori crteža su u `slike/tikz`, tabela u `tabele`, a koda u `kodovi`.
Podaci i izvorne slike imaju posebne podfoldere.

Automatski tekst u `mapa.json` je pomoć pri prepisivanju. Ne predstavlja kompletan
inventar formula, slika i koda. Tek posle pregleda originala popuniti `inventory`
i postaviti `inventory_confirmed`. Sačuvati stabilan `id` i izvornu lokaciju.

Posle pregleda originalnog i novog prikaza upisati statuse kategorija i preciznu
belešku u `pregled.json`, kao i oba otiska iz `build/pregled/otisci.json`.
Ne postoji komanda koja automatski potvrđuje sadržaj. Ponovno renderovanje nakon
promene otkriva zastarele potvrde. Prikaz tekstualnih razlika je pomoć, ne zamena
za pregled svih formula, ćelija i veza.

## Zavisnosti

- GNU Make, Python 3, Pillow (za isečke originala).
- Poppler: `pdfinfo`, `pdftotext`, `pdftoppm`.
- LuaLaTeX i latexmk, fontovi Latin Modern.
- TeX paketi: Beamer, fontspec, babel-serbian, AMS, mathtools, array, booktabs,
  tabularx, multirow, makecell, listings, TikZ, CircuitikZ, PGFPlots i karnaugh-map.

Provereno okruženje: LuaHBTeX 1.14.0 / TeX Live 2022-dev (Debian), latexmk 4.76,
GNU Make 4.3, Python 3.13.9, Pillow 12.0.0 i Poppler 22.02.0.
Računske provere koriste samo standardnu Python biblioteku. GHDL je korišćen
za dodatnu analizu izvornog HDL primera; nije zavisnost izgradnje ni `make check`.
Izgradnja ne pristupa mreži i koristi `-no-shell-escape`.
Tema i stilovi nalaze se u `_zajednicko`; `build` sadržaj se ne verzioniše.

## Poreklo

Originalni slajdovi nose oznake „Digitalna elektronika 1 - 2021/22“,
„Katedra za elektroniku“ i „prof dr Lazar Saranovac“.
Ovi ponavljajući elementi i ETF logo uklanjaju se iz novih slajdova prema planu.
Greške izvornog sadržaja evidentiraju se zasebno i ne ispravljaju prećutno.
