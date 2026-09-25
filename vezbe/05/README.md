# Vežbe 05 — Kodovi

`make` kompajlira sve ilustracije pa glavni PDF; `make check` pokreće nezavisne računske provere. `make clean` uklanja pomoćne LaTeX fajlove, a čuva PDF dokumente. Pokrenuti komande iz ovog foldera.

Zavisnosti: GNU Make, Python 3, pdfLaTeX, latexmk i TeX Live paketi za srpski jezik, Latin Modern, AMS, TikZ/Circuitikz, PGFPlots, standalone, tcolorbox, adjustbox i siunitx. Provere koje koriste SymPy zahtevaju i taj Python paket. Mreža, Pandoc i Word nisu potrebni za izgradnju.

Glavni `.tex` i izvori crteža u `Images/` ručno su izmenjivi. Izvorni dokument ostaje u roditeljskom folderu. `INVENTAR.md` povezuje izvorne celine i LaTeX oznake, a `IZVESTAJ_ISPRAVKI.md` obrazlaže izmene.

Potpuna provera iz septembra 2026: `code/audit_math.py` čita stvarne ćelije tabela i TikZ geometriju, uz nezavisne proračune iz `provera.py`. `code/PREGLED_DOKAZA.md` dokumentuje opšte dokaze i pretpostavke; `code/pregled_izvora.json` čuva otiske ručno pregledanih formula i crteža. Promena otiska zahteva novi pregled; nemojte automatski prepisivati potvrdu. Izgradnja uključuje SyncTeX za povezivanje registra sa PDF stranicama. Konačni pregled obuhvata 17 stranica.
