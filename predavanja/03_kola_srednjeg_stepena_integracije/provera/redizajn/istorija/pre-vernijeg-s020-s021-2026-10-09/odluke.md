# Odluke

Datum evidentiranja: 2026-10-01T10:00:37.756128+00:00

Korisnikova poruka o početku:

> ako je 02 zavrseno kreni na 03

Uslov je ispunjen: završni izveštaj 02 potvrđuje 54/54 slajda i 152/152 sadržajna elementa, a ponovljena komanda `make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza check` dala je `PROVERENO`. Poruka odobrava početak 03; rezultat 02 nije zasebno prihvaćen.

Odobrenje rezultata: nema. Prelazak na sledeće: nije odobren.

Otvoreno pitanje zatraženo od korisnika tokom obrade 03 (nije odobrenje):

> Na slajdu 03-s004 original tvrdi da dva dvoulazna NI kola mogu zameniti jedno troulazno NI kolo, ali prikazana jednačina važi za I kola, a ta NI kaskada nije ekvivalentna. Da li da ispravim tvrdnju i prikažem ispravnu realizaciju (uz dodatnu inverziju), ili da zadržim izvorni zapis i jasno označim grešku u beleškama?

Korisnikova kasnija stručna odluka:

> na slajdu s004 umesto NI kola stavi I kola. To ima vise smisla jer onda zaista 2 I kola menjaju jedno troulazno I kolo. Takodje, zamolio bih te da ne ostavljas komentare u prezentacijama. Prezentacije treba da sadrze samo ono sto PDF-ovi sadrze kao sto to pise u PLAN_PREDAVANJA.md

Odluka je primenjena: na s004 stoje I kola i jednakost za kaskadu I kola; izvorna NI tvrdnja dokumentovana je u beleškama. Urednički komentari uklonjeni su iz projektovanih slajdova. Ovo nije odobrenje završene prezentacije niti prelaska na 04.

## Ponovni pregled i dorada — 2026-10-02

> Procitaj PLAN_PREDAVANJA.md i prodji kroz generisanu 03 prezentaciju i kroz originalno 03 predavanje.  Po uzoru na 01 prezentaciju sredi i 03

Poruka odobrava ponovni pregled i doradu 03. Ranija ispravka I kola na s004 ostaje važeća. Ovo nije odobrenje rezultata 03 niti početka 04.

## Dorada beležaka prema novom planu — 2026-10-02

> procitaj PLAN_PREDAVANJA.md.  tvoj posao je da procitas PLAN, procitas slajdove 03, procitas originalna predavanja 03 i da napises beleske po planu

Nalog odobrava čitanje originala i slajdova 03 i prepravku beležaka prema novom koraku 6. Ne odobrava novi rezultat niti doradu drugih predavanja. Odobrena I realizacija na s004 ostaje neizmenjena. Urednička istorija više nije deo PDF-a beležaka; raniji navod u ovom dokumentu o njenom smeštanju u beleške opisuje prethodnu verziju. Izvorni tačan NI invertorski slučaj ostaje kao nastavno objašnjenje, a poreklo ispravke u ovoj evidenciji i arhiviranom izveštaju.

## Odobrena terminološka zamena — 2026-10-09

Korisnikova stvarna poruka nakon liste tri pojavljivanja:

> zameni sve

Korisnik je zatim izričito zatražio primenu plana „Zamena termina „kapija“ u slajdovima“. Za 03 odobrene su samo zamene „logičkih kapija“ → „logičkih gejtova“ u uvodu i „Broj kapija“ → „Broj gejtova“ u zaglavlju tabele na 03-s002. Ovo je dozvola za te terminološke izmene i obnovu pogođenih potvrda; ne predstavlja prihvatanje cele prezentacije 03 ili novih beležaka.

## Dorada s004/s007–s010 i odobrena podela — 2026-10-09

> za predavanje 03:
> s004: priblizi sadrzaj teksta generisanog slajda originalnom slajdu. naravno preformulisi i ulepsaj.
> s007: priblizi tekstualni sadrzaj originalu.
> s008: priblizi tekstualni sadrzaj originalu
> s009: sredi dijagram dekoder 4/6. Priblizi tekstualni sadrzaj originalu ali tako da sve i dalje moze da stane na jedan slajd.
> s10: Originalni slajd je potrebno podeliti na 2 slajda s obzirom da ima dosta teksta. Podeliti originalni slajd na 2 smislene celine. Srediti dijagram tako da se poklapa logicki sa originalnim dijagramom

