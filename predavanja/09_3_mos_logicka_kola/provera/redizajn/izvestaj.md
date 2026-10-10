# Redizajn 09_3 — raspored, šeme i beleške

**2026-10-03 — status `u_radu`.** Obrađena je prezentacija 09_3 po korisnikovom izričitom nalogu. Izgled, nastavni tekst i prateći prikazi su pripremljeni; završna sadržinska potvrda čeka odluke o **13 grupa stručnih pitanja** iz originala. Rezultat nije odobren. Predavanje 10 nije započeto.

## Obuhvat i izvori

Pojedinačno su pregledani svi originalni isečci (71), sačuvani početni LaTeX prikazi, novi slajdovi i tekst/prikaz beležaka uz njihove ID-jeve i naslove. Original ima 36 PDF strana, sa gornjim i donjim slajdom prema `provera/mapa.json`. Prezentacioni PDF ima **71 stranu**, redom `09_3-s001` do `09_3-s071`. Nema brisanja, spajanja, deljenja, novih razdelnika niti overlay strana. Originalni PDF ostao je neizmenjen.

Zadržani su autorstvo prof. dr Lazar Saranovac, Katedra za elektroniku i školska 2021/22. Korišćena je zamrznuta tema **ETF `etf-v1`, stil B**, uz lokalne rasporede i tamnocrvena nastavna isticanja. Zajednička tema nije menjana.

## Glavne promene

- Svaki od 71 slajda ima uređeni raspored: odvojeni naslovi i ilustracije, pregledni međukoraci formula, dosledni razmaci i isticanje. Osnovni tekst ne smanjuje se automatski da bi ceo okvir stao.
- Uređeno je **58 postojećih vektorskih izvora crteža**. Šeme su kompaktnije, oznake odvojene od vodova, MOS simboli sa strelicama i imenovanim priključcima korišćeni gde se prikazuju sami tranzistori. Četvoropriključni modeli parazitnih kapacitivnosti i funkcionalni simboli bilateralnog prekidača ostaju prema originalu.
- Posebno su precrtani kaskada invertora s006, jedinični invertor s013, baferi s024, četiri PUN/PDN realizacije s026, konflikt izlaza s045, zajedničke linije s048, prolazne kaskade s055, restauracija s056, barrel shifter s059, transmisioni gejt s060, selektor s066 i domino mreža s071.
- S048 ima odvojene četiri realizacije, pregledno vođene dozvole van tela kola i tekstualnih blokova. S057 odvojeni su naslov dekodera i izlazne oznake. Spojevi vodova označeni su tačkama; ukrštanja bez spoja sačuvana su bez tačaka ili uz most.
- S059 zadržava gornje veze na A3 i prekide podatkovnih kolona. Pomeranje udesno sa proširenjem znaka objašnjeno je u beleškama. S067 zadržava zadatak `Y=?`; odgovor i izvođenje su samo za predavača.

## Beleške i pokrivenost

**71 fajl `beleske/sNNN.tex`** sadrži dodatni nastavni tekst uz isti slajd. S001 ima samo vezu sa ID-jem. Izvedeni su A4 prikazi sa slajdom, naslovom, ID-jem i beleškama; trenutno ukupno 71 A4 strana. Nema vidljive istorije redizajna, izvora, odluka, kontrolnih suma, zahteva za odobrenje niti veštačkih poruka o praznim beleškama.

Preneti su svi detalji skraćeni sa originalnog slajda, uključujući objašnjenja kapacitivnosti, pune međukorake s011/s016/s017/s037, rad PUN/PDN i prolaznih mreža, bilateralne slučajeve i pripremu/izračunavanje dinamičkih kola. Dopune objašnjavaju oznake, fizički rad, faktorisanje, proveru funkcije i tipične zabune. Nastavni tekst je jedinstveno u LaTeX fajlovima; evidencija ne čuva njegovu drugu kopiju.

Inventar sadrži **304 elementa: 280 izvornih grupa i 24 proverene dopune**. Sva 304 elementa imaju provereno odredište; 74 grupe povezane su sa beleškama, a ostale sa vidljivim slajdom. [Pokrivenost](pokrivenost.md), [poreklo i odredišta beležaka](evidencija_beleski.md), [inventar](inventar.json). Puna pokrivenost ne odobrava stručnu tačnost osporenih izvornih tvrdnji.

## Poređenja i isporuka

- [Prezentacija](../../build/09_3_mos_logicka_kola.pdf)
- [A4 beleške](../../build/09_3_mos_logicka_kola_beleske.pdf)
- [Original / pre / posle / beleške — svih 71 ID](../../build/redizajn/pregled/index.html)
- [Sačuvan početni prikaz i izvori](pocetni_prikaz.tar.gz), nevezani za nove izgradnje.

