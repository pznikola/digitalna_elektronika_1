# Predavanje 04 — beleške i odobrene stručne ispravke

Datum: **2026-10-02**. Status predavanja: **ceka_odobrenje**. Beleške i sve odobrene stručne ispravke napisane su i pregledane; završne provere prolaze. **Nema otvorenih stručnih pitanja.** Nova isporuka cele 04 predata je korisniku na prihvatanje. Tema **etf-v1**, stil **B**, nepromenjeni.

Pročitani su [plan](../../../../PLAN_PREDAVANJA.md), svih **39 originalnih slajdova** iz 20 PDF strana, svih **39 postojećih slajdova** i pripadajući izvori beležaka. Original i projekcioni prikaz pojedinačno su upoređeni; svih **39 konačnih A4 strana** beležaka pregledano je u punoj veličini. Očuvani su broj, redosled i ID-jevi **04-s001–04-s039**. Pri pisanju beležaka projekcioni izvori nisu menjani. Posle korisnikovih odluka ispravljeni su s006, s009, s016, s034 i s035. Poslednja dorada obuhvata s009 i njegove beleške; projekcioni i A4 prikaz ponovo su pregledani, a ostalih 38 parova je identično prethodno pregledanoj verziji. Ostali nastavni tekst beležaka, tabele, crteži, originalni PDF i tema ostali su bajtno nepromenjeni u ovoj poslednjoj doradi.

## Nastavni tekst beležaka

Prepisano je svih 39 fajlova `beleske/sNNN.tex`. Na 37 slajdova beleške sadrže samo potrebno dodatno objašnjenje za predavača: potpuno objašnjene izvorne detalje koji nisu vidljivi, međukorake, značenje oznaka, rad postupka i proverene kratke primere. S001 i s011 zadržavaju ID i nevidljiva sidra bez veštačkog teksta. Ne propisuje se ista dužina svakom slajdu.

Uklonjeni su vidljivi redovi o izvoru, obavezni urednički podnaslovi, komentari o redizajnu, predlozi stručnih izmena i zahtevi za odobrenje. Poreklo, razlika između izvornog detalja i dopune, dokazi i korisnikove odluke čuvaju se samo u `provera/redizajn/`. Nema druge kopije teksta beležaka. Sva ranija `% element:` sidra sačuvana su, a proverene dopune imaju zasebne oznake `d01`.

| Slajdovi | Dodatno objašnjenje za predavača |
|---|---|
| s002–s007 | Pozicione težine, uloga nula, teleskopski maksimum, razlikovanje zapisa i vrednosti, potpuno školsko obrazloženje zapisa razlomkom. |
| s008–s010 | Puno početno razvijanje celobrojne i razlomljene vrednosti; izdvajanje cifara, ostatak i smer čitanja; konačnost celobrojnog postupka i odobreni strogi uslov s009, uz granični primer i najmanji broj cifara u beleškama. |
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

[Inventar](inventar.json), [mapa pokrivenosti](pokrivenost.md), [precizna odredišta](pokrivenost.json) i [evidencija novih beležaka po slajdu](evidencija_beleski.json) čuvaju poreklo i potvrde. Sve odobrene stručne ispravke povezane su sa izvornim elementima u mapi i računski potvrđene; nema preostalih spornih uslova.

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
- Svaka beleška i svaka konačna strana stvarno su pregledane: potpunost, stručna tačnost dodatnog sadržaja, čitljivost, upotrebljivost za predavača i odsustvo nepotrebnog ponavljanja. Posle poslednje odluke ponovo su pregledani projekcioni i A4 prikaz s009. Ostalih 38 parova je identično prethodno pregledanoj verziji, što je provereno otiscima prikaza i izvora.
- Postojeća [računska provera](../../kodovi/provera_logike.py) prolazi, uključujući tabele, konverzije, komplemente i fiksnu tačku. Tri stvarne binarne jednačine s034/s035 proverene su kroz svih 8.190 kodova širine 1–12 bita, uz proveru ponovljenog komplementiranja modulo 2ⁿ. S009 je izričito odobren i korigovan; stvarni uslov poređen je sa minimalnim brojem cifara iz uzastopnog deljenja kroz 76.157 slučajeva. Provereni su nula i tačni stepeni svih osnova 2–16, uz susedne vrednosti; ne koristi se zaokružen logaritam.
- [Dopunske računske provere beležaka](racunske_provere_beleski.json) prolaze: **13 grupa i 122.205 slučajeva**, sa tačnim razlomcima, rekonstrukcijom cifara, periodom, greškom odsecanja, kompatibilnim osnovama, skaliranjem i iscrpnim kodovima drugog komplementa/ofseta.
- `check` daje **PROVERENO** (izlazni kod 0). Potvrđeno je svih 39 slajdova i beležaka, 177 odredišta sadržaja, tačan broj/redosled/ID-jevi, dostupnost resursa i aktuelnost pojedinačnih potvrda. Nema otvorenih kategorija `problem`, nepokrivenih elemenata ili zastarelih potvrda.

