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
