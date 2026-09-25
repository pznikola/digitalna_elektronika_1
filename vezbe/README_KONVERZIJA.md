# Izgradnja vežbi 03, 04, 05, 07 i 08

Iz korena repozitorijuma:

```sh
make -C vezbe          # ilustracije i svih pet dokumenata, redom
make -C vezbe check    # nezavisne matematičke i logičke provere
make -C vezbe 05       # samo vežba 05
make -C vezbe clean    # pomoćni fajlovi; PDF-ovi ostaju
```

Svaki folder podržava i samostalno izvršavanje `make` i `make check`.

Potrebni su GNU Make, Python 3, pdfLaTeX, latexmk i TeX Live paketi za srpski jezik, Latin Modern, AMS, booktabs, TikZ, Circuitikz, PGFPlots, standalone, tcolorbox, adjustbox i siunitx. Provere vežbe 08 koriste i Python paket SymPy. Za provere ostalih vežbi dovoljna je standardna Python biblioteka. Pandoc je korišćen prilikom konverzije DOCX dokumenata; nije potreban za redovnu izgradnju.

Glavni `.tex` fajlovi i svi crteži u `Images/` mogu se uređivati direktno. Make prvo izvozi crteže u vektorske PDF-ove, a zatim kompajlira dokument pomoću latexmk-a. Datum na naslovnoj strani određuje `\today` pri kompilaciji. U vežbi 03 nema izvornih ilustracija, pa nema ni praznih direktorijuma za njihove izvoze.

[Zajednički izveštaj](IZVESTAJ_KONVERZIJE.md) povezuje PDF dokumente, inventare i obrazloženja ispravki. U DOCX konverzijama komentari `Izvor DOCX: blok ...` omogućavaju praćenje porekla teksta; numeraciju jednačina, tabela i slika određuje LaTeX.

Makefile obuhvata navedene nove vežbe. Izvorni DOCX/PDF fajlovi i postojeći rad u vežbama 01 i 02 sačuvani su.
