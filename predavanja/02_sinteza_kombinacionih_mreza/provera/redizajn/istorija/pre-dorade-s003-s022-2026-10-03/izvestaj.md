# Predavanje 02 — dorada slajdova i beležaka

**Status: `ceka_odobrenje` · datum: 2026-10-03.** Primenjene su sve dorade iz poslednjeg korisnikovog naloga: s002, s003, s004, s005, s006, s008, s009, s011, s012 i s013, uz pripadajuće beleške. Pročitani su plan, izvori, originalni slajdovi u punoj veličini i prethodna isporuka. Predavanje nema otvorenih stručnih pitanja; završni rezultat još nije odobren.

## Broj, redosled i odobrena podela

Originalni PDF ostaje neizmenjen: 27 strana sa 54 izvorna slajda. Korisnik je izričito tražio da se originalni s002 i s009 podele na po dve smislene celine. Zato novi prezentacioni PDF ima **56 strana**; A4 PDF ima **56 blokova i 56 strana**, sa po jednim odgovarajućim slajdom, ID-jem, naslovom i beleškama.

Prvi delovi zadržavaju oznake `02-s002` i `02-s009`; nastavci su `02-s002b` i `02-s009b`, odmah iza svojih prvih delova. Ostalih 52 originalnih ID-ja nije promenjeno niti izostavljeno. S003 i dalje znači izvorni s003, iako je sada na četvrtoj PDF strani. Isto važi za sve kasnije reference korisnika.

[Odobrenje podele](odobrenje_podela.json) čuva relevantne korisnikove rečenice i tačna dva ID-ja; njegov otisak je pinovan u [manifestu](manifest.json). [Mapa podele](mapa_podela.json) povezuje grupe prethodnog inventara sa novim odredištima. Istorijska `provera/mapa.json`, katalog i početni prikaz sa 54 slajda ostaju neizmenjeni. Izuzetak je unet u odeljak 1.1 plana; ne odobrava druge podele, overlay-e ili izostavljanje nastavnog sadržaja. Originalnih slajdova u celom katalogu ostaje 620, a projektovanih strana uz ovaj izuzetak 622.

Tema ostaje zamrznuta `etf-v1`, stil B, LuaLaTeX i 16:9. Autorstvo prof. dr Lazara Saranovca, Katedra za elektroniku i školska godina 2021/22 očuvani su. Fontovi ostaju postojeći; lokalna tamnocrvena služi isticanju izvornog gradiva. Ne predstavlja se kao zvanična ETF paleta.

## Izmene i poređenje sa prethodnom isporukom

