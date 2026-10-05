# Predavanje 02 — dorada beležaka za predavača

**Status: `ceka_odobrenje` · datum: 2026-10-02.** Po nalogu korisnika pročitani su aktuelni `PLAN_PREDAVANJA.md`, svi izvori i prikazi prezentacije 02 i svih 27 strana originalnog PDF-a (54 gornja/donja slajda). Napisane su nove beleške prema pravilima koraka 6; svih 54 A4 prikaza pregledano je pojedinačno.

Ovaj ciklus obuhvata samo beleške 02. Izvori slajdova, šema, tabela, koda, glavni izvor prezentacije, originalni PDF i zamrznuta tema `etf-v1` nisu menjani. Njihovi početni otisci provereni su posle rada. **Prezentacioni PDF je identičan prethodnoj isporuci:** 54 slajda, nepromenjen redosled i stabilni ID-jevi `02-s001`–`02-s054`, bez novih strana ili overlay-a. Autorstvo i školska godina su očuvani.

## Isporuka i prethodno stanje

- [PDF slajdova sa beleškama — 54 A4 strane](../../build/02_sinteza_kombinacionih_mreza_beleske.pdf).
- [Nepromenjeni prezentacioni PDF — 54 strane](../../build/02_sinteza_kombinacionih_mreza.pdf).
- [Uporedni pregled original / polazni LaTeX / sadašnji slajd / nove beleške](../../build/redizajn/pregled/index.html).
- [Jedini izvori teksta beležaka](../../beleske/), [redosled i strane blokova](../../build/02_sinteza_kombinacionih_mreza_beleske.notes-map.tsv).
- [Mapa pokrivenosti](pokrivenost.md), [precizna odredišta i sidra](pokrivenost.json), [inventar](inventar.json), [pojedinačne potvrde](pregled.json), [poreklo, dopune i računske provere](evidencija_beleski.json).

[Prethodni izveštaj o rasporedu i šemama](istorija/pre-dorade-beleski-2026-10-02/izvestaj.md) i tadašnje potvrde sačuvani su u istom arhivskom folderu. Oni dokumentuju prethodnu isporuku, ali ne potvrđuju nove beleške. Istorijske potvrde rekonstrukcije nisu menjane.

Manifestu su promenjeni samo naslovi blokova beležaka: umesto oznake ID kao naslova, PDF prikazuje stvarni naslov slajda uz ID. Iz istih `beleske/sNNN.tex` izvora gradi se dokument za čitanje; nisu uvedene druge kopije nastavnog teksta.

## Sadržaj novih beležaka

Beleške sada sadrže dodatno nastavno objašnjenje: potpune detalje koji nisu vidljivi na odgovarajućem slajdu, potrebne međukorake i proverljive dopune. Formula ili oznaka kratko se ponavlja kada je potrebna za objašnjenje. Ključne definicije, rezultati, tabele, karte, šeme i uslovi ostaju na slajdovima.

Uklonjeni su vidljivi urednički naslovi, redovi sa lokacijom originala, istorija promena, predlozi, korisnikove odluke i komentari o premeštanju gradiva. Njihova istorijska evidencija preneta je u `editorial_records` tehničkog zapisa; poreklo svakog dodatnog objašnjenja evidentirano je uz isti ID. Nevidljiva sidra `% element: …` i `\BeleskeID` su očuvani.

S001 nema dodatnog nastavnog sadržaja: njegov fajl sadrži samo ID i nevidljivo sidro. Ostala 53 fajla sadrže objašnjenja bez veštačkog ograničenja dužine i bez poruka o nedostatku beležaka.

Reprezentativna poređenja starih i novih beležaka:

