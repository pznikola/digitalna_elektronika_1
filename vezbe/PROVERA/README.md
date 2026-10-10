# Evidencija potpune provere

- `pocetno_stanje.json`, `POCETNO_GIT_STANJE.txt`: početno Git stanje i sačuvana radna kopija van dokumenata.
- `registar.json`: izvorni tekst svake inventarske celine, stabilan ID, lokacije i originalni DOCX blok/zadatak gde postoje, metoda, status, dokaz i PDF stranice. Tabele i njihovi redovi, formule i matematika u tekstu namerno su odvojene preklapajuće celine. Istorijske celine čuvaju se u `retired_items`.
- `rucni_pregled.json`: **ručno** zabeleženi otisci svih pregledanih izvora, dokaza, izvozâ i glavnih PDF-ova i lista svih pregledanih fizičkih stranica. Ni jedan automatski cilj ne izdaje ove potvrde.
- `IZVESTAJ.md`: mašinski osvežen pregled pokrivenosti po dokumentima i kategorijama; ne tvrdi da su nedovoljno zadati problemi numerički određeni.
- `REZULTATI.md`: trajni sažetak završnih provera i ograničenja. Detaljni prolazni logovi/slike ostaju u ignorisanom `_build/`.
- `dokazi/`: sačuvani mašinski rezultati, uključujući otiske čiste izgradnje, poređenje svih stranica i proveru registra. Ove kopije se ne prepisuju automatskim ciljem.
- `nalazi_*`: istorijski precizni tekstovi pre/posle. U 01 su povučene promene strelica eksplicitno označene kao povučene; konačan prikaz je originalni.

`audit.py` popisuje celokupne pasuse, sve formule i izraze u tekstu, pottačke, tabele/redove, slike i podslike, TikZ/Karnoove karte, uključene fajlove i izvorne/prateće materijale. **Pasus je jedinica ručnog dokaza za sve tvrdnje u njemu**; broj pasusa, preklapajućih jedinica ili testova ne meri nezavisnu pokrivenost. Originalni DOCX blokovi su sačuvani u komentarima i prenose se u registar. Originalne PDF stranice 07/08 vezuju se za zadatak preko inventara. SyncTeX mapira konačni izvor na fizičke PDF stranice; materijal bez prikaza ima eksplicitno navedenu ulogu.

Potvrda sadržaja važi samo kada se poklapaju lokalni izvori i dokazni/prateći izvori (MD izveštaji, PDF izvozi, originalni dokumenti, zajednički parseri/graditelj). Promena poništava potvrdu celog dokumenta i time svih zavisnih stavki. Promena glavnog PDF-a nezavisno poništava pregled njegovih stranica. Ovaj konzervativni pristup može zahtevati ponovnu potvrdu i posle bezazlene izmene, ali ne može prećutno ostaviti potvrđen zavisni rezultat.

`negative_checks.py` menja **privremene kopije** i traži očekivani neuspeh: pogrešna formula, bit tabele, prenos, Karnoova ćelija, izbrisana Hamingova ivica, promenjen nagib/grafik, prekid voda, pogrešan CMOS prag i nepostojeća referenca. Ne menja radne dokumente. `clean_build.py` dokazuje nezavisnost izgradnje od starih generisanih slika i keša.

`registry_check.py` u izolovanoj sintetičkoj kopiji proverava stabilnost ID-jeva, uključujući pomeranje izvornih linija, i poništavanje potvrde nakon izmene izvora, dokaza ili PDF-a i nakon izostavljanja pregleda stranice. Sintetička potvrda je isključivo testni podatak; nijedna potvrda radnih dokumenata ne menja se u tim testovima.

Za ponavljanje komandi i zavisnosti videti [zajednički README](../README.md). Za ponovnu stručnu proveru polazi se od lokalnih izveštaja, `code/PREGLED_DOKAZA.md` (03–08) i iz izvora vezanih provera. Nerešeni studentski zadaci provereni su privatno u skriptama/dokaznim prilozima; studentska rešenja nisu dopisana.

SystemVerilog dopuna koristi `systemverilog_check.py` za studentske/pomoćne testbenchove, iscrpne GHDL/Verilator tragove i GHDL/Icarus X/Z provere. `vendor_check.py` proverava stvarne Quartus/Questa skripte. `pdf_code_check.py` proverava tačan tekst svih 37 PDF listinga i simulira kopirani RTL. `clean_build.py` sada ponavlja i ceo `make check` iz nove kopije. Dokaz početnog prelaska je `dokazi/systemverilog_provera.json`; za 19 dodatnih primera merodavan je `dokazi/dopuna_provera.json`, a prethodna evidencija pregleda čuva se zasebno; istorijski dokazi nisu prepisani novim rezultatima.

`dopuna_check.py` proverava očuvanje originala, kompletnost 19 novih primera i sedam namernih grešaka. HDL provere i PDF izdvajanje sada obuhvataju 01/02/04/05. `dokazi/dopuna_originals.json` sadrži zamrznute otiske i spisak novih primera; prethodna potvrda pregleda čuva se u `dokazi/rucni_pregled_pre_dopuna.json`.


`zadatak4_check.py` proverava tri nova glavna modula i pomoćni konvertor vežbe 02, zadatka 4, odsustvo ciklusa kroz stvarne hijerarhijske zavisnosti i pet namernih grešaka u RTL-u. `dokazi/zadatak4_originals.json` čuva otiske svih 89 ranijih SV i 32 VHDL izvora; ranija zabrana izmene zadatka ostaje istorija u `dopuna_originals.json`. Prethodni pregled sačuvan je u `dokazi/rucni_pregled_pre_zadatak4.json`. Važeći rezultat nove izmene vodi se u `dokazi/zadatak4_provera.json` po završetku oba prolaza. PDF provera podržava i kompletan pomoćni modul sa njegovim testbenchom.


Provere očuvanja izvora dopuštaju samo tri evidentirana brisanja komentara u testbenchovima; izvršivi SV sadržaj i VHDL otisci porede se sa prethodnim verzijama. Tačne izmene i prethodni izvori čuvaju se u `PROVERA/dokazi/student_text_cleanup.json` (putanja od foldera vezbe). Svaka druga promena ranijih programa poništava proveru.
