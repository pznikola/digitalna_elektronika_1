# Rezultati potpune provere vežbi

## Korekcija stila listinga u zadatku 02/4 — 09.10.2026.

Uz sva četiri listinga zadatka 4 koristi se postojeći stil „Verilog kod koji implementira …“ i „Testbench koji simulira … je dat OVDE“. Link ka testbenchu odvojen je razmakom od naredne pottačke; uvod i lista zahteva c) ostaju zajedno. Lokalna izgradnja i strukturne provere prolaze, svih 37 listinga kopira se tačno u raw/layout režimu, a svih sedam promenjenih stranica pregledano je na 150 dpi. Broj stranica ostaje 32 za 02, odnosno 166 ukupno. Važeći pregled i otisci ove verzije su u [potvrdi pregleda](rucni_pregled.json), u polju `02.presentation_update`. RTL i testbenchovi nisu menjani. Čista izgradnja opisana u narednom odeljku odnosi se na verziju pre ove korekcije prikaza.

## Važeća provera zadatka 02/4 — 09.10.2026.

Materijali imaju **166 PDF stranica**, **53 RTL modula**, **44 testbenchova** i **37 celih Verilog listinga**. Zadatak 02/4 ima tri glavna modula, pomoćni `bcd_cifra` i četiri testbencha. Globalna greška računa se iz izvornih BCD ulaza; ERROR jedinica ne određuje G. Kaskada je kombinaciona, bez INIT-a i povratne putanje. Prelaz 00A5 → 0504 daje E → 504 bez resetovanja; 0000 prikazuje jednu nulu.

| Vežba | Stranice | RTL / testbench | Verilog listinzi | Računske i strukturne provere |
|---|---:|---:|---:|---:|
| 01 | 28 | 11 / 10 | 10 | 2.863 |
| 02 | 32 | 22 / 20 | 15 | 76.879 |
| 03 | 17 | 0 / 0 | 0 | 18.894 |
| 04 | 30 | 13 / 8 | 6 | 13.849 |
| 05 | 21 | 7 / 6 | 6 | 256.760 |
| 07 | 13 | 0 / 0 | 0 | 2.230 |
| 08 | 25 | 0 / 0 | 0 | 1.395 |

Radno stablo i nova privremena kopija prolaze kompletan `make check`: **88 studentskih simulacija po prolazu**, 37 simulacija RTL-a kopiranog iz PDF-a, postojeće računske/GHDL provere, 18 VHDL/SV binarnih poređenja i pet X/Z poređenja. Prolaze 16 postojećih negativnih proba, sedam proba registra, četiri prethodne HDL i sedam negativnih proba dopune, kao i **pet novih namerno pogrešnih realizacija zadatka 4**.

Verilatorom i Icarusom provereni su domeni 16 za a), 10 za b), 64 za pomoćni blok i svih 65.536 ulaza c), uz nezavisne tabele segmenata. Dodatno su provereni prelazi sa greške na ispravan broj i 17 Icarus X/Z slučajeva gašenja. Hijerarhijski graf stvarnih RTL zavisnosti nema kombinacionu petlju; ERROR ne zavisi od gašenja. Verzije u image-u `hdlview-tools:2025.12`: Verilator 5.042, GHDL 6.0.0-dev i Icarus 13.0 devel.

Svih **37 listinga** kopira se tačno u režimima Poppler `-raw` i `-layout`, sa izvornim razmacima i novim redovima. Provera uključuje pomoćni modul i njegov zasebni testbench. Čista kopija bez PDF-ova, TeX pomoćnih fajlova i minted keša gradi svih sedam dokumenata; **svih 166 stranica ima identične piksele na 110 dpi** u odnosu na radne PDF-ove.

Codex je pregledao novu šemu, četiri nova listinga na fizičkim stranicama 22, 25, 30 i 31 vežbe 02, ceo span zadatka 4 i sve promenjene stranice vežbi 01/07/08. Prethodno pregledan nepromenjen sadržaj ostaje vezan za sačuvanu evidenciju. Uklanjanje istorijskih napomena ne menja formule; naknadne dve tekstualne promene u 08 imaju dodatnu lokalnu izgradnju i računske/strukturne provere pre čiste izgradnje. Novi pregled nije predstavljen kao ljudski potpis.

