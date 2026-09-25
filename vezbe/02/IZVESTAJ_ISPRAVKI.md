# Izveštaj provere — vežba 02

Pregled obuhvata postojeći LaTeX, njegove uključene VHDL izvore i izmenjive crteže. Početne verzije sačuvane su u arhivi navedenoj u `../PROVERA/pocetno_stanje.json`. Originalni dokument izvan foldera 02 nije menjan. Brojevi stranica i otisci konačnog PDF-a vode se u zajedničkom registru, nakon završnog vizuelnog pregleda.

Provere se pokreću komandom `make check`. Čitaju se stvarne formule, redovi tabela i oblasti Karnoovih karata; proverava se kompajlirani VHDL. Logički opisi starijih Draw.io crteža ručno su izvedeni iz nacrtanih veza i vezani za SHA-256 izvora u `code/pregled_sema.json`. Promena crteža poništava tu potvrdu; Python ne predstavlja ručno izvedeni opis kao automatsko prepoznavanje svih slobodnih krajeva vodova.

## Stručni i grafički nalazi

| ID | Mesto u izvornom i novom materijalu | Pre → posle; razlog i uticaj | Ponovna provera |
|---|---|---|---|
| 02-G01 | Zadatak 1a, `fig:zadatak1-b`, `Images/Zadatak_1/Zadatak_1b` | U starom PDF-u nedostajao je deo veze između I kola za D2 i izlaznog ILI kola. Draw.io izvor već sadrži ispravnu vezu. **Regenerisan samo PDF**, bez izmene šeme. | Novi izvoz vizuelno pregledan; logički opis za svih 64 ulaza multipleksera, a stvarni VHDL za isti domen. |
| 02-G02 | Zadatak 1b, `fig:zadatak1-a`, `Images/Zadatak_1/Zadatak_1a` | U starom izvozu nedostajao je deo veze ¬AB → D2 gornjeg multipleksera. Izvor je ispravan; regenerisan PDF. | Novi izvoz i svih 16 kombinacija A, B, C1, C0. |
| 02-G03 | Zadatak 3b, `fig:zadatak3-a`, `Images/Zadatak_3/Zadatak_3a` | U starom PDF-u izostala je negacija Y0 prvog dekodera. Crta je već u izvorniku. Regenerisan PDF, bez menjanja izvora. | Svi izlazi oba dekodera pregledani; GHDL potvrđuje aktivno nizak izlaz za svih 16 adresa. |
| 02-G04 | Zadatak 4b, `fig:Zadatak_4b`, Draw.io ćelije `zfqoCNcEfpP9erQ9kGkR-{28,29,30,31,32,34,36,38}` | Desne oznake ABCD bile su obrnute u odnosu na leve DCBA i stvarne veze. Zamenjene su u DCBA, uključujući komplemente. Veze i raspored ostali isti. | Ručno praćenje vodova i a=D+B+¬(C⊕A), svih 16 ulaza (ova konkretna funkcija a slučajno radi i za 10–15). |
| 02-G05 | Zadatak 4c, `fig:Zadatak_4c_CompleteBCDLogic`, ćelija `xRcpgTjZ43rqUCvEUsDN-91` | Srednje **I** kolo zamenjeno **ILI** kolom. Izlazi NILI kola su n1=¬(D+B+A+¬C) i n2=¬(D+B+¬A+C). Njihov proizvod je uvek 0, jer n1 zahteva A=0,C=1, a n2 A=1,C=0. Prethodna šema zato je pri OFF=LZ_IN=0 palila a i za cifre 1 i 4. Ispravna funkcija je a′=¬(n1+n2+off_int). | Sva 64 ulaza DCBA,OFF,LZ_IN; slika i izraz upoređeni; raspored očuvan. |
| 02-G06 | Zadatak 4c, `fig:Zadatak_4c_4Digits`, ćelije `_5a-ulwvho9ZLbQOsWlU-157/158` | Oznake A0 i B0 nalazile su se iznad suprotnih priključaka poslednjeg bloka. Zamenjene su; ostali vodovi očuvani. | Praćenje DCBA do svakog bloka; kaskadna provera svih 65.536 četvorocifrenih ulaza posle opisanog resetovanja. |
| 02-S01 | Zadatak 2a, pasus pre `eq:zad2-a1` | Heuristika „promenljive sa najviše različitih kombinacija” predstavljena je kao pravilo izbora selekcije. Zamenjena je poređenjem Šenonovih kofaktora i potrebnih dodatnih kola. | Za AB dobijaju se D0=0, D1=C, D2=1, D3=C, provereno zamenom u stvarni izvorni izraz za svih 8 ulaza. |
| 02-S02 | Zadatak 2b/c, `eq:zad2-b2` i prateći tekst | Minimalnost višestepene NI2 mreže ne dokazuje se samo minimalnim zbirom proizvoda. Četiri NI2 kola jesu dovoljna i minimalna za direktne ulaze; uvedeno eksplicitno merilo. Broj kućišta uslovljen je bibliotekom. | Iscrpno generisane sve aciklične NI2 mreže do tri kola, uključujući dozvoljene konstante: nijedna ne daje ciljnu funkciju. TI katalozi potvrđuju primer kućišta, videti reference. |
| 02-S03 | Zadatak 2c/d, `fig:kmap-zad2-d` | 30 ns precizirano kao kašnjenje najduže putanje od B. Strelice su **ostale potpuno iste**. Dodato razlikovanje strukturne mogućnosti hazarda od impulsa pri jednakim kašnjenjima: B:1→0 daje pad Y posle 2T i povratak posle 3T; obrnuti smer u tom modelu nema impuls. | Sve 24 usmerene promene jednog ulaza, inertni i transportni model; provera I1,I2,I3,Y; rizični par CBA=101/111, dodatni CA pokriva oba stanja. |
| 02-S04 | Zadatak 3b, pasus pre `fig:zadatak3-a` | Izlazi nisu bezuslovno komplementi minterma: pri isključenom dekoderu svi su 1. Dodat izraz ¬(EYi), E=EN0·¬EN1·¬EN2. Objašnjeno da je široka linija magistrala. | Svih 64 kombinacija adrese i dozvola rada po VHDL dekoderu; svih 16 ulaza sastavljenog dekodera. |
| 02-S05 | Zadatak 3d, `eq:zad3-d`, `fig:zadatak3-d` | Postavka traži dekodere iz a), bez enable, dok stara šema koristi devet blokova iz b), sa enable i aktivno niskim izlazima. Sačuvani su postavka i originalna šema. Dodato je rešenje Y(8i+j)=HiLj za dva dekodera iz a) i 64 I kola, odnosno realizacija proizvoda dodatnim dekoderima ako su dozvoljeni samo ti blokovi. Stara šema jasno označena kao alternativa za b). | Za svih 64 adresa aktivan je samo traženi izlaz. Za alternativu provereni dozvole, redosled adresa, aktivni nivoi i mapiranje 8i+j. Broj 66 naveden je kao dovoljan, bez tvrdnje o minimalnosti. |
| 02-S06 | Zadatak 4a/b, tekst uz `fig:Zadatak4_a` i `tab:bcd-7seg-b` | Objašnjeno da se simbol NE, uz ograničenje na NILI, ostvaruje spajanjem ulaza NILI kola. Oznaka b u nedozvoljenoj ćeliji razdvojena od segmenta b; don’t care se koristi samo uz garanciju ispravnog BCD ulaza. Precizirano merilo minimizacije i uklonjena preširoka tvrdnja pre `eq:zad4-a`. | Idempotentnost X+X=X; obe tabele, svi segmenti, sve formule i svih 14 karata za segmente. |
| 02-S07 | Zadatak 4c, `tab:signali-bcd`, red OFF | „Kada je postavljen na 0 svi segmenti su isključeni” → **na 1**. Aktivni nivo u tabeli i nacrtana šema već su bili 1. | a′=a·¬off_int; svi ulazi kontrolnih šema. |
| 02-S08 | Zadatak 4c, ista tabela, LZ_IN/LZ_OUT | Nejasno „vodeće nule isključene” → LZ_IN=1 označava da su sve više cifre nule; LZ_OUT=1 da su i trenutna i sve više cifre nule. Najniža cifra ima LZ_IN=OFF=0. | Izraz `eq:lzout`; 0000→0, 0231→231, 0504→504 i ceo četvorocifreni domen. |
| 02-S09 | Zadatak 4c, napomena posle kaskade, `eq:feedback` | Izvor je pominjao pamćenje, ali nije zadao uslove ispravnog novog prikaza. Dodat stacionarni izraz F=I(R+F), gde R dolazi od izvornih ulaza, i protokol resetovanja pri uključivanju i svakoj promeni podatka. | Za R=0,I=1 i F=0 i F=1 zadovoljavaju jednačinu. Greška → ispravan ulaz bez resetovanja ostavlja E; reset briše F, a prisutna greška ga ponovo postavlja. Trajanje impulsa nije izmišljeno: zavisi od nezadatih kašnjenja. |
| 02-S10 | Zadatak 4c, naslov i tekst uz `fig:Zadatak_4c_CompleteBCDLogic` | Šema koja razrađuje samo a′ bila je opisana kao kompletan konvertor. Naslov i tekst sada navode njen stvarni obim. ERROR i ostali segmenti deo su apstraktnog bloka, a rešenja samostalnih zadataka b′–g′ nisu dopisana. | Pregled svih oznaka i grana šeme. |
| 02-V01 | `code/Zadatak_2/a/zadatak.vhd`, instanca UMUX | `T => 20 ns` → `T => T`; spoljni generički parametar ranije nije uticao na ponašanje. | GHDL sa T=7 ns: svaka promena očekivanog izlaza kasni 7 ns, i ne ostaje 20 ns. |
| 02-V02 | `code/Zadatak_3/{b,c}/decoder.vhd` i `3/a/zadatak.vhd` | Grana `others` tretirala je nepoznatu adresu kao 111, a nepoznatu dozvolu kao omogućeno kolo. Sada je 111 eksplicitna grana, a nepoznati ulazi daju X; sigurno isključeno kolo daje sve jedinice. Model bez enable takođe ne skriva nepoznatu adresu nulama. | GHDL: svih 64 binarnih kombinacija dozvola/adrese, U i Z na adresi, nepoznata dozvola, sigurno isključenje. Binarna funkcija ostala ista. |
| 02-V03 | `code/Zadatak_1/b/zadatak.vhd` | XOR zapisan kao A¬B+¬AB, u skladu sa dozvoljenim I, ILI i NE kolima i nacrtanom realizacijom. | Svih 16 ulaza; postojeći i nezavisni novi testbench. |

