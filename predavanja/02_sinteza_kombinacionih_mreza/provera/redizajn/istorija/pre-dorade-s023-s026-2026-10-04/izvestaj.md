# Predavanje 02 — dorada s003/s013/s015–s022

**Status: `ceka_odobrenje` · 2026-10-04.** Sve tražene dorade su primenjene i proverene. Nema otvorenih stručnih pitanja. Korisnikov nalog odobrava izmene i podelu s015; završni rezultat slajdova i beležaka još nije prihvaćen.

## Izvor, verzija i broj slajdova

Original ima 27 PDF strana i **54 slajda**; ostaje neizmenjen. Uz prethodne podele s002/s009, korisnik je izričito zatražio podelu s015. Aktuelna prezentacija ima **57 slajdova**, a prateći PDF **57 blokova i 57 A4 strana**. Nastavci `02-s002b`, `02-s009b` i `02-s015b` dolaze neposredno iza svojih prvih delova; svi originalni ID-jevi i njihov međusobni redosled ostaju očuvani. S016 i dalje označava izvorni s016, sada na PDF strani 19.

[Odobrenje podela](odobrenje_podela.json) sadrži stvarne korisnikove citate i tri dopuštena ID-ja; otisak je vezan u [manifestu](manifest.json). [Mapa podela](mapa_podela.json) povezuje prethodne grupe sa oba dela. Izvorna `provera/mapa.json` i početni prikaz sa 54 slajda ostaju neizmenjeni. Plan odeljak 1.1 sada evidentira tri konkretna izuzetka: 620 originalnih slajdova u katalogu, 623 projektovane strane ukupno. Druge podele nisu odobrene.

Stil B i zamrznuta tema `etf-v1`, LuaLaTeX, odnos 16:9, postojeći fontovi, autorstvo prof. dr Lazara Saranovca i školska godina 2021/22 ostaju isti. Tamnocrvena služi nastavnim naglascima. Nijedna formula ili topologija mreže nije stručno promenjena ovom doradom.

## Izmene i reprezentativna poređenja

| ID | Izmena |
|---|---|
| s003 | Desno od desnog vremenskog dijagrama dodato pitanje `T_ul = T_izl ???`, jasno odvojeno od osa i strelica. Beleške zadržavaju tačan račun širine uz uslov da se obe promene prenesu. |
| s013 | Funkcionalna tabela dobija blage horizontalne linije kao s012; istaknute jedinice i sve vrednosti ostaju iste. |
| s015/s015b | Prva celina: nulti red 000, proizvod koji prepoznaje kombinaciju, negacija i dualni NI/ILI opis. Druga: red 001, preostali nulti redovi, povezivanje pet uslova I kolom i konačni proizvod zbirova. Cela funkcionalna tabela je ponovljena na oba slajda. Beleške su razdvojene po istim nastavnim celinama, sa svim izvorno uklonjenim objašnjenjima i međukoracima. |
| s016 | Jednačina komplementne funkcije i jednačina F svaka su u jednom redu. Tabela i De Morganovo objašnjenje imaju odvojen, čitljiv raspored. |
| s017 | Cela jednačina F je u jednom redu; očuvana definicija kanoničke konjunktivne forme i pravilo iz redova sa nulom. |
| s018 | Tabela sa horizontalnim linijama; vraćen izvorni uvod o kraćem indeksnom zapisu i binarnim ciframa reda. Opšta formula vrednosti binarnog broja ostaje vidljiva. Beleške koriste „potpuni proizvod“ i „potpuni zbir“, sa primerom indeksa 5, bez neobjašnjenih stranih termina. |
| s019 | Naslov „Šema funkcije F u obliku zbira proizvoda“. Povećan razmak parova sabirnica; završno ILI kolo niže, simetrične putanje između dva nivoa. |
| s020 | Vraćeno pitanje o raspoloživosti pravih i komplementnih signala i potrebi za invertorima; istaknuta tvrdnja o nepovoljnom opterećenju tri ulaza. Veći slobodan razmak između invertora i vodova ispod njih. Prema dodatnom korisnikovom komentaru I kola su još niže i odmaknuta od A sabirnice, a završno ILI kolo dodatno je spušteno. Lokalni položaji ne menjaju priključke. |
| s021 | Razdvojeni invertori i dva polariteta, završno ILI kolo niže; veze simetrične, van simbola. |
| s022 | Jednačina F u jednom redu iznad šeme. Naslov „Šema funkcije F u obliku proizvoda zbirova“ zadržava ranije odobren stručni naziv. Razdvojeni invertori, završno I kolo niže i dve simetrične stepenaste putanje od ILI kola ka njemu. |
| s024/s026 | Isti invertorski izvori imaju novi razmak i ovde. Oba para dualnih/NI/NILI šema pregledana, vodovi odvojeni od simbola prvog/drugog nivoa. S026 jednačina je u jednom redu radi prostora za čitljiv crtež. Funkcije i negacije ostaju iste. |