| ID | Pre dorade → nova nastavna beleška |
|---|---|
| s002–s006 | Opis slajda i uredničke oznake → tumačenje vremenske odrednice, izlaznih prelaza, širine impulsa i uslova važenja izlaza. |
| s015–s016, s026 | Sažeta najava postupka → svih pet negiranih minterma, potpuni međukoraci i prelaz u POS/NILI zapis. |
| s029–s031 | Napomene o izboru/ispravnosti prikaza → razlika broja kapija i dubine putanje, konkretni kontraprimeri neispravnih kaskada i pravilne zamene troulaznih NI/NILI kola. |
| s034–s044 | Opis karte i istorija oznaka → binarno obrazloženje susedstva, uklanjanje promenljivih i izvođenje svih članova grupa; s044 razrađuje sva tri POS činioca. |
| s046–s049 | Kratki zaključci o čipovima → račun pinova, uloge kapija, 9 NI / 10 NILI kapija i uslovi alternativne realizacije sa dva kućišta. |
| s051–s054 | Uredničko poređenje primera → vremenski međukoraci gliča, potpuni zapis kartirane funkcije, dokaz konsenzusa i ograničenja pri promeni više ulaza. |

Precrtane šeme u ovom ciklusu: **nijedna**; pregled svih šema služio je pisanju i proveri beležaka. Raniji popis precrtanih šema ostaje u arhiviranom izveštaju.

## Pokrivenost po slajdovima

Potvrđeno je **205/205 elemenata: 152 izvorna i 53 dopune**. Odredišta na neizmenjenim slajdovima ostala su očuvana; odredište u beleškama navedeno je samo tamo gde se zaista prenosi dodatni detalj. Dopune imaju zasebno nevidljivo sidro `:d01` u beleškama. Tehnički zapis nije zamena za nastavno odredište.

Tabela navodi obuhvat i poreklo, bez druge kopije teksta beležaka. Puni opisi prenetih izvornih detalja, sidra i dokazi nalaze se u [evidenciji](evidencija_beleski.json).