## Jezik i format

Tačni tekstualni zapisi pre/posle i pojedinačna obrazloženja nalaze se u [`nalazi_02_tekst.json`](../PROVERA/nalazi_02_tekst.json). Polje `line` beleži liniju u trenutku ispravke, jer prethodne ispravke menjaju dužinu fajla; za konačne lokacije koristiti stabilne LaTeX oznake i zajednički registar.

- Zadatak 1b: `eqref` za tabelu zamenjen `ref`; veza ka testbenču ispravljena sa poddirektorijuma a na b.
- Zadatak 3c i 4c: ručno upisani brojevi slika zamenjeni referencama na konkretne LaTeX oznake.
- Zadatak 4: dvosmislena formulacija gašenja E usklađena sa postojećim primerom 00A5→E; tabela primera dobila je prelom dugih zaglavlja unutar margina.
- Samostalni zadatak 1a: `2^(n+m)` → `2^{n+m}`, da ceo zbir bude eksponent.
- U celom tekstu ispravljene su ponovljene reči, slaganje padeža i greške poput „mutliplekser”, „jednacinom”, „sadrđaj”, „ospegu”, „doulazna”, „LE displej” i „Naraspolaganju”.
- VHDL primeri i prateće uputstvo drže se na istoj stranici; uklonjene su preduge dekorativne linije komentara. Testbenčevima dodata automatska poređenja; komentari o 16 umesto 8 kombinacija tri bita popravljeni.
- Jedini PNG (`Zadatak_2b.png`) sačuvan je kao izvorni materijal, a u dokumentu zamenjen TikZ/PDF crtežom iste mreže i rasporeda. Originalne Draw.io šeme očuvane su, uz tri navedene stručne ispravke.
- Postojeća dvostrana plava strelica Karnoove karte sačuvana je **bajt po bajt**, zajedno sa izvornim pozicijama i grupama; SHA-256 se proverava regresiono.

