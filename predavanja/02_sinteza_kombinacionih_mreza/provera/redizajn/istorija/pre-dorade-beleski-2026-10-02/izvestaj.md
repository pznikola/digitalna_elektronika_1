# Predavanje 02 — izveštaj redizajna

**Status: `ceka_odobrenje` · završni pregled 2026-10-02.** Po nalogu „prodji kroz kreiranu 02 prezentaciju i kroz 02 originalna predavanja. Po uzoru na 01 sredi prezentaciju 02“ ponovo je pregledana i dorađena cela prezentacija. Rezultat 02 još nije odobren. Ranije odobrenje početka 03 ostaje zasebna odluka, zabeležena u [odlukama](odluke.md).

## Obuhvat i isporuka

Pregledano je svih **27 strana [originalnog PDF-a](<../../../02 Sinteza kombinacionih mreza.pdf>)**, odnosno svih 54 gornjih/donjih slajdova, uključujući formule, tabele, šeme i sadržaj u slikama. Original nije menjan. Pregledani su postojeći LaTeX izvori i njihova prethodna isporuka, završni prikaz svakog slajda u punoj veličini i sve pripadajuće beleške.

Sačuvani su **54 slajda, njihov redosled i ID-jevi `02-s001`–`02-s054`**, bez novih slajdova ili overlay strana. Mapa pokrivenosti potvrđuje **152/152 sadržajna elementa**. Autorstvo prof. dr Lazara Saranovca i izvorna školska godina 2021/22 su sačuvani.

- [Prezentacioni PDF — 54 strane 16:9](../../build/02_sinteza_kombinacionih_mreza.pdf), [glavni LaTeX izvor](../../02_sinteza_kombinacionih_mreza.tex).
- [Slajdovi sa detaljnim beleškama — 54 A4 strane](../../build/02_sinteza_kombinacionih_mreza_beleske.pdf), [izvori beležaka po ID-ju](../../beleske/).
- [Uporedni pregled original / polazni LaTeX / posle / beleške](../../build/redizajn/pregled/index.html).
- [Inventar](inventar.json), [mapa pokrivenosti](pokrivenost.json), [potvrde pojedinačnog pregleda](pregled.json), [stručne odluke](strucni_predlozi.md).

Prethodna isporuka ovog ciklusa sačuvana je kao [PDF pre dorade](../../build/dorada-2026-10-02/pre-02_sinteza_kombinacionih_mreza.pdf), sa beleškama i prethodnim JSON zapisima u istom folderu. Istorijski snapshot rekonstrukcije ostaje sačuvan zasebno; nije zamena za potvrde ovog pregleda.

## Usklađivanje sa odobrenom 01

Koristi se izabrani stil B i tema **`etf-v1`**. Nastavno isticanje je lokalno prebačeno na tamnocrvenu **`#A32638`**, kao u 01. Zamrznuta tema nije menjana. Fontovi su sačuvani; problemi sa prostorom rešeni su rasporedom, kompaktnijim crtežima i beleškama, bez automatskog smanjivanja celog slajda.

Naslovi ilustracija, tabela i odeljaka odvojeni su od prethodnog teksta i od svojih prikaza. Na gušćim slajdovima jednačine, tabele i objašnjenja raspoređeni su u jasne kolone. Ključne definicije, rezultati, uslovi i sve nastavne ilustracije ostaju vidljivi. Projektovani slajdovi sadrže gradivo, bez uredničkih napomena o postupku redizajna.

Reprezentativna poređenja:

