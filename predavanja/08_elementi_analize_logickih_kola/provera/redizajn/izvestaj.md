# Izveštaj redizajna — 08, Elementi analize logičkih kola

Datum: **2026-10-03**. Status: **u_radu**. Izgled i nastavni tekst beležaka obrađeni su za svih 67 slajdova. Završna sadržinska potvrda čeka odluku o **12 grupa stručnih nedoslednosti originala**, na 19 ID-jeva. Agent nije dao odobrenje rezultata niti prelaska na sledeće predavanje.

## Isporuka i obuhvat

- [Prezentacija — 67 strana](../../build/08_elementi_analize_logickih_kola.pdf).
- [A4 PDF za predavača — 67 strana](../../build/08_elementi_analize_logickih_kola_beleske.pdf).
- [Original / početna rekonstrukcija / novi slajd / beleške](../../build/redizajn/pregled/index.html).
- [Konkretni stručni predlozi P01–P12](otvorena_pitanja.md).
- [Mapa pokrivenosti](pokrivenost.md), [inventar](inventar.json), [poreklo beležaka](poreklo_beleski.json), [potvrde pregleda](pregled.json), [izgradnja](izgradnja.json), [odluke](odluke.md).

Obrađeno je samo predavanje 08, po korisnikovom izričitom nalogu evidentiranom u `odluke.md`. Pregledane su sve 34 originalne PDF strane, svih 67 izdvojenih originalnih slajdova, početni izvori i njihov kompajlirani prikaz, novi slajdovi u punoj veličini i sve A4 beleške. Poslednja prazna donja polovina izvornog PDF-a nije slajd.

Broj, redosled i ID-jevi `08-s001`–`08-s067` ostaju nepromenjeni. Nema brisanja, spajanja, deljenja ili overlay strana. Originalni PDF je neizmenjen. Početna rekonstrukcija sačuvana je u `build/redizajn/pre/` i u trajnoj [arhivi](pocetni_prikaz.tar.gz), zajedno sa izvorima i zavisnostima. Istorijski `provera/pregled.json`, `provera/izvestaj.md` i `provera/uocene_greske.md` nisu prepisani potvrdom redizajna.

## Izgled i reprezentativna poređenja

Predavanje je vezano za verziju `etf-v1`, stil B. Font ostaje Latin Modern; telo teksta je 11 pt, matematička tipografija dosledna, oznake dijagrama najmanje 9 pt u prikazu. Za zbijene dijagrame skraćena je geometrija, bez smanjivanja fonta celog slajda. Lokalni nastavni akcent je tamnocrvena `#A32638`, kao na 01. To je odluka za prezentaciju, a ne tvrdnja o zvaničnoj ETF paleti. Zajednička tema nije menjana.

Autorstvo, Katedra za elektroniku i školska godina 2021/22 ostaju prema izvornom materijalu. Datum obrade vodi se u ovoj evidenciji.

