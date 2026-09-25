# Vežbe 07 — Statičke karakteristike logičkih kola

`make` kompajlira sve ilustracije pa glavni PDF; `make check` pokreće nezavisne računske provere. `make clean` uklanja pomoćne LaTeX fajlove, a čuva PDF dokumente. Pokrenuti komande iz ovog foldera.

Zavisnosti: GNU Make, Python 3, pdfLaTeX, latexmk i TeX Live paketi za srpski jezik, Latin Modern, AMS, TikZ/Circuitikz, PGFPlots, standalone, tcolorbox, adjustbox i siunitx. Provere koje koriste SymPy zahtevaju i taj Python paket. Mreža, Pandoc i Word nisu potrebni za izgradnju.

Glavni `.tex` i izvori crteža u `Images/` ručno su izmenjivi. Izvorni dokument ostaje u roditeljskom folderu. `INVENTAR.md` povezuje izvorne celine i LaTeX oznake, a `IZVESTAJ_ISPRAVKI.md` obrazlaže izmene.

Ponovni potpuni pregled: `code/audit_math.py` parsira prikazane afine segmente, izvodi kompoziciju tačno, nalazi sve fiksne tačke/parne cikluse, proverava ćelije tabele i stvarne koordinate crteža. Opšti dokazi, praćene veze i ograničenje grafičkog zadatka 1 dokumentovani su u `code/PREGLED_DOKAZA.md`. Otisci u `code/pregled_izvora.json` zahtevaju novi ručni pregled pri promeni izvora. Build uključuje SyncTeX. Konačni PDF ima 14 pojedinačno pregledanih stranica.
