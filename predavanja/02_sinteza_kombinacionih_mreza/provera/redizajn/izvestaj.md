# Predavanje 02 — dorade s047–s054

**Status: `odobreno` · 2026-10-05.** Korisnik je prihvatio završenu prezentaciju i prateće beleške porukom „ok, prihvati 02 prezentaciju. Zavrsili smo sa njom“. Nema otvorenih stručnih pitanja. [Zapis odobrenja](odobrenje_rezultata.json) vezuje odluku za otiske prihvaćene verzije.

## Obuhvat i verzija

Originalni PDF je neizmenjen: 27 strana i 54 izvorna slajda. Korisnik je tražio podelu s048 i isti postupak za s049. Prezentacija i A4 beleške sada imaju po **62 strane**; s048b/s049b dolaze odmah iza svojih originalnih ID-jeva. Prethodnih šest nastavaka s002b/s009b/s015b/s023b/s024b/s032b ostaje isto. Svi originalni ID-jevi i njihov međusobni redosled su očuvani; originalna mapa ostaje neizmenjena. Katalog broji 620 originalnih, ukupno 628 projektovanih strana uz osam pojedinačnih izuzetaka. Stil B, zamrznuta tema etf-v1, fontovi, LuaLaTeX, autorstvo i godina 2021/22 nisu menjani.

## Poređenja pre/posle i pokrivenost

| ID / izlazna strana | Pre ove dorade → sada |
|---|---|
| s047 / 53 | Skraćen uvod i izbor kućišta → potpunije grupisanje na račun kašnjenja, isti izraz F, tri dvoulazna I u jednom čipu, druge potrebne vrste i ukupno tri kućišta. |
| s048 / 54 | NI transformacija i skraćeno poređenje na jednom slajdu → prva celina sa sva tri algebarska koraka, tačnim minimalnim brojem kola u tri vrste čipova i ograničenjem dokaza minimalnosti. |
| s048b / 55 | Novi odobreni nastavak: sva tri koraka zamene troulaznog NI, povećano kašnjenje, 4+3+2=9 i tri ista čipa; alternativa četiri NI plus preostali invertor u dva kućišta; popust na količinu i pitanje 1+1 naspram 3 bez opšteg odgovora. |
| s049 / 56 | Skraćena NILI realizacija na jednom slajdu → prva celina sa svim koracima, najmanje četiri invertora, tri dvoulazna i jednim troulaznim NILI, tri različite vrste čipova i ograničenjem minimalnosti. |
| s049b / 57 | Novi odobreni nastavak: zamena troulaznog NILI i 4+3+3=10, tri ista čipa; izvorni zadatak poređenja jednostepene složene CMOS realizacije uz dostupne komplementne ulaze. |
| s050 / 58 | Kratke definicije → izvorni uzroci različitih kašnjenja, početno i očekivano konačno stanje za lažnu nulu/jedinicu, glič i postojeći primer F; isti crtež. |
| s051 / 59 | Sažet rezultat → početno/konačno stanje, promena samo B, očekivana jedinica i naglašeno ALI/lažna nula; iste pretpostavke i oba neizmenjena vektorska crteža, tp ostaje iznad signala. |
| s053 / 61 | Skraćeno objašnjenje i jedna početna puna kontura → površine sa B=0/B=1, zajednička strana bez zajedničkih polja, promena jedne promenljive, lažna nula i odstupanje od minimalnosti; obe početne konture isprekidane, samo povezujuća puna. Ranije odobrena F i crveni dodatni član su isti. |
| s054 / 62 | Skraćen završni tekst → povezivanje nula u proizvodu zbirova, lažna jedinica, više promenljivih ulaza, različita kašnjenja do I/ILI dela, dodatne komponente/invertori ili preuređivanje, odstupanje od minimalnog oblika, heuristika/simulacija i iskustvo projektanta. |

