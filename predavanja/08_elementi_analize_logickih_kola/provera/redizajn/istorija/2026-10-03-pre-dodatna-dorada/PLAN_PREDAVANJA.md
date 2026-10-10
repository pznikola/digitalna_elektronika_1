# PLAN_PREDAVANJA.md — uputstvo za unapređenje prezentacija

**Kontrolna tačka 08, 2026-10-03:** korisnik je izričito odobrio obradu 08. Svih 67 originalnih, početnih i novih slajdova i A4 beležaka pojedinačno je pregledano; raspored i nastavni tekst beležaka obrađeni su po planu. Svih 231 elemenata ima provereno odredište. Kompilacija i računske provere prolaze; 12 grupa izvornih stručnih pitanja ostaje otvoreno, pa `check` vraća `NEZAVRŠENO` u 26 kategorija na 19 ID-jeva. Status je `u_radu`; vidi [izveštaj 08](predavanja/08_elementi_analize_logickih_kola/provera/redizajn/izvestaj.md) i [predloge P01–P12](predavanja/08_elementi_analize_logickih_kola/provera/redizajn/otvorena_pitanja.md). Rezultat 08 i početak 09_1 nisu odobreni.

**Kontrolna tačka 07, 2026-10-03:** početak 07 je izričito odobren korisnikovim nalogom. Svih 31 originalnih, početnih i novih slajdova i A4 beležaka pojedinačno je pregledano; izgled i nastavni tekst beležaka obrađeni su po planu. Svih 138 elemenata ima provereno odredište. Kompilacija i računske provere prolaze; šest grupa izvornih stručnih pitanja ostaje otvoreno, zbog čega `check` vraća `NEZAVRŠENO` u sedam kategorija. Status je `u_radu`; vidi [izveštaj 07](predavanja/07_uvod_u_hdl/provera/redizajn/izvestaj.md) i [predloge za odluku](predavanja/07_uvod_u_hdl/provera/redizajn/otvorena_pitanja.md). Početak 08 je naknadno izričito odobren nalogom od 2026-10-03; rezultat i stručne ispravke 07 time nisu prihvaćeni.

## 1. Namena i obavezna pravila

Ovo je uputstvo za agenta koji unapređuje postojeće LaTeX prezentacije iz foldera `predavanja/`. Cilj su akademske, profesionalne i čitljive prezentacije, sa kvalitetno nacrtanim šemama, jedinstvenim vizuelnim identitetom i beleškama koje sadrže **isključivo dodatni nastavni sadržaj za predavača**. Publika prezentacija su studenti predmeta Digitalna elektronika 1; beleške služe predavaču da zna šta treba dodatno da objasni uz odgovarajući slajd.

**Izrada ovog dokumenta nije početak redizajna.** Pri prvom pisanju galerija, template, beleške, novi alati i evidencija bili su budući zadaci. Njihovo aktuelno postojanje i status proveri u kontrolnoj tački ispod i centralnoj evidenciji.

**Kontrolna tačka 2026-10-02:** galerija 0.3 je izrađena; korisnik je izabrao **B** uz prihvaćene kompaktne analogne šeme. Pripremljena je samostalna tema [etf-v1](predavanja/_zajednicko/etf-v1/README.md) i implementirana [infrastruktura beležaka i provera redizajna](predavanja/_alati/REDIZAJN.md). Predavanje 01 je odobreno porukom „I approve 01“. Obrada 02 i ponovna dorada 03 prema odobrenoj 01 su završene; njihovi rezultati zasebno čekaju korisnikovo odobrenje. Korisnik je izričito odobrio početak 02, 03 i 04; raspored 04, beleške i pojedinačni pregled su završeni po njegovom nalogu od 2026-10-02. Korisnik je odobrio ispravke s006, s016 i naziva s034, a zatim jednačina s034/s035 i uslova s009; sve su primenjene i pregledane. Predavanje 04 ima status `ceka_odobrenje`: sve provere prolaze i nema otvorenih stručnih pitanja; vidi [izveštaj 04](predavanja/04_brojni_sistemi/provera/redizajn/izvestaj.md). Korisnik je 2026-10-02 izričito odobrio obradu slajdova i beležaka 05; izgled i beleške obrađeni su za svih 55 ID-jeva, a šest grupa izvornih stručnih pitanja čeka njegovu odluku. Status 05 ostaje `u_radu`; vidi [izveštaj 05](predavanja/05_aritmeticke_operacije/provera/redizajn/izvestaj.md) i [otvorena pitanja](predavanja/05_aritmeticke_operacije/provera/redizajn/otvorena_pitanja.md). Aktuelne odluke i otiske vodi [STATUS_PREDAVANJA.md](STATUS_PREDAVANJA.md); izbor B se ne traži ponovo.

**Kontrolna tačka 06, 2026-10-02:** korisnik je izričito odobrio obradu slajdova i beležaka 06. Svih 30 originalnih, početnih i novih slajdova i njihovih beležaka pregledano je; redizajn i nastavni tekst beležaka obrađeni su po ovom planu. Svih 127 elemenata ima provereno odredište. Kompilacija i računske provere prolaze; osam grupa izvornih stručnih pitanja ostaje otvoreno i `check` zato vraća `NEZAVRŠENO`. Status 06 je `u_radu`; vidi [izveštaj 06](predavanja/06_kodovi/provera/redizajn/izvestaj.md) i [predloge za odluku](predavanja/06_kodovi/provera/redizajn/otvorena_pitanja.md). Nalog za 06 ne odobrava rezultat 05 ni njegove stručne ispravke. Početak 07 je naknadno izričito odobren korisnikovim nalogom; rezultat i stručne ispravke 06 time nisu prihvaćeni.

**Izmena pravila beležaka 2026-10-02:** korisnik je odobrio plan „Izmena plana: beleške kao pomoć predavaču“. Ovaj korak menja samo uputstvo; prepravka postojećih beležaka je zaseban zadatak, predavanje po predavanje. Postojeći izveštaji i potvrde beležaka odnose se na prethodna pravila i ne dokazuju usklađenost sa novim pravilima. Odobrenje 01 ostaje vezano za tada pregledanu verziju; ova izmena ne pokreće automatsku doradu 01 niti menja statuse isporučenih predavanja.

### 1.1. Šta mora ostati očuvano