| Primer | Pre | Posle | Šta je uređeno |
|---|---|---|---|
| s006 | [Prikaz](../../build/redizajn/pregled/pre/p-06.png) | [Prikaz](../../build/redizajn/pregled/novi/p-06.png) | Kompaktna dva CMOS invertora i jasni spojevi |
| s024 | [Prikaz](../../build/redizajn/pregled/pre/p-24.png) | [Prikaz](../../build/redizajn/pregled/novi/p-24.png) | Kraće legende, čitljivi baferi; puna objašnjenja u beleškama |
| s045 | [Prikaz](../../build/redizajn/pregled/pre/p-45.png) | [Prikaz](../../build/redizajn/pregled/novi/p-45.png) | Dve šeme iznad pregledne tabele |
| s048 | [Prikaz](../../build/redizajn/pregled/pre/p-48.png) | [Prikaz](../../build/redizajn/pregled/novi/p-48.png) | Četiri odvojene realizacije zajedničke linije |
| s055 | [Prikaz](../../build/redizajn/pregled/pre/p-55.png) | [Prikaz](../../build/redizajn/pregled/novi/p-55.png) | Pogrešna i pravilna kaskada sa oznakama nivoa |
| s059 | [Prikaz](../../build/redizajn/pregled/pre/p-59.png) | [Prikaz](../../build/redizajn/pregled/novi/p-59.png) | Pravilne grane, prekidi i odvojeni upravljački vodovi |

## Jezičke dorade

Pri preformulisanju ispravljene su očigledne slovne i gramatičke greške iz istorijskog popisa, bez promene stručnog značenja. Relevantni ispravni izrazi u novom nastavnom tekstu: s003 „drejna“, s004 „dužina kanala“, s006 „prethodni stepen“, s010 „kapacitivnosti“, s011 „ekvivalentna“, s015 „minimizovanje“, s019/s021 „najbliži“, s023 „nebaferisana“ i „tranzistori“, s031 „realizacija“, s032 „promenljive“/„komplementne“, s041 „izbor kapacitivnosti“, s046 „prouzrokovana“, s050 „ako“, s056 „logičko kolo“, s062 „radi“, s063 „otpornošću“ i s070 uklonjeno ponavljanje „tranzistora“. Rečenice su prilagođene novom rasporedu i beleškama; nisu svi izrazi zadržani kao doslovna zamena jedne reči. Istorijska [evidencija rekonstrukcije](../uocene_greske.md) ostaje zasebna.

## Provere i otvorena pitanja

Kompilacija prezentacije i beležaka, renderovanje i postojeće **1007 računskih provera** prolaze. Nema `Overfull`, grešaka kompilacije, nedostajućih znakova, odsecanja ili uočenih preklapanja. Pregled šema obuhvatio je priključke, tipove tranzistora, polaritete, kontrolne signale, spojeve i ukrštanja. Automatska računanja ne pokrivaju sve crtane veze.

`check` ispravno vraća **NEZAVRŠENO**: samo 24 sadržinske kategorije na 18 ID-jeva, bez zastarelih potvrda, nepotpune pokrivenosti ili strukturnih nalaza. [Pun rezultat](rezultati_provera.md), [potvrde vezane za izvore i prikaze](pregled.json).

**P01–P13 nisu primenjeni:** model odnosa P/N, oznake fanouta i veličina, pretpostavke kašnjenja, neparni broj stepena, zatvorena forma, geometrijski faktor W/L, kritična putanja, završno CL, oznake/indeksi logičkog truda, prag prolaznog NMOS, znak napona s062, izlazna jednačina s066 i ograničenje domino logike. Svako pitanje ima konkretan predlog i obrazloženje u [otvorena_pitanja.md](otvorena_pitanja.md). Osporeni izvorni zapisi ostaju do odluke korisnika; izjašnjenje agenta nije odobrenje.

Komande za ovo predavanje:

```sh
make -C predavanja LECTURE=09_3_mos_logicka_kola all
make -C predavanja LECTURE=09_3_mos_logicka_kola notes
make -C predavanja LECTURE=09_3_mos_logicka_kola review
make -C predavanja LECTURE=09_3_mos_logicka_kola check
```

## Precrtani i uređeni vektorski izvori

