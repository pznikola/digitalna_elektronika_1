# Predavanje 04 — beleške kao pomoć predavaču

Datum: **2026-10-02**. Status predavanja: **u_radu**, zbog pet otvorenih stručnih odluka. Dorada beležaka po novom planu je napisana i pregledana; ovaj izveštaj nije tvrdnja da je cela prezentacija spremna za završno prihvatanje. Tema **etf-v1**, stil **B**, nepromenjeni.

Pročitani su [plan](../../../../PLAN_PREDAVANJA.md), svih **39 originalnih slajdova** iz 20 PDF strana, svih **39 postojećih slajdova** i pripadajući izvori beležaka. Original i projekcioni prikaz pojedinačno su upoređeni; svih **39 konačnih A4 strana** beležaka pregledano je u punoj veličini. Očuvani su broj, redosled i ID-jevi **04-s001–04-s039**. Projekcioni PDF i svi njegovi slajdovi, tabele, crteži, originalni PDF i tema ostali su bajtno nepromenjeni u ovoj doradi.

## Nastavni tekst beležaka

Prepisano je svih 39 fajlova `beleske/sNNN.tex`. Na 37 slajdova beleške sadrže samo potrebno dodatno objašnjenje za predavača: potpuno objašnjene izvorne detalje koji nisu vidljivi, međukorake, značenje oznaka, rad postupka i proverene kratke primere. S001 i s011 zadržavaju ID i nevidljiva sidra bez veštačkog teksta. Ne propisuje se ista dužina svakom slajdu.

Uklonjeni su vidljivi redovi o izvoru, obavezni urednički podnaslovi, komentari o redizajnu, predlozi stručnih izmena i zahtevi za odobrenje. Poreklo, razlika između izvornog detalja i dopune, dokazi i korisnikove odluke čuvaju se samo u `provera/redizajn/`. Nema druge kopije teksta beležaka. Sva ranija `% element:` sidra sačuvana su, a proverene dopune imaju zasebne oznake `d01`.

| Slajdovi | Dodatno objašnjenje za predavača |
|---|---|
| s002–s007 | Pozicione težine, uloga nula, teleskopski maksimum, razlikovanje zapisa i vrednosti, potpuno školsko obrazloženje zapisa razlomkom. |
| s008–s010 | Puno početno razvijanje celobrojne i razlomljene vrednosti; izdvajanje cifara, ostatak i smer čitanja; konačnost celobrojnog postupka bez samovoljne izmene otvorenog uslova na s009. |
| s012–s020 | Uslov konačnog razlomljenog zapisa, period 0011 i greška odsecanja, pisano deljenje u osnovi sedam, širenje pojedinačne cifre i dopuna grupa oko tačke. |
| s021–s028 | Registri i magistrale, tumačenje bitova prema odluci projektanta, MSB/LSB i fizička pozicija, puno izvođenje skaliranja i primeri za sadržaj 104. |
| s029–s038 | Tumačenje znaka i apsolutne vrednosti, ofseta, oba komplementa i fiksne tačke; dve nule, ograničenje širine, svih pet redova dokaza negativne težine MSB-a i veza sa ofsetom. |
| s039 | Razdvajanje mantise i eksponenta, efekat stepena dvojke i ograničenje preciznosti konačnog registra. |

Primer razlike prema starim beleškama: s008/s010 sada izlažu ceo početni izraz sa svim krajnjim članovima i objašnjenjem algoritma; s027 prikazuje sve članove zajedničkog imenioca i numeričke položaje tačke; s036 sadrži puno izvođenje sa oba ranije preneta međukoraka. S001/s011 nemaju poruku „nema dodatnih beležaka“. PDF za predavača zadržava prikaz slajda, naslov i ID.

## Pokrivenost i poreklo

