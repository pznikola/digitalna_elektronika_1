# Izveštaj 03 — dorada GS veza s019

## Poslednja dorada s019 — 2026-10-09

Po korisnikovom nalogu razdvojene su donje dve GS putanje u dijagramu. Sva četiri signala sada vode ka odgovarajućim ulazima I3/I2/I1/I0 bez ukrštanja ili preklapanja. Oznake, topologija, vidljivi tekst i nastavni tekst beležaka su očuvani. Lokalna izmena nalazi se u `slike/tikz/s019_koder_16_ulaza.tex`.

Novi slajd i cela A4 strana sa beleškama pojedinačno su pregledani; pogođene potvrde obnovljene su nakon pregleda. [Dokaz poređenja](poredjenje_gs_s019.json) potvrđuje da su svi otisci i prikazi ostalih 23 para identični prethodnoj verziji. Ostaju **24 slajda, 24 A4 strane i 94/94 potvrđena elementa**. `notes`, `review` i `check` prolaze; kompilacija je bez upozorenja. [Notes log](../../build/redizajn/dorada-gs-s019-2026-10-09/notes.log), [review log](../../build/redizajn/dorada-gs-s019-2026-10-09/review.log), [check log](../../build/redizajn/dorada-gs-s019-2026-10-09/check.log).

[Poređenje pre](../../build/redizajn/pre-razdvajanja-gs-s019-2026-10-09/pregled/novi/p-20.png) i [posle](../../build/redizajn/pregled/novi/p-20.png); [prethodna evidencija](istorija/pre-razdvajanja-gs-s019-2026-10-09/izvestaj.md). Status ostaje `ceka_odobrenje`: konkretni nalog nije prihvatanje cele prezentacije 03. Opis prethodne dorade s016–s021 ispod ostaje važeći, uz ovu ispravku prikaza s019; navedeni otisci na kraju odnose se na najnoviju verziju.

## Status — 2026-10-09

**Status: `ceka_odobrenje`.** Tekst s016–s021 približen je originalu; crteži i raspored su uređeni, a beleške usklađene sa dodatnim nastavnim sadržajem. Korisnik je izričito zatražio podelu s020 i s021 na po dve smislene celine. Novi s020b i s021b slede odmah iza odgovarajućih originalnih ID-jeva. Uz raniji s010b prezentacija sada ima **24 slajda**, a PDF beležaka **24 A4 strane**. Original i istorijska mapa imaju 21 slajd.

[Stvarni nalozi i odluke](odluke.md) odobravaju konkretnu doradu i ove podele, bez prihvatanja cele prezentacije 03. Nema novih otvorenih stručnih pitanja. Stil B, zamrznuta tema etf-v1, osnovna tipografija, autor Lazar Saranovac i školska godina 2021/22 očuvani su.

## Vidljivi sadržaj i šeme

| ID | Završena dorada |
|---|---|
| s016 | Vraćen odnos prema multiplekseru, upotreba u složenim/procesorskim sistemima, najveći aktivni indeks i dva adresna bita. Cela tabela, dve poslednje vrste i potreba za GS ostaju vidljivi. Tabela je kompaktnija i ima razdvojene vrste. |
| s017 | Vraćena mogućnost minimizacije i razlog direktnog crtanja pravilnih funkcija. Cela proširena tabela sa GS, pregledna prioritetna/koderska mreža, pravilne negacije i tačke na stvarnim spojevima. |
| s018 | Vraćeni samo jedna aktivna unutrašnja jedinica, lakša realizacija koderskog dela i lakše proširenje prethodne realizacije. Geometrija kompaktne šeme prilagođena je tako da zaključak ostane čitljiv. |
| s019 | Četiri osnovna kodera i koder drugog nivoa imaju poravnate priključke, odvojene lokalne/globalne oznake i četiri pregledne GS putanje. Vraćeni izbor prioritetne grupe, problem nižih bitova, zabrana direktnog spajanja i potreba za dodatnim I/O. |
| s020 | Prva celina originala: EI, nule na adresnim izlazima pri zabrani i značenje uslovljenog GS. Puna unutrašnja šema kodera sa EI/EO ima više prostora i čitljive oznake. |
| s020b | Druga celina: EO i prenos dozvole/zabrane. Vidljivo je zašto invertovani GS nije dovoljan ni u uslovljenoj ni u neuslovljenoj varijanti; izdvojena je njegova realizacija pomoću invertora i I gejta. |
| s021 | Cela mreža 16/4 prikazana je preko širine slajda. Četiri kodera su poravnata; EI/EO lanac je izdvojen iznad njih, a GS i adresne putanje ispod. Oba četvoroulazna ILI gejta i drugi nivo kodera čuvaju originalnu funkciju. |
| s021b | Druga celina: visoka impedansa, mogućnost direktnog objedinjavanja i pravila MSI simbola. Prikazan je jasan generički simbol sa svim oznakama; pravila iz originala naglašena su tamnocrveno. |

