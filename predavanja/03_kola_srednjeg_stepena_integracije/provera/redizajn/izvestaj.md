# Izveštaj 03 — verniji tekst i šeme s020/s021

## Status — 2026-10-09

**Status: `ceka_odobrenje`.** Završene su tražene dorade s020, s020b, s021 i s021b, uključujući dodatne zahteve za urednije invertore i GS spoj na s020 i za lepše vođenje šeme s021. [Stvarne poruke](odluke.md) odobravaju konkretne izmene; cela prezentacija 03 još nije prihvaćena. Nema otvorenih stručnih pitanja.

Ostaju **24 slajda i 24 A4 strane beležaka**. Očuvani su svi postojeći ID-jevi i redosled: 21 izvorni slajd i tri prethodno odobrena nastavka s010b/s020b/s021b. Dodatna podela nije bila potrebna. Ranije dorade s004–s019, uključujući odvojene GS veze s019, ostaju očuvane. Stil B, tema etf-v1, fontovi, autor Lazar Saranovac i školska godina 2021/22 su sačuvani.

## Vidljivi tekst i raspored

| ID | Šta je vraćeno iz originala i uređeno |
|---|---|
| s020 | Celokupan uvodni tok: aktivan EI daje validne A1/A0, neaktivan ih postavlja na nule; uslovljeni GS može biti nula zbog odsustva zahteva ili zabrane iz višeg prioriteta; potreban je EO koji dozvoljava nižem koderu da koduje. Puna interna šema ostaje vidljiva. |
| s020b | Prenos dozvole od višeg ka nižem prioritetu, obe varijante GS i razlozi zbog kojih njihova inverzija ne može zameniti EO. Vidljiva su sva tri izvorna slučaja: dozvoljeno bez zahteva → dozvoli nižima; dozvoljeno sa zahtevom → zabrani nižima; zabranjeno → prenesi zabranu. |
| s021 | Kompletna mreža 16/4 sa četiri kodera prvog nivoa, EI/EO lancem, četiri GS veze ka drugom nivou i oba ILI4 za niže bitove. Uz šemu je vraćen izvorni tekst o visokoj impedansi, direktnom povezivanju i mogućem izostavljanju ILI4. |
| s021b | Zasebna celina o MSI simbolima: nema jednog strogog načina crtanja, ulazi i izlazi idu na različite strane bez mešanja, često ulazi levo/izlazi desno. Zadržan je generički simbol koji to ilustruje. |

Preformulisanje čuva smisao originala; sve nastavne tvrdnje sa originalnih s020/s021 nalaze se u odgovarajućim odobrenim parovima. [Mapa s020](mapa_podele_s020.json) vraća uvod u EO u prvi deo, a [mapa s021](mapa_podele_s021.json) vraća visoku impedansu uz kompletnu mrežu. Izvorni katalog i istorijska mapa nisu menjani.

## Šeme

Nova lokalna interna šema je `slike/tikz/s020_koder_ei_eo.tex`. Sve negacije, prioritetni proizvodi, uslovljavanje EI, ILI izlazi i EO su očuvani. Inverzije imaju jednake simbole i odvojene izlazne vodove; komplementne grane imaju svoje vertikale, sa jasnim tačkama stvarnog grananja. GS se crta jednom: izlazna vertikala ima zasebnu tačku grananja ka invertoru i produženje ka svojoj oznaci. Izlazne oznake A1/A0/GS/EO su poravnate, a debljine linija simbola i vodova ujednačene. Oznake ove šeme su 9 pt. Zajednički izvor s017 nije menjan.

`slike/tikz/s021_koder_sa_enable_lancem.tex` sada ima četiri jednaka, vertikalno poravnata kodera, koder drugog nivoa desno i dva kompaktna ILI4 ispod. Adresni vodovi imaju zasebne vertikale i dovoljan razmak od gejtova. GS putanje su odvojene; nevezana ukrštanja nemaju tačke. Lokalni A1/A0 drugog nivoa pravilno su označeni kao globalni A3/A2 na izlazu. Korisnik je izričito dozvolio manji font u dijagramu: oznake su 7,8 pt, uz nepromenjen font teksta slajda. Geometrija je uređena bez automatskog smanjivanja celog slajda.