Pokriveno je **231/231 elemenata**: 170 izvornih grupa i 61 dopuna. **102 elementa** imaju odredište u beleškama. Finiji popis delova s048/s049 ne dodaje originalno gradivo. [Mapa pokrivenosti](pokrivenost.md), [mapa podela](mapa_podela.json) i [odobrenja](odobrenje_podela.json) povezuju stare izvorne grupe sa oba nova dela.

Nema precrtanih električnih šema: na s053 promenjen je samo stil dve početne konture; karte, mintermi i ranije odobrene formule s052/s053 sa barC su očuvani. NI/NILI međukoraci vraćeni su iz originala. Jezički sređeni zapisi: „koristimo sa NI ili NILI“ → „za realizaciju NI ili NILI kolima“, „dvoulazana“ → „dvoulazna“, „Ne postoji generalna odgovor“ → „Nema opšteg odgovora“. Očuvan je tačan broj kola/čipova. Prethodni opis s048 „invertor iz čipa sa četiri NI kola“ zamenjen je izvornom raspodelom: invertor iz šestostrukog invertorskog čipa, uz četiri NI u drugom kućištu. Nema novih stručnih izmena ni otvorenih predloga.

## Beleške

Potpuniji izvorni tekst ovih slajdova sada je vidljiv; beleške daju samo dodatno nastavno objašnjenje. Na s047 ostaju uloge tri I kola, jedno slobodno kolo i kritična putanja. Na s048/s049 objašnjeni su De Morganovi međusignali i razlika ekvivalentnosti/minimalnosti. Na nastavcima su potpuni međusignali zamene, raspodela i slobodna kola, uz smisao poređenja cene odnosno CMOS površine. Na s050 ostaje tumačenje direktne i zakašnjele komplementne putanje; izvorni uzroci kašnjenja više se ne prepisuju. Na s051 ostaju događaji u tri vremenska intervala i uslovi modela. Na s053 ostaje dokaz konsenzusa i putanja polje 3 → 1. Na s054 ostaju mehanizam lažne jedinice, međukombinacije više ulaza i očuvanje polariteta pri dodavanju invertora; izvorni završni tekst više se ne ponavlja.

Izvorni vremenski detalji s051:e03 ostaju povezani sa beleškama. Sav drugi sadržaj prenet u ranijim doradama ostaje na istim odredištima. [Evidencija beležaka](evidencija_beleski.json) čuva poreklo i dokaze odvojeno od nastavnog teksta, bez njegove druge kopije. Nema vidljivih uredničkih komentara, istorije ispravki ili odluka.

## Pregled i provere

Pročitani su originalni slajdovi PDF strana 24–27, prethodni i novi lokalni izvori i beleške. Stvarno su pregledani ceo konačni prikaz svakog od devet pogođenih ID-jeva i njegove A4 beleške: oznake, formule, negacije, računi, izbor kućišta, ćelije i konture, dijagrami, naslovi i razmaci. Nema preklapanja, odsecanja, smanjenja fonta ili izostavljenih nastavnih detalja.

[Poređenje prikaza](poredjenje_dorade_s047_s054.json) dokazuje da ostalih **53 slajda i nastavna A4 prikaza** ostaju isti: cele projektovane slike su pikselno jednake; za pomereni s052 razlikuje se samo broj A4 strane u donjem podnožju. Tela, zaglavlja i nastavni izvori ostaju isti. Promene zajedničkih otisaka ograničene su na odobrenje podela, manifest/glavni izvor i generisane veze sa novim redosledom. Potvrde nepogođenih slajdova očuvane su uz taj dokaz; devet pogođenih potvrda obnovljeno je nakon stvarnog pregleda.

Iscrpno su provereni grupisanje/NI/NILI oblici funkcije za **16 kombinacija DCBA**, obe zamene troulaznih kola za **8 kombinacija XYZ**, konsenzus i kartirani mintermi za **8 kombinacija CBA**, te niz izlaza **1 → 0 → 1** u modelu zakašnjelog invertora. Provereni su računi devet/deset kola i raspodela kućišta. Originalni PDF, istorijska mapa i korišćena zajednička tema ostaju isti.