Sva **32 VHDL fajla** i svih **49 prethodnih RTL izvora** imaju nepromenjene SHA-256 otiske. Od 89 prethodnih SV fajlova, 86 je bajtovski identično, a u tri testbencha uklonjen je isključivo po jedan istorijski komentar prema zahtevu korisnika; izvršivi sadržaj svih 89 ostaje isti. Tačna dozvoljena brisanja čuva [zapis uklanjanja napomena](dokazi/student_text_cleanup.json). U studentskom tekstu i SV kodu nema napomena o toku ovog rada; objašnjenja funkcije kola ostaju.

Važeći izvori, oba prolaza i stvarni pregled zabeleženi su u [dokazu zadatka 4](dokazi/zadatak4_provera.json) i [potvrdi pregleda](rucni_pregled.json). Raniji odeljci ispod su istorijski rezultati. Novi RTL nema kašnjenja, vremenske deklaracije, registre ni parametre. X/Z proverava Icarus; ActualText zahteva podršku PDF preglednika. Funkcija c) proverena je nakon smirivanja kola, bez garancije odsustva prolaznih impulsa. Novi primeri nisu proveravani Quartusom/Questom.

## Istorijska evidencija dopune sa 19 novih primera — 09.10.2026.

Tadašnja verzija sadržala je **163 PDF stranice**, **49 RTL modula**, **40 testbenchova** i **33 kompletna Verilog listinga**. Dopuna dodaje 19 glavnih primera, 12 pomoćnih modula i 22 testbencha (19 glavnih i tri dodatne provere pomoćnih modula). Kod prati postojeće formule i šeme, sa imenovanim međusignalima, eksplicitnim izrazima i povezivanjem portova. Originalnih 32 VHDL i 36 prethodnih SystemVerilog fajlova imaju nepromenjene SHA-256 otiske.

| Vežba | Stranice | RTL / testbench | Verilog listinzi | Računske i strukturne provere |
|---|---:|---:|---:|---:|
| 01 | 28 | 11 / 10 | 10 | 2.863 |
| 02 | 28 | 18 / 16 | 11 | 76.685 |
| 03 | 17 | 0 / 0 | 0 | 18.894 |
| 04 | 30 | 13 / 8 | 6 | 13.849 |
| 05 | 21 | 7 / 6 | 6 | 256.760 |
| 07 | 14 | 0 / 0 | 0 | 2.230 |
| 08 | 25 | 0 / 0 | 0 | 1.395 |

01 dobija tri NI/NILI mreže i realizaciju bez hazarda; 02 tri dekodera 6/64; 04 šest primera uz već rešene samostalne zadatke 3 i 4; 05 Grejov koder/dekoder, BCD sabirač, parnost i Hamingov koder/korektor. 03/07/08 nemaju dopune; njihovi PDF-ovi ostaju identični prethodnim. **Ceo zadatak 02/4, uključujući šeme i sedmosegmentne primere, ostaje neizmenjen i odložen.**

### Dvostruka funkcionalna provera

Radni izvori i nova privremena kopija prolaze ceo `make check`. U svakom prolazu svih 40 testbenchova završava uspešno na Verilatoru i Icarusu: **80 simulacija po prolazu**. Provereni su iscrpni mali binarni domeni, 256 ulaza četvorobitnog komparatora, 4.096 ulaza maksimuma, 200 dozvoljenih ulaza BCD sabirača, svih 64 Grejovih reči, parnost za zadate širine i svih 16 Hamingovih poruka bez greške i sa greškom na svakoj od sedam pozicija. Rastojanja osnovnog i proširenog Hamingovog koda proverena su za sve parove poruka.

Hazard je proveravan u oba smera za podrazumevani T=1 i promenjeni T=7ns, uz poređenje sa prethodnom strukturom. Icarus proverava X/Z odzive novih dekodera i isključivanje neizabranih grana. Ponovljena je prethodna GHDL/SV ekvivalencija za 18 modula, uključujući interne mreže, kašnjenja i dodatne četvorovrednosne slučajeve. Prolaze 16 postojećih negativnih proba, sedam proba registra, četiri prethodne HDL negativne probe i **sedam novih namerno pokvarenih dizajna**.

Image `hdlview-tools:2025.12` sadrži Verilator 5.042, GHDL 6.0.0-dev i Icarus 13.0 devel. Novi primeri nisu proveravani Quartusom/Questom; prethodni rezultati tih alata ostaju istorijska evidencija početnog prelaska.

### PDF, čista izgradnja i pregled

Sva **33 listinga** kopiraju se tačno preko PDF `ActualText`: Poppler `-raw` i `-layout` čuvaju izvorne razmake, uvlačenje, komentare i nove redove. Upravo izdvojeni RTL uspešno je simuliran Icarusom u oba prolaza.