Potvrđeno je **177/177 odredišta: 140 izvornih elemenata + 37 dopuna**. Izvorni popis nije zamenjen popisom novih beležaka. Svaki izvorni detalj uklonjen sa slajda ima odredište u beleškama istog ID-ja; tehnička evidencija nije njegovo nastavno odredište. Ključne definicije, rezultati, uslovi i ilustracije ostaju na postojećim slajdovima. Pojedini detalji mogu biti potpuno prisutni i na slajdu, pa se bez potrebe ne ponavljaju u beleškama.

| Slajd | Izvorni sadržaj koji je samo u beleškama |
|---|---|
| s006 | Školsko obrazloženje racionalne vrednosti i zahteva za zapisom u izabranoj osnovi (`e04`). |
| s008 | Puno početno razvijanje celobrojne vrednosti pre deljenja (`e04`). |
| s010 | Puno početno razvijanje razlomljenog dela pre množenja (`e04`). |
| s027 | Svi članovi preko zajedničkog imenioca (`e04`). |
| s036 | Dva međukoraka dokaza negativne težine vodećeg bita (`e05`). |

[Inventar](inventar.json), [mapa pokrivenosti](pokrivenost.md), [precizna odredišta](pokrivenost.json) i [evidencija novih beležaka po slajdu](evidencija_beleski.json) čuvaju poreklo i potvrde. Pokrivenost i vernost originalu ne znače odobrenje pet spornih izvornih zapisa.

## Sačuvani rezultat ranijeg redizajna

| Slajdovi | Promena |
|---|---|
| s001 | Naslovna strana prati 01; sačuvani autor, katedra i školska godina 2021/22. |
| s002–s003 | Definicije i istorijski pregled imaju odvojene kolone; celobrojni i razlomljeni deo, vodeće/prateće nule i njihovi ekvivalentni zapisi čine pregledne blokove. |
| s004–s007 | Ujednačene oznake poništavanja i tamnocrveni akcenti; dugi računi raspoređeni u više redova. Definicije, dokazi i rezultati ostaju vidljivi. |
| s008–s012 | Postupci deljenja i množenja imaju vidljive uslove i ključne korake. Početni izrazi su detaljno sačuvani u beleškama; pitanje s011 ostaje zaseban slajd. |
| s013–s015 | Tabele su centrirane i razmaknute od naslova; strelice čitanja nalaze se izvan ćelija. Sačuvani su svi koraci deljenja/množenja i svi redovi provere u osnovi sedam. |
| s016–s018 | Odvojene formule i grupe cifara; pregledne tabele kompatibilnih osnova sa svih 8 i 16 parova. Strelice kompatibilnosti imaju odvojene oznake. |
| s019–s020 | Dva smera konverzije u jednakim kolonama. Dodavanje i brisanje nula istaknuto je tamnocrveno; zadržani su svi primeri. |
| s021–s022 | Precrtani registri i magistrala, vodoravne oznake i čisti vektorski crteži fizičkih linija. Sačuvane su sve grane i oznaka nastavka. |
| s023–s027 | Pojmovi bit/nibble/byte/word/double word grupisani u tabelu, uz osmobitni registar i MSB/LSB. Položaj tačke povezan je sa zapisom i skaliranjem u preglednim tabelama. |
| s028 | Jasno odvojeni problem znaka, izbor kodovanja i četvorobitni primer. |
| s029–s032 | Svih 16 redova svake tabele ostaje vidljivo. Vodoravna pregrada razdvaja polovine kodnog prostora; objašnjenje i formule su u zasebnoj koloni. Sačuvani su i oba zapisa nule gde postoje. |
| s033–s036 | Definicije komplemenata, invertovanje, decimalni primeri i svojstva imaju zasebne blokove. Na s036 vidljivi su početak izvođenja, ključni korak, bit znaka i rezultat; dva međukoraka su u beleškama. |
| s037–s039 | Sačuvana tabela svih kodova drugog komplementa/ofseta, poravnati primeri fiksne tačke. Mantisa i eksponent imaju odvojene kolone sa dvorednim naslovima. |

