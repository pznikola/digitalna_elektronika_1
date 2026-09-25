# Rezultati potpune provere vežbi

Pregled obuhvata vežbe **01, 02, 03, 04, 05, 07 i 08**. Sačuvani su izvorni dokumenti i obim studentskih rešenja. Sadržaj zadataka za samostalni rad proveren je u dokaznim prilozima i skriptama; nova rešenja nisu dodata studentskim dokumentima.

Završni PDF-ovi imaju **154 stranice**. Svaka stranica pregledana je u čitljivom prikazu, a guste šeme dodatno uvećano. Posle promena ponovo su pregledane promenjene stranice; za ostale je potvrđena identičnost rendera. Tačne pregledane verzije i stranice zabeležene su u [`rucni_pregled.json`](rucni_pregled.json). Automatska izgradnja ne izdaje te potvrde.

## Obuhvat i najvažniji nalazi

| Vežba | Stranice | Automatske provere | Ispravke i dokazi |
|---|---:|---:|---|
| 01 | 25 | 2.863 | [Izveštaj](../01/IZVESTAJ_ISPRAVKI.md): negacije u dve realizacije, kriterijumi i smerovi hazarda, VHDL kašnjenja, uslovi minimalnosti. |
| 02 | 29 | 76.685 | [Izveštaj](../02/IZVESTAJ_ISPRAVKI.md): dekoderski enable, svih 16 BCD ulaza, ispravljene veze u BCD kaskadi, vodeće nule, inicijalizacija i VHDL očekivanja. |
| 03 | 17 | 18.894 | [Izveštaj](../03/IZVESTAJ_ISPRAVKI.md), [dokazi](../03/code/PREGLED_DOKAZA.md): sve konverzije i međukoraci, periodični zapisi, opsezi, obe nule, komplementi i proširenje znaka. |
| 04 | 27 | 13.842 | [Izveštaj](../04/IZVESTAJ_ISPRAVKI.md), [dokazi](../04/code/PREGLED_DOKAZA.md): prenosi/pozajmice, negativna nula u KMV, prekoračenje, nedostajuće veze i invertori; svih 42 petocifrenih operacija provereno. |
| 05 | 17 | 256.757 | [Izveštaj](../05/IZVESTAJ_ISPRAVKI.md), [dokazi](../05/code/PREGLED_DOKAZA.md): stvarne kodne tabele, BCD2421 komplementarnost, Grejova refleksija, Hamingove ivice, parnost i precizne garancije detekcije/korekcije. |
| 07 | 14 | 2.230 | [Izveštaj](../07/IZVESTAJ_ISPRAVKI.md), [dokazi](../07/code/PREGLED_DOKAZA.md): segmenti i kaskade, razlika preseka i stabilnosti, regeneracija, garantovane margine i grafičke aproksimacije. |
| 08 | 25 | 1.395 | [Izveštaj](../08/IZVESTAJ_ISPRAVKI.md), [dokazi](../08/code/PREGLED_DOKAZA.md): MOS oblasti i fizički koreni, pretpostavke modela, stvarne PDN/PUN veze, dimenzionisanje, istorija dinamičkog stanja i transmisioni gejtovi. |

Broj automatskih provera opisuje izvršene računske slučajeve, a **ne zamenjuje** stručni ili vizuelni pregled. Opšte tvrdnje proverene su izvođenjem ili primarnim izvorima navedenim u lokalnim izveštajima. Za neparsiran sadržaj ručni dokaz je vezan za tačan izvorni SHA256 otisak. Namera studentskog zadatka da proceni netačan iskaz sačuvana je.

U vežbi **01 vraćene su originalne strelice sve četiri Karnoove karte u zadacima 4–6**, sa izvornim položajem, smerovima i bojama. Čitavi odgovarajući TikZ blokovi poređeni su sa početnom Git verzijom i zaštićeni regresionim proverama. Ranije nepotrebno precrtavanje evidentirano je kao povučeno. Šeme rešenja zadržavaju horizontalne vodove signala i njihovih komplemenata, sa vertikalnim odvodima ka kolima; ispravljene su konkretne pogrešne veze. Izvorni crteži postavke zadatka 4 i njegovog vremenskog dijagrama nisu promenjeni. Njihovi PDF izvozi obnovljeni su radi ponovljive izgradnje; promenjeno je samo obrezivanje izvoza.