- Sačuvaj **tačan broj, redosled i stabilne oznake svih 620 slajdova u 12 prezentacija**. Jedan originalni slajd odgovara jednom Beamer okviru i jednoj strani prezentacionog PDF-a.
- Ne briši, ne spajaj i ne deli slajdove. Ne dodaj naslovne slajdove, razdelnike, automatske sadržaje ili dodatne overlay strane. Sačuvaj i ponovljene slajdove koji postepeno razvijaju objašnjenje.
- Pokrij sve logičke celine i sadržajne elemente originala: definicije, uslove, formule, primere, izvođenja, tabele, kod, dijagrame i napomene.
- Dozvoljeni su bolji raspored, jasnije formulacije uz očuvanje značenja, kvalitetnije šeme i premeštanje detaljnih objašnjenja u beleške **istog slajda**. Sadržaj ne seli na drugi slajd.
- Na projektovane slajdove i u beleške ne stavljaj uredničke komentare o originalu, procesu redizajna, ispravci ili otvorenom pitanju. Takvu evidenciju vodi u mapi pokrivenosti, izveštaju i odlukama u `provera/redizajn/`. Na slajdu ostaje nastavni sadržaj izvornog PDF-a ili korisnikom izričito odobrena stručna ispravka; beleške sadrže samo nastavno objašnjenje prema koraku 6.
- Ključne definicije, rezultati, uslovi važenja i nastavne ilustracije ostaju vidljivi. Cela logička celina ne sme postojati samo u beleškama. Primer, tabela, formula ili šema ne smeju nestati pod izgovorom rasterećenja.
- Duža obrazloženja i međukoraci mogu u beleške, uz vidljiv tok argumenta i rezultat na slajdu. Prenesi sve uklonjene nastavne detalje potpuno, uz jezičke i odobrene stručne ispravke. U mapi pokrivenosti navedi tačno šta je premešteno; zapis u tehničkoj evidenciji nije zamena za nastavni sadržaj u beleškama istog slajda.
- Očigledne slovne i gramatičke greške ispravi uz evidenciju. Promene formula, vrednosti, topologije kola, stručnih tvrdnji ili uslova zahtevaju korisnikovo izričito odobrenje. Grešku nastalu tvojim radom ispravi odmah.
- Originalne PDF-ove ne menjaj, ne premeštaj i ne prepisuj novim PDF-ovima. Postojeće izmene korisnika, materijal u `vezbe/` i `lab/` ne diraj.

Ako čitljivost, vidljivost ključnog sadržaja i isti broj slajdova ne mogu da se usklade, dokumentuj konkretan slajd i problem. Ne rešavaj ga prećutnim izostavljanjem sadržaja ili nedozvoljenim smanjivanjem fonta.

### 1.2. Odnos prema prethodnoj rekonstrukciji

[PREDAVANJA.md](PREDAVANJA.md) opisuje prethodnu rekonstrukciju. Za novu fazu ovaj dokument zamenjuje njegova suprotstavljena pravila: dozvoljava preformulisanje uz očuvanje značenja, beleške, evidentirane jezičke ispravke i ETF identitet. Pravila o očuvanju originala, broja, redosleda i sadržaja ostaju na snazi.

[Postojeći izveštaj](predavanja/IZVESTAJ.md), README dokumenti i ranije potvrde „završeno“ odnose se na **rekonstrukciju**, ne na ovaj redizajn. Koristi ih kao polazne podatke, ali njima ne potvrđuj kvalitet novih prikaza. Ne prepisuj istorijske izveštaje novim značenjem.

## 2. Polazno stanje i redosled predavanja

Katalog pri pisanju plana obuhvata 314 originalnih PDF strana i 620 slajdova. Putanje u tabeli su relativne u odnosu na `predavanja/`.

| ID | Originalni PDF | Folder LaTeX prezentacije | PDF strane originala | Slajdovi |
|---|---|---|---:|---:|
| 01 | `01 Logicke funkcije.pdf` | `01_logicke_funkcije` | 19 | 37 |
| 02 | `02 Sinteza kombinacionih mreza.pdf` | `02_sinteza_kombinacionih_mreza` | 27 | 54 |
| 03 | `03 Kola srednjeg stepena integracije.pdf` | `03_kola_srednjeg_stepena_integracije` | 11 | 21 |
| 04 | `04 Brojni sistemi.pdf` | `04_brojni_sistemi` | 20 | 39 |
| 05 | `05 Aritmeticke operacije.pdf` | `05_aritmeticke_operacije` | 28 | 55 |
| 06 | `06 Kodovi.pdf` | `06_kodovi` | 15 | 30 |
| 07 | `07 Uvod u HDL.pdf` | `07_uvod_u_hdl` | 16 | 31 |
| 08 | `08 Elementi analize logickih kola.pdf` | `08_elementi_analize_logickih_kola` | 34 | 67 |
| 09_1 | `09 1 MOS logicka kola.pdf` | `09_1_mos_logicka_kola` | 29 | 57 |
| 09_2 | `09 2 MOS logicka kola.pdf` | `09_2_mos_logicka_kola` | 31 | 62 |
| 09_3 | `09 3 MOS logicka kola.pdf` | `09_3_mos_logicka_kola` | 36 | 71 |
| 10 | `10 Logička kola sa bipolarnim tranzistorima.pdf` | `10_logicka_kola_sa_bipolarnim_tranzistorima` | 48 | 96 |
| **Ukupno** | | | **314** | **620** |

**Obavezni redosled: 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09_1 → 09_2 → 09_3 → 10.** Tri MOS dela obrađuju se i odobravaju zasebno.

Početni pregled naziva, broja slajdova i zajedničke infrastrukture sme obuhvatiti ceo katalog. Detaljna analiza gradiva, redizajn i potvrđivanje slajdova obuhvataju samo trenutno odobreno predavanje. Ne obrađuj sledeće predavanje u pozadini, preko drugog agenta ili dok čekaš odgovor korisnika.

### 2.1. Postojeća organizacija

- Glavni izvor je `<folder>/<folder>.tex`, sa eksplicitnim uključivanjem slajdova iz `slajdovi/`.
- Crteži su u `slike/tikz/`, tabele u `tabele/`, kod u `kodovi/`, a podaci i izvorne ilustracije u pripadajućim folderima.
- `provera/mapa.json` čuva izvorne lokacije, ID-jeve, inventar i očekivane izlazne strane. `provera/pregled.json` čuva ranije potvrde prikaza.
- `provera/uocene_greske.md` sadrži ranije uočene greške originala. Pročitaj ga pre uređivanja aktivnog predavanja.
- Zajednički stilovi su u `predavanja/_zajednicko/`, a alati u `predavanja/_alati/`.
- Generisani PDF-ovi, slike i HTML pregledi pripadaju folderima `build/`, izuzetim iz Git-a. Izvori i evidencija ostaju van njih.

### 2.2. Organizacija fajlova nove faze

Zajednička galerija, tema i alati već postoje. Fajlove pojedinačnog predavanja iz sledeće organizacije uvodi tek pri njegovom odobrenom početku; spisak nije tvrdnja da je predavanje već obrađeno:

```text
STATUS_PREDAVANJA.md                     # centralna evidencija u korenu
predavanja/_zajednicko/galerija/          # izvori demonstracionih stilova
predavanja/_zajednicko/etf-v1/            # usvojena, verzionisana tema
    stil.sty
    dijagrami.sty
    resursi/                            # zvanični grafički resursi
    README.md                           # specifikacija, poreklo i odluka
predavanja/<folder>/
    beleske/sNNN.tex                     # jedan izvor beležaka po slajdu
    <folder>_beleske.tex                 # dokument za čitanje beležaka
    provera/redizajn/
        manifest.json                   # verzija teme i otisci zavisnosti
        inventar.json                   # nezavisan sadržajni popis redizajna
        pokrivenost.json                 # uređiva mapa odredišta elemenata
        pokrivenost.md                   # generisana čitljiva tabela mape
        izgradnja.json                   # stvarni ulazi/izlazi i verzije alata
        pregled.json                    # nove potvrde po slajdu
        izvestaj.md                     # tekući i završni izveštaj
        odluke.md                       # stvarna korisnikova odobrenja
    build/
        <folder>.pdf
        <folder>_beleske.pdf
        redizajn/pre/                    # početni prikaz, pre izmena
        redizajn/pregled/index.html      # uporedni pregled sa beleškama
```

