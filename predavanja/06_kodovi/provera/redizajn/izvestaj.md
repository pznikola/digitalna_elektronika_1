# Predavanje 06 — Kodovi: redizajn i beleške

Datum: 2026-10-02. Status: **u_radu**. Izgled i beleške obrađeni su za svih 30 slajdova; osam grupa izvornih stručnih pitanja zahteva korisnikovu odluku. Predavanje zato nije spremno za završno prihvatanje.

## Isporuka

- [Prezentacija — 30 slajdova](../../build/06_kodovi.pdf).
- [Beleške za predavača — 30 A4 strana](../../build/06_kodovi_beleske.pdf).
- [Original / početni prikaz / novi slajd / beleške](../../build/redizajn/pregled/index.html).
- [Otvorena pitanja: konkretni predlozi i dokazi](otvorena_pitanja.md).
- [Mapa pokrivenosti](pokrivenost.md), [potvrde pregleda](pregled.json), [poreklo i dokazi beležaka](evidencija_beleski.json).

## Obuhvat i očuvanje

Pročitani su PLAN_PREDAVANJA.md, svih 15 strana originalnog PDF-a i svih 30 izdvojenih slajdova, glavni LaTeX izvor, pojedinačni slajdovi, uključene tabele i TikZ crteži, postojeće računske provere i početni kompajlirani prikaz. Vizuelno su upoređeni original, početni prikaz, novi slajd i beleške svakog ID-ja u punoj veličini.

Ostaju tačno **30 slajdova, redosled 06-s001 → 06-s030 i svi stabilni ID-jevi**. Nema brisanja, spajanja, deljenja, dodatnih razdelnika ni overlay strana. Originalni PDF i istorijska mapa/provere rekonstrukcije nisu menjani. Autor ostaje prof. dr Lazar Saranovac, godina 2021/22. Tema je konkretna verzija `etf-v1`, stil B; naglašavanje je tamnocrveno #A32638.

Nezavisni inventar sadrži **127 elemenata: 98 izvornih i 29 nastavnih dopuna**. Svih 127 ima provereno odredište u slajdu ili beleškama istog ID-ja. Pokrivenost potvrđuje da sadržaj nije izgubljen, a ne ispravnost spornih izvornih zapisa; njihove kategorije ostaju `problem`.

## Promene izgleda

Ujednačeni su naslovi, podnožje, margine, raspored i naglašavanje prema odobrenom izgledu 01. Tabele su centrirane, zaglavlja razdvojena od tela i sadržaj organizovan po logičkim grupama. Osnovni tekst zadržava postojeći font; na gustim slajdovima koristi se lokalnih 10 pt, oznake crteža najmanje 9 pt. Nije smanjivan ceo slajd.

Očuvane su sve ASCII ćelije, sve BCD kodne reči i međurezultati, svi koraci konverzija, posebne vrednosti pokretnog zareza i tabela zaokruživanja, posebni kodovi, oba Grejova ciklusa, tabele parnosti, kompletan CRC primer i obe Hemingove matrice. Sporne izvorne vrednosti ostaju predmet zasebnog odobrenja.

Uređivi crteži i tabele:

- s003: kompletna ASCII tabela, sedam bita zaglavlja i strelice, odvojena bočna objašnjenja.
- s004: četiri BCD koda sa preglednom oznakom autokomplementarnosti.
- s009–s011: sve postojeće vrste konverzije, jasna crvena korekcija i prenos.
- s018/s019: četiri nezavisna kanala, svi signali i kašnjenja; strelice trajanja ispod tragova, odvojene oznake. Sačuvani događaji, redosled i šest očitavanja.
- s020: obe Karnove karte, puna putanja 0–15 i BCD putanja 0–9, dosledni matematički indeksi.
- s021: poravnati redovi XOR prikaza i oba stupca konverzije.
- s024: uklonjena duga strelica kroz tekst; ostatak i poništavanje povezani crvenim naglašavanjem. Identitet množenja i rezultat ostaju vidljivi, sva tri međureda su u beleškama.
- s025: sve vrste deljenja i alternativni prijemni biti u zagradama, vrhovi strelica pomereni van cifara.
- s028/s029: kompletne matrice sa poravnatim kolonama i oznakama; sporna oznaka na poziciji 13 nije prećutno ispravljena.

Predavanje 06 nema šeme sa tranzistorima ili logičkim kapijama.