Odobrena je navedena dorada i podela isključivo 03-s010 na s010/s010b. Originalni dekoder s009 je 4/16 (četiri adresna ulaza, 16 izlaza); zapis „4/6“ u poruci tumači se prema prikazanom originalu. Sačuvana je ranija stručna odluka o I kolima na s004. Nalog nije prihvatanje završene prezentacije niti odobrenje drugih podela.

## Dorada s011–s015 — 2026-10-09

Korisnikova stvarna poruka:

> s011: Tekstualni sadrzaj priblizi orgiginalnom slajdu
> s012: Na originalnom slajdu nisu nacrtani dijagrami kako treba. Nadji na internetu kako treba da izgleda ovo i nacrtaj ga u stilu dekodera sa slajda s008. Priblizi tekst originalnom slajdu.
> s013: Priblizi tekst originalnom slajdu
> s014: Priblizi tekst originalnom slajdu. Desna horizontalna strelica treba da pokazuje od levog mux-a ka desnom mux-u. A dijagonalna strelica treba da pokazuje da se Funkcija F realizovana pomocu desnog mux-a.
> s015: Mozda smanji malo font i dijagrame tako da moze da stane ideja sa originalnog slajda na sam slajd. Trenutno ruzno izgleda, bolje je smanjiti font i dijagrame nego ga natrpati

Nalog odobrava konkretnu doradu i dovršavanje pogrešnih/nedostajućih prikaza s012 uz proveru na internetu. Proveren je zvanični Nexperia datasheet 74HC238, Rev. 8, Fig. 3 i Table 3: aktivno visoki E3 koristi se kao podatak, oba aktivno niska enable ulaza i A2 vezuju se na nulu. Iz toga je izvedena nenegirana nastavna šema 1/4, bez pretvaranja apstraktnog simbola u fizički pinout. Izvor i izvođenje dokumentovani su u evidencija_beleski.json.

Na s015 korisnik izričito dopušta manji font i dijagrame. Font je lokalno 10/12 pt; oznake šema ostaju najmanje 9 pt. Geometrija crteža je smanjena, bez skaliranja slova ili celog slajda. Uređene su i beleške istih pet ID-jeva, prema planu.

Ovaj nalog ne prihvata celu prezentaciju 03, ne daje novi strukturni izuzetak i ne odobrava početak drugog predavanja. Broj ostaje 22 slajda sa već odobrenim s010b.

## Dorada s016–s021 i podele s020/s021 — 2026-10-09

Korisnikova stvarna poruka:

> s016: Priblizi tekst originalnom sadrzaju teksta
> s017: nacrtaj dijagram lepsa, smanji ga slobodno malo ako treba ali bitno je da su komponente i linije nacrtane lepo i citljivo. Pribliziti tekst originalnom slajdu
> s018: pribliziti tekst originalnom slajdu
> s019: Nacrtati lepse dijagram. Smanjiti font ako treba na dijagramu. Pribliziti sadrzaj teksta originalnom slajdu
> s020: Originalni slajd ima previse teksta. Razbiti originalni slajd na dve smislene celine. To ce nam ostaviti onda mesta da se dijagram lepse nacrta. Pribliziti tekstualni sadrzaj originalnom slajdu
> s021: Isto kao za s020. Za s021 ima smisla smanjiti font na dijagramu kako bi lepsi dijagram mogao da se nacrta

Korisnik odobrava doradu navedenog teksta i crteža, uz lokalno smanjenje dijagrama i njihovih oznaka ako je potrebno. Originalni s020 podeljen je na EI i unutrašnju šemu (s020), odnosno EO i prenos zabrane (s020b). Zahtev „Isto kao za s020“ za s021 tumači se kao podela na kompletnu mrežu 16/4 (s021) i visoku impedansu/pravila simbola (s021b). Oznake crteža ostaju 9 pt; geometrija je prilagođena bez skaliranja celog slajda. Tabele s016/s017 imaju razdvojene vrste i lokalni font 10/12 pt.

Uz ranije odobreni s010b sada su 24 projektovana slajda i 21 izvorni slajd. Postojeći izvorni ID-jevi i njihov redosled ostaju očuvani. Nalog ne prihvata celu prezentaciju 03 niti odobrava druge podele.

## Razdvajanje GS vodova s019 — 2026-10-09

Stvarna korisnikova poruka:

> s019: sredi deo dijagrama sa slike tako da se signali ne preklapaju

Odobrena je lokalna geometrijska dorada GS veza. Priključci, funkcija, tekst, beleške, broj/redosled/ID-jevi ostaju isti. Ovaj nalog nije prihvatanje cele prezentacije 03.
