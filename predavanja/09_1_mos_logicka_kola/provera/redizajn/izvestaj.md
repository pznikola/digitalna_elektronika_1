# Izveštaj redizajna — 09_1, MOS logička kola, 1. deo

Datum: **2026-10-03**. Status: **`u_radu`**. Korisnik je odobrio obradu 09_1; rezultat i stručne ispravke nisu odobreni. Obrada 09_2 nije započeta.

## Isporuka i obuhvat

Pregledani su originalni PDF sa 29 strana, svih **57 izdvojenih slajdova**, svih 57 početnih LaTeX prikaza, pojedinačni izvori i crteži. Uređeni su raspored svih 57 slajdova i beleške po novim sadržinskim pravilima plana. Novi prikazi pregledani su pojedinačno u punoj veličini; pročitani su nastavni tekst i formule svih A4 beležaka uz odgovarajuće ID-jeve. Najduža izvođenja proverena su i na celim A4 stranama.

Sačuvani su **57/57 slajdova, redosled i ID-jevi `09_1-s001`–`09_1-s057`**. Prezentacioni PDF ima 57 strana; A4 PDF beležaka takođe ima 57 strana. Nema novih razdelnika, spajanja/deljenja, dodatnih overlay strana ili smanjivanja celog slajda. Original ostaje neizmenjen. Poreklo: Digitalna elektronika 1, 2021/22, Katedra za elektroniku, prof. dr Lazar Saranovac.

- [Prezentacioni PDF](../../build/09_1_mos_logicka_kola.pdf)
- [PDF za predavača](../../build/09_1_mos_logicka_kola_beleske.pdf)
- [Original / početni prikaz / novi slajd / beleške](../../build/redizajn/pregled/index.html)
- [Potpuna mapa pokrivenosti](pokrivenost.md), [potvrde i otvorene kategorije](pregled.json)
- [Otvoreni predlozi P01–P13](otvorena_pitanja.md), [izvođenja i protivprimeri](dokazi_ispravki.md)

## Glavne promene i poređenja

Primenjena je postojeća, konkretno vezana tema **etf-v1**, stil B. Tema i njeni resursi nisu menjani. Naslovi i osnovni tekst su ujednačeni; nastavna isticanja koriste lokalnu tamnocrvenu `#A32638`, a formula/oznaka ostaje razumljiva bez boje. Tekst ne sadrži uredničke komentare.

