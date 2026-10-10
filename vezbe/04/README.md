# Vežbe 04 — Aritmetičke operacije

`make` kompajlira sve ilustracije pa glavni PDF; `make check` pokreće nezavisne računske provere. `make clean` uklanja pomoćne LaTeX fajlove, a čuva PDF dokumente. Pokrenuti komande iz ovog foldera.

Zavisnosti: GNU Make, Python 3, pdfLaTeX, latexmk i TeX Live paketi za srpski jezik, Latin Modern, AMS, TikZ/Circuitikz, PGFPlots, standalone, tcolorbox, adjustbox i siunitx. Provere koje koriste SymPy zahtevaju i taj Python paket. Mreža, Pandoc i Word nisu potrebni za izgradnju.

Glavni `.tex` i izvori crteža u `Images/` ručno su izmenjivi. Izvorni dokument ostaje u roditeljskom folderu. `INVENTAR.md` povezuje izvorne celine i LaTeX oznake, a `IZVESTAJ_ISPRAVKI.md` obrazlaže izmene.

Ponovna provera: `code/audit_math.py` čita stvarne redove postupaka, funkcionalne tabele, izraze i ćelije/grupe Karnoovih karata. Ručno praćene šeme i deduktivni pregled vezani su za izvore kroz `code/pregled_izvora.json` i `code/PREGLED_DOKAZA.md`. Potreban je i zajednički `../PROVERA/logic.py`; nije potreban dodatni Python paket. Za sprečavanje odvajanja naziva od tabela koristi se LaTeX paket `needspace`. Kompilacija generiše SyncTeX. Konačni dokument nakon ove provere ima 30 stranica. Ne osvežavati otiske pregleda automatski posle izmene matematike ili veze.

## Dopuna Verilog primera — 09.10.2026.

Dodato 6 novih glavnih primera, svaki sa testbenchom i lokalnim Makefile-om. Kod je uključen uz postojeća rešenja, bez promene njihovih formula i šema.

- [code/Samostalni/Zadatak_3/a](code/Samostalni/Zadatak_3/a/zadatak.sv)
- [code/Samostalni/Zadatak_3/b](code/Samostalni/Zadatak_3/b/zadatak.sv)
- [code/Samostalni/Zadatak_4/a_zp](code/Samostalni/Zadatak_4/a_zp/zadatak.sv)
- [code/Samostalni/Zadatak_4/a_xor](code/Samostalni/Zadatak_4/a_xor/zadatak.sv)
- [code/Samostalni/Zadatak_4/b_x](code/Samostalni/Zadatak_4/b_x/zadatak.sv)
- [code/Samostalni/Zadatak_4/b_y](code/Samostalni/Zadatak_4/b_y/zadatak.sv)

Simulacija: `make` u folderu primera pokreće Verilator; `make run_iverilog` pokreće Icarus. Zajednički `make -C vezbe check-sv` obuhvata i ovu dopunu. Izvorni tekst listinga čuva PDF ActualText; `check-pdf-code` proverava kopiranje i simulaciju izvučenog koda.
