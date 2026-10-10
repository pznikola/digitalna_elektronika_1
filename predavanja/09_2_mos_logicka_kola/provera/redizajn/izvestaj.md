# Izveštaj redizajna — 09_2, MOS logička kola, 2. deo

Datum: **2026-10-03**. Status: **`u_radu`**. Korisnik je izričito odobrio obradu 09_2; rezultat i stručni predlozi nisu odobreni. Predavanje 09_3 nije započeto.

## Isporuka i obuhvat

Pročitan je plan, original sa **31 PDF stranom i 62 izdvojena slajda**, postojeći LaTeX, svi uključeni crteži i početni prikazi. Original, početni prikaz i novi slajdovi pregledani su pojedinačno. Nastavni tekst i formule svih A4 beležaka pročitani su uz njihove ID-jeve i naslove; opširna izvođenja proverena su i na celim A4 stranama.

Uređeni su svih **62/62 slajda**, redosled i ID-jevi **09_2-s001–09_2-s062** ostaju isti. Projekcioni PDF ima 62 strane, A4 PDF beležaka 62 strane, svaki ID odgovara jednom neprekinutom bloku beležaka. Nema dodatnih overlay strana, razdelnika, deljenja ili spajanja. Originalni PDF je neizmenjen. Autorstvo ostaje: prof. dr Lazar Saranovac, Katedra za elektroniku, Digitalna elektronika 1, 2021/22.

- [Prezentacija](../../build/09_2_mos_logicka_kola.pdf)
- [PDF beležaka za predavača](../../build/09_2_mos_logicka_kola_beleske.pdf)
- [Uporedni pregled: original / početni / novi slajd / beleške](../../build/redizajn/pregled/index.html)
- [Mapa pokrivenosti](pokrivenost.md), [pojedinačne potvrde](pregled.json)
- [Stručni predlozi P01–P16](otvorena_pitanja.md)

## Izgled i reprezentativna poređenja

Primenjen je postojeći, verzionisani **etf-v1**, stil B. Njegovi fajlovi/resursi nisu menjani. Osnovni font ostaje 11 pt, naslovi 18 pt; šeme koriste čitljive oznake 9–10 pt. Bela pozadina, taman tekst i lokalno tamnocrveno isticanje `#A32638` prate prihvaćenu 01. Prepunjenost je rešena rasporedom i potpunim beleškama istog slajda, bez smanjivanja celog slajda.