Fontovi su postojeći; lokalno isticanje **#A32638** prati plan i odobrenu 01. Boja nije predstavljena kao zvanični ETF standard. Osnovni tekst ostaje 11 pt, tabele i pojedini dugi izrazi koriste 9–10 pt. Nema skaliranja celog slajda, novih okvira, overlay strana ili uredničkih komentara na projekcionim slajdovima.

Precrtani uređivi izvori: `slike/tikz/s021_registri_magistrala.tex` i `slike/tikz/s022_fizicke_linije.tex`; strelice na s013/s015 i kompatibilnost na s017 uređene su u pripadajućim izvorima. Na ovim slajdovima nema novih analognih ili logičkih kola. Crteži registara i fizičkih linija upoređeni su sa originalnim oznakama i značenjem; boja nije jedini nosilac informacije.

## Provere ove dorade

```bash
make -C predavanja LECTURE=04_brojni_sistemi notes
make -C predavanja LECTURE=04_brojni_sistemi review
make -C predavanja LECTURE=04_brojni_sistemi check
python3 predavanja/04_brojni_sistemi/kodovi/provera_logike.py
git diff --check
```

- `notes` i `review` prolaze. PDF beležaka ima **39 A4 strana**, tačan redosled i vezu sa svih 39 ID-jeva. Nema grešaka kompilacije, upozorenja, nedostajućih znakova ili `Overfull`/`Underfull`.
- Svaka beleška i svaka konačna strana stvarno su pregledane: potpunost, stručna tačnost dodatnog sadržaja, čitljivost, upotrebljivost za predavača i odsustvo nepotrebnog ponavljanja. Poslednja dva pojašnjenja na s023/s027 ponovo su pregledana; ostalih 37 prikaza ostalo je identično prethodno pregledanoj verziji.
- Postojeća [računska provera](../../kodovi/provera_logike.py) prolazi, uključujući tabele, konverzije, komplemente i fiksnu tačku. Dokumentuje kontraprimere izvornih zapisa; uspeh ne odobrava te zapise.
- [Dopunske računske provere beležaka](racunske_provere_beleski.json) prolaze: **12 grupa i 46.048 slučajeva**, sa tačnim razlomcima, rekonstrukcijom cifara, periodom, greškom odsecanja, kompatibilnim osnovama, skaliranjem i iscrpnim kodovima drugog komplementa/ofseta.
- `check` daje **NEZAVRŠENO**, isključivo za **s006/formule, s009/formule, s016/formule, s034/tekst i s035/formule**. Nema zastarelih potvrda, nepokrivenih elemenata ili drugih prijavljenih problema. Te kategorije ostaju `problem` do stvarne stručne odluke korisnika.

[Log kompilacije](../../build/redizajn/provera-beleski/notes.log), [log pregleda](../../build/redizajn/provera-beleski/review.log), [log završne provere](../../build/redizajn/provera-beleski/check.log) i [log postojeće računske provere](../../build/redizajn/provera-beleski/provera-logike.log). Automatika ne zamenjuje pojedinačni pregled.

## Jezičke ispravke i otvorena pitanja

Zadržana su izvorna značenja uz gramatički uredan nastavni tekst. U prethodnom redizajnu evidentirane su očigledne ispravke s013 „tačnije rezultat“ → „tačniji rezultat“, s022 „RELAN“ → „Realan“, s024 „Ali sto tako“ → „Ali isto tako“, s028 „smo podrazumevalo“ → „smo podrazumevali“, ponovljeno „znaka“ na s031/s032, s034 „jec“ → „je“ i s039 „jedna registar“ → „jedan registar“. U novim beleškama s023 precizirano je da promena vrednosti LSB-a menja broj za jedan, a na s027 da se razmatraju težine sa negativnim eksponentom. Stručni izvorni zapisi nisu samovoljno menjani.