| Slajd | Preneti detalji — izvorna sidra | Dodatno objašnjenje |
|---|---|---|
| 02-s001 | — | Bez dodatnog sadržaja: samo ID i nevidljivo sidro. |
| 02-s002 | e01, e02, e03 | Vremenska odrednica, idealizacija trenutka i nepoznat prelazni izlaz. |
| 02-s003 | e01 | Smer promene izlaza i vremenske granice impulsa. |
| 02-s004 | e04 | Izvođenje širine izlaznog impulsa i uslov prenošenja obe promene. |
| 02-s005 | e01, e03 | Razlika stvarnog kašnjenja primerka i maksimalne specificirane granice. |
| 02-s006 | — | Sabiranje kašnjenja putanje i prolazne kombinacije međusignala. |
| 02-s007 | — | Razlika broja kapija, ulaza, kućišta i izabranog kriterijuma. |
| 02-s008 | e01, e04 | SSI komponente, orijentacija DIP pinova, mil i numerički primer nabavke. |
| 02-s009 | — | Normalni naspram potpunog člana; primer indeksa proizvoda i zbira. |
| 02-s010 | e02 | Izostavljanje posrednih zapisa i električne razlike ekvivalentnih mreža. |
| 02-s011 | — | Tačno dva naspram najmanje dva ulaza; brojanje kombinacija. |
| 02-s012 | — | Razvijanje skraćenih redova i razlika nebitnog ulaza i neodređenog izlaza. |
| 02-s013 | e01 | Potpuni uslovi rečima i dokaz da minterm izdvaja samo jedan red. |
| 02-s014 | — | Kanonički i nekanonički SOP i broj članova. |
| 02-s015 | e01, e02, e03 | Aktivna nula i svih pet negiranih proizvoda kao međukorak POS izvoda. |
| 02-s016 | e02 | Potpuni De Morganov međukorak negacije pet minterma komplementa. |
| 02-s017 | — | Primer maxterma reda 100 i izdvajanje nule. |
| 02-s018 | — | Primeri minterma i maxterma indeksa 5; značenje logičke sume indeksa. |
| 02-s019 | — | Čitanje tri grane mreže I–ILI i spojeva sabirnica. |
| 02-s020 | — | Brojanje tri neposredna opterećenja izvora A. |
| 02-s021 | — | Uloge dva invertora i različita kašnjenja pravog i komplementnog voda. |
| 02-s022 | — | Provera nultih i jediničnih redova mreže ILI–I. |
| 02-s023 | e03 | Više izlaza, obim brojanja resursa i ograničenje dvonivojskog kašnjenja. |
| 02-s024 | e01, e03 | Dvostruke negacije veza i eksplicitne dualnosti SOP i POS. |
| 02-s025 | e02 | Dvostruka negacija i dvoulazno NI kao invertor. |
| 02-s026 | e02, e04 | Potpuni međukoraci pet zbirova i NILI invertor. |
| 02-s027 | e01 | Očuvan broj resursa, moguća ušteda čipova i kontekst CMOS površine. |
| 02-s028 | — | Četiri identiteta invertora i četiri nivoa petoulaznog lanca. |
| 02-s029 | e02 | Odobreno razjašnjenje četiri kola u obe mreže, četiri naspram tri nivoa. |
| 02-s030 | — | Dokazi neekvivalencije NI lanca i stabla; analogni NILI kontra-primer. |
| 02-s031 | e03 | Tri međusignala pravilne NI/NILI realizacije i proširenje na troulazna kola. |
| 02-s032 | e01, e03 | Značenje Hemingovog rastojanja i potpun račun 8 naspram 3 ulaza. |
| 02-s033 | — | Slojevi i praktična ograničenja ručnog praćenja karte. |
| 02-s034 | e01 | Prirodni i Grejov raspored, preuređivanje i prsten; odobreni indeksi. |
| 02-s035 | e02 | Presavijanje karte preko obe orijentacije i binarna provera susedstva. |
| 02-s036 | — | Ugaona grupa 0,2,8,10 i njen stalni literalni proizvod. |
| 02-s037 | e02 | Susedstvo i uklanjanje E između dve karte. |
| 02-s038 | e02 | Susedni i nesusedni FE slojevi i promene indeksa 16 i 32. |
| 02-s039 | e02 | Veza reda grupe sa brojem literala; hiperkocke i nepravilne grupe. |
| 02-s040 | — | Ispravno zaglavlje C=1 i članovi grupa 0,4 i 0,1,4,5. |
| 02-s041 | e03 | Potpun uslov minimalnosti, preklapanje grupa i ograničenja kriterijuma. |
| 02-s042 | e01 | Razlika neodređenog izlaza i ulaza; SOP/POS sažimanje na konkretnom primeru. |
| 02-s043 | — | Tačna polja obe grupe, upotreba b i svi stalni i promenljivi literali. |
| 02-s044 | — | Izvođenje sva tri POS činioca i tačno pokrivanje nula. |
| 02-s045 | — | Obim brojanja ulaza i razlika spoljašnjih ulaza i ulaza kapija. |
| 02-s046 | e01, e02 | Potpuni račun 14-pinskih invertorskih i dvoulaznih kućišta. |
| 02-s047 | e02 | Tri dvoulazna I kola u jednom čipu i duža putanja jednog člana. |
| 02-s048 | e01, e02, e03 | Tri NI alternative, svih devet kapija, međuinverzija i dva kućišta. |
| 02-s049 | e02 | Deset NILI kapija i konkretni zahtevi poređenja složenog CMOS kola. |
| 02-s050 | e01 | Fizički uzroci, razlika hazard/glič i zakašnjeni komplement B. |
| 02-s051 | e01, e03 | Tri vremenska intervala i trajanje lažne nule u zadatom modelu. |
| 02-s052 | — | Odobrena karta, potpuni četiri minterma i razlikovanje dva primera. |
| 02-s053 | — | Susedni prelaz 3 na 1 i algebarski dokaz konsenzusa. |
| 02-s054 | e03 | POS statički hazard, više ulaza, očuvanje polariteta i iskustvo projektanta. |

## Stručne odluke i jezičke ispravke

Ranije odluke korisnika ostaju primenjene: s022 je proizvod zbirova sa prvim činiocem C+B+A; s029 ostaje u izabranom prikazu; s034/s040 imaju odobrene indekse/zaglavlja; s052/s053 čuvaju karte i odgovarajuće formule. Beleške predstavljaju ispravno gradivo neposredno, bez priče o odobravanju. Kod s029 objašnjeno je da oba rasporeda koriste četiri kapije, a najduža putanja ima četiri, odnosno tri nivoa. Kod s052/s053 objašnjen je kartirani primer, uz stručno razjašnjenje razlike prema mreži s050/s051.

