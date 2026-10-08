# Računske vežbe — izgradnja i potpuna provera

Obuhvaćeni su folderi **01, 02, 03, 04, 05, 07 i 08**. Glavni `.tex` i odgovarajući PDF nalaze se u svakom folderu. Izvorni DOCX/PDF dokumenti su sačuvani; izvorne šeme u 01/02 ostaju Draw.io, uz postojeći TikZ. Novi crteži 03–08 su izmenjivi TikZ/Circuitikz/PGFPlots izvori sa vektorskim PDF izvozima.

```sh
make -C vezbe             # svi dokumenti i potrebne ilustracije
make -C vezbe check       # računske/logičke provere, HDL simulacije i struktura
make -C vezbe check-sv    # svi SystemVerilog testbenchovi: Verilator i Icarus
make -C vezbe check-equivalence # originalni VHDL naspram SystemVeriloga
make -C vezbe check-pdf-code # tacan tekst iz PDF-a i simulacija kopiranog koda
make -C vezbe audit       # izgradnja, provere, PNG stranice i stanje pokrivenosti
make -C vezbe clean-build # potpuno nova privremena kopija, bez generisanih PDF-ova/keša
make -C vezbe/05          # pojedinačni dokument
make -C vezbe/05 check    # njegove provere
```

`audit` **ne potpisuje ručni pregled**. Završava se greškom kada izvor, dokaz, izvoz ilustracije ili glavni PDF odstupa od pregledane verzije. Nakon legitimne izmene treba ponovo pregledati pogođeni sadržaj/stranice i ručno zabeležiti otiske u `PROVERA/rucni_pregled.json`; ne prepisivati ih samo da bi cilj prošao. Konzervativno se poništava sadržinska potvrda celog dokumenta, uključujući zavisne rezultate.

Zavisnosti: GNU Make, Python 3 i SymPy, TeX Live sa pdfLaTeX-om i `latexmk`, srpski Babel, Latin Modern, TikZ/PGFPlots, Circuitikz, `standalone`, `karnaugh-map`, `minted`, `accsupp`, `stringenc` i paketi korišćeni u preambulama. Za `minted` u 01/02 potreban je Pygments (`pygmentize`) i dozvoljen `-shell-escape` za te lokalne izvore. HDL simulacije koriste Docker i lokalni image `hdlview-tools:2025.12`, koji sadrži Verilator, GHDL i Icarus; lokalna instalacija tih simulatora nije potrebna. Za PDF pregled koriste se Poppler (`pdfinfo`, `pdftotext`, `pdftoppm`) i SyncTeX.

## Verilog primeri i simulacije

Studentski primeri koriste SystemVerilog (`.sv`). U 01/02 sačuvani su svih 32 VHDL izvora, uz njihove SystemVerilog parnjake i četiri dodatna testbencha za pomoćne multipleksere/dekodere. Imena portova, interne mreže, polariteti, izrazi i podrazumevana kašnjenja prate originalno kolo. U 03/04/05/07/08 nema HDL listinga za prevođenje.

```sh
make -C vezbe/01/code/Zadatak_4                 # Verilator, bez GUI-ja
make -C vezbe/01/code/Zadatak_4 view_wave       # GTKWave, opciono
make -C vezbe/02/code/Zadatak_3/b run_iverilog TOP=tb_decoder
make -C vezbe/01/code/Zadatak_4 run_ghdl        # sačuvani VHDL primer
```

Listinzi u PDF-ovima 01/02 mogu se kopirati kao ceo blok koda. PDF `ActualText` sadrži izvorni UTF-8 tekst sa običnim razmacima, uvlačenjem i novim redovima; obojeni prikaz ostaje isti. `check-pdf-code` poredi svih 14 listinga iz Poppler režima `-raw` i `-layout` sa `.sv` izvorima i Icarusom simulira upravo izvučeni kod. Preglednik mora podržavati PDF `ActualText`; način označavanja teksta zavisi od preglednika.

`HDL_IMAGE` može izabrati drugi kompatibilan lokalni image. Svaki primer ima zaseban `.build/<simulator>/`, a testovi ekvivalencije rade u novim privremenim direktorijumima. Kontejner nema mrežu, izvori su pri zajedničkoj proveri montirani samo za čitanje. VCD fajl sadrži i interne signale. `clean` u folderu primera uklanja samo `.build/`.