Sačuvaj postojeće nazive i ID-jeve slajdova. Novi izvori beležaka koriste isti numerički deo; njihovo povezivanje sa punim ID-jem, npr. `01-s003`, mora biti eksplicitno proverljivo. Sačuvaj `\BeleskeID{...}` i nevidljiva sidra `% element: …` u izvorima beležaka. Ne prepisuj istorijske potvrde iz `provera/pregled.json` potvrdama redizajna.

## 3. Prva faza: galerija stilova i izbor korisnika

Pre redizajna predavanja 01 pripremi samostalnu galeriju. Ona služi izboru vizuelnog stila i ne ulazi u 620 nastavnih slajdova.

| Stil | Karakteristike |
|---|---|
| **A — Udžbenički** | Crno-bele šeme, precizni standardni simboli, jasna geometrija, bez dekorativnog senčenja. Pogodan i za štampu. |
| **B — Akademski sa akcentima** | Tamne šeme na beloj pozadini, diskretna boja za odabrane signale i funkcionalne grupe. Preporučena polazna varijanta. |
| **C — Objašnjavajući** | Ista preciznost, uz dodatne oznake, strelice i obojene putanje signala ili struje koje objašnjavaju konkretno stanje kola. |

U svakom stilu nacrtaj **iste** primere: malu mrežu logičkih kola sa grananjem i negacijom, CMOS invertor, BJT invertorski stepen i vremenski dijagram sa označenim kašnjenjem. Dodaj tekstualni slajd pre i posle rasterećenja i njegove beleške. Primeri su samostalni demonstracioni materijal; ne zahtevaju analizu predavanja 02–10.

Za poređenje zadrži iste funkcije, topologiju, oznake, veličinu slajda i približno istu površinu crteža. Pored prikaza u punoj veličini pripremi pregled A/B/C, uključujući crno-beli prikaz. Navedi kratke prednosti i ograničenja stilova i sačuvaj uređive izvore.

**Predaj galeriju i sačekaj korisnikov izbor.** Preporuka B nije odobrenje. Zabeleži izabrani stil, eventualne tražene izmene i stvarnu korisnikovu poruku u centralnoj evidenciji i README-u teme. Ako korisnik traži doradu galerije, doradi je pre primene. Nakon izbora usaglasi temu sa galerijom i pređi na 01 samo ako je njegov početak već odobren.

## 4. Profesionalni template i pravila crtanja

**Dopuna prema korisnikovoj odluci od 2026-09-25:** električne šeme sa tranzistorima, otpornicima, kondenzatorima i drugim analognim komponentama crtaju se prema [PRAVILA_ANALOGNIH_SEMA.md](PRAVILA_ANALOGNIH_SEMA.md), po uzoru na Razavija. To obuhvata i CMOS/BJT realizacije digitalnih kola. Fontovi ostaju postojeći; stilovi logičkih kapija i vremenskih dijagrama iz galerije ostaju očuvani. Posebna pravila analognih simbola i crnih vodova imaju prednost nad opštim galerijskim akcentima za taj tip šeme. Sekvencijalni rad, stručna vernost i odobrenja predavanja ostaju obavezni.

### 4.1. Vizuelni identitet ETF-a