| Slajdovi | Pre dorade → završni prikaz |
|---|---|
| [s003–s005](../../build/redizajn/pregled/index.html#02-s003) | Zbijeni opisi uz dijagrame → zasebni naslovi, čitljivi izrazi i izdvojene oznake kašnjenja. Šrafirani intervali na s005 su tamnocrveni. |
| [s009](../../build/redizajn/pregled/index.html#02-s009), [s010](../../build/redizajn/pregled/index.html#02-s010) | Dugi pasusi → poravnate definicije, simetrična pravila indeksiranja i jasno odvojeni koraci sinteze. Na s010 vraćen je izvorni izraz „broj kola iste vrste“. |
| [s011–s018](../../build/redizajn/pregled/index.html#02-s011) | Tabele i izvodi nadmetali su se za prostor → kompaktnije tabele, razmaknuta zaglavlja i očuvani svi članovi jednačina. Jedinice/nule za izvođenje funkcije su tamnocrvene. |
| [s020–s022](../../build/redizajn/pregled/index.html#02-s020) | Slabije izdvojene grane i gust odnos teksta/šeme → stvarni vodovi opterećenog ulaza istaknuti crveno, objašnjenje odvojeno od šeme i urednih pet ulaza završnog I kola. |
| [s026](../../build/redizajn/pregled/index.html#02-s026) | Izvod neposredno uz crteže → razmak između formule i obe ekvivalentne NILI mreže; svih pet činilaca ostaje vidljivo. |
| [s028–s031](../../build/redizajn/pregled/index.html#02-s028) | Oznake kritične putanje i neujednačena kola → crveni stvarni vodovi i simboli kritične putanje, ujednačena dvoulazna kola i jasno grananje invertera. S029 zadržava korisnikov izbor izvornog sadržaja. |
| [s034–s040](../../build/redizajn/pregled/index.html#02-s034) | Preklopljene oznake i gusto složene karte → razdvojene strelice, numerisani rasporedi, jasne orijentacije i svi izvorni parovi susedstva. Na s038 šire ćelije odvajaju dvocifrene indekse. Oznake su najmanje 9 pt. |
| [s043–s044](../../build/redizajn/pregled/index.html#02-s043) | Slabije razlikovanje grupa → tamnocrvena isticanja, isprekidana druga grupa na s043; s044 čuva jedinu nacrtanu izvornu grupu. |
| [s049](../../build/redizajn/pregled/index.html#02-s049), [s052–s053](../../build/redizajn/pregled/index.html#02-s052) | Gust tekst → izdvojena poređenja realizacija, centrirane karte i jasno obeležen konsenzus član; urednički uvod uklonjen sa s052. |

Vektorski su dorađeni vremenski dijagrami 03–05; oznake DIP-14 na 08; mreže 19–22, 24 i 26; kaskade/stabla 28–31; karte 34–38, 40, 43–44 i 52–53. Četiri karte s038 imaju zaseban lokalni TikZ izvor sa istim indeksima 0–63. S008 čuva prethodno dorađene simetrične ulazne vodove i dovoljno prostora za dimenzije. S051 čuva oznaku `t_p` iznad svih talasnih oblika.

U svim logičkim mrežama provereni su priključci, negacije, izlazi, stvarni spojevi i ukrštanja. Vodovi ne prelaze preko tela logičkih kola; prava grananja imaju tačke, a ukrštanja bez spoja ostaju bez njih. Izmena rasporeda ne menja topologiju. Predavanje 02 nema analogna tranzistorska kola.

## Izvorni sadržaj, odobrene ispravke i beleške

Prethodno odobrene stručne odluke su očuvane: s022 je proizvod zbirova sa prvim činiocem \(C+B+A\); s034 ima gornji indeks 0 i donji 1 u uspravnoj karti; s040 iznad \(C=1\) ima zaglavlja 0,1; s052–s053 čuvaju karte i koriste \(F=\bar C\bar B+BA\), odnosno \(F=\bar C\bar B+BA+\bar C A\). S029 ostaje prema korisnikovoj odluci. Obrazloženja i razlike prema originalu su u beleškama i [stručnoj evidenciji](strucni_predlozi.md).

U ovom ciklusu ispravljene su greške ranijeg prepisivanja: kriterijum „broj različitih vrsta kola“ na s010 vraćen je na izvorni „broj kola iste vrste“; beleška s015 sada kaže da **tri** preostala reda daju jedinicu; beleška s044 više ne tvrdi da su na karti nacrtane tri grupe. Na s049 vraćen je izvorni **klasični kriterijum minimizacije**, umesto tvrdnje o nedokazanoj minimalnosti po broju čipova. Izvorne stručne tvrdnje nisu samostalno menjane.

Zaseban `beleske/sNNN.tex` postoji za svaki ID. Izvorni postupci su sačuvani ili dopunjeni iz samog PDF-a: primeri termina na s009, eksplicitni petočlani izvod na s015/s026, poređenje rasporeda na s034 i identiteti zamene troulaznog NI/NILI kola na s048/s049. Dopunsko tumačenje i korisnikom odobrene korekcije razlikuju se od izvornog zapisa.

| Oblast / ID-jevi | Šta ostaje na slajdu | Razrada u beleškama istog ID-ja |
|---|---|---|
| 02–06 | Definicije, uslovi, vremenski dijagrami i oznake kašnjenja | Fizičko značenje, prelazni intervali, uslovi posmatranja i tumačenje šrafiranja |
| 07–18 | Kriterijumi, definicije, funkcionalne tabele i ključni izvodi | Puni primeri literala, pravila indeksiranja, redovi minterma/maxterma i međukoraci |
| 19–31 | Sve logičke mreže, transformacije i ekvivalencije/neekvivalencije | Provera grana, opterećenje ulaza, negacije i razlika broja kola/nivoa |
| 32–44 | Postupak sažimanja, sve karte, indeksi, grupe i minimalni izrazi | Binarni raspored, susedstvo u višim dimenzijama i izvođenje članova po površinama |
| 45–49 | Poređenja ulaza/čipova, formule i CMOS zadatak | Računanje pinova i broja kola/čipova, identiteti zamene i uslovi poređenja |
| 50–54 | Šeme, talasni oblici, karte i uklanjanje statičkog hazarda | Vremenski međukoraci, dva kartirana primera, konsenzus i ograničenja pri promeni više ulaza |

Tačna odredišta svih 152 elemenata, sa putanjama i sidrima, nalaze se u [mapi pokrivenosti](pokrivenost.json). Nijedna logička celina nije preneta u beleške u celosti.

## Provere i kontrolne sume

Uspešno su izvršeni:

```bash
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza all
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza review
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza check
```

`review` i `check` grade i prateći PDF beležaka. Završni `check` prijavljuje **`PROVERENO`**: 54/54 slajda, očuvan redosled/ID-jevi, 152/152 elemenata i važeće potvrde slajdova i beležaka. Postojeća računska provera prolazi za osam redova osnovne tabele, SOP/POS za svih 16 ulaznih kombinacija, oba konsenzus identiteta i oba primera gliča. Provera zapisa s022 prihvata njegov novi višeredni raspored uz istih pet obaveznih činilaca.

Sadržinski i vizuelno pregledani su svi slajdovi i sve 54 strane beležaka. Oba dokumenta se kompajliraju bez `Overfull`, `Missing character`, `LaTeX Error`, `Undefined control` ili nedefinisanih referenci. Nema nepokrivenog gradiva, preklapanja ili odsečenog sadržaja u završnim prikazima. `git diff --check` prolazi.

| Resurs | SHA-256 |
|---|---|
| Originalni PDF | `f631914c9f32a0472f4fa3af11115abaadb9316dfcf6f1528cd91ef4d28868f4` |
| [Manifest redizajna](manifest.json) | `be46b8d4dbd0d2acfe495e913f99a532bf1d5d261d5f48ac930e48a889cdcf9e` |
| [Arhiva polaznog stanja](polazno-stanje.tar.gz) | `51cae27d69a4c44d8d7461f8924e949d8dd63ca43462bdb7e42c14597761f2a2` |
| [Zapis izgradnje i pregledanih zavisnosti](izgradnja.json) | `4b11263f0571c24879ec25f646213a79ee9270dc8d355b051dc8c8e1f956663c` |
| Prezentacioni PDF | `3d700a61ed5e45397f91a7dba4c867acab71eab5669227b042525d2a3c8e5f21` |
| PDF beležaka | `2ecb52fcb38502c66cd2f7837b044d38d33266b0048eca3cc0a5ec83af5a37de` |
| Manifest teme `etf-v1` | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |

Pojedinačni otisci izvora, beležaka i pregledanih prikaza nalaze se u [potvrdama](pregled.json). Tema i izvorni PDF su neizmenjeni.

## Jezičke ispravke i sledeći korak

Očigledne jezičke ispravke obuhvataju „jedincama“ → „jedinicama“ (03), „zavisti“ → „zavisiti“ (05), „među korak“ → „međukorak“ (10), „promenjiva“ → „promenljiva“ (11, 13, 15, 17), „konjuktivnom“ → „konjunktivnom“ (17), „po srediti“ → „po sredini“ (35), „na povšini“ → „na površini“ (44) i slaganje uz „kolo/kola“ (24, 45–46). Pojedinačne evidencije su u beleškama i [ranijem popisu](../uocene_greske.md).

**Nema novih otvorenih stručnih pitanja.** Sledeći korak je korisnikov pregled ove isporuke i zasebno odobrenje rezultata 02. Status je `ceka_odobrenje`; agent nije sam odobrio prezentaciju. Ovaj ciklus ne pokreće obradu drugog predavanja. Naredni agent prvo proverava ovaj izveštaj i kontrolne sume, a završenu analizu ponavlja samo za promenjene izvore ili nove primedbe.