Reprezentativni prikazi: [s003](../../build/redizajn/pregled/index.html#02-s003), [s015](../../build/redizajn/pregled/index.html#02-s015), [s015b](../../build/redizajn/pregled/index.html#02-s015b), [s018](../../build/redizajn/pregled/index.html#02-s018), [s020](../../build/redizajn/pregled/index.html#02-s020) i [s022](../../build/redizajn/pregled/index.html#02-s022). Oba dela s015 porede se sa istim originalom i početnim prikazom. [Prethodni izveštaj](istorija/pre-dorade-s003-s022-2026-10-03/izvestaj.md) i arhiva `izvori-i-evidencija.tar.gz` u istom folderu čuvaju stanje neposredno pre ove dorade. Ranija dorada s002–s013 ostaje dokumentovana tom arhivom i ranijom istorijom.

Dorađeno je 13 vektorskih izvora: s003 sa kašnjenjem; s019 sabirnice i jezgro tri proizvoda; s020 invertori; s021 dvostruki invertori, rasterećenje i SOP jezgro; s022 šema i POS jezgro; oba s024 i oba s026 crteža. Precizan spisak izvora nalazi se u arhivi i Git razlikama. Tabele s013/s018 dobile su linije, a s016 raspored redova; nijedna tabelarna vrednost nije promenjena.

## Beleške i pokrivenost

Pokriveno je **213/213 elemenata: 157 izvornih grupa i 56 dopuna**. 118 elemenata ima provereno odredište u beleškama. Povećanje sa 210 na 213 dolazi iz podele složenih grupa s015 i zasebnog dopunskog objašnjenja s015b; stari sadržaj je u potpunosti obuhvaćen oba dela i njihovim beleškama.

[Inventar](inventar.json), [pokrivenost](pokrivenost.md), [uređiva mapa](pokrivenost.json), [evidencija beležaka](evidencija_beleski.json) i [odluke](odluke.md) čuvaju poreklo i dokaze izvan nastavnog PDF-a. Ne održava se druga kopija teksta beležaka. S015 beleške objašnjavaju prepoznavanje uslova i aktivnu nulu; s015b beleške čuvaju preostale redove i svih pet negiranih proizvoda pre konačnog POS izraza. S018 terminologija je prevedena na potpune proizvode/zbirove. Ostale beleške čuvaju nastavno značenje; njihov prikaz je obnovljen uz odgovarajući slajd i naslov.

S001 nema dodatni tekst, samo vezu sa ID-jem; preostalih 56 izvora daje dodatno nastavno objašnjenje. Beleške i slajdovi nemaju uredničke komentare, istoriju redizajna, poreklo PDF strana ili korisnikove odluke.

## Pregled i provere

Stvarno su pregledani originalni PDF prikazi, LaTeX izvori i **13 pogođenih projektovanih prikaza i celih A4 strana**: s003, s013, s015, s015b, s016–s022, s024 i s026. Provereni su svi redovi, formule, pravilni polariteti i priključci, tačke stvarnih spojeva, putevi van simbola, čitljivost i potpuni dodatni nastavni sadržaj.

Za **44 nepogođena ID-ja** [poređenje](poredjenje_nepogodjenih.json) dokazuje da su ceo projektovani prikaz i telo A4 beležaka pikselno identični prethodnoj isporuci. Samo numeracija fizičke A4 strane može se promeniti. Prethodni stvarni sadržinski pregled je zadržan, uz proveru novog redosleda. Svih 57 potvrda vezano je za aktuelne izvore, prikaze, mapiranje i pokrivenost.

Izvršeno:

```bash
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza notes
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza review
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza check
```

Sve tri konačne komande završavaju izlaznim kodom 0. **`check`: PROVERENO.** Konačna kompilacija nema `Overfull`, `Underfull`, upozorenja, nedostajuće znakove ili greške. Početna prekoračenja prostora rešena su rasporedom, podešavanjem geometrije crteža i razmacima; font oznaka nije automatski smanjivan.

Postojeća računska provera prolazi: tabela osam redova, SOP/POS za 16 ulaza, obe konsenzus jednakosti i oba primera gliča. Liste priključaka zajedničkih jezgara s019/s021/s022 dodatno su poređene sa arhivom: samo koordinate su promenjene, svi brojevi ulaza i izabrani polariteti ostaju isti. Originalna mapa je bajtno ista kao arhivirana. Nova podela koristi postojeću proverenu infrastrukturu odobrenih podela; zajednički alati i tema nisu menjani ovim nalogom.

Logovi: [notes](../../build/redizajn/dorada-s003-s022-2026-10-03/notes.log), [review](../../build/redizajn/dorada-s003-s022-2026-10-03/review.log), [check](../../build/redizajn/dorada-s003-s022-2026-10-03/check.log). Raniji regresioni/integracioni testovi alata ostaju dokumentovani u prethodnom izveštaju; ova dorada ne menja alat niti njihove rezultate.

Jezički su uređeni uvodi, pitanja i nazivi članova, uz očuvanje stručnog značenja. Ranije odobrene odluke za s022/s029/s034/s040/s052/s053 ostaju primenjene. Nema novih stručnih ispravki ni otvorenih pitanja.

## Isporuka i nastavak

- [Prezentacija — 57 slajdova](../../build/02_sinteza_kombinacionih_mreza.pdf).
- [PDF beležaka — 57 A4 strana](../../build/02_sinteza_kombinacionih_mreza_beleske.pdf).
- [Uporedni pregled](../../build/redizajn/pregled/index.html).

PDF/PNG/HTML i logovi ostaju u `build/` i ne verzionišu se. Prethodni PDF i prikazi sačuvani su u `build/redizajn/pre-dorada-s003-s022-2026-10-03/`; izvori i potvrde u arhivi prethodne isporuke. Novi agent proverava aktuelne otiske i nastavlja od ovog izveštaja, bez ponavljanja nepogođene analize.

Naredni korak je korisnikov pregled **ove verzije slajdova i beležaka 02**. Status `ceka_odobrenje`; prihvatanje rezultata nije izmišljeno. Ranija dozvola za početak 03 ostaje odvojena odluka. Ovaj ciklus ne menja druga predavanja.

## Dopunska dorada razmaka s020/s022 — 2026-10-04

Po dodatnim korisnikovim komentarima horizontalni vodovi sada imaju slobodan razmak i od invertora iznad i od invertora ispod. Povećan je razmak između parova vodova; vertikalni položaji su usklađeni sa raspoloživom visinom, uz iste fontove i veličine simbola. Na s022 oba nivoa kola su spuštena, a na s020 je dodatno usklađen razmak između I i završnog ILI kola. Vodovi ostaju van simbola, sa tačkama samo na stvarnim spojevima.

Stvarno su pregledani originali, konačni s020/s022 i obe cele A4 strane. S020 je PDF strana 23, s022 strana 25. Priključci su poređeni prema značenju svakog voda: svih devet SOP i petnaest POS priključaka zadržava iste literale i polaritete. Formule, nastavni tekst, 57 ID-jeva i broj strana ostaju isti.

Zajednički izvori sada dozvoljavaju lokalne koordinate s022; njihove podrazumevane vrednosti su sačuvane. [Poređenje](poredjenje_razmaka_s020_s022.json) dokazuje pikselnu jednakost **celog projektovanog prikaza i cele A4 strane za ostalih 55 ID-jeva** neposredno prethodnoj isporuci. Potvrde izvora s021/s024/s026 obnovljene su uz ovaj dokaz; nepogođene potvrde ostaju iste. Arhiva neposrednog prethodnog stanja je `istorija/pre-razmaka-s020-s022-2026-10-04/`; prikazi pre dorade su u `build/redizajn/pre-razmaka-s020-s022-2026-10-04/`.

Ponovo su izvršene komande `notes`, `review`, `check` sa `LECTURE=02_sinteza_kombinacionih_mreza`: sve završavaju kodom 0, **PROVERENO**, bez prekoračenja prostora ili upozorenja u konačnoj kompilaciji. [Notes log](../../build/redizajn/dorada-s020-s022-2026-10-04/notes.log), [review log](../../build/redizajn/dorada-s020-s022-2026-10-04/review.log), [check log](../../build/redizajn/dorada-s020-s022-2026-10-04/check.log). Status ostaje `ceka_odobrenje`; sledeći korak je korisnikov pregled ove verzije.

## SHA-256 pregledane verzije

| Resurs | Otisak |
|---|---|
| Originalni PDF | `f631914c9f32a0472f4fa3af11115abaadb9316dfcf6f1528cd91ef4d28868f4` |
| Izvorna mapa | `b2c8e07fa123a40da68c8b89b1b1c6ce88112e90c7417792cdec341d60136ca2` |
| Manifest | `1cb97554de93008f638f846758a479088e79693c179600a4e55db6022be4170d` |
| Odobrenje podela | `428d4768bfb2777c49716920d3318b1a649986b1056a74b6ad7c65e571db5509` |
| Mapa podela | `5b7909be400e9cb9ad5379085e4f1fc3abf62ccda803a2c8066378908f2e7e2f` |
| Prezentacioni PDF | `7db33f07afb78e05e32d9a1c9191ff316cc33f5c14ae7ff7b5fbef2bd9c3716d` |
| PDF beležaka | `78a2d01eee0d1c6765f4dc224512403d5f85df0351a86b91f9fad1c6c7aee0e1` |
| Zapis izgradnje | `6b405d576deb6b1d875eb42dc3ac74b18d437e8cbdec4efcbd37f6b71d0df89f` |
| Potvrde pregleda | `39ba8780306c24cd577894f2a8cd0caf217e306330b1428bc3771ab5dcbd58f3` |
| Evidencija beležaka | `6b5889d53d66f63f74dad7df8a2500cf7fcab97aa78a09c21a6fa0c426a1921a` |
| Arhiva prethodne isporuke | `ca41c9b6e863fa26e496fa7cc79d9d53c924716388955d5ca0248247c1a5c243` |