Gramatički ispravni oblici zadržani su u nastavnom tekstu. Raniji parovi poput „promenjiva“ → „promenljiva“, „konjuktivna“ → „konjunktivna“ i „među korak“ → „međukorak“ nalaze se u tehničkoj evidenciji i [ranijem popisu](../uocene_greske.md). Prethodne beleške sa uredničkim ispravkama nisu prepisivane kao nastavno gradivo. U ovom ciklusu nisu samostalno uvedene stručne promene formula, vrednosti, topologije ili izvornih tvrdnji.

**Nema novih otvorenih stručnih pitanja.** Završeno od strane agenta nije isto što i odobreno od strane korisnika.

## Provere

Uspešno su izvršene komande:

```bash
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza notes
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza review
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza check
```

Završni `check`: **PROVERENO**. [Log notes](../../build/redizajn/provera-beleski/notes.log), [log review](../../build/redizajn/provera-beleski/review.log), [log check](../../build/redizajn/provera-beleski/check.log). Postojeća računska provera osnovne tabele, SOP/POS, dva konsenzus identiteta i dva primera gliča prolazi. Dodatno su proverene 22 grupe tvrdnji za međukorake novih beležaka: logičke funkcije svim ulaznim kombinacijama, širina impulsa u 16 numeričkih slučajeva, 321 susedna binarna para za 1–6 promenljivih, račun pinova/kućišta i vremenska stanja oba gliča. Rezultati su u `logical_checks` evidencije.

Svih 54 originalnih slajdova upoređeno je sa 54 prikaza prezentacije; pročitan je svaki izvor beležaka i pregledana svaka njegova A4 strana u punoj veličini. Pregledani su tačnost, potpunost, upotrebljivost za predavača, oznake formula, veza sa istim ID-jem i odsustvo nepotrebnog ponavljanja. Nema preklapanja, odsecanja niti uredničkih oznaka u nastavnom tekstu. Kompilacija nema upozorenja, `Overfull`, `Underfull`, nedostajućih znakova ni grešaka. Redosled beležaka je 54/54; sva izvorna nevidljiva sidra su sačuvana. `git diff --check` prolazi.

## Pregledani otisci

| Resurs | SHA-256 |
|---|---|
| Originalni PDF | `f631914c9f32a0472f4fa3af11115abaadb9316dfcf6f1528cd91ef4d28868f4` |
| Manifest redizajna | `6d75a7ba4d60b5f3828020d0a50e6b12070486000b0fb0014c291493ff227af9` |
| Arhiva polaznog stanja | `51cae27d69a4c44d8d7461f8924e949d8dd63ca43462bdb7e42c14597761f2a2` |
| Zapis izgradnje | `8e7dece7c389747676b312d226aba0b1c70a8c1c6c1254ef960c63d7fbdf4868` |
| Prezentacioni PDF | `3d700a61ed5e45397f91a7dba4c867acab71eab5669227b042525d2a3c8e5f21` |
| PDF beležaka | `c3beab8568b26f83424f89c0780b4fce5ddc3c7915416c9e67affc48110e4d07` |
| Manifest teme etf-v1 | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |
| Evidencija novih beležaka | `bf5a71a7caed810ea58610b82b0cbe68a9b296f4ddd8ae5f19b3ac17ec8e1885` |

Pojedinačne potvrde vezane su za nove izvore i prikaze beležaka; raniji otisci nisu samo zamenjeni bez pregleda. Originalni PDF, izvori slajdova i prikazi prezentacije poređeni su sa početnim stanjem i identični su. Manifest teme ostaje nepromenjen.

## Sledeći korak

Korisnikov pregled novog PDF-a beležaka 02 i odobrenje ove verzije. Status: `ceka_odobrenje`; odobrenje nije dato niti je ovaj nalog tumačen kao prihvatanje rezultata. Ranija dozvola za početak 03 ostaje zasebna odluka. Ovaj ciklus ne obrađuje druga predavanja. Naredni agent čita ovaj izveštaj i proverava otiske; važeću analizu ne ponavlja ako se relevantni izvori i zavisnosti nisu promenili.
