# Izveštaj 03 — dorada s004 i s007–s010

## Status i verzija — 2026-10-09

**Status: `ceka_odobrenje`.** Završena je tražena dorada s004/s007/s008/s009/s010 i njihovih beležaka. Izvorni s010 podeljen je po izričitom nalogu na **s010 i s010b**. Original i istorijska mapa imaju **21 slajd**; projekcija i A4 beleške sada imaju po **22 strane**. Redosled je s001–s010 → s010b → s011–s021; nijedan postojeći ID nije prenumerisan ili izostavljen. Tema je zamrznuta **etf-v1**, stil **B**; fontovi i autorstvo ostaju očuvani.

[Stvarni nalog](odluke.md), [odobrenje podele](odobrenje_podela.json) i [mapa podele](mapa_podele_s010.json) povezuju oba dela sa originalom. To odobrava konkretnu doradu i podelu; nije prihvatanje cele prezentacije 03. Za ovu isporuku nema otvorenih stručnih pitanja.

## Sadržaj, raspored i dijagrami

| Slajd | Završena dorada |
|---|---|
| s004 | Tekst vernije prati original: istovrsna kola u pakovanju, početna tri čipa, neiskorišćeni ulazi i posledice, smanjenje broja čipova uz dozvoljeno veće kašnjenje. Ostaje ranije odobreno **I3 = kaskada dva I2**. Tačan NI invertorski slučaj ponovo je vidljiv kao zasebna tvrdnja. |
| s007 | Vraćena napomena o oznakama **unutar komponente** i njihovoj neophodnosti pri tumačenju zadatka/ispita. Objašnjena standardna indeksacija selektora i izlaza. |
| s008 | Vidljiva svrha CS pri pravljenju većih mreža, aktivna jedinica, neaktivna nula i I uslov svih CS ulaza. |
| s009 | Precrtana piramidalna šema **4/16**: lokalne i globalne oznake, razdvojeni vodovi, tačke samo na grananjima. Vraćen tekst o težinama, alternativnom rasporedu selektora, proširenju i nazivu strukture; sve ostaje na jednoj strani. |
| s010 | Načelo matričnog dekodovanja i kompletna šema vrste/kolone i izdvojenog izlaznog dekodera. Pomoćni blokovi imaju lokalne S1/S0, globalne S5/S4 odnosno S3/S2, oba CS uslova i globalne indekse izlaza. |
| s010b | Poređenje **18 prema 21 komponenti**, dva prema tri nivoa, prednost pri većem broju izlaza, potrebne komponente sa više CS ulaza i mogućnost kombinovanja struktura. |

Zapis „4/6“ u korisnikovoj poruci odnosi se na šemu originalnog s009, koja jasno prikazuje **4/16**. Dijagram nije promenjen u novu funkciju.

Lokalni izvor `dekoder_jezgro.tex` dobio je parametre za geometriju s007/s008, uz očuvane veličine slova. Vodovi su odmaknuti od invertora, a okvir od tela kola. Podrazumevani prikaz s005 ostao je pikselno jednak prethodnom. Zamrznuta tema i alati nisu menjani.

Jezički su popravljene očigledne greške originalnog s010: „tru“ → „tri“, „prikazan smo jedan“ → „prikazan je jedan“, „sturkture“ → „strukture“, „kao su“ → „kada su“ i „komponenet“ → „komponente“. Formulacije su potom prilagođene rasporedu. Ranije odobrene stručne odluke ostaju u [odlukama](odluke.md).

## Beleške i pokrivenost

[Inventar](inventar.json) i [mapa pokrivenosti](pokrivenost.md) imaju **92/92 potvrđena elementa**: 71 izvornu grupu, 20 dopuna i jedan nastavak postojeće dopune. Pri podeli e03/e04 originalnog s010 prelaze u s010b; detalji d01 raspoređeni su prema celinama i evidentirani u [mapi podele](mapa_podele_s010.json). Sve logičke celine ostaju vidljive kroz odobrena dva dela.

Beleške s004 pojašnjavaju brojanje raspoloživih kola i kritičnu putanju; s007 praćenje priključaka i indeksiranje; s008 izvođenje CS uslova; s009 globalni indeks i kaskadu. Beleške s010 objašnjavaju i/j/k, primer izlaza 39, matrična ukrštanja i lokalna imena ulaza; s010b poređenje pomoćnih blokova i kašnjenja. Ne prepisuju vraćene pasuse bez potrebe i ne sadrže istoriju dorade ili odobrenja. Poreklo, nevidljiva sidra i dokazi su u [evidenciji beležaka](evidencija_beleski.json).

