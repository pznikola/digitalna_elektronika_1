# Vežba 01

`make` izvozi potrebne Draw.io slike i kompajlira dokument. `make check` proverava matematiku, tabele, Karnoove karte, izmenjene Draw.io mreže i stvarni VHDL pomoću GHDL-a. Simulacije ne pokreću GUI i ne menjaju radne direktorijume postojećih primera.

Zavisnosti: Python 3, GNU Make, latexmk/pdfLaTeX, TeX Live paketi iz preambule, Pygments (minted), Draw.io Desktop, xvfb-run, GHDL sa VHDL-2008 podrškom. Zbog postojećeg minted-a pdfLaTeX koristi shell-escape. Draw.io/Chromium može zahtevati pokretanje van procesnog sandboxa. Izvoz proverava da je napravljen novi PDF, jer Draw.io neke greške prijavljuje tekstom uz izlazni kod 0.

Izvorni PDF sa velikim slovima u imenu nije generisani PDF. Ne briše se ni pri čistoj izgradnji.

Šeme rešenja zadržavaju izvorni raspored: horizontalni vodovi za signal i njegov komplement, vertikalne veze ka kolima i tačke na spojevima. Ukrštanje bez tačke nije spoj. Draw.io izvori ostaju izmenjivi. Veze starih crteža sa slobodnim krajevima ručno su praćene i zabeležene u `code/pregled_sema.json`; svaka promena XML izvora poništava taj pregled. Provera koristi njegovu listu veza i stvarne simbole kola. Originalne strelice Karnoovih karata čuvaju se bez promene položaja.

Za nalaze videti `IZVESTAJ_ISPRAVKI.md`; za pokrivenost i važenje ručnog pregleda `../PROVERA/IZVESTAJ.md`.
