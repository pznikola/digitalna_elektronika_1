# Vežba 02 — sinteza kola srednjeg stepena integracije

- `make` — izvoz uključenih Draw.io/TikZ ilustracija i izgradnja samostalnog PDF-a.
- `make check` — stvarne LaTeX formule, tabele i Karnoove karte, logički opisi pregledanih šema, iscrpna BCD provera i izolovane GHDL simulacije.
- `make clean` — uklanjanje pomoćnih LaTeX fajlova; izvori i PDF materijali ostaju sačuvani.

Potrebni su Python 3.10+, GHDL sa VHDL-2008 podrškom, TeX Live sa pdfLaTeX-om, latexmk-om, paketima minted/TikZ/karnaugh-map i Pygmentsom, kao i Draw.io Desktop CLI i xvfb-run. Minted zahteva shell-escape za lokalno bojanje uključenih primera. Izvozi se rade u privremenom direktorijumu; neuspešan izvoz ne može se sakriti postojećim starim PDF-om.

Crteže menjati kroz `.drawio` ili `.tex` izvor. Posle izmene šeme ponoviti praćenje veza i ažurirati njen pregled u `code/pregled_sema.json`; provera namerno odbija promenjen izvor bez novog pregleda. Karnoova karta sa strelicama ostala je u izvornom rasporedu. PNG je sačuvan, ali je njegova ilustracija u dokumentu zamenjena TikZ/PDF verzijom.

[Izveštaj ispravki](IZVESTAJ_ISPRAVKI.md) razlikuje greške izvora, zastarele izvoze i dopunske pretpostavke. [Inventar](INVENTAR.md) navodi korišćene i nekorišćene materijale. Prolazak `make check` sam po sebi ne potvrđuje ručni teorijski ili vizuelni pregled.