- [`slike/tikz/s003_kapacitivnosti_mos.tex`](../../slike/tikz/s003_kapacitivnosti_mos.tex)
- [`slike/tikz/s005_lanac_invertora.tex`](../../slike/tikz/s005_lanac_invertora.tex)
- [`slike/tikz/s006_dva_cmos_invertora.tex`](../../slike/tikz/s006_dva_cmos_invertora.tex)
- [`slike/tikz/s007_kapacitivnosti_dva_invertora.tex`](../../slike/tikz/s007_kapacitivnosti_dva_invertora.tex)
- [`slike/tikz/s008_kapacitivnosti_dva_invertora.tex`](../../slike/tikz/s008_kapacitivnosti_dva_invertora.tex)
- [`slike/tikz/s013_jedinicni_invertor.tex`](../../slike/tikz/s013_jedinicni_invertor.tex)
- [`slike/tikz/s024_povecanje_strujnog_kapaciteta.tex`](../../slike/tikz/s024_povecanje_strujnog_kapaciteta.tex)
- [`slike/tikz/s024_rasterecenje_izlaza.tex`](../../slike/tikz/s024_rasterecenje_izlaza.tex)
- [`slike/tikz/s026_pdn_paralelna_veza.tex`](../../slike/tikz/s026_pdn_paralelna_veza.tex)
- [`slike/tikz/s026_pdn_redna_veza.tex`](../../slike/tikz/s026_pdn_redna_veza.tex)
- [`slike/tikz/s026_pun_paralelna_veza.tex`](../../slike/tikz/s026_pun_paralelna_veza.tex)
- [`slike/tikz/s026_pun_redna_veza.tex`](../../slike/tikz/s026_pun_redna_veza.tex)
- [`slike/tikz/s027_ni_dimenzije.tex`](../../slike/tikz/s027_ni_dimenzije.tex)
- [`slike/tikz/s027_nili_dimenzije.tex`](../../slike/tikz/s027_nili_dimenzije.tex)
- [`slike/tikz/s028_nili_dimenzije.tex`](../../slike/tikz/s028_nili_dimenzije.tex)
- [`slike/tikz/s029_ni_dimenzije.tex`](../../slike/tikz/s029_ni_dimenzije.tex)
- [`slike/tikz/s031_pdn_slozene_funkcije.tex`](../../slike/tikz/s031_pdn_slozene_funkcije.tex)
- [`slike/tikz/s032_pun_slozene_funkcije.tex`](../../slike/tikz/s032_pun_slozene_funkcije.tex)
- [`slike/tikz/s033_pdn_mreza.tex`](../../slike/tikz/s033_pdn_mreza.tex)
- [`slike/tikz/s033_pun_mreza.tex`](../../slike/tikz/s033_pun_mreza.tex)
- [`slike/tikz/s034_potpuno_kolo_sa_dimenzijama.tex`](../../slike/tikz/s034_potpuno_kolo_sa_dimenzijama.tex)
- [`slike/tikz/s040_mesovita_kriticna_putanja.tex`](../../slike/tikz/s040_mesovita_kriticna_putanja.tex)
- [`slike/tikz/s045_spojeni_izlazi_logickih_kola.tex`](../../slike/tikz/s045_spojeni_izlazi_logickih_kola.tex)
- [`slike/tikz/s045_sukob_izlaznih_tranzistora.tex`](../../slike/tikz/s045_sukob_izlaznih_tranzistora.tex)
- [`slike/tikz/s046_trostaticki_invertor.tex`](../../slike/tikz/s046_trostaticki_invertor.tex)
- [`slike/tikz/s047_otvoreni_drejn.tex`](../../slike/tikz/s047_otvoreni_drejn.tex)
- [`slike/tikz/s048_centralna_kontrola.tex`](../../slike/tikz/s048_centralna_kontrola.tex)
- [`slike/tikz/s048_lokalne_dozvole.tex`](../../slike/tikz/s048_lokalne_dozvole.tex)
- [`slike/tikz/s048_otvoreni_drejnovi.tex`](../../slike/tikz/s048_otvoreni_drejnovi.tex)
- [`slike/tikz/s048_zajednicka_linija.tex`](../../slike/tikz/s048_zajednicka_linija.tex)
- [`slike/tikz/s050_prolazni_nmos.tex`](../../slike/tikz/s050_prolazni_nmos.tex)
- [`slike/tikz/s051_praznjenje.tex`](../../slike/tikz/s051_praznjenje.tex)
- [`slike/tikz/s051_punjenje.tex`](../../slike/tikz/s051_punjenje.tex)
- [`slike/tikz/s052_selektorska_prolazna_mreza.tex`](../../slike/tikz/s052_selektorska_prolazna_mreza.tex)
- [`slike/tikz/s053_i_a.tex`](../../slike/tikz/s053_i_a.tex)
- [`slike/tikz/s053_i_nula.tex`](../../slike/tikz/s053_i_nula.tex)
- [`slike/tikz/s053_ili_a.tex`](../../slike/tikz/s053_ili_a.tex)
- [`slike/tikz/s053_ili_jedan.tex`](../../slike/tikz/s053_ili_jedan.tex)
- [`slike/tikz/s054_degradacija_kaskade.tex`](../../slike/tikz/s054_degradacija_kaskade.tex)
- [`slike/tikz/s055_pogresna_kaskada.tex`](../../slike/tikz/s055_pogresna_kaskada.tex)
- [`slike/tikz/s055_pravilna_kaskada.tex`](../../slike/tikz/s055_pravilna_kaskada.tex)
- [`slike/tikz/s056_restauracija_nivoa.tex`](../../slike/tikz/s056_restauracija_nivoa.tex)
- [`slike/tikz/s057_mux_dekoder.tex`](../../slike/tikz/s057_mux_dekoder.tex)
- [`slike/tikz/s057_mux_prolazni_dekoder.tex`](../../slike/tikz/s057_mux_prolazni_dekoder.tex)
- [`slike/tikz/s058_pomerac_dva_bit_slice.tex`](../../slike/tikz/s058_pomerac_dva_bit_slice.tex)
- [`slike/tikz/s059_barrel_shifter.tex`](../../slike/tikz/s059_barrel_shifter.tex)
- [`slike/tikz/s060_bilateralni_prekidac.tex`](../../slike/tikz/s060_bilateralni_prekidac.tex)
- [`slike/tikz/s060_transmisioni_gejt.tex`](../../slike/tikz/s060_transmisioni_gejt.tex)
- [`slike/tikz/s061_bilateralni_prekidac.tex`](../../slike/tikz/s061_bilateralni_prekidac.tex)
- [`slike/tikz/s062_bilateralni_prekidac.tex`](../../slike/tikz/s062_bilateralni_prekidac.tex)
- [`slike/tikz/s063_bilateralni_prekidac.tex`](../../slike/tikz/s063_bilateralni_prekidac.tex)
- [`slike/tikz/s065_zakocen_bilateralni_prekidac.tex`](../../slike/tikz/s065_zakocen_bilateralni_prekidac.tex)
- [`slike/tikz/s066_selektor_transmisioni_gejtovi.tex`](../../slike/tikz/s066_selektor_transmisioni_gejtovi.tex)
- [`slike/tikz/s067_upitna_funkcija.tex`](../../slike/tikz/s067_upitna_funkcija.tex)
- [`slike/tikz/s068_dinamicka_mreza.tex`](../../slike/tikz/s068_dinamicka_mreza.tex)
- [`slike/tikz/s069_dinamicka_mreza.tex`](../../slike/tikz/s069_dinamicka_mreza.tex)
- [`slike/tikz/s070_kaskada_dinamickih_invertora.tex`](../../slike/tikz/s070_kaskada_dinamickih_invertora.tex)
- [`slike/tikz/s071_domino_mreza.tex`](../../slike/tikz/s071_domino_mreza.tex)

## Otisci pregledane verzije

| Resurs | SHA-256 |
|---|---|
| Original | `b4861aeee12f6f25f2c9be291bc9aae149747d053d5332f266738c14c74c0492` |
| Manifest teme | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |
| Manifest predavanja | `25fcccbc5256e69542637c7dfd063dcfb06e042edf0b957e6cbf45c575f6010e` |
| Zavisnosti izgradnje | `a96417efd25e7f3e88b9f00dd83048ce6ed5bb8acf168edad6cfee8ed843c773` |
| Inventar | `6186b81c4ab5c676b4a24d6fdb1b711fc6a7ca9ed167bd05921ea16b3c82da11` |
| Pokrivenost | `209c4ae524c2e6549276559518de05e5632bf5a49c6adbc3f2905e9d6e8410fd` |
| Prezentacioni PDF | `303d5c68058645e01176fef37ce48abd98621cc704e2ba051a778e13486cd0e9` |
| PDF beležaka | `9c0f2a4eebfa3423fcabd32949ace5436f50093121a3fbd6ce7c57e606a9d394` |
| Početni prikaz | `8bc2ff5c0a4792eb483d8d8f87f540d24eb40f2fb47657d25f7904bc15a6d7fe` |

Izvori, crteži, beleške i stvarno korišćene zavisnosti zamrznute teme imaju pojedinačne otiske u `izgradnja.json`; original/pre/novi/beleške imaju potvrde u `pregled.json`. Promena izvora ili beležaka zahteva obnovu pogođenih potvrda.

## Sledeći korak

Zatražiti korisnikove odluke **P01–P13**, primeniti samo odobrene stručne ispravke, ponovo pregledati pogođene slajdove i beleške, obnoviti pokrivenost/otiske i ponoviti `notes`, `review`, `check`. Ne ponavljati završeni pregled nepogođenih slajdova ako se njihovi izvori i stvarne zavisnosti nisu promenili. Tek kada sadržinska pitanja budu rešena, pripremiti završnu predaju sa statusom `ceka_odobrenje`. Prihvatanje 09_3 i dozvola za 10 evidentiraju se odvojeno. Nalog za 09_3 ne odobrava rezultate 09_2 ili ranijih predavanja.