## Pregled i provere

Stvarno su pregledani originalni i prethodni prikazi pet pogođenih originala, šest konačnih slajdova i svih šest A4 blokova. Provereni su priključci, polariteti, veze, tačke spojeva, indeksi izlaza, formule, veličina oznaka i razmaci. Nema preklapanja, odsecanja ili nedostajućeg nastavnog sadržaja.

Ostalih **16 projekcionih slajdova** pikselno je isto prethodnoj isporuci. Njihovi lokalni izvori slajdova/beležaka i pokrivenost nepromenjeni su; nastavni sadržaj celih A4 strana identičan je. Kod kasnijih beležaka menja se samo broj strane u podnožju. Dokaz je u [poređenju dorade](poredjenje_dorade_s004_s010.json). Ranije sadržinske potvrde sačuvane su uz taj dokaz; pogođene su obnovljene tek nakon pregleda. [Potvrde](pregled.json) vezane su za aktuelne izvore i prikaze.

Sve komande završene su kodom **0**:

```bash
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije notes
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije review
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije check
```

`check`: **PROVERENO**, uključujući postojeće računske provere dekodera/MUX-a i svih 65536 stanja proširenog kodera. Dodatno je provereno 32 slučaja piramidalnog 4/16 i 256 slučajeva matričnog 6/64 sa svim CS stanjima. Završni logovi oba PDF-a nemaju greške, upozorenja, prekoračenja prostora, nerešene reference ili nedostajuće znakove. Izvorna mapa, originalni PDF i tema ostaju neizmenjeni.

[Notes log](../../build/redizajn/dorada-s004-s010-2026-10-09/notes.log), [review log](../../build/redizajn/dorada-s004-s010-2026-10-09/review.log), [check log](../../build/redizajn/dorada-s004-s010-2026-10-09/check.log).

## Isporuka i otisci

- [Prezentacija — 22 slajda](../../build/03_kola_srednjeg_stepena_integracije.pdf)
- [PDF beležaka — 22 A4 strane](../../build/03_kola_srednjeg_stepena_integracije_beleske.pdf)
- [Uporedni pregled](../../build/redizajn/pregled/index.html#03-s004)
- [Prikaz neposredno pre ove dorade](../../build/redizajn/pre-dorade-s004-s010-2026-10-09/pregled/index.html)
- [Prethodni izveštaj](istorija/pre-dorade-s004-s010-2026-10-09/izvestaj.md) i [arhiva izvora/evidencije](istorija/pre-dorade-s004-s010-2026-10-09/izvori-i-evidencija.tar.gz)

Izlazi u `build/` ne verzionišu se; navedene komande obnavljaju ih iz izvora.

| Resurs | SHA-256 |
|---|---|
| Originalni PDF | `5e68d267ca2f60c1ccdf073c2579fd64a4b05278955cc3d3f920cc54e123fd86` |
| Izvorna mapa | `a3effdb79779d04df05ce98ece642a6068684e4b798018cc96122479136266cc` |
| Manifest redizajna | `72850e06c0f56c19b48e63cecbeafc78c51b42541927ec56d951ceae9ba513ea` |
| Zapis izgradnje | `2ee61f085ed8053c903313d9b233e7f981199191891e10b822f22e3452fa534f` |
| Potvrde pregleda | `b524195631abf614e89bc195c283afc121eca314e218225fd612d79779fff456` |
| Pokrivenost | `f08f8f4ad660387fb1ec2a04af134634ad197b3a98df3e4c736a856e1c388054` |
| Evidencija beležaka | `7134a9d0a9161f183323c8b96b0499c2f20a8e3c8a31fac9725fb9b1b9c8d64f` |
| Prezentacioni PDF | `fe62c56904db93ac2c5a7077b45258104f30626552e1bed6ad4a0f46490d8d0e` |
| PDF beležaka | `8515375ce38c61fb8f2616abf3a946a8755398ba2b37ee47d2fa506b57f1be18` |
| Dokaz poređenja | `79a98110c7990ef1aef7698be4fcdcb52097cb95a9041aff1d336a13578f7e6f` |
| Manifest teme | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |

## Nastavak

Tražena dorada je završena. Sledeći korak je korisnikov pregled ove verzije 03; status je `ceka_odobrenje`. Korisnik još nije prihvatio celu prezentaciju 03. Ranije dozvole za druga predavanja ostaju zasebne odluke i nisu predmet ove dorade. Novi agent prvo proverava navedene otiske i postojeće potvrde; završenu analizu nepromenjenih izvora ne ponavlja.
