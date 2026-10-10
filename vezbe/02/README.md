# Vežba 02 — sinteza kola srednjeg stepena integracije

- `make` — izvoz uključenih Draw.io/TikZ ilustracija i izgradnja samostalnog PDF-a.
- `make check` — stvarne LaTeX formule, tabele i Karnoove karte, logički opisi pregledanih šema, iscrpna BCD provera i referentne GHDL simulacije u Dockeru.
- `make clean` — uklanjanje pomoćnih LaTeX fajlova; izvori i PDF materijali ostaju sačuvani.

Potrebni su Python 3.10+, Docker sa lokalnim image-om `hdlview-tools:2025.12`, TeX Live sa pdfLaTeX-om, latexmk-om, paketima minted/TikZ/karnaugh-map i Pygmentsom, kao i Draw.io Desktop CLI i xvfb-run. Minted zahteva shell-escape za lokalno bojanje uključenih primera. Izvozi se rade u privremenom direktorijumu; neuspešan izvoz ne može se sakriti postojećim starim PDF-om.

Četrnaest aktivnih primera i osam pomoćnih modula napisani su u SystemVerilogu. U folderu primera `make` pokreće Verilator. Pomoćni modul proverava se ciljem `run_iverilog` uz odgovarajući `TOP=tb_decoder`, `TOP=tb_mux4` ili `TOP=tb_decoder3`. U osam postojećih VHDL/SV parova dostupan je i `make run_ghdl` za sačuvani VHDL. Zajednički `make -C .. check-sv` obuhvata sve testbenchove i njihove X/Z slučajeve; `check-equivalence` poredi izvorne VHDL/SV primere kroz sve signalne putanje. Detalji su u [zajedničkom README-u](../README.md#verilog-primeri-i-simulacije).

Crteže menjati kroz `.drawio` ili `.tex` izvor. Posle izmene šeme ponoviti praćenje veza i ažurirati njen pregled u `code/pregled_sema.json`; provera namerno odbija promenjen izvor bez novog pregleda. Karnoova karta sa strelicama ostala je u izvornom rasporedu. PNG je sačuvan, ali je njegova ilustracija u dokumentu zamenjena TikZ/PDF verzijom.

[Izveštaj ispravki](IZVESTAJ_ISPRAVKI.md) razlikuje greške izvora, zastarele izvoze i dopunske pretpostavke. [Inventar](INVENTAR.md) navodi korišćene i nekorišćene materijale. Prolazak `make check` sam po sebi ne potvrđuje ručni teorijski ili vizuelni pregled.

## Dopuna Verilog primera — 09.10.2026.

Dodato 3 novih glavnih primera, svaki sa testbenchom i lokalnim Makefile-om. Kod je uključen uz postojeća rešenja, bez promene njihovih formula i šema.

- [code/Zadatak_3/d/and](code/Zadatak_3/d/and/zadatak.sv)
- [code/Zadatak_3/d/only_decoders](code/Zadatak_3/d/only_decoders/zadatak.sv)
- [code/Zadatak_3/d/cascade](code/Zadatak_3/d/cascade/zadatak.sv)

Simulacija: `make` u folderu primera pokreće Verilator; `make run_iverilog` pokreće Icarus. Zajednički `make -C vezbe check-sv` obuhvata i ovu dopunu. Izvorni tekst listinga čuva PDF ActualText; `check-pdf-code` proverava kopiranje i simulaciju izvučenog koda.

U toj prethodnoj dopuni zadatak 4 bio je odložen; sadašnje rešenje opisano je ispod.


## Zadatak 4 — sedmosegmentni konvertori

- [a/zadatak.sv](code/Zadatak_4/a/zadatak.sv): svi segmenti pomoću NILI kola; nedozvoljeni BCD ulazi prikazuju E.
- [b/zadatak.sv](code/Zadatak_4/b/zadatak.sv): pojednostavljena mreža za dozvoljene ulaze 0–9.
- [c/zadatak.sv](code/Zadatak_4/c/zadatak.sv) i [bcd_cifra.sv](code/Zadatak_4/c/bcd_cifra.sv): četiri cifre, gašenje vodećih nula i jedno E na mestu jedinica.

Globalna greška računa se iz originalnih BCD podataka. Izlaz ERROR jedinica, koje dobijaju nametnuti kod za E, ostaje nepovezan. Nema povratne putanje, INIT-a ni pamćenja; promena 00A5 → 0504 vraća prikaz 504 nakon smirivanja kola. Broj 0000 prikazuje jednu nulu. Bitovi BCD ulaza imaju redosled DCBA, a SEG[6:0] redosled abcdefg; izlazi su aktivni u jedinici za zajedničku katodu.

```sh
make -C code/Zadatak_4/a
make -C code/Zadatak_4/b run_iverilog
make -C code/Zadatak_4/c
make -C code/Zadatak_4/c run_iverilog TOP=tb_bcd_cifra
```

Testbenchovi proveravaju 16, 10, 64 i 65.536 binarnih kombinacija, sve segmente i povratak sa greške bez resetovanja. Icarus proverava i gašenje pri X/Z ulazima. Četiri cela modula uključena su u PDF sa ActualText. Zajednička provera obuhvata hijerarhijski graf zavisnosti i pet namerno pogrešnih realizacija. Rezultati završnih provera vode se u [zajedničkoj evidenciji](../PROVERA/REZULTATI.md).
