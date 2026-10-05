# Predavanje 02 — dorada s043–s046

**Status: `ceka_odobrenje` · 2026-10-05.** Svi aktuelni nalozi primenjeni, pregledani i provereni. Nema otvorenih stručnih pitanja; konačni rezultat korisnik još nije odobrio.

## Obuhvat i pokrivenost

Original je neizmenjen: 27 PDF strana / 54 izvorna slajda. Prezentacija i A4 PDF beležaka imaju po **60 strana**, uz šest ranije odobrenih nastavaka s002b/s009b/s015b/s023b/s024b/s032b. ID-jevi, njihov redosled, zamrznuta tema etf-v1, stil B, fontovi, autorstvo i školska godina 2021/22 očuvani su. Ova dorada ne dodaje strane i ne menja formule ili crteže.

| Slajd / izlazna strana | Dorada |
|---|---|
| s043 / 49 | Uvod o formiranju tabele prema zahtevima; pokrivanje svih jedinica površinama najvišeg reda uz b; objedinjenje i sažimanje proizvoda, uz naglasak na nepromenljivim literalima. Dve postojeće karte zadržane su u istoj veličini uz tekst u trećoj koloni. |
| s044 / 50 | Potpunije pravilo pokrivanja svih nula uz b, objašnjeno sažimanje i naglašeni komplementi nepromenljivih literala. Karta i izraz ostaju isti. |
| s045 / 51 | Zaključak 7 naspram 9 ulaza odvojen od uokvirenog pravila: unapred nije poznat povoljniji oblik; treba izvesti oba minimalna izraza pa ih uporediti. Ključne tvrdnje tamnocrvene i podebljane. |
| s046 / 52 | Uvod o kriterijumu broja čipova; četiri potrebna komplementa, pregled upotrebljenih kola i poređenje 4/3 čipa. Vraćeni su šest invertora i četiri dvoulazna ILI kola u 14-pinskim kućištima, raspodela pinova i oba računa. |

Pokriveno je **222/222 elemenata** (163 izvorne grupe i 59 dopuna). **108 elemenata** ima odredište u beleškama. Svi originalni detalji s043–s046 sada su vidljivi na odgovarajućim slajdovima. [Mapa](pokrivenost.md) i [evidencija beležaka](evidencija_beleski.json) prate poreklo bez uredničkog sadržaja u nastavnim PDF-ovima.

Tekst beležaka s043/s044/s045 bajtno je nepromenjen: konkretne grupe, tumačenje literala i kriterijuma ostaju dodatna objašnjenja. Beleške s046 zadržavaju broj slobodnih kola i razjašnjenje da se različiti tipovi kola ne mogu proizvoljno smestiti u jedan standardni čip; računi sada prikazani na slajdu više se nepotrebno ne prepisuju. Precrtavanje šema nije bilo potrebno. Jezičke izmene: „Da bi dobili“ → „Za minimalnu funkciju“, „na povšini“ → „na površini“, „1 dvoulazno ILI kola“ → „jedno dvoulazno ILI kolo“. Stručni izrazi i brojčani podaci ostaju isti.

## Pregled i provere

Pročitani su originalni slajdovi na stranama 22–23, lokalni izvori i neposredno prethodni prikazi. Stvarno su pregledani sva četiri konačna slajda i njihove pune A4 beleške. Provereni su svi literali, vrednosti karata, formule, broj kola/čipova, razmaci i tamnocrveni naglasci; nema preklapanja, odsecanja ili uredničkih komentara.

[Poređenje prikaza](poredjenje_dorade_s043_s046.json) dokazuje pikselnu jednakost ostalih **56 celih slajdova i A4 strana** i nepromenjene otiske njihovih važećih potvrda. Obnovljene su samo četiri pogođene potvrde. Karnoove karte su bajtno neizmenjene. Oba izraza proverena su za svih 16 kombinacija DCBA prema obaveznim jedinicama/nulama i međusobno su jednaka; brojevi ulaza 7/9 i kućišta 4/3 provereni su.

Izvršene komande (izlazni kod 0):

```bash
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza notes
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza review
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza check
```

**`check`: PROVERENO.** Postojeće računske i strukturne provere prolaze. Oba konačna LaTeX loga nemaju upozorenja, prekoračenja prostora ili grešaka. Pregledane potvrde važe za svih 60 slajdova i njihove beleške. Alati i zajednički stilovi nisu menjani.

[Notes log](../../build/redizajn/dorada-s043-s046-2026-10-05/notes.log), [review log](../../build/redizajn/dorada-s043-s046-2026-10-05/review.log), [check log](../../build/redizajn/dorada-s043-s046-2026-10-05/check.log).

## Isporuka i nastavak

- [Prezentacija](../../build/02_sinteza_kombinacionih_mreza.pdf), pogođene strane **49–52**.
- [PDF beležaka](../../build/02_sinteza_kombinacionih_mreza_beleske.pdf).
- [Uporedni pregled](../../build/redizajn/pregled/index.html).

Neposredno prethodni izvori i evidencija sačuvani su u `istorija/pre-dorade-s043-s045-2026-10-05/izvori-i-evidencija.tar.gz`; ta arhiva prethodi i naknadno zatraženoj doradi s046. Tadašnji [izveštaj](istorija/pre-dorade-s043-s045-2026-10-05/izvestaj.md) i ranije arhive čuvaju istoriju prethodnih dorada, uključujući s040–s042. Prethodni prikazi su u `build/redizajn/pre-dorada-s043-s045-2026-10-05/`.

PDF/PNG/HTML i logovi u `build/` ne verzionišu se; gornje komande ih obnavljaju. Sledeći korak je korisnikov pregled ove verzije. Odobrenje rezultata 02 se čeka; ranije dozvole za druga predavanja ostaju zasebne.

## SHA-256 pregledane verzije

| Resurs | Otisak |
|---|---|
| Originalni PDF | `f631914c9f32a0472f4fa3af11115abaadb9316dfcf6f1528cd91ef4d28868f4` |
| Izvorna mapa | `b2c8e07fa123a40da68c8b89b1b1c6ce88112e90c7417792cdec341d60136ca2` |
| Manifest | `b01aa603f6dce15bfb20d7447e59bdb2898847455610b1fd7d07a8520b126fe4` |
| Prezentacioni PDF | `99b9aa3fa6d31a156931ffa6a13fff347c141730f6b25e7ce2c538144f46065b` |
| PDF beležaka | `f3e0d6e909f9376286f0063e16b2a2a5870b14137d38e933a1cbc3d3d493ba91` |
| Zapis izgradnje | `c3864d36d7a8be941d332f20f00945cee1ae34d87f01c16856c487692c460efe` |
| Potvrde pregleda | `d19d21d892115bbeb73755bfdc5afe5c4924c9818ef1b288008a6245407713df` |
| Evidencija beležaka | `f951e212c71bb06ed0d7cbbbbe5e307a1a44d2ce10b137615bf8b770db0f99af` |
| Poređenje prikaza | `d75dee04c97391329678356c44d836d7ab5340052e8e5cf852758f4d4bcc00d7` |
| Arhiva prethodne isporuke | `ba34c2022a46ac2d12e92b0d6bcf8da410fb9be222d625bf414a9f5e42cdd747` |