Precrtani/prilagođeni vektorski izvori: `prioritetno_jezgro.tex` (s017/s020), `koder_prioriteta_simbol.tex` i `s019_koder_16_ulaza.tex`, `s018_minimalniji_koder.tex`, `s021_koder_sa_enable_lancem.tex`; novi `s020b_eo.tex` i `s021b_simbol_kodera.tex`. Oznake ostaju **9 pt** u konačnoj projekciji, tabele s016/s017 koriste 10/12 pt. Menjaju se lokalna geometrija i raspored, bez smanjivanja celog slajda ili slova pomoću skaliranja. Vodovi ne prolaze kroz gejtove; stvarna grananja imaju tačke, nevezana ukrštanja ih nemaju.

## Beleške i pokrivenost

[Mapa pokrivenosti](pokrivenost.md) ima **94/94 potvrđena elementa**: 71 izvornu grupu, 20 dopuna i tri nastavka postojećih dopuna. Izvorni sadržaj s020/s021 raspodeljen je prema [mapi s020](mapa_podele_s020.json) i [mapi s021](mapa_podele_s021.json); izvorni katalog nije promenjen. Odobrenje je u [zapisu podele](odobrenje_podela.json).

Beleške s016 objašnjavaju X i validnost koda 00; s017 daju sve prioritetne međusignale i izlazne jednačine; s018 potpune korake pojednostavljenja; s019 primer pogrešnog objedinjavanja lokalnih kodova. S020 objašnjava lokalni zahtev H i uslovljeni GS, a s020b izvodi EO i potpuno tumači tri slučaja prenosa dozvole, uključujući neuslovljeni GS. S021 prati primer I10/I5/I1 i prazan lanac; s021b razjašnjava visoku impedansu, uslov jednog aktivnog drajvera i značenje priključaka. Vraćeni vidljivi tekst ne prepisuje se bez potrebe. Beleške ne sadrže istoriju dorade, poreklo, zahteve za odobrenje ili uredničke komentare; to je u [evidenciji](evidencija_beleski.json).

## Pregled i provere

Svih **osam pogođenih projekcija i osam celih A4 strana** pregledano je uz originale i prethodni prikaz. Proverene su sve veze, negacije, izlazne oznake, formule i tabele. Nema preklapanja, odsecanja, nečitljivih oznaka ili nepokrivenog sadržaja.

Ostalih **16 projekcija i 16 celih A4 strana** pikselno je identično neposredno prethodnoj verziji. Njihovi lokalni izvori i pokrivenost su nepromenjeni, pa su prethodne sadržinske potvrde sačuvane uz [dokaz poređenja](poredjenje_dorade_s016_s021.json). Pogođene [potvrde](pregled.json) obnovljene su nakon stvarnog pregleda, uz proveru da ponovljena izgradnja nije promenila pregledane prikaze.

Završne komande prolaze, kod izlaza **0**:

```bash
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije notes
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije review
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije check
```

`check`: **PROVERENO**. Postojeće nezavisne računske provere uključuju obe tabele, kompaktne jednačine, zabranu EI i svih **65536 ulaznih kombinacija** mreže 16/4. Dodatno su provereni svi slučajevi EO i primeri iz beležaka; [logički dokaz](logicka_provera_s016_s021.json). Završni logovi oba PDF-a nemaju upozorenja, prekoračenja prostora, nedostajuće znakove ili greške. [Notes log](../../build/redizajn/dorada-s016-s021-2026-10-09/notes.log), [review log](../../build/redizajn/dorada-s016-s021-2026-10-09/review.log), [check log](../../build/redizajn/dorada-s016-s021-2026-10-09/check.log).

## Isporuka i poređenje