U vežbi **04**, posle korisničkih primedbi, vraćena je strelica kružnog prenosa u 1.4 i pisani prikaz svih koraka množenja i deljenja u 2.5/2.6. Raniji sažeti pregled čuvao je rezultate, ali nije prenosio sve didaktičke detalje originala. Karnoove grupe sada imaju obojenu ispunu; Slika 5 neposredne vodove i izmenjen raspored ulaza desnog I kola. Na Slici 7 uklonjena je dijagonala D₁: svi spojni vodovi su horizontalni/vertikalni. Nalazi **04-A13–A18** dokumentuju razlog i proveru. Ponovo su pregledane fizičke PDF stranice 4,15–20,24,26; ostalih 18 stranica ove vežbe je identično prethodnoj verziji. [Dokaz nove čiste izgradnje 04](../04/code/provera_prikaza.json) potvrđuje svih 27 identičnih stranica i dve dodatne negativne probe pisanih računskih koraka. Naknadno su u Slici 5 poravnati ulazni priključci sa levim izlazima, tako da su obe tražene veze horizontalne (04-A18). Ponovo je pregledana samo promenjena fizička stranica 24, potvrđena identičnost ostalih 26 stranica i ponovljene lokalne računske/strukturne provere. Lokalni JSON razlikuje ovu dopunu od prethodne čiste izgradnje. Ukupan broj stranica ostaje 154. Promena broja inventarskih celina posledica je novog rasporeda tabela i uklanjanja ponovljenih zaglavlja; prethodne stavke ostaju u istoriji registra.

U vežbi **05** sačuvani su kompletni geometrijski prikazi Hamingovog rastojanja, horizontalna osa komplementarnosti BCD2421 i sva četiri koraka refleksivne konstrukcije Grejovog koda. Provere čitaju stvarne kodne reči i skup jedinstvenih ivica crteža. Tabele imaju diskretne linije između podataka, bez dodatnih tankih linija uz naglašene granice. Ispravljeni prelomi drže naslove, zadatke, rešenja i pripadajuće tabele/slike zajedno.

U naknadnoj dopuni vežbe **05** (05-A08–A13) vraćeno je označavanje različitih bita u Tabeli 6, dodatnih bita parnosti u Tabeli 7 i strelica kontrolnih grupa u Tabeli 11. Oznaka d₃ na Slici 3 podignuta je iznad kružnice. Prvi primer Tabele 13 i njegova postavka, koji su u izvorniku nedosledni, po zahtevu korisnika usklađeni su na 43; vraćen je početni binarni zapis u svih pet prelaza u Grejov kod. Provere čitaju oznake i stvarne korake iz LaTeX-a. Dokument i dalje ima 17 stranica, ukupno 154. Ponovljeni su lokalna izgradnja, računske/strukturne provere i pregled promenjenih stranica; istorijski dokazi čiste izgradnje ne predstavljaju novu čistu izgradnju ove dopune.

U dopuni **05-A14** proširena je i kolona „Grej binarni“ u Tabeli 14: sva tri para binarnog i decimalnog zapisa sada su u istom redu, sa označenim osnovama. Vrednosti su sačuvane, a lokalne računske provere i pregled konačnog izgleda ponovljeni.

Dopune **05-A15/A16** vraćaju pisane BCD postupke zadatka 2.2 (44 računska reda) i korake dekodovanja zadatka 2.3, uključujući binarne međuzapise Grejovih suseda i isticanje promenjenih bita. Raniji sažeti prikaz nije sadržao sve didaktičke detalje originala; taj propust je izričito zabeležen. Pregledane su promenjene fizičke stranice 2 i 12–17; ostalih deset identično je prethodnoj verziji. Lokalna izgradnja/provere prolaze, a četiri dodatne namerne greške na privremenim kopijama su otkrivene. [Dokazni zapis](../05/code/provera_prikaza.json) vezan je za konačne izvore i PDF.

U dopuni **05-A17** postupak i objašnjenje u tabelama 15–18 razdvojeni su praznim prostorom od 8 mm; računske crte završavaju se pre tog razmaka. Pregledane su promenjene fizičke stranice 12 i 13 i ponovljene lokalne provere.

## Ograničenja i uslovni zaključci