Verilator se pokreće sa `--binary --timing --trace --assert --timescale 1ns/1ps`. RTL primeri nemaju deklaracije `timeunit` ili `timeprecision`. Vremenske jedinice pripadaju podešavanju simulacije: Verilator koristi navedenu opciju, Icarus generisani `simulation_timescale.sv` u direktorijumu izgradnje, a Questa `vlog -timescale 1ns/1ps`. Testbenchovi imaju svoje vremenske deklaracije. [Verilator opcija za podrazumevane vremenske jedinice](https://verilator.org/guide/latest/exe_verilator.html#cmdoption-timescale).

Parametar `T` je `time`; zadate vrednosti su celobrojni nanosekundni intervali. Kontinuirane dodele `assign #(T)` koriste inertno kašnjenje i služe simulaciji. Testbenchovi čuvaju originalne stimuluse i razmake, proveravaju rezultate i završavaju sa `$finish`.

Verilator pretežno simulira 0/1 i nema punu četvorovrednosnu semantiku. Dodatne X/Z provere pokreće Icarus (`-g2012 -DFOUR_STATE`); VHDL `U` poredi se sa SystemVerilog `X`. Slabi nivoi VHDL `STD_LOGIC` nisu zasebna stanja SystemVerilog modela. [Ograničenja Verilatora](https://verilator.org/guide/latest/languages.html#unknown-states).

Poređenje VHDL/SV obuhvata sve binarne ulaze, jednoulazne prelaze, interne signale i fizička vremena događaja, uz podrazumevani `T` i 7 ns. Obuhvaćeni su impulsi kraći od, jednaki i duži od `T`. Poređenje počinje posle početnog smirivanja, jer se početno neodređeno stanje simulatora razlikuje; događaji u delta ciklusima porede se kroz konačnu vrednost u istom fizičkom trenutku. Četiri namerne HDL greške proveravaju da poređenje zaista otkriva pogrešno kolo ili vreme.

Aktivne Quartus skripte koriste `SYSTEMVERILOG_FILE` i projekat `zadatak_sv`; Questa/ModelSim koriste `vlog -sv` i biblioteku `work_sv`. Sačuvane varijante imaju sufiks `_vhdl`, uz Make ciljeve `run_schematic_vhdl` i `run_vsim_vhdl`. `python3 vezbe/PROVERA/vendor_check.py` proverava elaboraciju i simulaciju bez GUI-ja u privremenim kopijama, uz odvojeno evidentiranje nedostupne licence. Ti alati nisu potrebni za Docker provere.

Izvoz Draw.io bez GUI-ja na Linuxu zahteva `drawio`, `xvfb-run` i Xvfb. `PROVERA/build.py` poziva `xvfb-run -a drawio --no-sandbox --export --format pdf --crop`; zastavica se odnosi na Electron pod Xvfb. Pokretati samo sopstvene pregledane izvore. Izvoz nastaje u novom privremenom fajlu i mora biti važeći PDF; stari PDF ne može prikriti neuspeh izvoza. `--disable-gpu` se ne koristi jer je u ovom okruženju izazivao završetak bez izvoznog fajla.

`clean-build` kopira samo izmenjive izvore/prateći kod u novi `/tmp/de1-clean-audit-*`, kompajlira svih sedam dokumenata, ponavlja ceo `make check` i poredi **svaku stranicu** sa radnom verzijom na 110 dpi. Razlike u PDF datumima/metapodacima ne utiču na poređenje slike. Ako postoji razlika, cilj pada i navodi stranice za pregled; ne ažurira postojeću potvrdu pregleda. Putanja i otisci su u `PROVERA/_build/clean_build.json`.

[Zajednička pokrivenost](PROVERA/IZVESTAJ.md), [završni rezultati i ograničenja](PROVERA/REZULTATI.md) i lokalni `IZVESTAJ_ISPRAVKI.md` objašnjavaju šta je promenjeno, zašto i kako je provereno. [Registar](PROVERA/registar.json) razlikuje potvrđeno, ispravljeno i ponovo provereno, ograničeno nedostajućim podacima i neprovereno. Broj testova nije dokaz ručnog pregleda.

`.gitignore` u ovom folderu već isključuje pomoćne LaTeX/SyncTeX, minted, Python/GHDL i editorske fajlove; glavni izvori i PDF dokumenti/ilustracije ostaju sačuvani. Raniji vodič `README_KONVERZIJA.md` i izveštaj konverzije zadržani su kao istorija.