[Log kompilacije](../../build/redizajn/provera-beleski/notes.log), [log pregleda](../../build/redizajn/provera-beleski/review.log), [log završne provere](../../build/redizajn/provera-beleski/check.log) i [log postojeće računske provere](../../build/redizajn/provera-beleski/provera-logike.log). Automatika ne zamenjuje pojedinačni pregled.

## Jezičke ispravke i otvorena pitanja

Zadržana su izvorna značenja uz gramatički uredan nastavni tekst. U prethodnom redizajnu evidentirane su očigledne ispravke s013 „tačnije rezultat“ → „tačniji rezultat“, s022 „RELAN“ → „Realan“, s024 „Ali sto tako“ → „Ali isto tako“, s028 „smo podrazumevalo“ → „smo podrazumevali“, ponovljeno „znaka“ na s031/s032, s034 „jec“ → „je“ i s039 „jedna registar“ → „jedan registar“. U novim beleškama s023 precizirano je da promena vrednosti LSB-a menja broj za jedan, a na s027 da se razmatraju težine sa negativnim eksponentom. Stručni izvorni zapisi nisu samovoljno menjani.

Korisnik je 2026-10-02 izričito odobrio promene s006/s016 i naziva s034, zatim binarnih jednačina s034/s035 i uslova s009; [odluke.md](odluke.md) čuva njegovu stvarnu poruku:

| Slajd | Primenjena stručna ispravka i dokaz |
|---|---|
| s006 | U oba izraza početak decimala je `346938775510204081632653061224489795…`. Proverena je svaka stvarno ispisana cifra algoritmom deljenja tačnog razlomka 17/49. |
| s009 | Strogi uslov `n > log_r CV10`, uz `CV10 > 0`, i zaseban zapis nule jednom cifrom. U beleškama objašnjeni rᵐ, 8 = 1000₂ i minimalni broj cifara; 76.157 provera kriterijuma. |
| s016 | Prva dva dvostruka indeksa su `b_{(n-1),(k-1)}` i `b_{(n-1),(k-2)}`, sa zarezom i zagradama prema korisnikovom primeru. Težine `q^{kn-1}` i `q^{kn-2}` i grupisanje nisu menjani. |
| s034 | Naziv je „komplement 10-tke“, u skladu sa 1000 − 123 = 877. Binarna formula je ekvivalentno preuređena u M−B+1 = invertovani B+1, gde je M=2ⁿ−1, kako bi pratila opštu formulu. |
| s035 | Druga formula ispravljena u M−(invertovani B+1)+1 = B: ceo prethodni drugi komplement je u zagradama. Prva formula ostaje ista. |

Svi pogođeni projekcioni i A4 prikazi su sadržinski i vizuelno pregledani. Postojeća računska provera čita stvarne izvore korigovanih formula; za binarne jednačine tumači dozvoljene aritmetičke izraze i poredi ih sa vrednostima neoznačenog i invertovanog koda, uključujući nulu i krajeve opsega. Nastavni tekst beležaka je usklađen bez nepotrebnog prepisivanja vidljivih ispravki. Na s009 dodat je provereni granični primer i formula najmanjeg broja cifara, radi nastavnog objašnjenja strogog uslova.