Iz nove kopije bez PDF-ova, pomoćnih TeX fajlova ili minted keša izgrađeno je svih sedam dokumenata i ponovljene su kompletne provere. **Svih 163 stranica ima identičan prikaz na 110 dpi** u odnosu na radne PDF-ove. Nakon kopiranja korigovani su linkovi u dva Markdown dokazna priloga i precizirana VHDL uputstva u dva README-a; svi kompajlirani izvori i skripte identični su svežoj kopiji.

Codex je pregledao sedam pregleda svih stranica i svih **17 stranica novih listinga u punoj veličini na 150 dpi**, uključujući pogođene prelome. Izrazi i strukture provereni su prema postojećim formulama i šemama. Za nepromenjenu teoriju sačuvana je [prethodna evidencija](dokazi/rucni_pregled_pre_dopuna.json), uz dvaput ponovljene računske provere. Ova evidencija ne predstavlja novi ljudski potpis. Završni `audit.py --require-complete` potvrđuje svih sedam dokumenata i 4.783 inventarske celine, bez neproverenih stavki. Važeći otisci, rezultati oba prolaza i pregled listinga sačuvani su u [dokaznom zapisu dopune](dokazi/dopuna_provera.json) i [potvrdi pregleda](rucni_pregled.json).

Novi RTL nema `timeunit`, `timeprecision` ni `timescale`. Vreme se podešava u simulatoru i testbenchu. Novi primer hazarda koristi T=1 za 1ns: Icarus iz navedenog image-a podrazumevani vremenski literal u zaglavlju parametra tumači kao nulu, dok eksplicitno prosleđeni T=7ns radi ispravno. Ograničenje i podešavanje opisani su u [README-u](../README.md). Verilator X/Z slučajeve proveravamo Icarusom. Kopiranje zahteva preglednik sa podrškom za ActualText; clipboard svih GUI preglednika nije testiran.

Zadatak 02/4 bio je sledeći posao nakon te dopune; merodavno sadašnje stanje opisano je u novom završnom zapisu.

## Istorijska evidencija početnog prelaska na SystemVerilog — 09.10.2026.

Tadašnja verzija obuhvatala je svih sedam vežbi i **151 PDF stranicu**. U vežbama 01/02 dodato je **36 SystemVerilog fajlova: 18 modula i 18 testbenchova**. Svaki od 32 VHDL fajla ima `.sv` parnjak, uz četiri dodatna testbencha za pomoćne module. Svih 32 originala ima nepromenjen SHA-256. Studentski primeri zadržavaju eksplicitne izraze, pojedinačne bitove proizvoda, interne mreže, polaritete, instanciranje i logičke stepene originalnih kola.

RTL nema deklaracije `timeunit` ni `timeprecision`. Vremenske jedinice podešavaju simulatori i testbenchovi, kako je opisano u [README-u](../README.md). Podrazumevani Make cilj je `run_verilator`; prikaz talasa je zaseban cilj. GHDL i `_vhdl` varijante Quartus/Questa skripti su sačuvani. Aktivne skripte koriste `.sv`, odvojene projekte/biblioteke i `SYSTEMVERILOG_FILE`.

| Vežba | Stranice | RTL / testbench | Verilog listinzi | Ponovljene postojeće računske provere |
|---|---:|---:|---:|---:|
| 01 | 25 | 6 / 6 | 6 | 2.863 |
| 02 | 26 | 12 / 12 | 8 | 76.685 |
| 03 | 17 | 0 / 0 | 0 | 18.894 |
| 04 | 27 | 0 / 0 | 0 | 13.842 |
| 05 | 17 | 0 / 0 | 0 | 256.757 |
| 07 | 14 | 0 / 0 | 0 | 2.230 |
| 08 | 25 | 0 / 0 | 0 | 1.395 |

U 03/04/05/07/08 nema HDL primera za prevođenje. Njihovi lokalni izvori i prethodno provereni teorijski sadržaj ostali su nepromenjeni; dokumenti su ponovo izgrađeni i pregledani.

### Prva provera: funkcija i vreme