| Primer | Pre | Posle | Promena |
|---|---|---|---|
| s003 | [Početni prikaz](../../build/redizajn/pregled/pre/p-03.png) | [Novi prikaz](../../build/redizajn/pregled/novi/p-03.png) | Puna ASCII tabela i bočna objašnjenja |
| s018 | [Početni prikaz](../../build/redizajn/pregled/pre/p-18.png) | [Novi prikaz](../../build/redizajn/pregled/novi/p-18.png) | Kompaktni kanali, odvojene strelice kašnjenja |
| s024 | [Početni prikaz](../../build/redizajn/pregled/pre/p-24.png) | [Novi prikaz](../../build/redizajn/pregled/novi/p-24.png) | Pregledno deljenje i množenje, detalji u beleškama |
| s025 | [Početni prikaz](../../build/redizajn/pregled/pre/p-25.png) | [Novi prikaz](../../build/redizajn/pregled/novi/p-25.png) | Strelice ne prekrivaju cifre |

## Beleške i preneti detalji

Svaki slajd ima `beleske/sNNN.tex`, vezu sa ID-jem i nevidljiva sidra sadržaja. Naslovni s001 ima samo vezu sa ID-jem; ostalih 29 fajlova sadrži dodatno nastavno objašnjenje. Beleške nemaju istoriju redizajna, poređenja, rezultate provera, korisnikove odluke, otvorene predloge ni oznake PDF porekla. Te informacije nalaze se isključivo u evidenciji.

| Slajd | Preneti izvorni detalji | Šta ostaje vidljivo |
|---|---|---|
| s002 | Potpuna programska napomena o proveri prekoračenja i akciji | Četiri zastavice, nazivi registara i ključna programska poruka |
| s003 | Pun naziv ISO i kontekst kodovanja znakova | 128 ćelija, ASCII/ANSI nazivi, primeri, Windows-1252, UTF-8, ISO 8859 |
| s005 | Potpuni postupak izdvajanja cifara količnikom i ostatkom | Sabiranje 59 i 13, svi redovi i korekcija |
| s008 | Svih osam koraka opisano rečima | Osam prefiksa, vrednosti i operacija, potpuna Hornerova formula |
| s022 | Fizički uzroci grešaka i redundantna zaštita | Ključna tvrdnja, puna tabela parnosti i svojstva detekcije |
| s024 | Sva tri sabirka množenja i pojedinačna poništavanja | Poruka, generator, količnik, ostatak, kodna reč, identitet i poništavanje |

Dopune objašnjavaju BCD prenose i korekcije 6/3, raspored binarnog zareza, subnormalne vrednosti, zaokruživanje negativnih brojeva, kašnjenja kanala, Grejove cikluse, CRC međukorake i značenje parnosti/sindroma/rastojanja. Proverene su nezavisnim računicama i sadržinskim pregledom; preneti detalji nisu zamenjeni kratkim rezimeima.

## Ispravke i otvorena pitanja

Jezičke dorade: s002 slaganje „predstavljene“ i „komplementu“; s005 „kako“ umesto „kao“; s008 „sa leve strane nadesno“; s022 „Bit parnosti“; s026 „rastojanje“ i „Hemingovo“ umesto pogrešnog zapisa; s027 „zaštititi“. Ujednačena su velika/mala slova i matematički indeksi bez promene značenja. „Generator polynomial“ preformulisan je kao „generator polinom“.

**Osam grupa odluka** odnosi se na s007, s013, s014, s016, s019, s021, s028 i s029. Precizni predlozi, kontraprimeri i izvor za format pokretnog zareza nalaze se u [otvorena_pitanja.md](otvorena_pitanja.md). Odobrenje stručnih ispravki još nije primljeno. Zato su 22 ID-ja potpuno potvrđena, a na osam ID-jeva ostaje deset kategorija `problem`. Sve ostale kategorije i dokazi pregleda ažurni su.

## Dokazi provere

```sh
make -C predavanja all LECTURE=06_kodovi
make -C predavanja notes LECTURE=06_kodovi
make -C predavanja review LECTURE=06_kodovi
make -C predavanja check LECTURE=06_kodovi
```

`all`, `notes` i `review` prolaze. Prezentacioni PDF ima 30 strana 16:9, PDF beležaka 30 A4 strana. Konačni LaTeX logovi nemaju greške, `Overfull`, nedostajuće znakove ni upozorenja. Izgradnja ostaje LuaLaTeX, postojeći latexmk sistem i `-no-shell-escape`.