U [otvorena_pitanja.md](otvorena_pitanja.md) **nema otvorenih pitanja**. Poslednja stvarna poruka „ispravi i s009 molim te“ izričito odobrava preostalu ispravku; sada su sva stručna pitanja rešena. Odobrene ispravke ne predstavljaju prihvatanje nove isporuke cele 04 niti dozvolu za 05. U beleškama su samo nastavna objašnjenja; odluke i poreklo ostaju u odvojenoj evidenciji.

## Izlazi i kontrolne sume

- [PDF beležaka — 39 A4 strana](../../build/04_brojni_sistemi_beleske.pdf).
- [Prezentacija sa odobrenim ispravkama — 39 slajdova](../../build/04_brojni_sistemi.pdf).
- [Uporedni pregled originala, prethodnog i trenutnog slajda i novih beležaka](../../build/redizajn/pregled/index.html).
- [Poređenje ranijeg redizajna pre/posle](../../build/poredjenje/poredjenje-pre-posle.pdf); poređenje opisuje raniji redizajn, a ne naknadno odobrene ispravke.
- [Evidencija pre završne ispravke s009](istorija/pre-ispravke-s009-2026-10-02/izvestaj.md).
- [Evidencija pre ispravke jednačina s034/s035](istorija/pre-ispravke-jednacina-s034-s035-2026-10-02/izvestaj.md).
- [Evidencija pre tri stručne ispravke](istorija/pre-strucnih-ispravki-2026-10-02/izvestaj.md).
- [Prethodna evidencija i izveštaj](istorija/pre-dorade-beleski-2026-10-02/izvestaj.md); stari urednički opisi beležaka nisu aktuelna pravila ni dokaz pregleda novih beležaka.
- [Trajna arhiva početne rekonstrukcije](polazni-izvori.tar.gz), [manifest](manifest.json), [zapis izgradnje](izgradnja.json) i [obnovljene pojedinačne potvrde](pregled.json).

| Resurs | SHA-256 |
|---|---|
| Originalni PDF | `e1f763084b19156c790ffe1f30b9d703081c8fbdc57e2ad9b2d9b73140ad1518` |
| Manifest etf-v1 | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |
| Manifest redizajna | `f4301065e016daa6b3495b27b353908594353b4c49559ce042c8f7f88a839d9b` |
| Zapis izgradnje | `91b4e9954fbad88827e5c582a6ff47e7e8a39c0ce8170ca179cb7255e5403f14` |
| Potvrde pregleda | `c0b0fb4a3070c6c84177cd165668606d828179d935f7a2cc64c6f92ffabdad90` |
| Inventar | `a5fb314bb23508017090af891a151ffae7cd1623eb7f010523e8697458ace20e` |
| Mapa pokrivenosti | `f6719ddd6f57acd0f972f234cee169a8056fd01c134d400db6e7da96bea45b62` |
| Evidencija novih beležaka | `052ee26bf27c626375e0ca237b3a7c9beed813893e14d24ef71d820b1e356757` |
| Dokazi dopunskih računskih provera | `2d13c5cae4fcc50a139838bf23418baa31960af3b9d407e78c3af8f165f9ae65` |
| Prezentacioni PDF | `0523380bd046584ec8d4f5407861355b6ad6c3c1b5b5833382714868b78b6dc4` |
| PDF beležaka | `c0e42e27262b8fd5fe1e31b388e02ae9c39510e88cf53808f37786a669235be4` |
| Arhiva početnog stanja | `6f718955699cacea9fed24eeabece63dc1ae28412d345915c321662c6d658675` |

## Tačka nastavka

**Predavanje 04 je spremno za korisnikov pregled; status `ceka_odobrenje`.** Svih 39 slajdova i beležaka je pregledano, 177/177 elemenata ima potvrđeno odredište, sve stručne ispravke su izričito odobrene i primenjene, `notes`, `review` i `check` prolaze. Nema otvorenih sadržinskih pitanja ni upozorenja kompilacije.

Ne ponavljati važeće provere ako se izvori i zavisnosti nisu promenili. Sledeći korak je korisnikovo prihvatanje cele nove isporuke 04; odobrenje pojedinačnih ispravki nije prihvatanje te isporuke. **Početak 05 nije odobren.**
