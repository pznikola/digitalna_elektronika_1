# Vežbe 03 — Brojni sistemi i predstave brojeva

`make` kompajlira sve ilustracije pa glavni PDF; `make check` pokreće nezavisne računske provere. `make clean` uklanja pomoćne LaTeX fajlove, a čuva PDF dokumente. Pokrenuti komande iz ovog foldera.

Zavisnosti: GNU Make, Python 3, pdfLaTeX, latexmk i TeX Live paketi za srpski jezik, Latin Modern, AMS, TikZ/Circuitikz, PGFPlots, standalone, tcolorbox, adjustbox i siunitx. Provere koje koriste SymPy zahtevaju i taj Python paket. Mreža, Pandoc i Word nisu potrebni za izgradnju.

Glavni `.tex` i izvori crteža u `Images/` ručno su izmenjivi. Izvorni dokument ostaje u roditeljskom folderu. `INVENTAR.md` povezuje izvorne celine i LaTeX oznake, a `IZVESTAJ_ISPRAVKI.md` obrazlaže izmene.

Ponovni stručni pregled nalazi se u završnom odeljku `IZVESTAJ_ISPRAVKI.md` i u `code/PREGLED_DOKAZA.md`. `code/audit_math.py` čita račune i ćelije tabela iz glavnog TeX-a; koristi samo Python standardnu biblioteku. `code/pregled_formula.json` vezuje ručne matematičke dokaze za tačne izvore formula. Promena formule zahteva novi pregled, a ne automatsko osvežavanje otiska. Kompilacija sada uključuje SyncTeX, radi povezivanja izvornog mesta sa PDF stranicom u zajedničkom registru. Konačni PDF posle provere ima 17 stranica.