| Slajdovi / poređenje | Promena i rezultat |
|---|---|
| [s003](../../build/redizajn/pregled/index.html#08-s003) | Logički i fizički opis razdvojeni; detaljno tumačenje ulaza/izlaza i prelaznih oblasti dato u beleškama. |
| [s005–s008](../../build/redizajn/pregled/index.html#08-s008) | Kompaktnije napojne i povratne putanje, oznake izvan simbola, jasni spojevi i sačuvane lokalne putanje dekaplinga. Razdelnici 1000/1001 i 1/2, objašnjenje energije i lokalnih kondenzatora potpuno preneti u odgovarajuće beleške. |
| [s009/s015](../../build/redizajn/pregled/index.html#08-s015) | Četvoropol sa jasnim referentnim smerovima i urednim portovima; sačuvana topologija i nelinearne impedanse. |
| [s013/s016/s017](../../build/redizajn/pregled/index.html#08-s016) | Jednake logičke kapije, oznake izvan tela, putanje do priključaka i oznake oblasti iznad karakteristika. Nema vodova preko tela kapija. |
| [s019/s021/s025](../../build/redizajn/pregled/index.html#08-s019) | Kraće kaskade i čitljivije ose/oznake; razdvojeni dijagrami i njihove nastavne oznake, bez preklapanja. |
| [s035/s036](../../build/redizajn/pregled/index.html#08-s036) | Precrtane ivice i oznake 10/90/50%; strelice vremena smeštene izvan talasnih oblika, merne tačke poravnate. Definicije vremena ostaju vidljive. |
| [s041/s042/s046](../../build/redizajn/pregled/index.html#08-s046) | Kompaktne uređive električne šeme; jasni priključci, polariteti, struje, napajanje i Tevenenova zamena. Stručna greška u jednačini s042 nije prećutno ispravljena. |
| [s050](../../build/redizajn/pregled/index.html#08-s050) | Rezultati 2.2τ i 0.69τ i tok izvođenja ostaju na slajdu; pune zamene 10/90/50% i logaritmovanje su u njegovim beleškama. |
| [s057/s058](../../build/redizajn/pregled/index.html#08-s058) | Dva modela opterećenja su poravnata; šema i impuls odvojeni od računa. Strelica s058 više ne prolazi kroz tekst. Namerno pogrešan postupak i upitnici su sačuvani, uz nastavno objašnjenje razloga u beleškama. |
| [s059–s061](../../build/redizajn/pregled/index.html#08-s059) | Tri pobude s059 u jednoj ravni, pregledniji blokovi formula, potpuni međukoraci u beleškama istog slajda. Izvorne nenamerne greške s059 izdvojene su u P10. |
| [s063](../../build/redizajn/pregled/index.html#08-s063) | Četiri talasna dijagrama u mreži 2×2; oznake odnosa TI/τ iznad, amplituda i trenuci izvan krivih. |
| [s067](../../build/redizajn/pregled/index.html#08-s067) | Šema i izrazi u gornjem redu, četiri kvalitativna odziva ispod. Odvojene oznake R/C i strelica izlaza; kompenzacioni uslov vidljiv. Opšti početni uslov čeka P12. |

Ukupno su uređena **73 vektorska izvora na 42 slajda**: negde potpuno precrtani, a negde popravljene geometrija, spojevi, debljine i oznake. Šeme ostaju uređive; kvalitativne karakteristike nisu predstavljene kao numerički izmereni podaci. Vodovi su povezani na priključke, spojene grane imaju pune tačke, a nespojena ukrštanja nisu proglašena spojevima.

## Beleške i pokrivenost

Postoji 67 zasebnih `beleske/sNNN.tex`, sa eksplicitnom vezom na odgovarajući ID i nevidljivim sidrima. S001 ima samo ID jer naslovnom slajdu nije potrebno dodatno veštačko objašnjenje. Ostalih 66 sadrže nastavni tekst za predavača, formule i međukorake gde su potrebni.

Nema vidljivih naslova o poreklu/redizajnu, oznaka „Izvor: PDF strana”, kontrolnih suma, odluka ili zahteva za odobrenje. Poreklo, preneti delovi, proverene dopune i otvorena pitanja vode se u `provera/redizajn/`; nastavnog teksta nema u drugoj paralelnoj kopiji. Sačuvani su svi preneti izvorni detalji. Stručne nedoslednosti originala, uključujući intuitivni argument s043, ostaju evidentirane kao problem do odluke.

Inventar sadrži **232 elementa: 209 izvornih i 23 izdvojene dopune**. Svih 232 ima provereno odredište na istom slajdu ili u njegovim beleškama. Kratke dopune unutar prenetih objašnjenja dodatno su opisane metapodacima u `poreklo_beleski.json`. Potvrda pokrivenosti znači da sadržaj nije izgubljen; ne proglašava izvorne stručne greške tačnim.

Detaljniji originalni tekst ili međukoraci preneti su u beleške s003, s005–s008, s010–s013, s015, s017, s022, s025, s027–s030, s033, s035–s039, s041, s043, s045–s047, s049–s051, s053–s056, s058–s062, s064–s067. Mapa navodi svaki pojedinačni element i njegovo sidro; nijedna cela logička celina nije zamenjena beleškama. Definicije, relevantni uslovi, rezultati, tabele i nastavne šeme ostaju vidljivi.

## Jezičke i rekonstrukcijske ispravke

- S003: „nuli” → „nulu”, „nelinerana” → „nelinearna”; sređene rečenice o fizičkoj i logičkoj veličini bez promene značenja.
- S011: „u logičko kola” → „u logičko kolo”; stručna tvrdnja o verovatnoći ostaje P01.
- S012: jezički uređena rečenica o šematski identičnim kolima; nesaglasni stručni završetak sačuvan za P01.
- S015: „smatrano” → „smatramo”, „na njegov izlazu” → „na njegovom izlazu”.
- S026: „fukciji” → „funkciji”; s038: „ulaznom signala” → „ulaznom signalu”.
- S043: „na ulaz”, „napona”, „kondezatoru”, „i nekom” gramatički/slovno uređeni u prenetom pasusu; stručni problem nije uklonjen.
- S051: „Dugačije” → „Drugačije”; s065: „stuje” → „struje”. S035 u beleškama koristi čitljivo „silazne ivice”.
- S024: `a=+1` na dva mesta prethodne rekonstrukcije vraćeno na izvorno `a=−1`, potvrđeno originalnim prikazom i izvlačenjem teksta. Ovo je ispravka odstupanja rekonstrukcije od originala, ne nova promena izvorne formule.

Ostala preformulisanja služe rasporedu: izvorni pasusi potpuno su sačuvani u beleškama kada su skraćeni na slajdu. Stručne promene formula, vrednosti, topologije i tvrdnji navedene u P01–P12 nisu primenjene.

## Provere i praktična ograničenja

```sh
make -C predavanja all LECTURE=08_elementi_analize_logickih_kola
make -C predavanja notes LECTURE=08_elementi_analize_logickih_kola
make -C predavanja review LECTURE=08_elementi_analize_logickih_kola
make -C predavanja check LECTURE=08_elementi_analize_logickih_kola
python3 predavanja/08_elementi_analize_logickih_kola/kodovi/provera_logike.py
```

`all`, `notes` i `review` uspešno izgrađuju prezentaciju i A4 beleške. Konačni logovi nemaju greške, `Overfull`, `Underfull` ni upozorenja. Oba PDF-a imaju po 67 strana; prezentacija je 16:9, beleške A4. Provereni su tačan skup/redosled ID-jeva i pravilno povezivanje beležaka sa slajdom. Nema nedostajućih resursa, izgubljenih odredišta ili zastarelih otisaka pregleda.

Postojeća računska provera prolazi: **72 RC/CR stanja**, impulsni odziv superpozicijom i po intervalima, naponske margine, struje/grananje, vremena 10/90/50%, RL i uslov kompenzacije. Dodatni nezavisni dokazi predloženih ispravki su u [provera_predloga.json](provera_predloga.json), uključujući 48 tačaka odziva razdelnika sa nenultim prethodnim stanjem. Ti dokazi potvrđuju predložene izraze, ne pogrešne zapise originala.

`check` vraća **NEZAVRŠENO** isključivo zbog **26 namerno nepotvrđenih stručnih kategorija na 19 ID-jeva**, povezanih sa P01–P12. Puna lista stvarnih nalaza je u [provere.json](provere.json). U tim kategorijama rezultat je `problem`; ostale primenljive kategorije stvarno pregledanog materijala su `provereno`. Automatska provera ne zamenjuje pregled svake šeme, formule i slajda. Prezentacija još nije spremna za završno prihvatanje nastavne tačnosti.

## Dodatna dorada po ponovljenom nalogu, 2026-10-03

Provereni su lokalni otisci svih 67 slajdova i beležaka prema prethodnoj isporuci: korisnik ih u međuvremenu nije promenio. Sačuvani su važeći pregledi nepromenjenog materijala. Pre dorade je arhivirana [prethodna evidencija i pogođeni izvori](istorija/2026-10-03-pre-dodatna-dorada/).

Dodatno su upoređeni nastavni tekst i formule sa originalom. Na s046 skraćen je uvod u Tevenenovu zamenu; potpuni smisao i objašnjenje ostaju u njegovim beleškama. Na s049 jasno su razdvojeni krajnja vrednost, matematički završetak i praktični kriterijum 5τ/99.3%, uz potpuno objašnjenje u beleškama. Beleške s004 sada objašnjavaju postupak merenja i razliku kašnjenja/trajanja ivice; s014 izbor manje margine i izvođenje identiteta njihovog zbira; s039 kvadratno izdvajanje doprinosa kola; s045 postupak deaktiviranja izvora, bez ponavljanja vidljive definicije τ.

Na s039 dodat je kratak, nezavisno proveren primer: izmereni 5 ns i 3 ns daju doprinos kola 4 ns, jer je 5²−3²=4². Primer ima zaseban element `08-s039:e04`, sidro i poreklo dopune. Novi inventar ima 232 elementa (209 izvornih + 23 dopune), svi sa proverenim odredištem. Rezultati provere primera i identiteta margina su u [dodatna_provera.json](dodatna_provera.json).

Pojedinačno su pregledani novi projektovani slajdovi s046/s049 i sve pogođene A4 strane; obnovljene su samo potvrde s004, s014, s039, s045, s046 i s049. `review` uspešno gradi oba PDF-a; konačni logovi ostaju bez grešaka i upozorenja. Broj i redosled ostaju 67/67. Stručni predlozi P01–P12 nisu primenjeni, jer ponovljeni nalog nije njihovo izričito odobrenje. `check` i dalje ima samo istih 26 otvorenih stručnih kategorija na 19 ID-jeva.

## Kontrolne sume pregledane verzije

| Resurs | SHA-256 |
|---|---|
| Originalni PDF | `55221ef5cb220ba6c31a345ad9b685811f7068f466ac25ef9beff941f4a349b1` |
| Početni prezentacioni PDF | `724ef06c584c33a2d69b7609e9d91f5601803570d78342f163ebfcbcb547486d` |
| Arhiva početnog stanja | `54cf443535c72d358e138edf007ba92ba4ca2adce7c80dd78455ca0d4b41a0de` |
| Manifest teme etf-v1 | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |
| Manifest redizajna | `f6499f651e9bcffea3c4c8d63842f6539e57e4aa0de5cc878ca5702d09b75265` |
| Novi prezentacioni PDF | `946eab59337861c6b586a11e0c9f6b7133dccaed15c8349225ffef95c1e35988` |
| A4 PDF beležaka | `2a6e109393676d4a5a88c6770cd5398fa56385321366066ce555a663db851fe4` |

Stvarni ulazi, alati i izlazi su u `izgradnja.json`. Pojedinačni otisci originala, početnog prikaza, novog slajda, njegovih beležaka i relevantnih zavisnosti su u `pregled.json`. Promena beležaka poništava njihove pogođene potvrde i zahteva novi prikaz/pregled.

## Sledeći korak

Korisnik bira ispravke iz [P01–P12](otvorena_pitanja.md). Naredni agent čita ovu kontrolnu tačku, odluke i aktuelne otiske, primenjuje samo odobrene stručne promene i pregleda pogođene slajdove i beleške. Ne ponavlja već potvrđenu analizu nepromenjenog materijala.

Posle uspešnog `check`, ažuriranja izveštaja i statusa `ceka_odobrenje` sledi zasebno prihvatanje rezultata 08. Početak 09_1 **nije odobren**. Nalog za 08 nije odobrenje rezultata ili stručnih predloga 07.

## Uređeni vektorski izvori

- [s002_apstraktni_signal.tex](../../slike/tikz/s002_apstraktni_signal.tex)
- [s003_realni_signali.tex](../../slike/tikz/s003_realni_signali.tex)
- [s005_napajanje.tex](../../slike/tikz/s005_napajanje.tex)
- [s005_oznake_napajanja.tex](../../slike/tikz/s005_oznake_napajanja.tex)
- [s006_masa.tex](../../slike/tikz/s006_masa.tex)
- [s007_promena_potrosnje.tex](../../slike/tikz/s007_promena_potrosnje.tex)
- [s007_zajednicko_napajanje.tex](../../slike/tikz/s007_zajednicko_napajanje.tex)
- [s008_dekapling_potrosac.tex](../../slike/tikz/s008_dekapling_potrosac.tex)
- [s008_lokalni_kondenzatori.tex](../../slike/tikz/s008_lokalni_kondenzatori.tex)
- [s009_cetvoropol.tex](../../slike/tikz/s009_cetvoropol.tex)
- [s010_oblast_prenosa.tex](../../slike/tikz/s010_oblast_prenosa.tex)
- [s011_opsezi_napona.tex](../../slike/tikz/s011_opsezi_napona.tex)
- [s013_lanci_kola.tex](../../slike/tikz/s013_lanci_kola.tex)
- [s013_opsezi_nivoa.tex](../../slike/tikz/s013_opsezi_nivoa.tex)
- [s015_cetvoropol.tex](../../slike/tikz/s015_cetvoropol.tex)
- [s016_invertujuca.tex](../../slike/tikz/s016_invertujuca.tex)
- [s016_lanac_bafera.tex](../../slike/tikz/s016_lanac_bafera.tex)
- [s016_lanac_invertora.tex](../../slike/tikz/s016_lanac_invertora.tex)
- [s016_neinvertujuca.tex](../../slike/tikz/s016_neinvertujuca.tex)
- [s017_dozvoljene_oblasti.tex](../../slike/tikz/s017_dozvoljene_oblasti.tex)
- [s017_tri_oblasti.tex](../../slike/tikz/s017_tri_oblasti.tex)
- [s018_invertujuca.tex](../../slike/tikz/s018_invertujuca.tex)
- [s018_neinvertujuca.tex](../../slike/tikz/s018_neinvertujuca.tex)
- [s019_dva_invertora.tex](../../slike/tikz/s019_dva_invertora.tex)
- [s019_dva_prenosa.tex](../../slike/tikz/s019_dva_prenosa.tex)
- [s019_preklopljene_karakteristike.tex](../../slike/tikz/s019_preklopljene_karakteristike.tex)
- [s020_invertujuca.tex](../../slike/tikz/s020_invertujuca.tex)
- [s020_neinvertujuca.tex](../../slike/tikz/s020_neinvertujuca.tex)
- [s021_cetiri_invertora.tex](../../slike/tikz/s021_cetiri_invertora.tex)
- [s021_regeneracija.tex](../../slike/tikz/s021_regeneracija.tex)
- [s023_dodavanje_suma.tex](../../slike/tikz/s023_dodavanje_suma.tex)
- [s024_granicni_naponi.tex](../../slike/tikz/s024_granicni_naponi.tex)
- [s024_tacke_pojacanja.tex](../../slike/tikz/s024_tacke_pojacanja.tex)
- [s025_visestruki_sum.tex](../../slike/tikz/s025_visestruki_sum.tex)
- [s027_cetvoropol.tex](../../slike/tikz/s027_cetvoropol.tex)
- [s027_spoj_i_struje.tex](../../slike/tikz/s027_spoj_i_struje.tex)
- [s029_izvor_struje.tex](../../slike/tikz/s029_izvor_struje.tex)
- [s029_ponor_struje.tex](../../slike/tikz/s029_ponor_struje.tex)
- [s032_fanout.tex](../../slike/tikz/s032_fanout.tex)
- [s034_idealna_karakteristika.tex](../../slike/tikz/s034_idealna_karakteristika.tex)
- [s035_ivice_signala.tex](../../slike/tikz/s035_ivice_signala.tex)
- [s035_vremena_ivica.tex](../../slike/tikz/s035_vremena_ivica.tex)
- [s036_period_i_kasnjenje.tex](../../slike/tikz/s036_period_i_kasnjenje.tex)
- [s040_idealan_signal.tex](../../slike/tikz/s040_idealan_signal.tex)
- [s041_rc_kolo.tex](../../slike/tikz/s041_rc_kolo.tex)
- [s041_step_pobuda.tex](../../slike/tikz/s041_step_pobuda.tex)
- [s042_rc_struje.tex](../../slike/tikz/s042_rc_struje.tex)
- [s046_slozeno_kolo.tex](../../slike/tikz/s046_slozeno_kolo.tex)
- [s046_tevenen_rc.tex](../../slike/tikz/s046_tevenen_rc.tex)
- [s049_eksponencijalni_odziv.tex](../../slike/tikz/s049_eksponencijalni_odziv.tex)
- [s054_integrator.tex](../../slike/tikz/s054_integrator.tex)
- [s054_odziv.tex](../../slike/tikz/s054_odziv.tex)
- [s055_diferencijator.tex](../../slike/tikz/s055_diferencijator.tex)
- [s056_odziv_diferencijatora.tex](../../slike/tikz/s056_odziv_diferencijatora.tex)
- [s057_model_izlaza.tex](../../slike/tikz/s057_model_izlaza.tex)
- [s057_model_veze.tex](../../slike/tikz/s057_model_veze.tex)
- [s058_impuls.tex](../../slike/tikz/s058_impuls.tex)
- [s058_rc.tex](../../slike/tikz/s058_rc.tex)
- [s059_negative.tex](../../slike/tikz/s059_negative.tex)
- [s059_pulse.tex](../../slike/tikz/s059_pulse.tex)
- [s059_step.tex](../../slike/tikz/s059_step.tex)
- [s060_integrator.tex](../../slike/tikz/s060_integrator.tex)
- [s060_promena_pocetka.tex](../../slike/tikz/s060_promena_pocetka.tex)
- [s062_pogresna_pretpostavka.tex](../../slike/tikz/s062_pogresna_pretpostavka.tex)
- [s062_razliciti_integratorski_odzivi.tex](../../slike/tikz/s062_razliciti_integratorski_odzivi.tex)
- [s063_odziv_1.tex](../../slike/tikz/s063_odziv_1.tex)
- [s063_odziv_2.tex](../../slike/tikz/s063_odziv_2.tex)
- [s063_odziv_3.tex](../../slike/tikz/s063_odziv_3.tex)
- [s063_pobuda.tex](../../slike/tikz/s063_pobuda.tex)
- [s064_pobuda.tex](../../slike/tikz/s064_pobuda.tex)
- [s064_rl_kolo.tex](../../slike/tikz/s064_rl_kolo.tex)
- [s067_kompenzacija_odzivi.tex](../../slike/tikz/s067_kompenzacija_odzivi.tex)
- [s067_razdelnik.tex](../../slike/tikz/s067_razdelnik.tex)