Izvor je [zvanična stranica vizuelnog identiteta ETF-a](https://www.etf.bg.ac.rs/sr/fakultet/vizuelni-identitet). Pri pripremi galerije proveri dostupne zvanične resurse i eventualno objavljena detaljna pravila. Zabeleži URL, datum preuzimanja, naziv originalnog fajla i SHA-256 lokalnog resursa.

- Razlikuj **znak** (grafički akronim ETF), **logotip** (ispis imena institucije) i **zaštitni znak** (njihovu kombinaciju). Zvanična stranica dopušta samostalnu upotrebu znaka, a zabranjuje samostalnu upotrebu logotipa.
- Koristi zvanične fajlove, njihove proporcije i dozvoljene varijante. Ne precrtavaj znak, ne izmišljaj kombinacije i ne koristi pečat kao dekoraciju.
- Prednost daj zvaničnom vektorskom resursu; po potrebi ga tehnički konvertuj u PDF uz očuvanje izgleda. Ako je dostupan samo PNG, proveri kvalitet na konačnoj veličini. Ne predstavljaj automatski precrtanu sliku kao zvanični vektor.
- Ne navodi neproverene vrednosti boja ili izabrani font kao zvaničan ETF standard. Stranica proverena pri pripremi ovog plana nije navodila preciznu paletu ni fontove. Razdvoji potvrđena pravila identiteta od naših odluka za nastavni template.
- Na postojećem naslovnom slajdu koristi odgovarajući zvanični resurs, a na sadržajnim slajdovima diskretan znak u podnožju. Obezbedi razmak od sadržaja; bez vodenih žigova preko šema.
- Sačuvaj istinito poreklo i autorstvo. Originali nose podatke „Digitalna elektronika 1 — 2021/22“, „Katedra za elektroniku“ i „prof dr Lazar Saranovac“. Ne proglašavaj agenta autorom izvornog materijala i ne menjaj školsku godinu prema datumu obrade. Datum redizajna vodi odvojeno.

Ako potrebni zvanični resursi nisu dostupni, dokumentuj nedostatak u galeriji i zatraži odgovarajući resurs ili korisnikovu odluku; ne izmišljaj identitet.

### 4.2. Tipografija i raspored

Zadrži Beamer 16:9 i LuaLaTeX sa `latexmk`. Koristi belu pozadinu, taman tekst, ujednačene margine i ograničenu paletu iz odobrene galerije. Početne margine su 7 mm levo i desno, kao u postojećem stilu.

Početna tipografija je Latin Modern Sans za tekst, Latin Modern Mono za kod i dosledna postojeća matematička tipografija. Veličine: naslovi 16–18 pt, osnovni tekst 11–12 pt, oznake šema, tabela i koda najmanje 9 pt **u konačnom prikazu**. Diskretno podnožje može biti 8 pt. Skaliranje crteža ne sme oboriti oznake ispod minimuma.

U zajedničkom stilu definiši rasporede za tekst i ilustraciju, poređenje dve realizacije, dominantnu šemu, tabelu i izvođenje. Naslov treba da govori o sadržaju; slajdu bez naslova možeš dodati kratak opisni naslov unutar postojećeg okvira. Ne dodaj novi slajd zbog naslova.

Koristi jasnu hijerarhiju teksta, kratke pasuse ili sažete stavke, pregledne blokove formula i dosledne razmake. Izbegavaj duge pasuse velikim slovima, duboko ugnježdene liste, dekorativne okvire, senke, gradijente i nepotrebne navigacione elemente.

Za prepunjen slajd prvo popravi raspored, geometriju crteža i ponavljanje teksta, zatim prebaci detaljna objašnjenja u beleške. Ne koristi `shrink`, smanjivanje celog slajda, `allowframebreaks`, `\pause` ili overlay naredbe koje povećavaju broj izlaznih strana.

### 4.3. Izbor alata i stručna vernost

| Sadržaj | Izvor za uređivanje | Obavezna provera |
|---|---|---|
| Logička kola | TikZ, postojeća biblioteka `circuits.logic.US` | Vrsta kola, svi ulazi, negacije, aktivni nivoi i veze |
| MOS/BJT i ostale električne šeme | CircuitikZ, uz dokumentovane TikZ dopune | Tip komponente, priključci, strelice, napajanja, vrednosti i topologija |
| Blok dijagrami | TikZ | Smer signala, grananje, povratne sprege i nazivi |
| Vremenski dijagrami | TikZ ili `tikz-timing` | Nivoi, događaji, kašnjenja, impulsi i vremenske oznake |
| Karakteristike | PGFPlots i TikZ | Ose, skale, jedinice, oblasti i karakteristične tačke |
| Karnoove karte | Postojeći `karnaugh-map` i TikZ | Grejov raspored, vrednosti i sve grupe, uključujući ivice |
| Tabele, formule i kod | Izvorni LaTeX, tekstualni izvori koda | Svaka ćelija, simbol, indeks, negacija i uslov |

Referentna dokumentacija: [Beamer](https://ctan.org/pkg/beamer), [PGF/TikZ](https://ctan.org/pkg/pgf), [CircuitikZ](https://ctan.org/pkg/circuitikz), [PGFPlots](https://ctan.org/pkg/pgfplots). Koristi mogućnosti dostupne u instaliranim verzijama; ne uvodi nadogradnje bez potrebe.

Ne koristi generisane rasterske slike ili snimak originalnog slajda kao zamenu za nastavnu šemu. Zadrži fotografije i snimke interfejsa kada su sami predmet objašnjenja. Ne izmišljaj numeričke podatke za kvalitativne krive.

### 4.4. Pravila profesionalnog crteža

- Gradi crtež na doslednoj mreži poravnanja. Tok signala prvenstveno vodi sleva nadesno, a napajanja i tranzistorske grane rasporedi pregledno po vertikali.
- Definiši dimenzije simbola, dužine izvoda, veličine strelica i razmake kroz zajedničke stilove. Početna debljina glavnih linija je 0,7–0,9 pt; naglašene putanje mogu biti deblje, bez zaklanjanja spojeva.
- Veze vodi pregledno, pretežno ortogonalno. Nijedan vod ne sme da prelazi preko tela logičkog kola ili da zakloni njegov negacioni kružić. Zaobiđi simbol i smanji nepotrebna ukrštanja.
- Svako stvarno grananje vodova i spoj na zajedničkoj sabirnici označi punom tačkom. Na običnom uglu i na ukrštanju bez električne veze ne stavljaj tačku; takva ukrštanja učini nedvosmislenim razmakom ili drugačijim vođenjem vodova.
- Oznake ulaza, izlaza, čvorova, komponenti, vrednosti i jedinica ne smeju prekrivati linije ili simbole. Sačuvaj originalne nazive i smisao oznaka.
- Za MOS proveri gejt, sors, drejn, bulk kada je prikazan, tip kanala i negacije; za BJT bazu, kolektor, emiter, tip i strelicu. Ne uvodi prećutnu električnu ekvivalenciju kao zamenu za originalnu topologiju.
- Kod logičkih simbola zadrži postojeću konvenciju; posebne varijante prikazane radi nastave ostaju posebne. Galerija menja stil, ne značenje simbola.
- Koristi boju za konkretno objašnjenje, uz natpis, stil linije ili drugi znak. Značenje mora ostati razumljivo u crno-belom prikazu; ne oslanjaj se samo na razliku crveno/zeleno.
- Za isticanje izabrane kolone/vrednosti u tabeli, logičke operacije, jednačine ili ključnog simbola koristi **tamno crvenu `#A32638`** i po potrebi podebljanje ili veoma svetlu crvenu podlogu. Ne koristi plavu za isti tip isticanja: u prikazu se premalo razlikuje od tamnog teksta. Ovo je odluka za nastavne prezentacije, a ne zvanična ETF boja. U već postojećoj temi `etf-v1` boja `DEcrvena` je plava; ne menjaj odobrene prezentacije tihom izmenom teme, već primeni lokalnu definiciju ili napravi novu verziju teme i evidentiraj njenu upotrebu.
- Dodatna strelica struje ili označena provodna grana mora imati naveden uslov/stanje kola. Detaljnost znači potpunost i jasnu vezu sa objašnjenjem, ne više ukrasa.

### 4.5. Verzije i izolacija teme

Usvojeni template objavi u `_zajednicko/etf-v1/`, sa dokumentovanim fontovima, bojama, geometrijom, logotipskim resursima i stilovima dijagrama. Aktivno predavanje eksplicitno uključuje tu verziju i beleži njen otisak u manifestu.

Ne menjaj stare zajedničke stilove tako da sva predavanja automatski dobiju novi izgled. Ne prebacuj glavne izvore budućih predavanja na novu temu unapred. Dok 01 još nije odobreno, tema može da se dorađuje, ali izmena poništava pogođene preglede.

Verziju koju koristi odobreno predavanje smatraj zamrznutom. Za kasniju promenu napravi sledeću verziju; već odobrena predavanja ostaju na svojoj verziji dok korisnik ne odobri njihovo ponovno otvaranje. Nova verzija mora zadržati usvojeni vizuelni identitet; značajnu promenu stila ponovo pokaži korisniku.

## 5. Ciklus rada za trenutno predavanje

### Korak 1 — Učitaj stanje i proveri odobrenje

Pročitaj ovaj dokument, `STATUS_PREDAVANJA.md`, izveštaj i odluke aktivnog predavanja. Proveri korisnikov nalog i kontrolne sume relevantnih izvora. Poštuj već data odobrenja; ne traži ih ponovo ako su jasna i važe za istu verziju rada.

Ako centralna evidencija još ne postoji, napravi je prema odeljku 8: svih 12 predavanja počinju sa `nije_zapoceto`, a galerija sa statusom da izbor još nije donet. Ne prenosi oznaku „završeno“ iz rekonstrukcije. Odobrenje za pisanje ovog plana samo po sebi nije odobrenje za redizajn.

Zabeleži aktivno predavanje, fazu, poslednji provereni slajd i sledeći korak. Kada nastavljaš prekinut rad, sačuvaj važeće rezultate i proveri samo ono što nedostaje ili je promenjeno.

### Korak 2 — Pregledaj originalni PDF

Proveri SHA-256 originala prema postojećoj mapi. Pregledaj sve strane kao slike i izdvojene slajdove prema `pdf_page`, `position` i `bbox_pt` iz `provera/mapa.json`. Redosled je gornji pa donji slajd; prazna donja polovina poslednje strane nije dodatni slajd.

Tekst izvuci kao pomoć za pretragu, ali pregledaj svaku formulu, sliku i sitnu napomenu na uvećanom originalu. Posebno, kada odgovarajuće predavanje dođe na red, proveri poznate slučajeve: HDL slajd 23 ima kod dostupan kao slika; u 09_2 slajd 54 nema deo uobičajenog podnožja; u 10 slajdovi 94–96 sadrže kataloške tabele kao slike. Nijedan od njih nije prazan.

Za svaki slajd napravi sadržajni popis nezavisan od trenutnog LaTeX-a. Nečitljivo mesto evidentiraj sa lokacijom; ne nagađaj.

### Korak 3 — Pregledaj postojeći LaTeX i sačuvaj početni prikaz

Pregledaj glavni `.tex`, pojedinačne slajdove, izvore crteža i tabela, kod, lokalne stilove i postojeće izveštaje. Kompajliraj samo aktivno predavanje i otvori ceo PDF.

Pre izmena sačuvaj početni PDF i slike u `build/redizajn/pre/`. U manifestu zabeleži otiske polaznih izvora i resursa, komandu izgradnje i verzije alata. Kada izvori nisu verzionisani u Git-u, sačuvaj i njihovu početnu kopiju među lokalnim artefaktima; ne pretpostavljaj da ih Git može vratiti. Sačuvaj i zavisnosti potrebne za reprodukciju početnog izgleda.

Za svaki slajd zapiši probleme: gust tekst, nečitljiva oznaka, nedovoljno jasna šema, loše poravnanje, nedosledan simbol, neodgovarajuća hijerarhija ili sadržinski nesklad. Raniji izveštaj pomaže, ali ne zamenjuje pregled.

### Korak 4 — Napravi mapu pokrivenosti

U `provera/redizajn/pokrivenost.md` vodi najmanje sledeću tabelu. Jedan red predstavlja proverljiv sadržajni element, ne samo ceo slajd.

Implementirani alati generišu ovu tabelu iz ručno održavanih `inventar.json` i `pokrivenost.json`; struktura, odredišta i način potvrđivanja opisani su u [uputstvu](predavanja/_alati/REDIZAJN.md). Ne održavaj dve različite kopije iste mape.

| Element / slajd | Lokacija u originalu | Sadržaj | Odredište na slajdu | Odredište u beleškama | Promena i provera |
|---|---|---|---|---|---|
| `<ID>:<element>` | PDF strana, gornji/donji, deo slajda | Definicija, formula, primer, tabela, šema, kod ili napomena | Putanja i prepoznatljiv blok | Putanja i sidro bloka, ili „nije potrebno“ | Očuvano / preformulisano / premešteno / odobrena ispravka; status |

Svaki element originala mora imati odredište i proveru. Proveri i nastavni sadržaj postojećeg LaTeX-a koji nije u originalu: evidentiraj ga kao postojeću dopunu i sačuvaj, osim ako korisnik odobri njegovu izmenu. Poreklo prenetog sadržaja, razliku između izvornog objašnjenja i dopune, dokaze, ispravke i odluke vodi u postojećoj evidenciji `provera/redizajn/`, povezano sa ID-jem i sidrom odgovarajućeg bloka. Dodata objašnjenja označi kao dopune u toj evidenciji, bez vidljivih oznaka porekla u beleškama. Ne uvodi drugu kopiju teksta beležaka.

Ne koristi automatsko poklapanje teksta kao dokaz pokrivenosti. Sažimanje nije dozvola da nestanu pretpostavke, broj, jedinica, uslov ili izuzetak. Suštinske tabele, kod i šeme proveri zasebno, element po element.

### Korak 5 — Redizajniraj u grupama od 5–10 slajdova

Primeni odobreni template i popravi raspored, tekst, tabele i crteže. Svaki novi crtež uporedi sa originalom i polaznim LaTeX prikazom. Proveri i konačnu veličinu oznaka posle skaliranja.

Posle svake grupe kompajliraj, pregledaj sve izmenjene slajdove i ažuriraj mapu i beleške. Otkloni greške pre sledeće grupe. Ne označavaj ostatak predavanja pregledanim na osnovu uzorka.

Jezičke ispravke evidentiraj sa originalnim i novim zapisom u `provera/redizajn/`. Stručnu sumnju zabeleži tamo uz dokaz, predlog i pogođene slajdove; zatraži odluku bez menjanja spornog stručnog sadržaja na slajdu ili u beleškama. Otvorene predloge i zahteve za odobrenje ne unosi u beleške. Dok čekaš, možeš raditi nezavisne delove istog predavanja. Ne možeš ga proglasiti spremnim dok relevantan problem nema rešenu odluku.

### Korak 6 — Napiši i poveži beleške

Napravi `beleske/sNNN.tex` za svaki slajd, sa vezom na njegov stabilni ID. Beleške sadrže **samo nastavni sadržaj koji predavač treba dodatno da objasni uz taj slajd**. Piši ih kao smislen tekst koji predavač može pročitati i upotrebiti tokom izlaganja; formule i kratke stavke koristi kada olakšavaju objašnjenje.

Postupak pisanja:

1. Uporedi originalni i uređeni slajd i utvrdi koji nastavni detalji više nisu vidljivi na slajdu.
2. Prenesi sve te detalje u beleške istog slajda i objasni ih potpuno, uz jezičke i odobrene stručne ispravke. Ne zamenjuj ih kratkim rezimeom.
3. Dodaj samo potrebne, proverljive dopune: međukorake izvođenja, tumačenje oznaka i rada kola, uslove važenja, kratke primere i razjašnjenja tipičnih studentskih zabuna. Ne dodaj nepotvrđene stručne tvrdnje.
4. Proveri da beleške objašnjavaju ono što predavač treba dodatno da kaže. Sadržaj već jasno prikazan na slajdu ne prepisuj bez potrebe; kratko podsećanje na formulu ili oznaku dozvoljeno je radi povezivanja objašnjenja.

Ne propisuj dužinu. Ako nema dodatnog nastavnog sadržaja, fajl zadržava vezu sa ID-jem, bez veštačkog popunjavanja ili poruke „nema dodatnih beležaka“. Ključne definicije, rezultati, uslovi i nastavne ilustracije ostaju vidljivi na slajdu prema odeljku 1.1.

**Iz beležaka isključi** istoriju redizajna, poređenja verzija, kontrolne sume, rezultate provera, korisnikove odluke, zahteve za odobrenje, predloge ispravki i komentare o premeštanju sadržaja. Ne koristi uredničke naslove „Objašnjenje iz originala“, „Dopunsko objašnjenje“ ili „Odobrena stručna ispravka“, niti redove „Izvor: PDF strana…“. Po potrebi koristi sadržajne podnaslove, npr. „Kašnjenje kaskade“ ili „Izvođenje izraza“.

Odobrene stručne ispravke predstavi neposredno kao ispravan nastavni sadržaj, bez priče o odobravanju. Ako je korisnik odobrio zadržavanje izvornog zapisa, dozvoljeno razjašnjenje napiši kao stručno objašnjenje. Dokaz, izvorni zapis, odluku i razliku prema originalu sačuvaj u evidenciji iz koraka 4–5. Nerešena stručna pitanja ostaju u toj evidenciji i sprečavaju završnu predaju.

Primer odgovarajuće beleške uz poređenje dve realizacije petoulazne I funkcije:

> U obe realizacije koriste se četiri dvoulazna I kola. Kašnjenje zavisi od broja uzastopnih nivoa na kritičnoj putanji. Uravnoteženo stablo skraćuje tu putanju.

### Korak 7 — Proveri svaki slajd i beleške

Generiši uporedni pregled originala, polaznog LaTeX prikaza, novog slajda i pripadajućih beležaka. Pregledaj sve parove u punoj veličini; pregled u sličicama služi samo za proveru ritma i doslednosti.

Proveri svaku vezu i oznaku u šemi, svaku ćeliju tabele, formulu i kod. Pregledaj i redosled čitanja, slobodan prostor, poravnanje, kontrast i vidljivost na projektorskoj veličini. Tek zatim upiši nove potvrde i otiske tačno pregledane verzije.

Za beleške posebno proveri potpunost prenetih nastavnih detalja, stručnu tačnost, upotrebljivost za predavača, odsustvo nepotrebnog ponavljanja i odsustvo uredničke evidencije. Svaki uklonjeni nastavni detalj mora imati stvarno objašnjenje u beleškama istog slajda, ne samo zapis u izveštaju.

### Korak 8 — Predaj izveštaj i zaustavi prelazak

Kada sve provere prođu, dovrši izveštaj, navedi konkretne izlazne fajlove i postavi `ceka_odobrenje`. Predaj korisniku prezentaciju, PDF beležaka, pregled i izveštaj. PDF beležaka sadrži nastavno objašnjenje; istorija rada, odluke i dokazi ostaju u odvojenoj evidenciji.

**Ne počinji analizu sledećeg predavanja dok korisnik izričito ne odobri prelazak.** Uspešna kompilacija, završen izveštaj, proteklo vreme i preporuka agenta nisu odobrenje. Ako korisnik traži izmene, status je `dorada`, a nakon izmena ponavljaju se pogođene provere i predaja.

## 6. Prateći PDF beležaka

Običan PDF ostaje namenjen projekciji: jedan slajd po strani, bez stranica beležaka. Poseban `<folder>_beleske.pdf` je dokument za predavača, u formatu A4, sa prikazom svakog slajda, njegovim stabilnim ID-jem, naslovom i dodatnim nastavnim objašnjenjem prema koraku 6. Beleške jednog slajda smeju zauzeti više strana; naslov nastavka treba da zadrži ID. Za slajd bez dodatnog objašnjenja prikaži samo slajd, ID i naslov, bez zamenskog teksta.

Koristi jedan izvor teksta beležaka: `beleske/sNNN.tex`. Glavni dokument beležaka uključuje te fajlove istim redosledom kao slajdove i prikazuje odgovarajuću stranu upravo izgrađenog prezentacionog PDF-a. Ne održavaj ručno drugu kopiju beležaka.

Beleške piši pomoću LaTeX naredbi koje rade u dokumentu za čitanje; ne vezuj ih za Beamer overlay naredbe. Ako se naknadno omogući predavački prikaz kroz `\note{...}`, i on mora čitati iste izvore, a običan PDF mora ostati u režimu bez beležaka.

Provera broja slajdova i `slide-map.tsv` odnosi se isključivo na prezentacioni PDF. Za PDF beležaka proveri redosled ID-jeva, kompletne blokove beležaka i ispravne prikaze slajdova, bez zahteva da broj strana bude jednak broju slajdova. Promena beležaka mora poništiti njihovu potvrdu čak i kada se slajd nije vizuelno promenio.

## 7. Izgradnja i dopune postojećih alata

### 7.1. Komande koje već postoje

Pokreći iz korena repozitorijuma, uvek sa punim folderom aktivnog predavanja u `LECTURE`. Primer za 01:

```bash
make -C predavanja LECTURE=01_logicke_funkcije all
make -C predavanja LECTURE=01_logicke_funkcije review
make -C predavanja LECTURE=01_logicke_funkcije check
```

`all` gradi prezentaciju; `review` pravi uporedni pregled; `check` uključuje izgradnju, strukturne provere, dostupnu računsku proveru i provere potvrda. Bez manifesta redizajna to su postojeće provere rekonstrukcije. Sa `phase: redizajn` proveravaju se prezentacija, beleške, mapa pokrivenosti i **nove** potvrde. Nakon promene izgleda stare potvrde rekonstrukcije mogu očekivano biti zastarele i ne zamenjuju nove preglede.

Izbor `LECTURE` sada je obavezan za `all`, `notes`, `review`, `check`, `preview` i `clean`; prazan izbor se odbija i u odgovarajućim Python komandama. `inventory` nije komanda za potvrđivanje novog pregleda. `clean` odbija brisanje sačuvanog početnog prikaza; pre čišćenja je potrebna trajna arhivska kopija.

### 7.2. Implementirane dopune za novu fazu

Alati u `_alati/` i Makefile podržavaju novu fazu uz očuvanu proveru starih prezentacija. [Tehničko uputstvo](predavanja/_alati/REDIZAJN.md) dokumentuje inicijalizaciju posle stvarnog odobrenja, šeme evidencije i rad komandi. Novi režim određuje eksplicitno polje `phase: redizajn` u manifestu aktivnog predavanja. Dok manifest ne postoji, komande zadržavaju ponašanje rekonstrukcije. Samo postojanje manifesta ne potvrđuje završenost.

Stari primeri u tehničkom uputstvu ne propisuju vidljive naslove ili oznake porekla u beleškama. Nova sadržinska pravila ovog plana imaju prednost. Sačuvaj tehničke veze sa ID-jevima i nevidljiva sidra; oznake porekla i evidenciju ispravki vodi izvan prikazanih beležaka. Automatske provere ne dokazuju da je tekst beležaka nastavno upotrebljiv — to potvrdi pregledom iz koraka 7.

Za predavanje u novoj fazi obezbedi:

- `all` gradi projekcioni PDF iz eksplicitno vezane verzije teme; broj, redosled, oznake i originalne lokacije ostaju strogo provereni.
- Cilj `notes` prvo obezbeđuje aktuelan projekcioni PDF, pa gradi prateći PDF beležaka.
- `review` pravi pregled u `build/redizajn/pregled/`, sa originalom, početnim LaTeX prikazom, novim slajdom i beleškama. Nedostajući početni prikaz je vidljiva greška, ne razlog da se novi prikaže kao stari.
- `check` za novu fazu proverava oba PDF-a, pokrivenost slajda i beležaka zajedno i nove potvrde iz `provera/redizajn/`. Ne zahteva da tekst prenet u beleške ostane i na slajdu, ali zahteva njegovu evidentiranu i proverenu lokaciju.
- Nasleđene potvrde ostaju arhiva rekonstrukcije. Novi pregled vodi odvojeno i nikada se automatski ne popunjava statusom `provereno`.

Implementirana komanda za beleške:

```bash
make -C predavanja LECTURE=01_logicke_funkcije notes
```

Manifest obuhvata ID predavanja, fazu, izabrani stil i verziju teme, originalni SHA-256, potpis početnog snapshot-a, niz ID-jeva i vezu sa beleškama. Polje `build_record` upućuje na `provera/redizajn/izgradnja.json`, sa otiscima aktuelnih izvora, izlaznih PDF-ova i stvarno korišćenih zavisnosti, komandom i verzijama alata. U izveštaju i centralnom statusu evidentiraj putanje i SHA-256 oba zapisa.

Istorijski `dependency_digest` ostaje deo rekonstrukcije. Novi režim prati **stvarno korišćene zavisnosti** i eksplicitnu verziju teme, uz LaTeX `.fls` zapis, fontove/verzije alata, uključene crteže, tabele, kod, slike, beleške i mapu. Dodavanje nekorišćene nove teme ne poništava odobrenje prezentacije u režimu redizajna.

Nove potvrde po slajdu čuvaju proveru teksta, formula, tabela, koda, crteža, čitljivosti, pokrivenosti i beležaka, uz datum, opis pregleda i otiske pregledanih prikaza/izvora. Statusi kategorija su `ceka`, `provereno`, `problem`, `nije_primenljivo`; pokrivenost, čitljivost i veza sa beleškama nisu neprimenljive kategorije.

Zadrži rad bez mreže tokom izgradnje i postojeći `-no-shell-escape`. Lokalno sačuvani odobreni grafički resursi ne preuzimaju se iznova pri svakoj kompilaciji.

## 8. Centralna evidencija i nastavak rada

### 8.1. STATUS_PREDAVANJA.md

Centralna evidencija nalazi se u korenu repozitorijuma. Sadrži izbor galerije, aktivno predavanje, sledeću dozvoljenu radnju i tabelu svih 12 predavanja. Za svako navedi status, verziju teme, datum, rezultate provera, putanju izveštaja, manifest i njegov SHA-256, odobrenje rezultata i zasebnu dozvolu za početak sledećeg.

Obrazac reda, koji se popunjava stvarnim podacima:

| ID | Status | Tema | Ažurirano | Provere | Izveštaj | Manifest / SHA-256 | Odobren rezultat | Prelazak na sledeće |
|---|---|---|---|---|---|---|---|---|
| `<ID>` | `nije_zapoceto` | — | `<datum>` | Nisu izvršene | — | — | Nema | Nije odobren |

Statusi imaju precizno značenje:

| Status | Značenje |
|---|---|
| `nije_zapoceto` | Redizajn nije započet; istorijska rekonstrukcija ne menja ovaj status. |
| `u_radu` | Početak je odobren i radi se analiza, uređivanje ili provera. |
| `ceka_odobrenje` | Agent je završio rad, provere prolaze i izveštaj je predat; korisnik još nije odobrio rezultat. |
| `odobreno` | Korisnik je izričito prihvatio pregledanu verziju rezultata. |
| `dorada` | Korisnik je zatražio izmene ili je ranije pregledana verzija promenjena; pogođene potvrde se obnavljaju. |

Uobičajen tok je `nije_zapoceto → u_radu → ceka_odobrenje → odobreno`, uz povratak u `dorada` kada je potrebno. Najviše jedno predavanje aktivno je u obradi. Kada predavanje 01 čeka odobrenje, 02 i sva kasnija ostaju nezapočeta.

Za svako odobrenje sačuvaj korisnikovu poruku ili njen precizan citat, datum, predmet odluke i vezu sa verzijom/manifestom na koji se odnosi. Ne izmišljaj identifikator poruke ako ga nema. Jedna poruka može i prihvatiti predavanje i odobriti sledeće, ali to zabeleži kao dve odluke. Ne pretpostavljaj da svako „u redu“ automatski daje oba odobrenja.

### 8.2. Kontrolna tačka pri prekidu

Pre prekida rada ažuriraj centralni status i tekući izveštaj: faza, poslednji provereni ID, preostali ID-jevi, otvoreni problemi, komande koje su izvršene, izlazi i naredni korak. Ne koristi samo podatak „odrađeno 20 slajdova“ bez identifikatora i dokaza provere.

Novi agent najpre proverava status i relevantne otiske. Za odobreno i nepromenjeno predavanje čita samo evidenciju potrebnu za nastavak; **ne ponavlja kompletnu analizu**. Predavanje koje čeka odluku ne proglašava odobrenim i ne koristi kao dozvolu za sledeće.

Promena lokalnog slajda ili njegovih beležaka poništava pogođene potvrde; promena korišćene teme može pogoditi sve slajdove te prezentacije. Ako obim uticaja nije pouzdano poznat, ponovo proveri celo pogođeno predavanje. Promena nepovezanog fajla ili druge verzije teme ne poništava važeći pregled.

Doradu postojećih beležaka prema novim pravilima radi kao zaseban zadatak za konkretno predavanje. Sačuvaj nastavne detalje, prenesi uredničku evidenciju u `provera/redizajn/`, pregledaj sve pogođene prikaze i obnovi njihove potvrde. Pokreni `notes`, `review` i `check` sa njegovim punim `LECTURE`. Odobreno predavanje ponovo otvori samo po korisnikovom nalogu; izmena ovog plana sama po sebi nije odobrenje dorade.

Kontrolne sume omogućavaju utvrđivanje promene, ali nisu dokaz sadržinske ispravnosti. Nikada ih samo ne zameni novim vrednostima da bi provera prošla. Ako su nestali generisani artefakti, obnovi ih iz zabeleženih izvora i potvrdi da odgovaraju pregledanoj verziji; ako ne odgovaraju, uradi potreban novi pregled.

## 9. Obrazac izveštaja jednog predavanja

Vodi ga u `provera/redizajn/izvestaj.md`, od početka rada do predaje. Zadržavaj sažetu istoriju dorada i odluka. Završni izveštaj mora omogućiti korisniku da proceni rezultat, a sledećem agentu da nastavi bez ponovne analize.

```markdown
# Izveštaj redizajna — <ID i naziv predavanja>

## Status i verzija
- Status, datum i izvršilac pregleda:
- Originalni PDF i SHA-256:
- Stil galerije i verzija teme:
- Manifest i SHA-256 pregledane verzije:
- Očekivano / dobijeno slajdova; potvrda redosleda i ID-jeva:

## Pokrivenost i izmene
- Sve originalne logičke celine i link ka mapi pokrivenosti:
- Glavne promene rasporeda i čitljivosti:
- Precrtane šeme i dijagrami, po ID-jevima:
- Šta je premešteno u beleške, po ID-jevima:
- Poreklo dopunskih objašnjenja, sidra blokova i dokazi stručne provere:
- Reprezentativna poređenja pre/posle:

## Ispravke i otvorena pitanja
- Jezičke ispravke: ID, originalni zapis, novi zapis, razlog:
- Stručni predlozi: dokaz, korisnikova odluka i primenjena promena:
- Preostali problemi i njihov uticaj; ili izričito „nema“:

## Dokazi provere
- Komande, izlazni kodovi i putanje logova:
- Rezultati strukturne i postojeće računske provere:
- Pregled svakog slajda, beležaka i pokrivenosti:
- Potpunost beležaka, upotrebljivost za predavača i odsustvo uredničke evidencije:
- Broj proverenih / ukupan broj slajdova i beležaka:
- Upozorenja i njihovo razrešenje:

## Isporuka i nastavak
- Link ka prezentaciji:
- Link ka PDF-u beležaka:
- Link ka uporednom pregledu:
- Izvori i komande za ponovnu izgradnju:
- Poslednji završen korak i naredna dozvoljena radnja:
- Odobrenje rezultata: čeka se / stvarna korisnikova odluka:
- Prelazak na sledeće: nije odobren / stvarna korisnikova odluka:
```

Ako su PDF i HTML fajlovi u `build/`, navedi da se ne verzionišu i kako se ponovo grade. Ne stavljaj linkove ka nepostojećim izlazima bez jasnog objašnjenja. Pri predaji navedi tačno za koje predavanje i koju verziju korisnik daje odluku.

## 10. Provere i kriterijumi prihvatanja

### 10.1. Automatske provere

Za aktivno predavanje proveri:

- neizmenjen originalni PDF, postojeće sve uključene izvore i resurse;
- očekivani broj slajdova, tačan niz ID-jeva, izvornih lokacija i stvarno poslatih PDF strana;
- odsustvo nedozvoljenog deljenja, duplikata, overlay strana i automatskog smanjivanja;
- kompilaciju oba PDF-a bez grešaka, prekoračenja prostora, nedostajućih znakova i nerešenih referenci;
- vezu svakog slajda sa odgovarajućim izvorom beležaka i redosledom u pratećem PDF-u;
- kompletnu mapu pokrivenosti, bez neodređenih odredišta ili nepotvrđenih elemenata;
- aktuelnost pregleda, izvora, korišćene verzije teme, beležaka i izlaznih artefakata;
- postojeće računske/logičke provere. Posle odobrene stručne ispravke uskladi očekivanja sa dokazom ispravnosti, ne sa željom da test prođe.

Za izmene alata dopuni postojeće testove smislenim slučajevima: izostavljen/dupliran slajd, promenjen redosled, izostavljen sadržaj, ispravno premešten sadržaj u beleške, pogrešan ID beležaka, nedostajući resurs, promenjene samo beleške, zastarela potvrda, promenjena korišćena tema i dodata nekorišćena tema. Proveri i kompatibilnost sa starim režimom rekonstrukcije.

Postojeći testovi alata pokreću se komandom:

```bash
make -C predavanja test
make -C predavanja test-redizajn
```

To su testovi infrastrukture, ne dozvola za sadržinsku obradu drugih predavanja. Ne smanjuj strogoću postojećih provera da bi redizajn prošao; uvedi proveru novog, jasno definisanog značenja pokrivenosti.

### 10.2. Vizuelna i sadržinska provera

Automatske provere ne mogu potvrditi topologiju svakog nacrtanog kola, smisao svakog izvođenja ili čitljivost svih slajdova. Ručno, odnosno stvarnim vizuelnim pregledom agenta, proveri svaki slajd i beleške: formule, ćelije tabela, vodove, spojeve, polaritete, oznake, dijagrame, kod i veze između njih.

Poredi značenje i pokrivenost, ne pikselnu jednakost. Proveri preklapanje, odsecanje, kontrast, veličinu slova, doslednost simbola, sklad rasporeda i razumljivost bez oslanjanja samo na boju. Beleške moraju biti čitljive u svom PDF-u, bez odsečenih pasusa ili nedostajućih matematičkih delova.

Pročitaj beleške uz svaki slajd kao predavač: da li jasno objašnjavaju šta treba dodatno reći, čuvaju sve uklonjene nastavne detalje i sadrže samo proverene dopune? Proveri da nema nepotrebnog prepisivanja slajda, uredničkih naslova, poređenja verzija, izvornih PDF lokacija, istorije ispravki ili korisnikovih odluka. Poreklo i dokaze proveri u odvojenoj evidenciji. Fajl sa samo vezom na ID je prihvatljiv kada nema dodatnog sadržaja; nemoj ga popunjavati radi dužine.

### 10.3. Uslov za predaju korisniku

Predavanje može dobiti `ceka_odobrenje` samo kada su svi originalni sadržajni elementi pokriveni slajdom i pripadajućim beleškama, svi slajdovi i beleške pregledani, provere uspešne, a izveštaj potpun. Beleške moraju zadovoljiti pravila koraka 6: potpuno dodatno nastavno objašnjenje, bez uredničke evidencije i nepotrebnog ponavljanja. Ne sme ostati nerešen sadržinski problem, nečitljiva oznaka, odsečen prikaz ili neprimenjena dogovorena dorada.

Korisnik može izričito odlučiti da se neka stručna primedba reši objašnjenjem u beleškama ili zadržavanjem izvornog zapisa; takvu odluku priloži u `provera/redizajn/` kao razrešenje. U beleškama prikaži samo dozvoljeno stručno objašnjenje, bez opisa korisnikove odluke ili procesa ispravke. Bez odluke sporna tvrdnja ostaje otvoreno pitanje, ne prećutno prihvaćen izuzetak.

**Završeno od strane agenta nije isto što i odobreno od strane korisnika.** Nakon izveštaja i ažuriranja evidencije sledi korisnikov pregled; prelazak na sledeće predavanje dozvoljen je isključivo prema zabeleženom odobrenju.

## 11. Provera i održavanje ovog plana

Pri promeni dokumenta proveri da katalog odgovara stvarnim PDF-ovima, folderima i mapama, da zbir ostaje 620 i da primeri komandi biraju jedno predavanje. Proveri da su budući fajlovi i komande jasno označeni kao budući dok se ne implementiraju.

Proveri da nijedno pravilo istovremeno ne nalaže očuvanje i brisanje istog sadržaja, da beleške ne menjaju broj projekcionih strana i da nova evidencija ne prepisuje istoriju rekonstrukcije. Odluke korisnika unosi tačno i dosledno; ne menjaj zahtev za odobrenjem prelaska na sledeće predavanje bez njegove izričite instrukcije.

Pri izmeni pravila beležaka proveri da nijedno preostalo pravilo ne nalaže prikaz porekla ili uredničke evidencije u beleškama, da svaki uklonjeni nastavni detalj ima provereno odredište u beleškama istog slajda i da su sačuvani odobravanje stručnih ispravki i poništavanje potvrda nakon izmene beležaka. Sama izmena ovog uputstva ne zahteva kompilaciju prezentacija niti promenu alata; provere konkretnih beležaka rade se pri njihovoj zasebnoj doradi prema odeljku 8.2.
