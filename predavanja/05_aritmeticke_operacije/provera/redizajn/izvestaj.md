# Izveštaj — predavanje 05, aritmetičke operacije

Datum: **2026-10-02**. Status: **`u_radu`**. Izgled i beleške obrađeni su za svih 55 slajdova; završnu sadržinsku potvrdu sprečavaju šest grupa stručnih pitanja u originalu. **Ovaj izveštaj nije zahtev za prihvatanje cele prezentacije.** Potrebna je odluka o konkretnim ispravkama iz [otvorenih pitanja](otvorena_pitanja.md).

## Obuhvat i očuvane celine

Pročitan je [PLAN_PREDAVANJA.md](../../../../PLAN_PREDAVANJA.md), originalni [PDF 05](../../../05%20Aritmeticke%20operacije.pdf), svih 55 postojećih LaTeX slajdova, njihovi uključeni crteži, tabele, pseudokod i računske provere. Svaka izdvojena originalna strana/slajd i početni kompajlirani prikaz pregledani su vizuelno; tekstualno izvlačenje služilo je kao pomoć. Pregledani su i redizajnirani slajdovi i sve A4 strane beležaka.

Očuvani su **55 slajdova, redosled i ID-jevi `05-s001`–`05-s055`**, sa tačno jednom projekcionom stranom po ID-ju. Nema uklonjenih, spojenih ili novih slajdova, overlay strana ili novih razdelnika. Originalni PDF i istorijski `provera/mapa.json`, `provera/pregled.json` ostaju neizmenjeni. Početni PDF, 55 prikaza i zavisnosti sačuvani su u `build/redizajn/pre/`; trajna arhiva je [pocetni_prikaz.tar.gz](pocetni_prikaz.tar.gz).

Pokrivene su sve celine: komparatori i proširenje/kaskade (s002–s011), sabiranje i oduzimanje sa fiksnom tačkom (s012–s020), komplementi i prekoračenje (s021–s029), proširenje, pomeranje i INC/DEC (s030–s036), neoznačeno i označeno množenje (s037–s044), Boothov algoritam (s045–s048), odsecanje i zaokruživanje (s049–s052), deljenje (s053–s055). Namerno pogrešne realizacije sa nastavnim pitanjima na s007, s038 i s040 zadržane su; s011 ostaje pitanje sa ispravnom realizacijom.

## Promene izgleda

Prezentacija koristi zamrznutu temu **`etf-v1`**, izbor **B**, iste fontove i 16:9 format kao prethodno sređena 01. Nastavna isticanja su lokalno tamnocrvena `#A32638`; strukturni plavi okviri i zaglavlja tabela ostaju dosledni temi. Autorstvo prof. dr Lazara Saranovca i školska 2021/22 sačuvani su iz postojećih izvora; ne zavise od datuma obrade. ETF resurs potiče iz verzionisane teme.

Ujednačeni su naslovi, margine, veličine oznaka, raspored kolona i razmaci. Gusta mesta sređena su pojedinačno rasporedom i nastavnim beleškama, bez automatskog smanjivanja celog slajda. Šeme su uređivi TikZ izvori; oznake su 9 pt. Ključne formule, tabele, primeri i pseudokod ostaju na slajdu.

Precrtane/dorađene šeme i dijagrami:

- s002, s004–s011: jezgro komparatora, kaskade/stabla i blokovi; preglednije vođenje vodova i vidljive tačke stvarnih spojeva. Nepovezani četvrti simbol iz izvornog prikaza ostaje prisutan.
- s008: simbol komparatora organizovan uspravno, sa svim istim priključcima.
- s012/s018: poravnanje operanada i tri početna prikaza, uz pune pojedinačne korake u beleškama.
- s014: oba dijagrama prelamanja i zasićenja, uz odvojene primere/račune.
- s015/s016: polusabirač i potpuni sabirač, simetrične grane, odvojene oznake i spojevi.
- s028: sabirač/oduzimač, upravljačka magistrala i OVF grane; topologija očuvana, spojevi označeni.
- s034–s036: detektor najniže pozicije i INC/DEC blokovi; tekst ne preseca upravljačke strelice, grananje podatka označeno.
- s048: ceo dijagram toka, razmaknuti blokovi, jasno usmerene strelice i izdvojena povratna grana. Logika odluka i koraka ostaje ista.

Tabele množenja zadržavaju svaku cifru i namerne nastavne upitnike. S032 ima sva četiri pomeranja i razmak između poslednje tabele i zaključka. Na s031 su razdvojeni tekst, tabele i tumačenje formule. Na s045/s046 očuvani su parcijalni proizvodi i konačni izraz, uz dodatno izvođenje u beleškama.

