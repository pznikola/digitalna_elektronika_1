# Računske vežbe — izgradnja i potpuna provera

Obuhvaćeni su folderi **01, 02, 03, 04, 05, 07 i 08**. Glavni `.tex` i odgovarajući PDF nalaze se u svakom folderu. Izvorni DOCX/PDF dokumenti su sačuvani; izvorne šeme u 01/02 ostaju Draw.io, uz postojeći TikZ. Novi crteži 03–08 su izmenjivi TikZ/Circuitikz/PGFPlots izvori sa vektorskim PDF izvozima.

```sh
make -C vezbe             # svi dokumenti i potrebne ilustracije
make -C vezbe check       # računske/logičke/VHDL i strukturne provere
make -C vezbe audit       # izgradnja, provere, PNG stranice i stanje pokrivenosti
make -C vezbe clean-build # potpuno nova privremena kopija, bez generisanih PDF-ova/keša
make -C vezbe/05          # pojedinačni dokument
make -C vezbe/05 check    # njegove provere
```

`audit` **ne potpisuje ručni pregled**. Završava se greškom kada izvor, dokaz, izvoz ilustracije ili glavni PDF odstupa od pregledane verzije. Nakon legitimne izmene treba ponovo pregledati pogođeni sadržaj/stranice i ručno zabeležiti otiske u `PROVERA/rucni_pregled.json`; ne prepisivati ih samo da bi cilj prošao. Konzervativno se poništava sadržinska potvrda celog dokumenta, uključujući zavisne rezultate.

Zavisnosti: GNU Make, Python 3 i SymPy, TeX Live sa pdfLaTeX-om i `latexmk`, srpski Babel, Latin Modern, TikZ/PGFPlots, Circuitikz, `standalone`, `karnaugh-map`, `minted` i paketi korišćeni u preambulama. Za `minted` u 01/02 potreban je Pygments (`pygmentize`) i dozvoljen `-shell-escape` za te lokalne izvore. Za VHDL je potreban GHDL (VHDL-2008); testovi rade u odvojenim privremenim direktorijumima i ne pokreću GTKWave ni stare `clean`/GUI ciljeve. Za PDF pregled koriste se Poppler (`pdfinfo`, `pdftotext`, `pdftoppm`) i SyncTeX.

Izvoz Draw.io bez GUI-ja na Linuxu zahteva `drawio`, `xvfb-run` i Xvfb. `PROVERA/build.py` poziva `xvfb-run -a drawio --no-sandbox --export --format pdf --crop`; zastavica se odnosi na Electron pod Xvfb. Pokretati samo sopstvene pregledane izvore. Izvoz nastaje u novom privremenom fajlu i mora biti važeći PDF; stari PDF ne može prikriti neuspeh izvoza. `--disable-gpu` se ne koristi jer je u ovom okruženju izazivao završetak bez izvoznog fajla.

`clean-build` kopira samo izmenjive izvore/prateći kod u novi `/tmp/de1-clean-audit-*`, kompajlira svih sedam dokumenata, proverava reference/logove i poredi **svaku stranicu** sa radnom verzijom na 110 dpi. Razlike u PDF datumima/metapodacima ne utiču na poređenje slike. Ako postoji razlika, cilj pada i navodi stranice za pregled; ne ažurira postojeću potvrdu pregleda. Putanja i otisci su u `PROVERA/_build/clean_build.json`.

[Zajednička pokrivenost](PROVERA/IZVESTAJ.md), [završni rezultati i ograničenja](PROVERA/REZULTATI.md) i lokalni `IZVESTAJ_ISPRAVKI.md` objašnjavaju šta je promenjeno, zašto i kako je provereno. [Registar](PROVERA/registar.json) razlikuje potvrđeno, ispravljeno i ponovo provereno, ograničeno nedostajućim podacima i neprovereno. Broj testova nije dokaz ručnog pregleda.

`.gitignore` u ovom folderu već isključuje pomoćne LaTeX/SyncTeX, minted, Python/GHDL i editorske fajlove; glavni izvori i PDF dokumenti/ilustracije ostaju sačuvani. Raniji vodič `README_KONVERZIJA.md` i izveštaj konverzije zadržani su kao istorija.
