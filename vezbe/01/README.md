# Vežba 01

`make` izvozi potrebne Draw.io slike i kompajlira dokument. `make check` proverava matematiku, tabele, Karnoove karte, izmenjene Draw.io mreže i referentni VHDL pomoću GHDL-a u Dockeru. Zajednički `make -C .. check-sv` i `check-equivalence` proveravaju aktivni SystemVerilog i poređenje vremenskih odziva.

Zavisnosti: Python 3, GNU Make, latexmk/pdfLaTeX, TeX Live paketi iz preambule, Pygments (minted), Draw.io Desktop, xvfb-run, Docker i lokalni image `hdlview-tools:2025.12`. Zbog minted-a pdfLaTeX koristi shell-escape. Draw.io/Chromium može zahtevati pokretanje van procesnog sandboxa. Izvoz proverava da je napravljen novi PDF, jer Draw.io neke greške prijavljuje tekstom uz izlazni kod 0.

U folderu primera `make` pokreće SystemVerilog testbench Verilatorom bez GUI-ja. `make view_wave` otvara njegov VCD. U šest postojećih VHDL/SV parova dostupan je i `make run_ghdl` za sačuvani VHDL testbench. Svih šest prevoda čuva strukturu kola; zadaci 4–6 koriste inertno kašnjenje `assign #(T)`. Detalji simulacija i završnih provera su u [zajedničkom README-u](../README.md#verilog-primeri-i-simulacije).

Izvorni PDF sa velikim slovima u imenu nije generisani PDF. Ne briše se ni pri čistoj izgradnji.

Šeme rešenja zadržavaju izvorni raspored: horizontalni vodovi za signal i njegov komplement, vertikalne veze ka kolima i tačke na spojevima. Ukrštanje bez tačke nije spoj. Draw.io izvori ostaju izmenjivi. Veze starih crteža sa slobodnim krajevima ručno su praćene i zabeležene u `code/pregled_sema.json`; svaka promena XML izvora poništava taj pregled. Provera koristi njegovu listu veza i stvarne simbole kola. Originalne strelice Karnoovih karata čuvaju se bez promene položaja.

Za nalaze videti `IZVESTAJ_ISPRAVKI.md`; za pokrivenost i važenje ručnog pregleda `../PROVERA/IZVESTAJ.md`.

## Dopuna Verilog primera — 09.10.2026.

Dodato 4 novih glavnih primera, svaki sa testbenchom i lokalnim Makefile-om. Kod je uključen uz postojeća rešenja, bez promene njihovih formula i šema.

- [code/Zadatak_1/b](code/Zadatak_1/b/zadatak.sv)
- [code/Zadatak_1/c](code/Zadatak_1/c/zadatak.sv)
- [code/Zadatak_1/d](code/Zadatak_1/d/zadatak.sv)
- [code/Zadatak_4/c](code/Zadatak_4/c/zadatak.sv)

Simulacija: `make` u folderu primera pokreće Verilator; `make run_iverilog` pokreće Icarus. Zajednički `make -C vezbe check-sv` obuhvata i ovu dopunu. Izvorni tekst listinga čuva PDF ActualText; `check-pdf-code` proverava kopiranje i simulaciju izvučenog koda.