| Primer | Promena i poređenje pre/posle |
|---|---|
| [s002–s004](../../build/redizajn/pregled/index.html#09_2-s004) | Kompaktan depletion invertor levo; bilans i pragovi jasno odvojeni. Duga diferenciranja imaju puna objašnjenja u beleškama; oba člana sistema s004 ostaju vidljiva. |
| [s011/s023](../../build/redizajn/pregled/index.html#09_2-s023) | Tropriključna šema, šema sa osnovama i fizički presek raspoređeni jedan uz drugi uz odgovarajuće razmake. Očuvane sve veze, kontakti i dopirane oblasti. |
| [s012–s015](../../build/redizajn/pregled/index.html#09_2-s012) | Negativna i pozitivna konvencija imaju dosledne rasporede: definicije i uslovi vidljivi, modeli razdvojeni. Izvorne stručne nedoslednosti ostaju izdvojene u P02. |
| [s017/s018](../../build/redizajn/pregled/index.html#09_2-s017) | Prva i druga jednačina imaju jasan sled; višeredni izrazi poravnati. Izvorni sporni koeficijenti nisu prećutno promenjeni. |
| [s027/s033](../../build/redizajn/pregled/index.html#09_2-s027) | Aproksimacije, bilans i rezultat izdvojeni; pune racionalne polazne jednačine i međukoraci u beleškama. |
| [s037](../../build/redizajn/pregled/index.html#09_2-s037) | Šema, karakteristika i svih pet parova oblasti vidljivi; natpisi pragova razdvojeni od krive i jedan od drugog. |
| [s040–s045](../../build/redizajn/pregled/index.html#09_2-s040) | Projektantski uslovi odvojeni od rezultata za odnos širina; konačni izrazi ostaju na slajdovima, duge zamene parametara u beleškama. |
| [s047/s048](../../build/redizajn/pregled/index.html#09_2-s048) | Sačuvana cela istorijska lista i 18 veza; primer zaokruživanja prikazan tabelom uz šemu sa širinama 2/1. |
| [s050/s051](../../build/redizajn/pregled/index.html#09_2-s050) | Presek i parazitno kolo odvojeni; precizni NPN/PNP simboli, pregledni bazni vodovi, spojne tačke i odvojene oznake. Potpuna petlja reakcije u beleškama. |
| [s055](../../build/redizajn/pregled/index.html#09_2-s055) | Razdvojeni prikazi punjenja i pražnjenja, vidljive sve energije; energetski integral potpuno prenet u beleške. |
| [s058/s059](../../build/redizajn/pregled/index.html#09_2-s059) | Strelica iSC odvojena od VO; vremenske dimenzije izvan talasnih oblika; tri nivoa imaju zasebne natpise. |
| [s060–s062](../../build/redizajn/pregled/index.html#09_2-s062) | Definicije PDP/EDP, rezultat i optimum vidljivi; jedinice i postupak optimizacije objašnjeni u beleškama. |

Uređeno je **47 postojećih TikZ izvora**; potpuni spisak i provera priključaka/polariteta/topologije su u [proveri šema](provera_sema.md). Svi ostaju vektorski i uređivi.

## Beleške i mapa sadržaja

**280/280 elemenata ima provereno nastavno odredište**: 263 izvorne sadržajne grupe i 17 dopunskih objašnjenja. Potvrda pokrivenosti potvrđuje prisustvo sadržaja, ne stručnu tačnost spornih izvornih zapisa. Ključne definicije, rezultati, uslovi i ilustracije ostaju vidljivi.

Postoje 62 zasebna izvora beležaka; s001 ima samo ID, ostalih 61 smislen nastavni tekst. Beleške potpuno objašnjavaju uklonjene detalje i potrebne međukorake, bez uredničkih naslova, porekla, istorije rada, odluka ili predloga ispravki. Poreklo i odvojene dopune nalaze se u [evidencija_beleski.json](evidencija_beleski.json); to nije druga kopija nastavnog teksta. Sav nastavni tekst uređuje se samo u `beleske/sNNN.tex`.

U 83 unosa mape beleške su odredište (uključujući s004 sa odredištem i na slajdu). Sledeća tabela navodi sadržajne grupe, ne prepisuje beleške:

| ID | Sadržaj za dodatno izlaganje |
|---|---|
| 09_2-s002 | Provera nemogućnosti nulte struje u zasićenju TL i izbor radne tačke |
| 09_2-s003 | Ravnoteža pre i posle zamene napona priključaka i objašnjenje zamena |
| 09_2-s004 | Polazna ravnoteža i oba reda diferenciranja, dve nepoznate |
| 09_2-s005 | Promena radnih tačaka i naponski uslovi u oznakama priključaka; Ravnoteža pre zamene i izbor pozitivne grane korena |
| 09_2-s006 | Razlozi idealizovane vertikale i fizičko značenje korekcija modela |
| 09_2-s007 | Promena napona, ravnoteža priključaka i diferenciranje |
| 09_2-s008 | Zamena ulazne logičke jedinice i obrazloženje zanemarenog kvadrata; Provera pretpostavke za zanemarivanje kvadratnog člana |
| 09_2-s009 | Prvi parametarski uslov za VOL i objašnjenje regeneracije nivoa u kaskadi |
| 09_2-s010 | Čitanje osa i graničnih tačaka karakteristike |
| 09_2-s011 | Obrazloženje odsustva problema polarizacije osnove |
| 09_2-s012 | Tumačenje predznaka i algebarsko preuređenje napona zasićenja; Algebarski postupak ekvivalentnosti oba napona zasićenja |
| 09_2-s013 | Tumačenje predznaka i izbor pogodnog oblika struje |
| 09_2-s014 | Povezanost sa apsolutnim vrednostima negativnih napona; Eksplicitna veza napona VSG=−VGS i VSD=−VDS |
| 09_2-s015 | Izbor zapisa i potreba dosledne konvencije |
| 09_2-s016 | Nulta radna tačka i odbacivanje zasićenja sa prikazanom nenultom strujom |
| 09_2-s017 | Ravnoteža pre zamene i oba reda diferenciranja |
| 09_2-s018 | Ponovljeni i normalizovani zapis VIL i tumačenje svih odnosa |
| 09_2-s019 | Uslovi priključaka, početni bilans i izvorne oznake T1/T2 |
| 09_2-s020 | Početna ravnoteža, diferenciranje i alternativni zapis VIH sa faktorom četiri |
| 09_2-s021 | Opšta polazna ravnoteža, linearizacija i skraćivanje pri jednakim pragovima |
| 09_2-s022 | Nesređeni uslov VOL i objašnjenje oba kriterijuma održivosti |
| 09_2-s023 | Tumačenje zajedničkih gejtova i drejnova iz preseka |
| 09_2-s024 | Odbacivanje zasićenja P, uključujući ceo izvorni izraz |
| 09_2-s025 | Početak provođenja, dugački kanal i uslovi oba tranzistora u oznakama priključaka |
| 09_2-s026 | Negativna konvencija P i razlog smera nejednakosti |
| 09_2-s027 | Puna polazna ravnoteža sa imeniteljima; Diferenciranje i nenormalizovani VI zajedno sa ekvivalentnim zapisom |
| 09_2-s028 | Razlog pojednostavljenja i tok zamene u ravnotežu; Tok zamene simetrije u jednačinu nagiba |
| 09_2-s029 | Promena radnih tačaka i uslovi u oznakama priključaka |
| 09_2-s030 | Ravnoteža u oznakama priključaka; Razjašnjenje realnog nagiba i veza sa posebnim izvođenjem za ispit |
| 09_2-s031 | Prelaz N u omsku oblast i uslovi u oznakama priključaka |
| 09_2-s032 | Početna ravnoteža priključaka i zamene napona |
| 09_2-s033 | Puna ravnoteža kratkog kanala i obrazloženje aproksimacija |
| 09_2-s034 | Zamena i oba međukoraka kvadratne jednačine, postupak rešavanja; Poništavanje kvadratnih članova pri rešavanju |
| 09_2-s035 | Promena radne tačke N i značaj krajnjih nivoa |
| 09_2-s036 | Tumačenje margina i zamena krajnjih napona; Tumačenje obe definicije margine šuma |
| 09_2-s037 | Tumačenje regeneracije nivoa i sređivanje obe nejednakosti; Međukoraci sređivanja nejednakosti održivosti |
| 09_2-s038 | Tumačenje tačke prebacivanja i pristup tri naredna izvođenja |
| 09_2-s039 | Objašnjenje predznaka i poreklo naziva ratio |
| 09_2-s040 | Geometrijski izraz kP/kN i postupak podešavanja širinama |
| 09_2-s041 | Ekvivalentna ravnoteža sa LC faktorima i algebarski međukoraci |
| 09_2-s042 | Puna zamena k parametara i skraćivanje faktora |
| 09_2-s043 | Obrazloženje dominantnih članova |
| 09_2-s044 | Početna linearna ravnoteža struja sa Cox i VI |
| 09_2-s045 | Tok izvođenja i poređenje navedenih odnosa |
| 09_2-s046 | Određivanje širine uz dozvoljene dimenzije tehnologije |
| 09_2-s047 | Potpun opis reprezentativne geometrije i prilagođavanja parametara |
| 09_2-s048 | Polovina minimalne dimenzije, skaliranje i konvencija označavanja; Najmanje zauzeće/kapacitivnosti, kompromis i oprez pri većim tranzistorima; Razjašnjenje greške preuranjenog zaokruživanja |
| 09_2-s049 | Potpun mehanizam nakupljanja naelektrisanja i delovanja dioda |
| 09_2-s050 | Povezivanje fizičke strukture sa elementima ekvivalentnog kola; Veza otpornosti ostrva/osnove sa ekvivalentnim kolom |
| 09_2-s051 | Potpun opis regenerativne petlje iz originala; Pokretanje negativnim impulsom na TP i samoodrživ kratki spoj |
| 09_2-s052 | Ograničen strujni kapacitet izvora, spoljašnji priključci i smanjenje međusobnog uticaja |
| 09_2-s053 | Oba primera značenja kapaciteta baterije; Oprez za složene sisteme i izvorna tvrdnja o manjim stvarnim strujama |
| 09_2-s054 | Objašnjenje dva odvojena mehanizma; Tumačenje dva odvojena mehanizma disipacije |
| 09_2-s055 | Puni integral napajanja sa izvornim zapisom integranda; Puna razlika energija i objašnjenje oba procesa |
| 09_2-s056 | Detaljno energetsko tumačenje i izvorni primer overklokovanja |
| 09_2-s057 | Sve izvorne tvrdnje o overklokovanju, hlađenju i baterijskim sistemima |
| 09_2-s058 | Mehanizam istovremenog provođenja i površine oba trougla; Razlikovanje trajanja cele ivice i istovremenog provođenja |
| 09_2-s059 | Puno objašnjenje naponskog intervala, linearne ivice, 10–90% i dva impulsa; Tumačenje 10–90% definicije i faktor dva za dve ivice |
| 09_2-s060 | Objašnjenje poređenja tehnologija i poništavanja kašnjenja; Jedinica PDP u prikazanom modelu |
| 09_2-s061 | Tumačenje dodatnog faktora kašnjenja; Jedinica EDP i poređenje pod istim opterećenjem |
| 09_2-s062 | Početna otpornost sa izvornim lambda predznakom i svrha optimizacije; Izvod, domen i potvrda minimuma pojednostavljene EDP funkcije |

## Provere i ograničenja

Izvršene su komande za konkretno predavanje:

```sh
make -C predavanja LECTURE=09_2_mos_logicka_kola all
make -C predavanja LECTURE=09_2_mos_logicka_kola notes
make -C predavanja LECTURE=09_2_mos_logicka_kola review
make -C predavanja LECTURE=09_2_mos_logicka_kola check
python3 predavanja/09_2_mos_logicka_kola/kodovi/provera_redizajna.py
```

`all`, `notes` i `review` uspešno proizvode oba PDF-a i HTML. Poslednji LaTeX logovi nemaju overfull hbox/vbox, nestale znakove ili upozorenja. Broj/redosled/ID-jevi, neprekinuti blokovi beležaka, odredišta, resursi i aktuelne potvrde odgovaraju izvorima. **179 postojećih + 24 dopunska računska poređenja = 203 uspešna poređenja**. Dopunska skripta pokreće se zasebno; postojeći `check` automatski pokreće `provera_logike.py`. Računski dokazi potvrđuju i protivprimere izvornih grešaka; njihov prolaz ne znači da su te greške ispravljene u nastavnom materijalu.

`check` vraća **NEZAVRŠENO: 50 otvorenih kategorija na 32 ID-ja**, tačno zbog P01–P16. Nema dodatnih nepokrivenih elemenata, zastarelih otisaka ili problema kompilacije. Izgled je pregledan, ali predavanje nije spremno za završno sadržinsko prihvatanje dok stručna pitanja ostaju nerešena.

[Jezička evidencija](jezicke_ispravke.md) razlikuje gramatičku redakciju i ispravke rekonstrukcije od stručnih predloga. Pitanja obuhvataju NMOS koren/odnos i održivost, pseudo NMOS izvod, PMOS konvenciju i brzinske modele, indekse, CMOS oblast i normalizaciju, domen linearne aproksimacije, značenje tehnološkog čvora, zaštitne diode, RS1/RS2, energetsku jedinicu/integral/trajanja i uslove optimuma EDP. Predlozi nisu primenjeni; sporan zapis ostaje u svom nastavnom odredištu, uključujući beleške.

## Otisci pregledane verzije

| Fajl | SHA-256 |
|---|---|
| Originalni PDF | `da2c97a21eab5b7a0c553e2e2edd61a7c9c3fd6319deed1a0ee7136f556f0483` |
| Manifest teme | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |
| Manifest redizajna | `98fe349f9cfcceae23c4187cd90d1545972c778d2dfbd9e1cf9271655203710a` |
| Početni snapshot | `850e31d4bc7320a5d0e2c27ef47c431381e585d1833d43a466cb82afea657c04` |
| Arhiva početnog prikaza | `ff69f855e410dbb6b854a3ac5be9cb26d7d1ae740daf5e8d7a4d3d4936adfafd` |
| Prezentacioni PDF | `2d15bc3d254edb7a325f1f11baaeaa468c760416f924e21913c8f5fc06c7576f` |
| PDF beležaka | `64e5959784d6316ae2aa8fdf1cf98236396c52a846e87ded4fccec00f82d88d2` |
| Zapis izgradnje | `fc26974ea8de89e7f2f04a066e155d71378d46b157d2f7a35a9cd0c095e25eac` |
| Potvrde prikaza | `ad8aae1afb7bdd4edb24e2d710bcc66b3e46c498118de34e381ed620fb469915` |
| Inventar | `982fc96be4156c087a5aa0435359150c1f1f859c6f0ec5226eeffc80ae6f73e1` |
| Mapa odredišta | `d83135f5826b69cb07b2746278537a6cbb4dab24a3ac7310735fc1c12a4830df` |
| Evidencija beležaka | `2499ea0244916d503f30b409c525babb577fc115d1f0fae7ff96584f2e20b4d8` |

Pojedinačni otisci originala, početnog i novog prikaza, izvora, beležaka, mape i korišćene teme nalaze se u `pregled.json` i `izgradnja.json`. Arhiva polaznog prikaza je izvan ignorisanog build/; `init` ne pokretati ponovo.

## Precizan sledeći korak

1. Sačekati korisnikove odluke o [P01–P16](otvorena_pitanja.md); odluke evidentirati doslovno u `odluke.md`.
2. Primeniti samo odobrene stručne izmene na pogođene slajdove i beleške istog ID-ja. Ne prebacivati obrazloženja odluka u nastavni PDF.
3. Ažurirati pogođene unose pokrivenosti i inventara, izgraditi `notes`/`review`, pojedinačno pregledati pogođene prikaze, obnoviti potvrde i pokrenuti `check`.
4. Tek kada nema otvorenih sadržinskih problema, predati završni rezultat na prihvatanje. Prihvaćen rezultat 09_2 i početak 09_3 evidentirati kao odvojene korisnikove odluke.

Naredni agent nastavlja od ove kontrolne tačke, ne ponavlja celu već evidentiranu analizu. Izmena relevantnog izvora, beleške ili korišćene teme poništava pogođene potvrde, uključujući prikaz beležaka. Rezultati ranijih predavanja nisu prihvaćeni ovim nalogom.