| Izvorni slajd | Dorada |
|---|---|
| s002 → s002/s002b | Vraćen tok originalnih pitanja o vremenu ulaza i značenju „trenutnog“. Prvi deo sadrži ceo traženi uvod, definiciju i fizičko tumačenje trenutka. Drugi deo sadrži ostatak: pitanje o promenama, nepoznat prelazni izlaz, zašto i kašnjenje kola. Naglasci originala su vidljivi. Beleške odvojeno objašnjavaju apstraktni opis i ograničenja funkcionalne tabele. |
| s003 | Veći razmak gornjih i donjih dijagrama na obe strane. Odvojene oznake širina ulaznog i izlaznog impulsa `T_ul`/`T_izl`, bez prelaska preko signala. Beleške daju račun oba vremena prelaza i širine, uz uslov da se obe promene prenesu. |
| s004 | Istaknuto „nekih“. Leva kolona je šira: cela rečenica o pojednostavljenju staje u jedan red. Desni dijagram je uži i pomeren udesno, bez smanjivanja fonta oznaka. Umesto kratke oznake ishoda stoje pitanje, mogućnost promene oblika/trajanja ili izostanka impulsa i zavisnost od trajanja prema kašnjenjima. |
| s005 | Dijagram levo, šira tekstualna kolona desno. Dodate razdvojene strelice „Sigurno 0“ i „Sigurno 1“ na završecima maksimalnih intervala; šrafure ostaju. Naglašeni maksimum, sigurno stanje, promenljivost stvarnog kašnjenja, tip kola i svi primerci. |
| s006 | Vraćena izvorna najava posebne pažnje lažnim nulama i jedinicama u sintezi. Beleške objašnjavaju prelaznu kombinaciju međusignala i potrebu provere privremenih stanja. |
| s008 | Tri rečenice su u zasebnim redovima. SSI ima puni naziv Small Scale Integration. Korak pinova 2.54 je centriran i pomeren ispod kote; oznaka visine 2.54 pomerena je udesno. Sačuvane veze, tip i simetrični ulazi četiri I kola, fotografija, sve dimenzije i jedinice. Ekonomski faktor ostaje vidljiv, a numerički primer u beleškama. |
| s009 → s009/s009b | Prema originalu napravljene dve celine bez kolona: literal, proizvod/zbir i normalni/potpuni članovi; zatim indeksi članova i SOP/POS oblici. Svi originalni pojmovi i primeri ostaju pokriveni. Beleške nude dodatne primere i obrazloženje pravila indeksiranja. |
| s011 | Uvodni zahtev i numerisana sva tri uslova, uključujući tri ulaza i jedan izlaz. Funkcionalna tabela dobija blage horizontalne linije. Beleške potpuno razrađuju dodelu C/B/A/F, pozitivnu logiku i formiranje tabele prema zahtevima. |
| s012 | Vraćeno pravilo o svim mogućim vrednostima ulaza i skraćenoj formi. Jasno uveden isti sistem sa drugačijim zahtevom. Istaknuti `b`, „bilo šta“ i `X`; četiri reda tabele su razdvojena blagim linijama. Beleške proveravaju svih osam kombinacija. |
| s013 | Vraćen uvod o pisanju logičke funkcije iz funkcionalne tabele. Uklonjena oznaka „Tri reda sa jedinicom“; formule, označeni redovi i I/ILI veze ostaju. Potpuni uslovi rečima i obrazloženje minterma ostaju u beleškama. |

Precrtani/dorađeni vektorski izvori u ovom ciklusu: `s003_bez_kasnjenja.tex`, `s003_sa_kasnjenjem.tex`, `s004_kratak_impuls.tex`, `s005_maksimalna_kasnjenja.tex` i `s008_dip14_dimenzije.tex`. Tabele: `s011_funkcionalna_tabela.tex`, `s012_skracena_tabela.tex`. Nije promenjena funkcija kola ili vrednost u tabeli.

