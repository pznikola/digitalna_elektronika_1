# Vežbe 08 — Analiza logičkih kola sa MOS tranzistorima

`make` kompajlira sve ilustracije pa glavni PDF; `make check` pokreće nezavisne računske provere. `make clean` uklanja pomoćne LaTeX fajlove, a čuva PDF dokumente. Pokrenuti komande iz ovog foldera.

Zavisnosti: GNU Make, Python 3, pdfLaTeX, latexmk i TeX Live paketi za srpski jezik, Latin Modern, AMS, TikZ/Circuitikz, PGFPlots, standalone, tcolorbox, adjustbox i siunitx. Provere koje koriste SymPy zahtevaju i taj Python paket. Mreža, Pandoc i Word nisu potrebni za izgradnju.

Glavni `.tex` i izvori crteža u `Images/` ručno su izmenjivi. Izvorni dokument ostaje u roditeljskom folderu. `INVENTAR.md` povezuje izvorne celine i LaTeX oznake, a `IZVESTAJ_ISPRAVKI.md` obrazlaže izmene.

Potpuni pregled svih formula i crteža dokumentovan je u [code/PREGLED_DOKAZA.md](code/PREGLED_DOKAZA.md). `make check` ima 1.395 provera: čita stvarne parametre/tabele, izdvaja graf Circuitikz vodova, proverava sve binarne provodne putanje, TG sa visokom impedansom i koordinate vremenskih dijagrama. Neparsirani detalji vezani su za ručni pregled SHA256 otiskom. Potreban je Python 3 sa SymPy; zajednički pomoćni parser je `../PROVERA/logic.py`. Lokalni folder ostaje samostalno kompajlabilan, dok provere koriste zajednički prilog.

Dokumentovano je pet ograničenja podataka/modela; uspešan test ne određuje nezadate tehnološke parametre. Zajednički registar i stanje vizuelnog pregleda vode se u `../PROVERA/`.