- **02-S05 / 02-S09:** alternativna realizacija dekodera sa enable ulazom odvojena je od doslovnog zahteva bez enable-a. BCD kaskada sa povratnom spregom zahteva opisani reset protokol; trajanje resetovanja nije određeno bez kašnjenja kola. Minimalnost se tvrdi samo za navedenu biblioteku i merilo troška.
- **07-L01:** izvorni graf bez analitičke karakteristike ne određuje tačnu numeričku granicu. Grafički zaključak i iteracije provereni su, a proizvoljan model nije predstavljen kao izvorni podatak.
- **08-L01:** za zadatak 1 nije zadat $E_C L$; numerički odgovor jasno je označen kao aproksimacija.
- **08-L02:** parametri zadatka 2 blago su neusaglašeni; prikazana su dva označena tumačenja, umesto prikrivanja razlike.
- **08-L03:** zadatak 3 nema sve podatke za numerički rezultat. Simbolički izrazi imaju eksplicitne pretpostavke, uključujući tretman praga pri efektu podloge.
- **08-L04 / 08-L05:** poređenje CMOS geometrija i normalizacija otpora koriste navedene pretpostavke o tehnologiji. Apsolutne dimenzije nisu proizvoljno dopisane.
- **08-A02:** zadati interpolacioni strujni model ima ograničenje blizu granice oblasti. To je pokazano izvodom; zadržan je kao eksplicitna aproksimacija, uz razlikovanje od globalno fizičke karakteristike.

Ograničene stavke imaju poseban status u registru. Taj status ne znači da su uslovni izvodi ili provere preskočeni; označava granicu onoga što dati problem određuje. Status se konzervativno prenosi na pripadajuću sadržinsku celinu.

## Ponovljivost i trajni dokazi

```sh
make -C vezbe
make -C vezbe check
make -C vezbe audit
make -C vezbe clean-build
```

Zavisnosti i postupak posle izmena opisani su u [README-u](../README.md). Zajednički `check` obuhvata sve računske provere, GHDL, reference, oznake, slike i relevantne poruke kompilacije. **16 namerno unetih grešaka** u privremenim kopijama uspešno je otkriveno: pogrešni rezultati, kodni biti, prenos, Karnoova ćelija, Hamingova ivica, nagib, koordinata, veza i referenca. Dodatnih **7 provera registra** potvrđuje stabilnost ID-jeva i poništavanje potvrde posle izmene izvora/dokaza/PDF-a ili nedostajućeg pregleda stranice. Privremena potvrda u testu registra isključivo je sintetički testni podatak.

Prvobitna zajednička čista izgradnja počela je bez generisanih PDF-ova, pomoćnih TeX fajlova ili minted keša. Sve ilustracije i dokumenti izrađeni su iz izmenjivih izvora, pa je **svih 154 stranica poređeno na 110 dpi** sa pregledanim radnim verzijama. Poređenje piksela izbegava lažne razlike zbog PDF datuma i metapodataka. Nije bilo razlika u prikazu. Za naknadno izmenjenu vežbu 04 ponovljena je zasebna čista izgradnja sa istim kriterijumom; za njeno trenutno stanje merodavan je novi lokalni dokaz naveden iznad. Zajednički `audit` dodatno generiše render svake stranice na 150 dpi.

Trajni mašinski dokazi su u [`dokazi/`](dokazi/): otisci čistih izvora i PDF-ova, poređenja stranica, GHDL rezultati, strukturne i negativne probe i stanje prvobitne potpune provere. Naknadna dopuna 04 ima zaseban lokalni dokaz; istorijski JSON zapisi nisu predstavljeni kao otisci novog PDF-a. Detaljni logovi i renderi u `_build/` i `/tmp/` mogu se obrisati ili ponovo napraviti. Otisci sačuvanih originala odvojeni su od otisaka radnih dokumenata; za originale izvan početnog inventara ne tvrdi se da postoji početno poređenje otisaka.

[`IZVESTAJ.md`](IZVESTAJ.md) prikazuje pokrivenost svih **4.528 inventarskih celina** po dokumentima i kategorijama. Celine se namerno preklapaju: pasus, njegova formula, tabela i njeni redovi imaju zasebne lokacije. [`registar.json`](registar.json) povezuje lokaciju u izvoru, DOCX blok ili izvorni PDF zadatak, konačnu PDF stranicu, metod, dokaz i nalaz. Promena izvora ili zavisnog dokaza poništava potvrdu celog dokumenta; promena PDF-a poništava pregled njegovih stranica.

Početno stanje i istorija ispravki su sačuvani. Završni materijali nisu automatski commitovani niti poslati u udaljeni repozitorijum.