Reprezentativna poređenja u [uporednom pregledu](../../build/redizajn/pregled/index.html): [s015](../../build/redizajn/pregled/index.html#05-s015), [s016](../../build/redizajn/pregled/index.html#05-s016), [s024](../../build/redizajn/pregled/index.html#05-s024), [s028](../../build/redizajn/pregled/index.html#05-s028), [s031](../../build/redizajn/pregled/index.html#05-s031), [s045](../../build/redizajn/pregled/index.html#05-s045), [s048](../../build/redizajn/pregled/index.html#05-s048). Svako poređenje sadrži original, prethodni LaTeX prikaz, novi slajd i beleške istog ID-ja.

## Beleške i mapa uklonjenih objašnjenja

Jedini izvori beležaka su `beleske/s001.tex`–`beleske/s055.tex`, sa vezama na stabilne ID-jeve i nevidljivim sidrima. Sve beleške napisane su kao dodatno nastavno objašnjenje za predavača. Nema uredničkih naslova, PDF lokacija, istorije redizajna, rezultata testova ili korisnikovih odluka. S001 ima samo ID; A4 dokument prikazuje slajd i naslov bez veštačkog pasusa.

| ID-jevi | Preneti nastavni detalji, potpuno objašnjeni u beleškama istog slajda |
|---|---|
| s002 | Minimizacija pojedinačnih izlaza, komercijalne komponente i smisao lokalnih relacija |
| s004–s011 | Tumačenje šest lokalnih relacija uz I/NILI kola; priključci i samo kolo ostaju vidljivi |
| s012 | Svi pojedinačni decimalni koraci sabiranja i prenosa |
| s018 | Ceo niz pozajmica i ekvivalentno oduzimanje sa prenosom |
| s021 | Zašto negativni operandi zahtevaju oba pisana postupka i poređenje apsolutnih vrednosti |
| s023 | Značenje pojave/odsustva izlaznog prenosa i dodatog petog bita |
| s027 | Korekcija još jednom jedinicom i kružni prenos prvog komplementa |
| s045 | Potpuno označeno tumačenje zapisa D i međukoraci komplementiranja |

Ostale beleške dodaju samo potrebna proverljiva tumačenja: rad i smer kaskade, OVF, ASR negativnih neparnih brojeva, znak parcijalnih proizvoda, Boothove iteracije, razlika numeričkog dodatka i pravila zaokruživanja, znak količnika i uslovi reprezentabilnosti. Beleške ne zamenjuju nijednu celu nastavnu celinu.

Poreklo, prenos i dopune odvojeno su evidentirani u [evidencija_beleski.json](evidencija_beleski.json), [inventar.json](inventar.json) i [pokrivenost.json](pokrivenost.json); ne održava se druga kopija teksta beležaka. Popis sadrži **210 elemenata: 156 izvornih i 54 dopune**. Svaki ima provereno odredište na slajdu i/ili u beleškama istog ID-ja. Proverena pokrivenost znači da sadržaj nije izgubljen; ne znači prihvatanje spornih izvornih formula.

## Provere

Izvršene komande:

```bash
make -C predavanja LECTURE=05_aritmeticke_operacije notes
make -C predavanja LECTURE=05_aritmeticke_operacije review
make -C predavanja LECTURE=05_aritmeticke_operacije check
python3 predavanja/05_aritmeticke_operacije/kodovi/provera_logike.py
```

- `notes` i `review`: uspešno. Prezentacija ima **55 strana**, beleške **55 A4 strana**, svaki ID povezan je sa odgovarajućim prikazom. Nema grešaka kompilacije, `Overfull` kutija, nedostajućih znakova/resursa ili upozorenja u konačnim LaTeX logovima.
- Računske provere: uspešno; 16 dvobitnih, 256 četvorobitnih i 4.096 šestobitnih parova komparatora, svih 512 ADD/SUB stanja i OVF, 16 ekstenzija, 256 pomeranja/INC/DEC, sve ćelije sedam tabela proizvoda, Boothova jednakost za širine 2–8 i sva stanja prikazanog primera, kvantizacija i 74:8. Namerni primer s007 daje 1.344 neslaganja i nije proglašen ispravnim.
- Dodatna nezavisna provera beležaka: tačni racionalni decimalni računi, zapisi drugog komplementa, reprezentabilni zbirni slučajevi prvog komplementa, 256 uslova ASL, negativan ASR, sve iteracije 2×6, bitovski niz 001110, 256 generičkih odsecanja i deljenje. Integrisana je u postojeću računsku proveru. [Rezultati](rezultat_racunskih_provera.txt).
- Vizuelni/sadržinski pregled: original, početni prikaz, novi slajd i beleške pregledani za svih **55 ID-jeva**. Vodovi, spojevi, smerovi strelica, cifre, formule, polarnosti/negacije i veze beležaka provereni su pojedinačno. **47 ID-jeva nema otvoren problem; osam ima izvorno stručno pitanje**. [Potvrde i aktuelni dokazi](pregled.json).
- `check`: **NEZAVRŠENO**, zbog 11 nepotvrđenih kategorija na s014, s024, s026, s050–s054. S052 uključuje i potvrdu usklađenosti beležaka sa spornim dodatkom. Nema strukturnih problema, nepokrivenih elemenata, zastarelih potvrda ili neuspešne računske provere. [Tačan izlaz](rezultat_check.txt). Uspešna generička provera odsecanja sa granicom 15/128 ne potvrđuje pogrešno skaliranje proizvoda iz s050–s052.

## Jezičke ispravke i stručna pitanja

Bez promene značenja ispravljeni su „apsoluta vrednost“ → „apsolutna vrednost“ (s021), „operecije“ → „operacije“ (s043), duplirano „je“ (s051), velika slova i interpunkcija u običnim naslovima/oznakama. Ostale skraćene rečenice čuvaju izvorno značenje i, gde je potrebno, potpuno obrazloženje u beleškama.

Stručne izmene **nisu odobrene** i nisu primenjene. Otvorene grupe su:

1. s014: `001000` → `011000` u redu prenosa osnove 7.
2. s024: tekst dodatka `100000` → `10000`.
3. s026: ispraviti obrnute izlazne prenose za granice označenog zbira.
4. s053/s054: neuspeh `R<0`, uspeh `R≥0`; nulti rezultat ne sme pripadati obe grane.
5. s050–s052: uskladiti tačku, indekse i preciznost proizvoda; ponuditi usklađen primer s051 ili izričito zaseban generički primer kvantizacije.
6. s052: usloviti zaokruživanje naviše nenultim odbačenim delom i odvojiti bit odluke od numeričkog dodatka.

[Otvorena pitanja](otvorena_pitanja.md) daju računsku proveru, kontraprimere i precizan predlog za svaku grupu. Zahtev za odluku poslat je korisniku; odgovor nije primljen u ovoj obradi. Prema odeljku 1.1 [plana](../../../../PLAN_PREDAVANJA.md), „Promene formula, vrednosti, topologije kola, stručnih tvrdnji ili uslova zahtevaju korisnikovo izričito odobrenje.“; odeljak 10 zabranjuje završnu predaju sa nerešenom tvrdnjom.

## Isporuka i nastavak

- [Prezentacioni PDF](../../build/05_aritmeticke_operacije.pdf).
- [PDF beležaka za predavača](../../build/05_aritmeticke_operacije_beleske.pdf).
- [Uporedni pregled svih slajdova i beležaka](../../build/redizajn/pregled/index.html).
- [Mapa pokrivenosti](pokrivenost.md), [dokazi pregleda](pregled.json), [manifest](manifest.json), [stvarne zavisnosti izgradnje](izgradnja.json).

Poslednji pregledani ID: **05-s055**, obrađeni su svi s001–s055. Nema preostalih neobrađenih slajdova ili beležaka. Preostaje odluka o šest grupa ispravki i zatim dorada osam pogođenih ID-jeva. Nakon odobrenja sačuvati stvarnu poruku u `odluke.md`, primeniti samo odobreni obuhvat, uskladiti povezane beleške, inventar/pokrivenost i testove, pokrenuti `notes`, `review`, `check`, stvarno pregledati pogođene prikaze i obnoviti njihove potvrde. Važeće preglede nespornih i nepromenjenih ID-jeva ne ponavljati bez razloga.

Odobrenje cele 05: **nema**. Početak 06: **nije odobren**. Dok se pitanja ne razreše status ostaje `u_radu`, a ne `ceka_odobrenje`.

## Kontrolne sume pregledane verzije

- Originalni PDF: `a181158ccdb62d376871ab658d804dae129b0e79dd969a731c8dca25731309d8`.
- Manifest redizajna: `df23c8fe09eeaffaa97792f2469f903132cdf8eabed74bfcbf75ded0815b3b25`.
- Zapis izgradnje: `9c8c804c4dec6aae02224ac4b2be40f69193619d91d58ddc7065b877d610cd7e`.
- Inventar: `0e5011674dd459e9cda2d6cb54f494134281f484d378d50c771ce0a8ade8c897`.
- Mapa pokrivenosti: `a16a4a8add80941eb82953115169d489c5cc533ae6142039d7372ca7a03bb289`.
- Evidencija beležaka: `864d938feadcd7148ce105ecc2b56ae50b3b8e33077702a589462a000a10fab9`.
- Potvrde pregleda: `6246694dbf9f52c6645d6790a50b794fae575239eb3b3bad60dffcc83fc8efb5`.
- Arhiva početnog prikaza: `bb7cdb453c8c9c8f8c779f12d20e38766ec8417aac3d6ae2865a929a7cb2412a`.
- Prezentacioni PDF: `956f9445f609ff7ebc6910540bef73063e24b5d584c3880cb86282c36db99143`.
- PDF beležaka: `3578f0857301fdb63fab43c3fd1753a6ecb27ef3020daa5ecf900cc998e7eb8f`.
- Manifest teme: `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41`.
- Potpis početnog snapshot-a: `c4f9366080ac86c4db5998bc2bf9f9b8fd78e1b3c01da77bd0cbf22634995895`.

- Početni PDF `build/redizajn/pre/prezentacija.pdf`: `cfb877aaed1de26ef9e7a62edf1bd278e36da8a23dec096cc183f46e2a76fc52`.