Komande završavaju izlaznim kodom 0:

```bash
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza notes
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza review
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza check
```

**`check`: PROVERENO.** Postojeće računske i strukturne provere prolaze. Oba konačna LaTeX loga su bez grešaka, upozorenja i prekoračenja prostora. Svih 62 ID-ja povezano je sa odgovarajućim slajdom i beleškama. Alati nisu menjani.

[Notes log](../../build/redizajn/dorada-s047-s054-2026-10-05/notes.log), [review log](../../build/redizajn/dorada-s047-s054-2026-10-05/review.log), [check log](../../build/redizajn/dorada-s047-s054-2026-10-05/check.log).

## Isporuka i nastavak

- [Prezentacija — 62 slajda](../../build/02_sinteza_kombinacionih_mreza.pdf); dorade na stranama **53–59 i 61–62**.
- [PDF beležaka — 62 A4 strane](../../build/02_sinteza_kombinacionih_mreza_beleske.pdf).
- [Uporedni pregled](../../build/redizajn/pregled/index.html).

Neposredno prethodna verzija sa 60 strana sačuvana je u `istorija/pre-dorade-s047-s048-2026-10-05/izvori-i-evidencija.tar.gz`, sa [tadašnjim izveštajem](istorija/pre-dorade-s047-s048-2026-10-05/izvestaj.md). Tadašnji prikazi nalaze se u `build/redizajn/pre-dorada-s047-s048-2026-10-05/`; naziv arhive odgovara prvom nalogu ove objedinjene dorade. Prethodne arhive i odluke ostaju istorija. Generisani PDF/PNG/HTML i logovi u `build/` ne verzionišu se; obnavljaju se gornjim komandama.

Predavanje 02 je završeno i odobreno. Preostali zadaci: nema. Pri nastavku proveriti relevantne otiske iz [zapisa odobrenja](odobrenje_rezultata.json); ako su isti, preskočiti završenu analizu 02. Ranija zasebna dozvola za početak 03 ostaje važeća; ovom porukom nisu prihvaćeni rezultati drugih predavanja. Prethodni izveštaj koji je čekao odluku sačuvan je [u istoriji](istorija/pre-odobrenja-2026-10-05/izvestaj.md).

## SHA-256 pregledane verzije

| Resurs | Otisak |
|---|---|
| Originalni PDF | `f631914c9f32a0472f4fa3af11115abaadb9316dfcf6f1528cd91ef4d28868f4` |
| Izvorna mapa | `b2c8e07fa123a40da68c8b89b1b1c6ce88112e90c7417792cdec341d60136ca2` |
| Manifest | `9cee4786e297b7979acf11d39a44f004dfa586e1623d55b92a62b968a812755f` |
| Odobrenje podela | `8ccd96066474d679f2c64c0ff94d88608bf082ab96c4bd408342f598e9c7867f` |
| Prezentacioni PDF | `e2bce5e724ce41cce7c7df3ab52f7503349fa1505e13196c2e3dc27ebd8481c3` |
| PDF beležaka | `460ed29d80122ddfb70099770bab41eb6a70aa039b07c5a09d691c87e6ec432e` |
| Zapis izgradnje | `b7cebc207fa99e1bdc80bc90d080377e77f3027c68bfe6877ed74044900e37e5` |
| Potvrde pregleda | `b601434886d3f5cef4bcde593e84a3f45cbe9b04fb10323ff05027c019006fd1` |
| Evidencija beležaka | `5ccd5f4578909d6f9310855c2643bc5e9af6947f460e936b43c9a63ddb99df57` |
| Poređenje prikaza | `b974d4054d2a987f1f75de20c35c28a654ed722ffb1a931c33db6c5a91d9e3d2` |
| Arhiva prethodne isporuke | `145cef5b1318fb40fc2b69e8c661a2c5ea4cd68369104d50aab4f5842f7bf3ee` |
| Odobrenje rezultata | `d66d9546852d11ec4a54b7c6a327eaf20de4c50aca3a88f8e01bab3651bcb790` |