[Ručno proverena topologija i veze](topologija_s020_s021.json) dokumentuju svaku funkcionalnu granu obe šeme. Nema promena formula, polariteta, funkcije ili topologije originala; popravljene su geometrija i jasnoća prikaza.

## Beleške i pokrivenost

Svih **94/94 elemenata** ima potvrđeno odredište; broj obuhvata 71 izvornu grupu, 20 dopuna i tri nastavka postojećih dopuna. [Mapa pokrivenosti](pokrivenost.md) prati svaki element. Uvod u EO i tekst o visokoj impedansi vraćeni su na prve delove postojećih parova, uz ista izvorna porekla.

Beleške s020 objašnjavaju H, GS=EI H i uslovljavanje međusignala. S020b zadržava potpuno izvođenje EO, primer zabrane kroz praznu srednju grupu i rad neuslovljenog GS, bez prepisivanja tri slučaja koji su sada jasni na slajdu. S021 zadržava primer I10/I5/I1, lokalne/globalne bitove i potpune uslove za direktno objedinjavanje izlaza visoke impedanse. S021b tumači priključke i odnos 4/2. Formula EO i njeni međukoraci nalaze se u beleškama; dodatni izdvojeni crtež iz prethodne s020b zamenjen je izvornim nastavnim tekstom, dok cela izvorna interna šema ostaje na s020.

Beleške sadrže samo dodatni nastavni sadržaj. Poreklo, odluke i istorija su u [evidenciji](evidencija_beleski.json). Sačuvani su ID-jevi i nevidljiva sidra; naslovi u manifestu i A4 dokumentu usklađeni su sa novim slajdovima. Nastavne dopune su proverene; jezičke greške originala „ne prvi pogled“ i „ne uslovima GS“ zamenjene su pravilno formulisanim objašnjenjima. Stručne tvrdnje nisu menjane.

## Pregled i provere

Pojedinačno su pregledana **sva četiri nova slajda i sve četiri cele A4 strane**, uz originale i prethodnu verziju. Provereni su smisao teksta, veze, negacije, priključci, spojevi, oznake, formule, čitljivost i prostor oko simbola. Nema preklapanja, odsecanja, nečitljivih oznaka ili nepokrivenih celina.

[Dokaz poređenja](poredjenje_vernijeg_s020_s021.json) potvrđuje da su lokalni izvori, svi otisci i prikazi ostalih **20 slajdova i 20 celih A4 strana identični** neposredno prethodnoj verziji. Njihove sadržinske potvrde ostaju važeće. Pogođene [potvrde](pregled.json) obnovljene su nakon stvarnog pregleda; ponovljena izgradnja nije promenila pregledane prikaze.

Završne komande daju kod izlaza **0**:

```bash
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije notes
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije review
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije check
```

`check`: **PROVERENO**. Oba PDF-a kompajlirana su bez upozorenja, prekoračenja prostora, nedostajućih znakova ili grešaka. Postojeća nezavisna računska provera prolazi, uključujući svih **65536 kombinacija** kodera 16/4. Računski rezultat dopunjuje ručni pregled šema, umesto da ga zameni. [Notes log](../../build/redizajn/verniji-s020-s021-2026-10-09/notes.log), [review log](../../build/redizajn/verniji-s020-s021-2026-10-09/review.log), [check log](../../build/redizajn/verniji-s020-s021-2026-10-09/check.log).

## Isporuka i poređenje