Reprezentativna poređenja originala, početnog LaTeX-a i nove isporuke: [s002](../../build/redizajn/pregled/index.html#02-s002), [s002b](../../build/redizajn/pregled/index.html#02-s002b), [s003](../../build/redizajn/pregled/index.html#02-s003), [s005](../../build/redizajn/pregled/index.html#02-s005), [s008](../../build/redizajn/pregled/index.html#02-s008), [s009b](../../build/redizajn/pregled/index.html#02-s009b) i [s011](../../build/redizajn/pregled/index.html#02-s011). Oba dela podele prikazuju isti odgovarajući original i početni slajd. Neposredno prethodna isporuka dokumentovana je u [arhiviranom izveštaju](istorija/pre-dorade-slajdova-2026-10-03/izvestaj.md); njeni izvori i potvrde su u `izvori-i-evidencija.tar.gz` u istom folderu.

## Beleške i pokrivenost

Potvrđeno je **210/210 elemenata: 155 izvornih grupa i 55 dopuna**. Broj grupa je porastao sa 205 zbog razlaganja ranijih složenih grupa s002, izdvajanja njegovog izvornog pitanja, evidentiranja uvoda s013 i dva zasebna dopunska bloka nastavaka. Podela nije gubitak izvornih elemenata: veze sa ranijim inventarom proverene su u `mapa_podela.json`. Pokrivenost svakog originala proverava se kroz odobrene delove i njihove beleške zajedno.

Ukupno **115 elemenata** ima odredište u beleškama. [Mapa](pokrivenost.md), [inventar](inventar.json), [uređiva pokrivenost](pokrivenost.json) i [poreklo/dokazi beležaka](evidencija_beleski.json) navode konkretne lokacije i nevidljiva sidra. Ne vode drugu kopiju nastavnog teksta. Sve što je sada vraćeno na s002 i s009 ostaje vidljivo u odgovarajućem delu; beleške ga nepotrebno ne prepisuju. Detalji formiranja funkcionalne tabele dopunjeni su u s011, a račun širine impulsa u s003. Ostali izvorni detalji i postojeće dopune ostaju sa svojim ID-jevima.

S001 zadržava samo vezu na ID i nevidljivo sidro, bez veštačkog popunjavanja. Ostalih 55 fajlova sadrži dodatno nastavno objašnjenje. Beleške nemaju uredničke naslove, poreklo PDF strana, istoriju redizajna, korisnikove odluke ili zahteve za odobrenje. Na projektovanim slajdovima ostaje nastavni sadržaj. Dokumentacija odluka je odvojena u `provera/redizajn/`.

## Pregled i provere

Pojedinačno su pregledani originali svih deset traženih ID-jeva, svih 12 novih projektovanih prikaza i njihovih 12 punih A4 strana (uključujući oba nastavka). Pročitani su odgovarajući izvori i beleške; provereni značenje formula, granice vremenskih intervala, spojevi i oznake, redovi tabela, potpunost, upotrebljivost za predavača i odsustvo nepotrebnog ponavljanja.

Za ostala **44 ID-ja** sačuvan je stvarni prethodni sadržinski i vizuelni pregled. [Dokaz poređenja](poredjenje_nepogodjenih.json) potvrđuje da su projektovani prikazi i cela tela A4 strana pikselno identični neposredno prethodnoj isporuci. U A4 podnožju menja se samo broj fizičke strane. Provereni su novi izlazni redosled i veza sa istim ID-jem; te celine nisu ponovo sadržinski redizajnirane. Svih 56 potvrda u [pregled.json](pregled.json) vezano je za aktuelne izvore, prikaze, mapiranje i alate. Izmenjena numeracija nije zamena za identitet slajda.

Izvršene komande:

```bash
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza notes
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza review
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza check
make -C predavanja test
make -C predavanja test-redizajn
```

Završni `check`: **PROVERENO**, izlazni kod 0. Njime su ponovo izgrađena oba konačna PDF-a i uporedni pregled. Kompilacija nema upozorenja, `Overfull`, `Underfull`, nedostajućih znakova ili grešaka. Struktura, odobrenje podele, ID-jevi, 56 prezentacionih strana, 56 A4 blokova, svi resursi, svih 210 elemenata i svih 56 potvrda prolaze. `git diff --check` prolazi.

Računska provera postojeće tabele, SOP/POS, konsenzusa i oba gliča prolazi bez izmene koda. Račun T_izl dodatno je algebarski proveren; uslov prenosa obe promene izričito je naveden. Indeks 3 za proizvod i zbir proverava se za CBA=011. Nova horizontalna razgraničenja ne menjaju nijednu tabelarnu vrednost.

Prošlo je **40 regresionih testova** i integracioni primer redizajna. Dodati slučajevi potvrđuju očuvanje originalne mape i lokacija, eksplicitno odobren nastavak, tačan redosled, broj strana, odvojene beleške, odbijanje nedostajućeg/promenjenog odobrenja, neodobrene druge celine, pogrešne putanje i promene izvorne strukture. Stari režim bez podele ostaje strogo 1:1. Alati čitaju prošireni niz iz manifesta; ne prepisuju istorijske potvrde. Promena zajedničkog alata poništava ranije otiske korišćenih alata u drugim predavanjima, pa njihov naredni `check` traži obnovu zavisnosti/pogođenih potvrda prema planu; njihovi izvori i potvrde ovim radom nisu menjani.

Logovi: [notes](../../build/redizajn/dorada-2026-10-03/notes.log), [konačni review](../../build/redizajn/dorada-2026-10-03/review.log), [konačni check](../../build/redizajn/dorada-2026-10-03/check.log), [regresije](../../build/redizajn/dorada-2026-10-03/test.log), [integracioni primer](../../build/redizajn/dorada-2026-10-03/test-redizajn.log). Komanda notes je korišćena tokom dorade; konačne prikaze dodatno potvrđuju završni review/check.

## Jezičke i stručne odluke

Jezički su uređeni interpunkcija pitanja, „100ms“ → „100 ms“, formulacija stvarnog vremenskog intervala, „Trajanje signala PREMA kašnjenjima“ → čitljiva rečenica o odnosu trajanja ulaznog impulsa i kašnjenja, te uvodi s011–s013. Na s012 jasno stoji tri ulaza i jedan izlaz, u skladu sa prethodnim primerom. SSI i definicija gejta imaju odvojene redove, bez novih uredničkih komentara.

Ranije stručne odluke za s022, s029, s034, s040 i s052/s053 ostaju primenjene i nepromenjene. Ovaj nalog odobrava navedene dorade i tačno dve podele; ne predstavlja prihvatanje cele isporuke. **Nema otvorenih stručnih pitanja za 02.**

## Isporuka i sledeći korak

- [Prezentacija — 56 slajdova](../../build/02_sinteza_kombinacionih_mreza.pdf).
- [Slajdovi sa beleškama — 56 A4 strana](../../build/02_sinteza_kombinacionih_mreza_beleske.pdf).
- [Uporedni pregled sa beleškama](../../build/redizajn/pregled/index.html).

Generisani PDF/PNG/HTML i logovi ostaju u `build/` i ne verzionišu se. Izvori, istorijska arhiva, izveštaj i potvrde ostaju izvan `build/`. Ponovna izgradnja koristi navedene komande sa obaveznim `LECTURE`. Prethodni PDF-ovi za poređenje sačuvani su u `build/redizajn/pre-dorada-2026-10-03/`.

Sledeći korak: korisnikov pregled i prihvatanje **ove verzije slajdova i beležaka 02**. Status `ceka_odobrenje`; agent ne daje sebi odobrenje. Prethodna dozvola za početak 03 ostaje zasebna odluka. Ovaj ciklus ne obrađuje druga predavanja. Novi agent proverava aktuelne otiske i nastavlja od ovog izveštaja; važeća analiza se ne ponavlja bez relevantne promene.

## Pregledani otisci SHA-256

| Resurs | Otisak |
|---|---|
| Originalni PDF | `f631914c9f32a0472f4fa3af11115abaadb9316dfcf6f1528cd91ef4d28868f4` |
| Istorijska izvorna mapa | `b2c8e07fa123a40da68c8b89b1b1c6ce88112e90c7417792cdec341d60136ca2` |
| Manifest redizajna | `88c2997b375cbd09dbf6a2df838893b8c792a1dcb6ee706b4afbebf6a109bfc6` |
| Odobrenje podele | `91b1d17866e4bb3252738a0280d881bf91e7739e62bbcd6e46702a97e238f8a4` |
| Mapa podele | `6ac84a1d9ab15b1bee35af22ea21bb29195fe075bc3795156dfcd1b501ea47fa` |
| Prezentacioni PDF | `0e26aaa7e4bdefe06902fd825cbe3816ee80e703e42bb08480110c9a33d41a6b` |
| PDF beležaka | `cb24a32b035f9c8180384687d3175d2f722b36a1304a34a1eabca779ac3204ca` |
| Evidencija beležaka | `78883f596eb1d4118090656ed0e66920d9b64fe34accfc3f9bd168fd491247c2` |
| Potvrde pregleda | `84e086efbbd0b12c358214f5b0e2c1945856a432a73d473f8fdfd6beb7ea055d` |
| Arhiva prethodne isporuke | `91766c16f75f39d7d1baeaf6d9d70d9e9a19f586350de772bb2241d6ce32eb47` |
| Manifest teme etf-v1 | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |
