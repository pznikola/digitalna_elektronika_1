# Predavanje 04 — redizajn po uzoru na odobrenu 01

Datum: **2026-10-02**. Status: **u_radu — raspored i beleške završeni; čeka stručnu odluku za pet izvornih zapisa**. Tema **etf-v1**, izabrani stil **B**.

Pregledani su originalni PDF (20 strana), svih **39/39 originalnih slajdova**, prethodno generisana prezentacija i novi prikaz svakog slajda. Očuvani su broj, redosled i stabilni ID-jevi **04-s001–04-s039**. Projekcioni PDF ima **39 strana**; PDF beležaka takođe ima **39 strana**. Svih **140/140 sadržajnih elemenata** iz nezavisnog popisa originala ima provereno odredište na slajdu ili u njegovim beleškama. To potvrđuje pokrivenost i vernost originalu, a ne ispravnost pet izdvojenih izvornih nepreciznosti.

Nalog za početak je u [odluke.md](odluke.md). Ovaj rad ne daje odobrenje rezultatu 03 niti dozvolu za 05. Predavanje 01, ostala predavanja i zamrznuta tema nisu menjani. Originalni PDF je neizmenjen.

## Raspored i izgled

| Slajdovi | Promena |
|---|---|
| s001 | Naslovna strana prati 01; sačuvani autor, katedra i školska godina 2021/22. |
| s002–s003 | Definicije i istorijski pregled imaju odvojene kolone; celobrojni i razlomljeni deo, vodeće/prateće nule i njihovi ekvivalentni zapisi čine pregledne blokove. |
| s004–s007 | Ujednačene oznake poništavanja i tamnocrveni akcenti; dugi računi raspoređeni u više redova. Definicije, dokazi i rezultati ostaju vidljivi. |
| s008–s012 | Postupci deljenja i množenja imaju vidljive uslove i ključne korake. Početni izrazi su detaljno sačuvani u beleškama; pitanje s011 ostaje zaseban slajd. |
| s013–s015 | Tabele su centrirane i razmaknute od naslova; strelice čitanja nalaze se izvan ćelija. Sačuvani su svi koraci deljenja/množenja i svi redovi provere u osnovi sedam. |
| s016–s018 | Odvojene formule i grupe cifara; pregledne tabele kompatibilnih osnova sa svih 8 i 16 parova. Strelice kompatibilnosti imaju odvojene oznake. |
| s019–s020 | Dva smera konverzije u jednakim kolonama. Dodavanje i brisanje nula istaknuto je tamnocrveno; zadržani su svi primeri. |
| s021–s022 | Precrtani registri i magistrala, vodoravne oznake i čisti vektorski crteži fizičkih linija. Sačuvane su sve grane i oznaka nastavka. |
| s023–s027 | Pojmovi bit/nibble/byte/word/double word grupisani u tabelu, uz osmobitni registar i MSB/LSB. Položaj tačke povezan je sa zapisom i skaliranjem u preglednim tabelama. |
| s028 | Jasno odvojeni problem znaka, izbor kodovanja i četvorobitni primer. |
| s029–s032 | Svih 16 redova svake tabele ostaje vidljivo. Vodoravna pregrada razdvaja polovine kodnog prostora; objašnjenje i formule su u zasebnoj koloni. Sačuvani su i oba zapisa nule gde postoje. |
| s033–s036 | Definicije komplemenata, invertovanje, decimalni primeri i svojstva imaju zasebne blokove. Na s036 vidljivi su početak izvođenja, ključni korak, bit znaka i rezultat; dva međukoraka su u beleškama. |
| s037–s039 | Sačuvana tabela svih kodova drugog komplementa/ofseta, poravnati primeri fiksne tačke. Mantisa i eksponent imaju odvojene kolone sa dvorednim naslovima. |

Fontovi su postojeći; lokalno isticanje **#A32638** prati plan i odobrenu 01. Boja nije predstavljena kao zvanični ETF standard. Osnovni tekst ostaje 11 pt, tabele i pojedini dugi izrazi koriste 9–10 pt. Nema skaliranja celog slajda, novih okvira, overlay strana ili uredničkih komentara na projekcionim slajdovima.