- [Prezentacija — 24 slajda](../../build/03_kola_srednjeg_stepena_integracije.pdf)
- [Beleške — 24 A4 strane](../../build/03_kola_srednjeg_stepena_integracije_beleske.pdf)
- [Uporedni pregled sa originalima i beleškama](../../build/redizajn/pregled/index.html#03-s020)
- [Prethodni izvori i evidencija](istorija/pre-vernijeg-s020-s021-2026-10-09/izvestaj.md)

| Slajd | Pre | Posle |
|---|---|---|
| s020 | [Pre](../../build/redizajn/pre-vernijeg-s020-s021-2026-10-09/pregled/novi/p-21.png) | [Posle](../../build/redizajn/pregled/novi/p-21.png) |
| s020b | [Pre](../../build/redizajn/pre-vernijeg-s020-s021-2026-10-09/pregled/novi/p-22.png) | [Posle](../../build/redizajn/pregled/novi/p-22.png) |
| s021 | [Pre](../../build/redizajn/pre-vernijeg-s020-s021-2026-10-09/pregled/novi/p-23.png) | [Posle](../../build/redizajn/pregled/novi/p-23.png) |
| s021b | [Pre](../../build/redizajn/pre-vernijeg-s020-s021-2026-10-09/pregled/novi/p-24.png) | [Posle](../../build/redizajn/pregled/novi/p-24.png) |

Artefakti u `build/` ne verzionišu se; navedene komande ih obnavljaju. Originalni PDF-ovi, istorijska mapa, zamrznuta tema i druga predavanja nisu menjani.

## Otisci završne verzije

| Resurs | SHA-256 |
|---|---|
| Originalni PDF | `5e68d267ca2f60c1ccdf073c2579fd64a4b05278955cc3d3f920cc54e123fd86` |
| Izvorna mapa | `a3effdb79779d04df05ce98ece642a6068684e4b798018cc96122479136266cc` |
| Manifest redizajna | `dfda44ee2e7e9c6cd9855296eb6ec2228a1954430f5477248cf92cc9237c9581` |
| Zapis izgradnje | `f037bc4ec71b0084d742bb688a84fe595568fedb4cc46681fbefca5615b04f05` |
| Potvrde pregleda | `318b4897fcb3f8ac9a16a4949dbfdf33b7310eb0214c9df565535fd3858fc942` |
| Inventar | `4533ff899b97ef8a8eea8a13c0b02398dcb6ab0632a6b95fd0f142edc8879391` |
| Pokrivenost | `7081445ca48e22945f55584eb4d06d8884c999e7f5a13b55d5114dc24526a4fe` |
| Evidencija beležaka | `d9efde0ab2367b7959a593c09a48ff848f2dc3d0644cce23822d35b4d61a0906` |
| Prezentacioni PDF | `abaa526407db0b6c2f2fbf12d8c505fa845e1450ae070137422719835e054f31` |
| PDF beležaka | `c611be3e0543209c6068983d6c894e75b4d90c887c6b5fa152cc7945b14193ae` |
| Dokaz poređenja | `a61ec61e109fd57a0e1052472db6aa19d8e4dc0d85793dd17a41a923bfec0901` |
| Topologija šema | `2c5ea10235e3ea19c4fcac2a29455f18a7ae5ded1f386c8df7ad3d0b01c84c4f` |
| Mapa podele s020 | `638595bcc20e65585763e6df8b4e420903ab0d580610dc66355bbd705eadb19b` |
| Mapa podele s021 | `58d6d859bdfa980b36d5105c5021e07a101f0626b724970fdcb5729473004d41` |
| Manifest teme | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |

## Nastavak

Tražene dorade s020/s020b i s021/s021b su završene, zajedno sa dodatnim zahtevima za invertore i GS. Naredna radnja je korisnikov pregled ove verzije 03. Status ostaje `ceka_odobrenje`; agent ne daje odobrenje rezultata. Novi agent proverava otiske i nastavlja sa stvarno evidentiranog koraka, bez ponavljanja analize nepromenjenih izvora. Izmena izvora slajda, beležaka ili prikaza poništava pogođene potvrde.