- Svih 18 testbenchova prolazi na Verilatoru i Icarusu: **36 uspešnih simulacija**.
- Iscrpna VHDL/SV provera svih 18 modula obuhvata **488 binarnih ulaznih kombinacija**, **2.552 usmerenih jednoulaznih prelaza** i **20.149 poređenih fizičkih vremenskih trenutaka**. Porede se izlazi i interne mreže kroz pune hijerarhijske putanje i normalizovane vremenske jedinice. Kašnjenja su proverena sa podrazumevanim `T` i 7 ns, uključujući prosleđivanje parametra i impulse trajanja `T−1 ps`, `T`, `T+1 ps` i `2T`.
- Dodatnih **738 vremenskih poređenja** GHDL/Icarus proverava X/Z adrese i dozvole dekodera, uključujući sigurno isključenje; VHDL `U` se poredi sa SV `X`. Posebno je potvrđena podudarnost originalnih stimulusa svih 14 studentskih VHDL/SV testbenchova.
- Ponovljene GHDL referentne provere prolaze: **1.616** za 01 i **606** za 02.
- Četiri namerne HDL greške otkrivene su: negacija u množaču, veza multipleksera, prosleđivanje `T` i kašnjenje invertora.
- **14 Quartus elaboracija i 14 Questa simulacija bez GUI-ja** prolazi. U ovoj proveri nije bilo ograničenja licence.

Docker image je `hdlview-tools:2025.12`: Verilator **5.042**, GHDL **6.0.0-dev** i Icarus **13.0 devel**. Dodatno su korišćeni Quartus Prime **24.1std SC Lite** i Questa Intel Starter **2023.3**. Verzije i rezultati svakog primera sačuvani su u [dokaznom zapisu](dokazi/systemverilog_provera.json).

### Druga provera: materijali, kopiranje i čista izgradnja

Svih 14 aktivnih LaTeX listinga koristi SystemVerilog lexer i `.sv` izvore; testbench linkovi takođe vode na `.sv`. U tekstu stoji „Verilog kod“, uz objašnjenje jezika i simulatora. Aktivni listinzi i linkovi nemaju zaostale VHDL putanje.

PDF `ActualText` uz svaki listing sadrži stvarni UTF-8 tekst izvora. Kopiranje celog bloka čuva uvlačenje, obične razmake, komentare i nove redove. `make -C vezbe check-pdf-code` potvrđuje **tačno podudaranje svih 14 listinga** u Poppler režimima `-raw` i `-layout`, a zatim uspešno simulira upravo izvučeni RTL Icarusom. Ne normalizuje unutrašnje razmake niti prelama redove radi poređenja. Dodatak za kopiranje nije promenio izgled nijedne od 51 stranice vežbi 01/02.

Završna nova privremena kopija započela je bez generisanih PDF-ova, TeX pomoćnih fajlova i minted keša. Ponovo su izgrađena sva dokumenta i ilustracije i izvršen ceo `make check`, uključujući postojeće računske provere, strukturu svih sedam dokumenata, PDF kopiranje, HDL simulacije, ekvivalenciju, **16 postojećih negativnih proba**, **7 proba registra** i četiri nove HDL negativne probe. **Svih 151 stranica** čiste izgradnje poređeno je na 110 dpi sa radnim PDF-ovima; prikaz je identičan.

Codex je pregledao prevode prema izvornim VHDL izrazima i šemama, svih sedam dokumenata kroz renderovane stranice i svih 14 listinga u punoj veličini na 150 dpi. Prikaz dodatka za kopiranje potvrđen je poređenjem piksela. Ranije izvođenje nepromenjene teorije ostaje vezano za [sačuvanu prethodnu evidenciju](dokazi/rucni_pregled_pre_systemverilog.json), uz ponovljene postojeće računske provere; ovaj pregled nije predstavljen kao novi ljudski potpis. Važeća evidencija je u [rucni_pregled.json](rucni_pregled.json), a [registar](registar.json) obuhvata **4.642 inventarske celine**.

Verilator nema punu četvorovrednosnu semantiku; zato X/Z proverava Icarus. Poređenje počinje posle početnog smirivanja, a delta ciklusi se porede kroz završnu vrednost u istom fizičkom trenutku. VHDL slabi nivoi nisu posebna SV stanja. Vrednosti parametra `T` u ovim primerima su celobrojni nanosekundni intervali. Kopiranje zahteva PDF preglednik koji podržava `ActualText`; provereno je Popplerom, bez tvrdnje da je testiran clipboard svakog GUI preglednika. Lokalni izvori testbench linkova postoje; dostupnost novih GitHub putanja zavisi od kasnijeg slanja izmena u repozitorijum.

### Istorijska evidencija pre prelaska na SystemVerilog

Tekst ispod čuva ranije rezultate i broj stranica prethodne VHDL verzije. Za trenutno stanje merodavni su rezultati iznad i `dokazi/systemverilog_provera.json`.

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