Precrtani uređivi izvori: `slike/tikz/s021_registri_magistrala.tex` i `slike/tikz/s022_fizicke_linije.tex`; strelice na s013/s015 i kompatibilnost na s017 uređene su u pripadajućim izvorima. Na ovim slajdovima nema novih analognih ili logičkih kola. Crteži registara i fizičkih linija upoređeni su sa originalnim oznakama i značenjem; boja nije jedini nosilac informacije.

## Beleške i pokrivenost

Svaki slajd ima pojedinačni izvor `beleske/sNNN.tex`, stabilni ID i naslov. Pregledane su sve strane beležaka u konačnom prikazu. Izvorna objašnjenja i dopunska tumačenja jasno su razdvojeni. Definicije, ključni uslovi, rezultati, tabele i nastavne ilustracije ostaju vidljivi.

| Slajd | Detalj prenet u beleške istog ID-ja |
|---|---|
| s008 | Početno razvijanje celobrojne vrednosti pre deljenja sa r; na slajdu ostaju deljenje, izdvajanje c₀ i uslov za ostatak. |
| s010 | Početno razvijanje razlomljenog dela pre množenja sa r; na slajdu ostaju množenje, izdvajanje c₋₁ i uslov za preostali deo. |
| s027 | Puni razvoj preko zajedničkog imenioca sa svim članovima; vidljivi početak i rezultat RV = CV/rᵏ, registar i svi položaji tačke. |
| s036 | Dva srednja koraka algebarskog izvođenja; početak, završni oblik, bₙ₋₁ = 1 i negativna težina vodećeg bita ostaju vidljivi. |

Ostali sažeti pasusi imaju puno objašnjenje u beleškama, uključujući komentare tačnosti konverzije s013, školski primer s014, projektantovo tumačenje s024/s028 i objašnjenje kodnih tabela. Precizna odredišta, opis svake promene i izvori nalaze se u [pokrivenost.md](pokrivenost.md), [pokrivenost.json](pokrivenost.json) i [inventar.json](inventar.json).

## Provere

```bash
make -C predavanja LECTURE=04_brojni_sistemi all
make -C predavanja LECTURE=04_brojni_sistemi review
make -C predavanja LECTURE=04_brojni_sistemi check
python3 predavanja/04_brojni_sistemi/kodovi/provera_logike.py
git diff --check
```

Kompilacije prezentacije i beležaka prolaze bez grešaka, upozorenja, `Overfull`/`Underfull` i nedostajućih znakova. `review` gradi beleške iz istih pojedinačnih izvora i prikazuje original / pre / posle / beleške. Potvrđeni su broj, redosled, ID-jevi, 140 odredišta sadržaja, veza svih beležaka sa odgovarajućim ID-jem, prisustvo resursa i aktuelnost pojedinačnih otisaka.

`check` trenutno daje **NEZAVRŠENO**, isključivo za **s006/formule, s009/formule, s016/formule, s034/tekst i s035/formule**. Nema drugih prijavljenih problema. Te kategorije su namerno ostavljene kao `problem` dok se čeka stručna odluka; potvrde nisu automatski proglašene uspešnim. [Završni check log](../../build/poredjenje/check-zavrsno.log) i [review log](../../build/poredjenje/review-zavrsno.log) čuvaju rezultate.

Nezavisna [računska provera](../../kodovi/provera_logike.py) prolazi: čita sve ćelije konverzionih i kodnih tabela, proverava težinske sume, prelaze između osnova, decimalni niz, oba komplementa i fiksnu tačku. Dokumentuje i kontraprimere izvornih zapisa s006/s009/s035; njen uspeh ne potvrđuje te izvorne zapise. [Log](../../build/poredjenje/racunska-provera.log). Automatika ne zamenjuje stvarni pregled svakog slajda, formule, tabele, crteža i beležaka, koji je izvršen.

## Jezičke ispravke i stručna pitanja

Evidentirane očigledne jezičke ispravke: s013 „tačnije rezultat“ → „tačniji rezultat“; s022 „RELAN“ → „Realan“; s024 „Ali sto tako“ → „Ali isto tako“ (puna formulacija u beleškama); s028 „smo podrazumevalo“ → „smo podrazumevali“; s031/s032 uklonjeno ponovljeno „znaka“; s034 „jec“ → „je“; s039 „jedna registar“ → „jedan registar“. Preformulisani pasusi čuvaju izvorno značenje. Istorijski spisak rekonstrukcije nije prepisivan novim statusom.