- [Prezentacija — 24 slajda](../../build/03_kola_srednjeg_stepena_integracije.pdf)
- [Beleške — 24 A4 strane](../../build/03_kola_srednjeg_stepena_integracije_beleske.pdf)
- [Uporedni pregled sa originalima i beleškama](../../build/redizajn/pregled/index.html#03-s016)
- [Neposredno prethodni prikazi](../../build/redizajn/pre-dorade-s016-s021-2026-10-09/pregled/index.html)
- [Prethodni izveštaj s011–s015](istorija/pre-dorade-s016-s021-2026-10-09/izvestaj.md)
- [Sačuvani prethodni izvori](istorija/pre-dorade-s016-s021-2026-10-09/izvori/)

| Primer | Pre | Posle |
|---|---|---|
| Prioritetna mreža s017 | [Pre](../../build/redizajn/pre-dorade-s016-s021-2026-10-09/pregled/novi/p-18.png) | [Posle](../../build/redizajn/pregled/novi/p-18.png) |
| Proširenje s019 | [Pre](../../build/redizajn/pre-dorade-s016-s021-2026-10-09/pregled/novi/p-20.png) | [Posle](../../build/redizajn/pregled/novi/p-20.png) |
| EI/EO s020 | [Pre](../../build/redizajn/pre-dorade-s016-s021-2026-10-09/pregled/novi/p-21.png) | [EI](../../build/redizajn/pregled/novi/p-21.png), [EO](../../build/redizajn/pregled/novi/p-22.png) |
| Kompletna mreža s021 | [Pre](../../build/redizajn/pre-dorade-s016-s021-2026-10-09/pregled/novi/p-22.png) | [Mreža](../../build/redizajn/pregled/novi/p-23.png), [druga celina](../../build/redizajn/pregled/novi/p-24.png) |

Izlazi u `build/` ne verzionišu se; komande ih obnavljaju iz izvora. Originalni PDF, istorijska mapa, zamrznuta tema i druga predavanja nisu menjani.

## Otisci pregledane verzije

| Resurs | SHA-256 |
|---|---|
| Originalni PDF | `5e68d267ca2f60c1ccdf073c2579fd64a4b05278955cc3d3f920cc54e123fd86` |
| Izvorna mapa | `a3effdb79779d04df05ce98ece642a6068684e4b798018cc96122479136266cc` |
| Manifest redizajna | `c77f0c3144c5e00840a8da914fb4c521a893b4f8cc68c6a2c613d28c1415238f` |
| Zapis izgradnje | `86fbddb97e20a60dceee5a71828d22d7554b3a51f110563c7eda04475ced9e3a` |
| Potvrde pregleda | `cc1c7d1241112475f9010bbc024031edd5ec6366283b03fe5756e22bf0bb8a8e` |
| Pokrivenost | `2e956948e08c5be06ad78bdca50e335f7e76101dfd54409c2bc5ae9ae638fea5` |
| Evidencija beležaka | `a91bc45ee61c64b7808927402d7980db3b5ea7a5831ee32141a0895f32c9d575` |
| Prezentacioni PDF | `713a46513df80ba989f7871f0a120749d07685e8499f6f195b08bdbe60b0529a` |
| PDF beležaka | `be857373cd36fc2c3ad4be164064bc7ccf2a5f8529c995b5742312b92c3faab6` |
| Odobrenje podele | `8dd8718fd9e5358d432dbea86c837b2b9f5d06946e447b9570afa7669ad923bb` |
| Dokaz nepromenjenih prikaza | `88d75990e060512366d4172939094dac71b50c020282e91bb7d37c2349710298` |
| Dokaz razdvajanja GS s019 | `66b45017efc8b016218452742fbb0d1793ef603d40bb42d8bbaaef063acfe703` |
| Logički dokaz | `b3c0da6b9d58583b3550bf4dc8b06124117be02a7d555e0ae20dc165d36292ff` |
| Manifest teme | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |

## Nastavak

Tražena dorada s016–s021 i razdvajanje GS veza s019 su završeni. Sledeća radnja je korisnikov pregled ove verzije 03; status `ceka_odobrenje`. Cela prezentacija 03 još nije prihvaćena. Ranije dorade ostaju očuvane. Novi agent proverava relevantne otiske i nastavlja po korisnikovom nalogu bez ponavljanja završene analize nepromenjenih izvora. Izmene beležaka ili prikaza poništavaju pogođene potvrde.