## Teorija, ograničenja i predlozi

Šenonovo razlaganje, binarno dekodiranje, De Morganove transformacije, pokrivanje susednih polja Karnoove karte i logika BCD segmenata provereni su algebarski i iscrpnim konačnim domenima. Broj testova nije potvrda vizuelnog pregleda. Za stručne dopune razlikujemo dokaz od pretpostavke:

1. **Kaskada BCD:** postavka traži kombinacionu funkciju trenutnog broja, a sačuvano izvorno rešenje ima povratnu spregu. Ono radi uz opisani protokol inicijalizacije. Predlog budućeg poboljšanja je da se globalna greška računa neposredno iz originalnih DCBA svake cifre, pre nametanja C0/D0. Time bi se izbegli pamćenje i potreba za INIT. Ta alternativa nije potajno uvedena u postojeću šemu.
2. **Minimum u samostalnom zadatku 2:** postavka ne definiše potpuno biblioteku „osnovnih kola”. Dodat zahtev da se biblioteka i deljenje međurezultata navedu. Privatna računska provera koristi NE, I i ILI sa proizvoljnim brojem ulaza, zajedničke međurezultate i besplatne konstante. Studentskom dokumentu nisu dodata rešenja.
3. **Dekoder 13 ulaza:** uravnoteženo stablo dvoulaznih I kola ima dovoljnu dubinu četiri, uz zanemareno kašnjenje invertora iz postavke. Provereno je svih 8192 minterma. To nije tvrdnja da je određena celokupna mreža globalno minimalna po broju kola.
4. **Simulacije hazarda:** vremenski zaključci važe za navedeni model i promenu jednog ulaza. Inertna dodela `after T` i privremena transportna varijanta proverene su odvojeno; simulaciona kašnjenja nisu tvrdnja o sintetizovanom hardveru.

Primarni izvori:

- Texas Instruments, [SN74HC00, SCLS181H](https://www.ti.com/lit/ds/symlink/sn74hc00.pdf), str. 1 i 3: četiri NI2 kola i raspored 14 priključaka; odeljak 6.7 razlikuje stvarna kašnjenja zavisna od uslova rada.
- Texas Instruments, [SN74HC153, SCLS112E](https://www.ti.com/lit/ds/symlink/sn74hc153.pdf), str. 1 i 3: dva multipleksera 4/1 i raspored 16 priključaka; odeljak 7.3, str. 9: tabela izbora podatkovnog ulaza.
- MIT 6.004, [Combinational Logic, odeljak 4.1](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c4/c4s1/), delovi o multiplekserima i „Glitches”: funkcionalna realizacija i uslovi pojave prolaznih grešaka. Konkretni prelazi u ovom materijalu provereni su zasebno, iz stvarnih VHDL putanja.

Mašinski dokazi izvršavanja: `../PROVERA/_build/math02.json`, `../PROVERA/_build/ghdl02.json` (ponovo se generišu, nisu zamena za izvore). Konačni vizuelni status određen je isključivo važećom potvrdom u `../PROVERA/rucni_pregled.json`.