| Primer | Početni problem i novi prikaz |
|---|---|
| [s003](../../build/redizajn/pregled/index.html#09_1-s003) | Parametri izdvojeni u desnu kolonu; modeli i uslovi ostaju levo. Struje, polariteti i naponske strelice uređeni; značenja parametara objašnjena u beleškama. |
| [s008](../../build/redizajn/pregled/index.html#09_1-s008) | Tri izvorna dijagrama i konačni model ostaju vidljivi; pune polazne zamene su u beleškama. |
| [s010/s011](../../build/redizajn/pregled/index.html#09_1-s010) | Tri realizacije svake mreže ravnomerno raspoređene u dva reda. Blok PUN/PDN ima dovoljno prostora za natpise; zajednički čvorovi imaju tačke. |
| [s012](../../build/redizajn/pregled/index.html#09_1-s012) | Kompaktan invertor i odvojena karakteristika; objašnjenje početka provođenja i potpuno izvođenje granice preneti u beleške. |
| [s015](../../build/redizajn/pregled/index.html#09_1-s015) | Dve karakteristike stoje jedna pored druge; strelice odvojene od natpisa i usmerene u odgovarajuće granice. Oba osnovna modela ostaju vidljiva. |
| [s023](../../build/redizajn/pregled/index.html#09_1-s023) | Karakteristika levo, uslovi održivosti desno, β ispod. Strelica VO(IH) odvojena od tekstualnih oznaka. |
| [s028](../../build/redizajn/pregled/index.html#09_1-s028) | Dva RC ekvivalentna kola precrtana sa kratkim vodovima, jasnim spojnim tačkama, strujama i polaritetima. |
| [s031–s033](../../build/redizajn/pregled/index.html#09_1-s031) | Glavne definicije/srednje vrednosti vidljive, duge zamene modela i međukoraci potpuno objašnjeni u beleškama. |
| [s036–s039](../../build/redizajn/pregled/index.html#09_1-s036) | Dosledne dimenzije TD/TL i kratki nezavisni ulazni vodovi, uredne kolone za šemu i formule. |
| [s049–s051](../../build/redizajn/pregled/index.html#09_1-s049) | Gejt TL vezan na napajanje vodom koji obilazi simbol; prikazane spojne tačke. |
| [s056](../../build/redizajn/pregled/index.html#09_1-s056) | Očuvana oba četvoropriključna nastavna primera. Zajednička osnova jasno odvojena od izlaznog voda preskokom bez spoja. |

Uređeno je **44 postojeća TikZ izvora**: svi su i dalje vektorski i uređivi. Električna kola sa tri priključka koriste postojeće Razavi nMOS/pMOS simbole; s002/s010/s011 čuvaju konvencije koje su predmet nastave, a s056 čuva neophodne četvoropriključne simbole. Kvalitativne karakteristike nisu zamenjene proizvoljnim merenjima. Potpuna evidencija topologije, priključaka, čvorova i polariteta je u [proveri šema](provera_sema.md).

## Beleške i pokrivenost

Mapa ima **284/284 proverena odredišta**: 270 izvornih sadržajnih grupa i 14 dopunskih objašnjenja. To je semantički inventar formula, uslova, crteža i nastavnih objašnjenja; nije broj rečenica. Sve grupe imaju sidro u slajdu ili beleškama istog ID-ja. Tehnički izveštaj ne zamenjuje nastavno odredište.

Postoji 57 pojedinačnih `beleske/sNNN.tex`; **55 sadrži nastavna objašnjenja**, dok s001/s057 imaju samo ID i ne izmišljaju dopunski tekst. Beleške čuvaju pune uklonjene nastavne detalje i potrebne međukorake, bez vidljivih oznaka porekla, istorije redizajna, izveštaja provera, odluka ili predloga ispravki. Poreklo i razlika izvornog sadržaja/dopune vode se u [poreklo_beleski.json](poreklo_beleski.json), bez druge kopije nastavnog teksta.

### Mapa nastavnih objašnjenja po slajdu

Stavke uključuju preneti izvorni detalj i/ili proverenu dopunu; polje `origin` u inventaru ih razdvaja. Ključni modeli, rezultati, uslovi i ilustracije ostaju na slajdovima.

| ID | Nastavni sadržaj beležaka |
|---|---|
| 09_1-s002 | Tumačenje svih konvencija i tipova kanala |
| 09_1-s003 | Potpuna značenja parametara, veze brzine i polja, jedinice |
| 09_1-s004 | Dve pune granične zamene, diskontinuitet i obrazloženje izbora modela |
| 09_1-s005 | Eksperimentalno opažanje, nazivi dužina kanala i razlog ranijeg zasićenja |
| 09_1-s006 | Tumačenje korekcija, graničnog uslova i modulacije |
| 09_1-s007 | Algebra preuređivanja struje preko parametara |
| 09_1-s008 | Početni omski izraz, zamena graničnog napona i međukorak |
| 09_1-s009 | Dodatno tumačenje PUN, PDN i visokoomskog stanja |
| 09_1-s010 | Tumačenje tri realizacije, paralelne i redne putanje |
| 09_1-s011 | Tumačenje PMOS upravljanja i dualnih funkcija |
| 09_1-s012 | Početak provođenja, puna zamena za VDSsat, mali pad RL i VO<VDD; drive i load |
| 09_1-s013 | Razlog implicitnog pristupa i neopterećenost |
| 09_1-s014 | Polazna ravnoteža i opis promene radne oblasti |
| 09_1-s015 | Razlika dve podele i moguća pojačanja; ponovljeni omski izraz |
| 09_1-s016 | Obrazloženje kvalitativnog i kvantitativnog približenja |
| 09_1-s017 | Potpuna dva zanemarivanja i prenos člana VOL/RL |
| 09_1-s018 | Obrazloženje određivanja pragova i malo prekoračenje praga |
| 09_1-s019 | Međukorak implicitnog izvoda i zamena praga |
| 09_1-s020 | Ponovljena relacija i pravilo izvoda proizvoda |
| 09_1-s021 | Međukorak sređivanja izvoda i način rešavanja sistema |
| 09_1-s022 | Razlikovanje ispitnih zahteva i izuzetka |
| 09_1-s023 | Potpuno obrazloženje održivosti i ponovljeni uslov VOL<VTn |
| 09_1-s024 | Početna ravnoteža, zamena VS, puna nenormalizovana kvadratna jednačina |
| 09_1-s025 | Obrazloženje aproksimacije i puna preporuka za ispit |
| 09_1-s026 | Statičko idealizovanje i tumačenje ulazne kapacitivnosti |
| 09_1-s027 | Potpuno obrazloženje strujnog opterećenja, margine i izbora najgoreg ulaza |
| 09_1-s028 | Potpuno obrazloženje RC modela, početne struje i formalnog negativnog krajnjeg nivoa |
| 09_1-s029 | Obrazloženje pomeranja granice i provere pri kašnjenju |
| 09_1-s030 | Cilj RC zamene i puna izvorna tvrdnja o trajanju pražnjenja; savremena kola |
| 09_1-s031 | Pune zamene kratkokanalne struje u RON1 i RON2 |
| 09_1-s032 | Puna aritmetička sredina i linearni međukorak koji daje 5/6 |
| 09_1-s033 | Puni RON i IDnsat, izdvajanje faktora, ponovljeni integral i poređenje |
| 09_1-s034 | Obrazloženje orijentacije i dva načina usrednjavanja |
| 09_1-s035 | Puno obrazloženje kompromisa, tehnologije, Lmin i projektovanja širine |
| 09_1-s036 | Obrazloženje izbora dugog kanala i kontrolnog napona |
| 09_1-s037 | Dve pune zamene napona i poništavanje izlaza u uslovu |
| 09_1-s038 | Puna interpretacija jedine radne tačke pri nultoj struji |
| 09_1-s039 | Tumačenje rada, zamena napona i faktorizacija |
| 09_1-s040 | Obe pune zamene i skraćivanje do jednačine po izlazu |
| 09_1-s041 | Povezivanje Δ=0 sa granicom zasićenja i kvadratnom jednačinom |
| 09_1-s042 | Način upotrebe dvaju ekvivalentnih zapisa |
| 09_1-s043 | Puna ravnoteža pomnožena sa dva i zamena napona |
| 09_1-s044 | Pravilo izvoda proizvoda i postupak eliminacije ulaza |
| 09_1-s045 | Uslovi primene rezultata i provera oblasti |
| 09_1-s046 | Obrazloženje zanemarivanja i visokog ulaza |
| 09_1-s047 | Tumačenje poništavanja F i ograničenje statičkog zaključka |
| 09_1-s048 | Puna objašnjenja dinamičke otpornosti u oba režima i kompromisa |
| 09_1-s049 | Razlog izostavljanja dodatnog napajanja i tumačenje stvarnog provođenja |
| 09_1-s050 | Punjenje izlaza do praga opterećenja |
| 09_1-s051 | Puna ravnoteža zasićenih modela i međukorak diferenciranja |
| 09_1-s052 | Ponovljena ravnoteža i izbor fizičke grane pri korenovanju |
| 09_1-s053 | Puna ravnoteža modela i izvorni prvi red diferenciranja |
| 09_1-s054 | Provera pretpostavljenog režima pri primeni rezultata |
| 09_1-s055 | Obrazloženje aproksimacije i smanjenog visokog nivoa |
| 09_1-s056 | Opšta jednačina efekta osnove, VSB,L=VOH, postupci rešavanja i puna objašnjenja pragova |

## Ispravke i stručna pitanja

[Jezička redakcija](jezik_i_rekonstrukcija.md) evidentira slovne i gramatičke ispravke. Na s027 uklonjena je suvišna zagrada prethodnog LaTeX-a: vizuelnim poređenjem potvrđeno je da je nema u originalu. To je ispravka rekonstrukcije.

**13 grupa izvornih stručnih pitanja** ostaje otvoreno na 20 ID-jeva: oznake/indeksi, granica zasićenja s014, uslov zanemarivanja s020, opseg pražnjenja s029/s030, decimali s033, oznaka pMOS krive s034, degenerisani slučajevi s041/s052, izgubljeni koeficijenti i povezani rezultati s044–s047/s051/s053–s055. Predlozi sadrže konkretnu zamenu, izveden dokaz i uslove upotrebe; [P01–P13](otvorena_pitanja.md) nisu primenjeni. Sporni izvorni zapisi ostaju u svom nastavnom odredištu, uključujući beleške s030/s053. Njihova stručna tačnost zato nije potvrđena.

## Provere

```sh
make -C predavanja LECTURE=09_1_mos_logicka_kola all
make -C predavanja LECTURE=09_1_mos_logicka_kola notes
make -C predavanja LECTURE=09_1_mos_logicka_kola review
make -C predavanja LECTURE=09_1_mos_logicka_kola check
python3 predavanja/09_1_mos_logicka_kola/kodovi/provera_logike.py
```

- `all`, `notes`, `review`: uspešna izgradnja LuaLaTeX-om; finalni logovi bez prepunjenih okvira, nedostajućih znakova i LaTeX upozorenja.
- Provereni broj prezentacionih strana, broj/raspored A4 prikaza i oba niza stabilnih ID-jeva: 57/57.
- Pokrivenost: 284/284; nema nepoznatih/nepovezanih elemenata, zastarelih otisaka ili nedostajućih resursa.
- Postojeća računska skripta: **231 poređenje prolazi**, protivprimeri izvornih grešaka potvrđeni. To potvrđuje prenete formule u njenom obuhvatu i otkriva probleme originala; nije odobrenje njihovih ispravki.
- Dodatni dokazi predloga P08/P12 proveravaju i ravnotežu struja i nagib −1 u fizički dopustivim radnim tačkama; [izračunate vrednosti](dokazi_ispravki.json).
- `check`: **NEZAVRŠENO**, isključivo **22 otvorene kategorije na 20 ID-jeva**. Potvrde označavaju `problem` i daju vezu na odgovarajući predlog. Sve preostale kategorije su proverene ili nisu primenljive. Nema drugih strukturnih, sadržinskih ili kompilacionih nalaza u obuhvatu provere.
- [Log provere](../../build/provera-redizajn.log), [svih 22 nalaza](../../build/otvorene-kategorije.log), [računski log](../../build/provera_logike-redizajn.log), [zapis izgradnje i stvarne zavisnosti](izgradnja.json).

## Kontrolne sume pregledane verzije

- Originalni PDF: `9b3e0c4ed413f9ab40e4e7d31607960e3fc4abe2a4566a2e7f46a12fe84d69cb`.
- Početni PDF: `11254a5ac68801bb536021e06bd9c6877c07420a08318859d70098132feac572`.
- Arhiva početnog prikaza: `c9f8c31d6bc4075a411c7a9f7f415f834c53047ab1bba2b7afeadf88bfa5f346`.
- Prezentacioni PDF: `6afbf075cebb1c4f097c4ef9009a6f34fc3c910de15283ae44d5cef8eef53691`.
- PDF beležaka: `154f4e3f1df25708c4988554bd5cb5c35176136d339cfabf16f7bf6c96d65482`.
- Manifest redizajna: `bb97e7f16e17b9da4c5758a4aa1925c1cceb4b04be6a6ac9e3ccfa7099b12aec`.
- Manifest teme: `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41`.

Pojedinačni izvori, renderi originala/početnog/novog prikaza i beležaka, pokrivenost i korišćene zajedničke zavisnosti vezani su otiscima u `pregled.json`; finalni uporedni pregled sadrži i `otisci.json`. Promena relevantnog izvora poništava samo pogođene potvrde, uključujući beleške.

## Precizan sledeći korak

Korisnik odlučuje o P01–P13. Po odluci primeniti samo odobrene izmene u pogođenim slajdovima i njihovim beleškama; obnoviti inventar/pokrivenost ako se sadržaj menja, pokrenuti `notes`, `review`, `check`, ponovo pregledati pogođene prikaze i obnoviti njihove potvrde. Preostale preglede preskočiti ako relevantni izvori, prikazi i zavisnosti nisu menjani. Tek bez nerešenih pitanja predavanje može dobiti `ceka_odobrenje`.

Odobrenje završne prezentacije i dozvola za početak 09_2 vode se odvojeno, uz stvarnu korisnikovu poruku. Ovaj izveštaj ne daje nijedno od tih odobrenja.
