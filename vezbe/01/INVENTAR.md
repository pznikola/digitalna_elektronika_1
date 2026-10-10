# Inventar — vežba 01

Obuhvaćeni su uvod sa osam osnovnih logičkih kola i deset pravila Bulove algebre, šest zadataka sa postojećim rešenjima, dva izdvojena zadatka za samostalni rad i oba dodatna samostalna zahteva uz zadatak 4.

Uvod, zadaci i pottačke, sve formule (uključujući izraze u tekstu), tabele, redovi tabela, Karnoove karte, slike i uključeni kod evidentirani su u `../PROVERA/registar.json` pod prefiksom `01-`. Registar čuva izvorni tekst, lokaciju, LaTeX oznaku gde postoji, SyncTeX stranicu i dokaze pregleda.

Šest šema za zadatke 1–3 ponovo je uređeno u postojećem Draw.io formatu. Zadatak 4 zadržava izvornu šemu i vremenski dijagram. Ugrađene Karnoove karte ostaju izmenjivi LaTeX/TikZ sadržaj. Nisu dodata studentska rešenja samostalnih zadataka.

## Aktivni SystemVerilog materijali

Vežba 01 sadrži deset glavnih `.sv` realizacija, pomoćni model izvorne mreže i deset testbenchova; svih 12 VHDL izvora ostalo je sačuvano.
Aktivni listing i testbench linkovi koriste SystemVerilog. Registar prati `.sv` izvore i odvojeno sačuvane VHDL reference; stari brojevi VHDL listinga u inventaru odnose se na istorijsku verziju.

## Dopuna Verilog primera — 09.10.2026.

Dodato 4 novih glavnih primera, svaki sa testbenchom i lokalnim Makefile-om. Kod je uključen uz postojeća rešenja, bez promene njihovih formula i šema.

- [code/Zadatak_1/b](code/Zadatak_1/b/zadatak.sv)
- [code/Zadatak_1/c](code/Zadatak_1/c/zadatak.sv)
- [code/Zadatak_1/d](code/Zadatak_1/d/zadatak.sv)
- [code/Zadatak_4/c](code/Zadatak_4/c/zadatak.sv)

Simulacija: `make` u folderu primera pokreće Verilator; `make run_iverilog` pokreće Icarus. Zajednički `make -C vezbe check-sv` obuhvata i ovu dopunu. Izvorni tekst listinga čuva PDF ActualText; `check-pdf-code` proverava kopiranje i simulaciju izvučenog koda.