Pet postojećih predloga ostaje u [otvorena_pitanja.md](otvorena_pitanja.md): decimale 17/49, strogi logaritamski uslov, dva dvostruka indeksa, naziv komplementa 10-tke i zagrade oko oduzimanog komplementa. Predlozi i odobravanje nisu deo nastavnih beležaka. Korisniku je ponuđena konkretna odluka prema §1.1 plana; odgovor nije primljen. Nova poruka o pisanju beležaka ne predstavlja odobrenje tih stručnih izmena, rezultata 04 ili početka 05.

## Izlazi i kontrolne sume

- [PDF beležaka — 39 A4 strana](../../build/04_brojni_sistemi_beleske.pdf).
- [Nepromenjena prezentacija — 39 slajdova](../../build/04_brojni_sistemi.pdf).
- [Uporedni pregled originala, prethodnog i trenutnog slajda i novih beležaka](../../build/redizajn/pregled/index.html).
- [Poređenje ranijeg redizajna pre/posle](../../build/poredjenje/poredjenje-pre-posle.pdf); ova dorada menja samo beleške.
- [Prethodna evidencija i izveštaj](istorija/pre-dorade-beleski-2026-10-02/izvestaj.md); stari urednički opisi beležaka nisu aktuelna pravila ni dokaz pregleda novih beležaka.
- [Trajna arhiva početne rekonstrukcije](polazni-izvori.tar.gz), [manifest](manifest.json), [zapis izgradnje](izgradnja.json) i [obnovljene pojedinačne potvrde](pregled.json).

| Resurs | SHA-256 |
|---|---|
| Originalni PDF | `e1f763084b19156c790ffe1f30b9d703081c8fbdc57e2ad9b2d9b73140ad1518` |
| Manifest etf-v1 | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |
| Manifest redizajna | `f4301065e016daa6b3495b27b353908594353b4c49559ce042c8f7f88a839d9b` |
| Zapis izgradnje | `35e78760fc8367ab3cc66c18a6c47693a928794ef5aeb2fc6b803f088cc7f8ac` |
| Potvrde pregleda | `4cf2bb1691adef13f5224f8a685baac352f49c69be1e3f61a15e0a5280ac502a` |
| Inventar | `a5fb314bb23508017090af891a151ffae7cd1623eb7f010523e8697458ace20e` |
| Mapa pokrivenosti | `11b55a31f0b73f9379cd363b65bbc54a088732a1bdc730b489d0c75b31ad8246` |
| Evidencija novih beležaka | `d355bb0474ce9f4221b4cdf3e32f68111b15ba28f844a36d40d368a63059f4b9` |
| Dokazi dopunskih računskih provera | `4742d11f4c863ac7ea6bd21de0d354b9f604521ea25bf3d3f572d8312e16ca2b` |
| Prezentacioni PDF | `0c6165a235f0f2db1d02df6b457a7f9a69ef4235bb8e37edebb8f111b8011fd8` |
| PDF beležaka | `94cf575c207d32de9800b20d2871c9272550e0e25e08787efdd18eef7bedaa04` |
| Arhiva početnog stanja | `6f718955699cacea9fed24eeabece63dc1ae28412d345915c321662c6d658675` |

## Tačka nastavka

Beleške su napisane i pregledane, a evidencija vezana za konačne izvore i prikaze. **Ne ponavljati važeći pregled ako se izvori i zavisnosti nisu promenili.** Status 04 ostaje `u_radu` zbog pet stručnih pitanja. Sačekati korisnikovu konkretnu odluku, sprovesti samo odobrene izmene, uskladiti nastavni tekst i mapu pokrivenosti, pregledati pogođene slajdove i beleške, obnoviti potvrde i izvršiti `notes`, `review` i `check` za 04. Tek bez nerešenih sadržinskih problema postaviti `ceka_odobrenje` i predati celu 04 na prihvatanje. **Početak 05 nije odobren.**