Pet stručnih predloga detaljno je navedeno u [otvorena_pitanja.md](otvorena_pitanja.md): tačne decimale 17/49 na s006, strogi uslov za broj cifara na s009, dosledni dvostruki indeksi na s016, naziv komplementa 10-tke na s034 i zagrade oko oduzimanog komplementa na s035. **Nijedna stručna ispravka nije primenjena bez odluke.** Izvorni zapisi ostaju u prezentaciji, a nepreciznosti su objašnjene u beleškama. Zahtev za odluku poslat je korisniku, ali odgovor još nije primljen.

## Izlazi i kontrolne sume

- [Prezentacija — 39 slajdova](../../build/04_brojni_sistemi.pdf).
- [PDF beležaka — 39 strana](../../build/04_brojni_sistemi_beleske.pdf).
- [Uporedni pregled sva 39 slajda](../../build/redizajn/pregled/index.html).
- [Vektorsko poređenje pre/posle — s002, s013, s021, s023, s027, s032](../../build/poredjenje/poredjenje-pre-posle.pdf).
- [Polazni PDF](../../build/redizajn/pre/prezentacija.pdf) i [trajna arhiva početnog prikaza i izvora](polazni-izvori.tar.gz), izvan ignorisanog `build/`.
- [Manifest](manifest.json), [zapis izgradnje](izgradnja.json) i [pojedinačne potvrde](pregled.json).

| Resurs | SHA-256 |
|---|---|
| Originalni PDF | `e1f763084b19156c790ffe1f30b9d703081c8fbdc57e2ad9b2d9b73140ad1518` |
| Manifest etf-v1 | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |
| Manifest redizajna | `f4301065e016daa6b3495b27b353908594353b4c49559ce042c8f7f88a839d9b` |
| Zapis izgradnje | `5d7e8582d18a9d3cef27c10141fede7cae659aad07647c1936122cfeb63ad43b` |
| Potvrde pregleda | `e6c0ceabd2c9cbe0dd78c5799c094b150b5047f9fe3597561bfbb157db450741` |
| Inventar | `26fa982fda96c0dca8bc2c81ac7ef4c8a84e7881a1e2707dc569a302cdf70aae` |
| Mapa pokrivenosti | `6a0e1d4b104e29ab5957f0bfeee85558d65657a550454415e86e063748562705` |
| Prezentacioni PDF | `0c6165a235f0f2db1d02df6b457a7f9a69ef4235bb8e37edebb8f111b8011fd8` |
| PDF beležaka | `b66e2087052fba3429c5db2cd0753ff1cc07d2a2c58295a171a2f4ade19772f5` |
| PDF poređenja | `fca95054e6a64060f317b028888f66377214bc15829ad0b61f9c7d3969e38080` |
| Arhiva početnog stanja | `6f718955699cacea9fed24eeabece63dc1ae28412d345915c321662c6d658675` |

Otisak početnog snapshot manifesta: `5bf89dc993feb89e00ac5efc6d03391bb135a660d1c4037f389c9d5de5367549`. Izvori beležaka i lokalne zavisnosti svakog slajda imaju zasebne kontrolne sume u potvrdi i zapisu izgradnje. Kasnija promena poništava samo stvarno pogođene potvrde; zamrznuta tema nije menjana.

## Tačka nastavka

Redizajn rasporeda, originalni popis, pokrivenost, pregled svih 39 slajdova i beležaka završeni su. **Ne ponavljati taj rad ako se pregledani izvori nisu promenili.** Čeka se samo korisnikova stručna odluka za pet navedenih zapisa; završni rezultat 04 još nije odobren.

Posle odluke sprovesti odobrene izmene ili evidentirati odobreno zadržavanje izvornih zapisa, prilagoditi beleške, ponovo pregledati pogođene prikaze, obnoviti potvrde, izvršiti `check`, osvežiti ovaj izveštaj i centralne otiske. Kada nema nerešenog sadržinskog problema, postaviti `ceka_odobrenje` i predati 04 korisniku. **Početak 05 nije odobren.**