Računske provere prolaze: postojeća provera ASCII/BCD/FPF/Grejovih/paritetnih tabela, CRC svih međurezultata i Hemingovog koda, plus nezavisna provera svih 256 bajtova konverzije, svih 256 CRC poruka, 14 CRC međurezultata u beleškama, tri sabirka polinomskog množenja, šest vremenskih očitavanja i nastavnih numeričkih dopuna. Ulazni `provera_logike.py` poziva novu proveru beležaka koja uključuje postojeće provere. Dokazi **ne potvrđuju sporne originalne zapise**.

`check` vraća **NEZAVRŠENO**, isključivo za deset kategorija na osam spornih ID-jeva. Nema greške broja/redosleda/ID-jeva, izostavljenog sadržaja, pogrešnog ID-ja beležaka, nedostajućeg resursa, pokrivenosti, zastarele potvrde ili kompilacije. Sačuvani stvarni izlazi: [all](kompilacija.txt), [notes](kompilacija_beleski.txt), [review](uporedni_pregled.txt), [check](provera.txt), [računske provere](racunske_provere.txt).

## Početni prikaz i oporavak teme

Početni prikaz sačuvan je pre promena. [Arhiva](pocetni_prikaz.tar.gz) sadrži svih 94 fajla snapshot-a; svaki je provereno bajtno identičan lokalnom početnom prikazu. Ne inicijalizovati predavanje ponovo.

Na početku je zajednički `etf-v1/manifest.json` već sadržao Markdown umesto JSON-a i sprečavao izgradnju. Sačuvan je [oštećeni sadržaj](osteceni_manifest_teme.txt). Obnovljen je **bajtno isti odobreni manifest**, SHA-256 `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41`, koristeći arhivsku strukturu i proverene postojeće izvore. Nije menjan izgled niti izvor teme. Detalji su u [odluke.md](odluke.md); početni snapshot nije menjan.

## Nastavak i odobrenja

Korisnikov nalog za početak 06 sačuvan je u [odluke.md](odluke.md). On ne prihvata rezultat 05 niti njegove stručne ispravke. Nema odobrenja rezultata 06 ni dozvole za 07.

Sledeći korak: korisnikova odluka o osam grupa predloga. Primeniti samo odobrene ispravke, uskladiti beleške i računska očekivanja, pregledati pogođene prikaze i obnoviti potvrde, zatim pokrenuti `notes`, `review`, `check`. Nepromenjene potvrđene delove ne analizirati iznova. Kada nema sadržinskih problema i `check` prođe, predati završni rezultat sa statusom `ceka_odobrenje`. Prihvatanje predavanja i početak 07 evidentiraju se odvojeno.

## Otisci pregledane kontrolne tačke

- `predavanja/06 Kodovi.pdf`: `2f25c024f135c19deef55c9ebae2f7995d3e8c87e68945b4e3073a96d3210148`.
- `predavanja/_zajednicko/etf-v1/manifest.json`: `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41`.
- `predavanja/06_kodovi/provera/redizajn/manifest.json`: `2d4e913e7da1c80ce981a33a75a61312bf9edae61e8672389132b7f6c5115e47`.
- `predavanja/06_kodovi/provera/redizajn/izgradnja.json`: `e172ff209a397bb609c43aca10af08012803a9c50d79c5779ff637372e500bc7`.
- `predavanja/06_kodovi/build/redizajn/pre/snapshot.json`: `9dafe0439ffd7afe5b266f953bcd46ba7cdc6aba097605344e245c82336c453f`.
- `predavanja/06_kodovi/provera/redizajn/pocetni_prikaz.tar.gz`: `87ab6f6068a84cdccf092d4f47debd214f17abf1873191645355ca0b8f803031`.
- `predavanja/06_kodovi/build/06_kodovi.pdf`: `abaec2760cac960fdeea1e17c05766275f76933d9739082f32fee2ba6b28c26d`.
- `predavanja/06_kodovi/build/06_kodovi_beleske.pdf`: `b3900a751d9b1144c2dbcef256801cc4dce83de10245a97a8315c7e64a9c2e78`.
- `predavanja/06_kodovi/provera/redizajn/inventar.json`: `5b7303457c62bc3367d811464031eb58b1e220c1052c7da9b4d8f996cf68495b`.
- `predavanja/06_kodovi/provera/redizajn/pokrivenost.json`: `eae8291af7d85454825c5759bee0a72b4d9148e038ad0f19a870d635c28e0c9b`.
- `predavanja/06_kodovi/provera/redizajn/pregled.json`: `d48305c846bb161d6406024e7f71d67d45363d485900a596d51fcc7959804f03`.
- `predavanja/06_kodovi/build/redizajn/pregled/otisci.json`: `9c3f8b070e1a9f689db7a2352251dd0f57883d87c76dca5ab65e27897215941e`.
