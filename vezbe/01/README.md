# Vežba 01

`make` izvozi potrebne Draw.io slike i kompajlira dokument. `make check` proverava matematiku, tabele, Karnoove karte, izmenjene Draw.io mreže i referentni VHDL pomoću GHDL-a u Dockeru. Zajednički `make -C .. check-sv` i `check-equivalence` proveravaju aktivni SystemVerilog i poređenje vremenskih odziva.

Zavisnosti: Python 3, GNU Make, latexmk/pdfLaTeX, TeX Live paketi iz preambule, Pygments (minted), Draw.io Desktop, xvfb-run, Docker i lokalni image `hdlview-tools:2025.12`. Zbog minted-a pdfLaTeX koristi shell-escape. Draw.io/Chromium može zahtevati pokretanje van procesnog sandboxa. Izvoz proverava da je napravljen novi PDF, jer Draw.io neke greške prijavljuje tekstom uz izlazni kod 0.

U svakom `code/Zadatak_*` folderu `make` pokreće SystemVerilog testbench Verilatorom bez GUI-ja. `make view_wave` otvara njegov VCD, `make run_ghdl` sačuvani VHDL testbench. Svih šest prevoda čuva strukturu kola; zadaci 4–6 koriste inertno kašnjenje `assign #(T)`. Detalji simulacija i završnih provera su u [zajedničkom README-u](../README.md#verilog-primeri-i-simulacije).

Izvorni PDF sa velikim slovima u imenu nije generisani PDF. Ne briše se ni pri čistoj izgradnji.

Šeme rešenja zadržavaju izvorni raspored: horizontalni vodovi za signal i njegov komplement, vertikalne veze ka kolima i tačke na spojevima. Ukrštanje bez tačke nije spoj. Draw.io izvori ostaju izmenjivi. Veze starih crteža sa slobodnim krajevima ručno su praćene i zabeležene u `code/pregled_sema.json`; svaka promena XML izvora poništava taj pregled. Provera koristi njegovu listu veza i stvarne simbole kola. Originalne strelice Karnoovih karata čuvaju se bez promene položaja.

Za nalaze videti `IZVESTAJ_ISPRAVKI.md`; za pokrivenost i važenje ručnog pregleda `../PROVERA/IZVESTAJ.md`.
