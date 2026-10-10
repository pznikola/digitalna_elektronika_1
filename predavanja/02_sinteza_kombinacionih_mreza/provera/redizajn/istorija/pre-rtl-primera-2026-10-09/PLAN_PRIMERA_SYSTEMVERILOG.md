# PLAN_PRIMERA_SYSTEMVERILOG.md — primeri uz slajdove predavanja

## 1. Cilj i redosled rada

Ovaj dokument propisuje izradu SystemVerilog dizajna i testbench-ova uz slajdove predavanja, prema stilu postojećih primera iz `vezbe/`. Namenjen je agentu koji će izrađivati primere; piše se i održava na srpskom jeziku, latinicom.

**Trenutna faza, 2026-10-09: pripremljeno je uputstvo.** Konkretni primeri izrađuju se tek kada korisnik navede predavanje i slajdove. Dopune alata iz odeljka 4 uvode se pri izradi prvog izabranog primera.

Za svaki odabrani slajd pregledaj originalni PDF, aktuelni slajd, šemu i beleške, pa utvrdi funkciju i realizaciju koju primer treba da pokaže. Koristi stabilni ID slajda, a ne njegov trenutni broj strane u PDF-u.

Posle odabranog slajda dodaj jedan ili više slajdova sa RTL kodom. Korisnik je izričito dozvolio ove dodatke, blago smanjenje fonta, dve kolone i nastavke na više slajdova. Ova dozvola važi za slajdove koje naknadno izabere; pravila o stručnim ispravkama, originalnim PDF-ovima, beleškama i odobravanju iz [PLAN_PREDAVANJA.md](PLAN_PREDAVANJA.md) ostaju na snazi.

## 2. Stil dizajna i testbench-a

Kao uzore koristi primere iz vežbi:

| Tema | Izvor dizajna |
|---|---|
| NI realizacije i međusignali | [01 — dvoulazna NI kola](vezbe/01/code/Zadatak_1/c/zadatak.sv) |
| Multiplekseri i povezivanje modula | [02 — realizacija sa multiplekserom](vezbe/02/code/Zadatak_2/a/zadatak.sv) i [pomoćni multiplekser](vezbe/02/code/Zadatak_2/a/mux4.sv) |
| Dekoderi i aktivni nivoi | [02 — dekoder sa dozvolom rada](vezbe/02/code/Zadatak_3/b/decoder.sv) |
| Komparatori i hijerarhija | [04 — četvorobitni komparator](vezbe/04/code/Samostalni/Zadatak_3/a/zadatak.sv) |
| Sabirači i širine rezultata | [05 — BCD sabirač](vezbe/05/code/BCD_sabirac/zadatak.sv) |
| Koderi i kratki komentari | [05 — Hamingov koder](vezbe/05/code/Haming/koder/zadatak.sv) |

Za automatske provere pogledaj [testbench NI realizacije](vezbe/01/code/Zadatak_1/c/tb_zadatak.sv), [testbench BCD sabirača](vezbe/05/code/BCD_sabirac/tb_zadatak.sv) i [primer provere hazarda](vezbe/01/code/Zadatak_4/c/tb_zadatak.sv). Postojeći izvori iz vežbi služe kao uzor i ostaju očuvani.

**Dizajn:**

- Koristi `.sv`, uvlačenje od četiri razmaka i imenovane veze portova.
- Portovi, međusignali, širine magistrala, redosled bita i aktivni nivoi prate oznake sa slajda. Za komplement koristi dosledan sufiks, uz kratko objašnjenje.
- Piši kratke `//` komentare na srpskom, latinicom, koji objašnjavaju funkcionalnu celinu ili manje očigledan korak.
- Ako slajd prikazuje konkretnu mrežu gejtova, kaskadu ili prenos, opiši tu strukturu odgovarajućim međusignalima i pomoćnim modulima.
- Za jednostavne kombinacione izraze koristi `assign`; za grananje i izbor koristi potpun `always_comb`, bez nenamernih lečeva.
- Eksplicitno vodi računa o širini aritmetičkih rezultata, prenosu i označenim brojevima.
- Kašnjenja dodaj samo kada su predmet slajda. Takav kod označi kao simulacioni model, odvojen od sintetizabilnog RTL-a.
- Neslaganje originala i aktuelnog slajda evidentiraj; stručnu izmenu ne uvodi bez korisnikove odluke.

**Testbench:**

- Instanciraj dizajn imenovanim vezama i koristi iste oznake signala.
- Koristi `timeunit 1ns`, `timeprecision 1ps`, automatske provere, jasan `$fatal`, završnu poruku `PASS` i `$finish`.
- Snimaj VCD, uključujući međusignale.
- Očekivane rezultate izvedi nezavisno iz funkcionalne tabele ili nastavne specifikacije.
- Za male mreže proveri sve dozvoljene binarne kombinacije; za veće dodaj sistematske i granične slučajeve. Vremenske prelaze i X/Z proveravaj kada pripadaju temi.

## 3. Organizacija i prikaz RTL koda

Svaki primer dobija izolovan direktorijum:

`predavanja/<predavanje>/kodovi/primeri_sv/<ID-slajda>/`

U njemu su `zadatak.sv`, `tb_zadatak.sv`, potrebni pomoćni moduli, `Makefile` i kratak `README.md` sa vezom ka slajdu i komandama za simulaciju. Glavni modul je `zadatak`, a testbench `tb_zadatak`, po uzoru na izolovane primere sa vežbi. Nazivi pomoćnih modula opisuju njihovu funkciju; oznake portova i međusignala prate slajd.

- Slajdove koda učitavaj direktno iz izvršivih `.sv` izvora preko `listings`, uz SystemVerilog sintaksno bojenje. Prikaz i simulacija koriste isti izvor.
- Sačuvaj postojeći ETF izgled i monospaced font. Početno koristi 10 pt; po potrebi smanji do 9 pt, bez skaliranja celog slajda.
- Za malo duži kod dozvoljene su dve kolone. Ako ni tada nije pregledan, prikaži nastavke na sledećim slajdovima.
- Podelu pravi između smislenih blokova; redosled čitanja u dve kolone je leva pa desna.
- **Za dve kolone ili više slajdova obavezni su brojevi linija.** Brojevi odgovaraju stvarnim linijama izvornog fajla i nastavljaju se kroz kolone i slajdove. Za različite fajlove prikaži naziv i njihov sopstveni raspon. Pri učitavanju raspona eksplicitno podesi početni broj linije; ne započinji svaki nastavak od 1.
- Ne izostavljaj izvršivi kod radi skraćivanja prikaza. Pomoćne module prikaži na nastavcima kada su deo primera.
- Na svakom slajdu koda navedi kratko: „Testbench: …“, sa jasnom putanjom i linkom ka fajlu. TB se ne prikazuje kao RTL.
- Beleške dodatnih slajdova sadrže samo potrebna nastavna objašnjenja, prema aktuelnom planu predavanja. Ako nema dodatnog objašnjenja, sačuvaj vezu sa ID-jem bez veštačkog popunjavanja.

Kratki nastavni komentari u RTL kodu i tražena napomena o lokaciji TB-a pripadaju prikazu primera. Istoriju rada, rezultate provera, kontrolne sume i odluke korisnika vodi u tehničkoj evidenciji, izvan vidljivog nastavnog sadržaja.

## 4. Povezivanje sa postojećim alatima

Postojeći [simulator iz vežbi](vezbe/PROVERA/simulacija.py) ograničen je na `vezbe/`; trenutno ne podržava primere iz predavanja. Postojeća provera predavanja podržava originalne slajdove i odobrene podele, ali zahteva dopunu za nove slajdove koda. Cilj `check-sv` za predavanja i podrška tim dodacima su **buduće dopune**, a ne već dostupne mogućnosti.

Pri izradi prvog izabranog primera:

- Dodaj pokretanje simulacija za predavanja po uzoru na postojeće Docker simulacije: Verilator i Icarus, zasebni direktorijumi izgradnje i opcioni pregled VCD-a. Sačuvaj postojeće provere i izvore vežbi.
- Uvedi cilj `check-sv` sa obaveznim izborom `LECTURE`, dok svaki primer podržava `run_verilator`, `run_iverilog` i `view_wave`.
- Evidentiraj dodatke zasebno od podela originalnih slajdova. ID-jevi su oblika `03-s020-rtl01`, `03-s020-rtl02`; postojeći ID-jevi ostaju očuvani. Ove oznake ilustruju imenovanje, ne predstavljaju izbor konkretnog slajda.
- Dodaci idu neposredno posle izabranog ID-ja, uključujući slučaj kada je izabran postojeći nastavak poput `s020b`. Njegov dodatak dobija, na primer, ID `03-s020b-rtl01`.
- Uskladi manifest, beleške, pokrivenost, uporedni pregled i očekivani broj izlaznih strana. Originalni PDF i istorijska mapa ostaju očuvani. Nove primere označi kao nastavne dopune povezane sa odabranim slajdom; ne predstavljaj ih kao sadržaj originalnog PDF-a.
- U `PLAN_PREDAVANJA.md` evidentiraj korisnikovo odobrenje dodatnih RTL slajdova, uz stvarne poruke i konkretan izbor slajdova. Dodavanje primera povećava broj projektovanih strana; postojeći slajdovi se ne brišu niti prenumerišu.
- Potvrde veži za dizajn, pomoćne module, testbench i pregledane prikaze. Izmena bilo kog od tih izvora poništava pogođenu potvrdu. Ranija odobrenja ostaju vezana za tada pregledane verzije.

## 5. Provere i predaja

Za svaki primer proveri:

- podudarnost funkcije, topologije i oznaka sa nastavnim sadržajem;
- uspešnu simulaciju i automatske provere u oba simulatora;
- čitljivost koda, komentara, brojeva linija i napomene o TB-u;
- potpunost prikazanog koda i pravilno nastavljanje linija;
- tačan položaj dodataka i očuvanje svih postojećih slajdova.

Za pogođeno predavanje pokreni postojeće ciljeve `notes`, `review`, `check` i novi `check-sv`, uz konkretan `LECTURE`. Obrazac komandi, nakon implementacije budućih dopuna, jeste:

```text
make -C predavanja LECTURE=<pun_folder_predavanja> notes
make -C predavanja LECTURE=<pun_folder_predavanja> review
make -C predavanja LECTURE=<pun_folder_predavanja> check-sv
make -C predavanja LECTURE=<pun_folder_predavanja> check
```

Pregledaj nove slajdove i njihove A4 prikaze, kao i postojeće prikaze pogođene dodatkom, pa obnovi stvarno pogođene potvrde. Automatska simulacija ne zamenjuje pregled šeme, nastavnog značenja i čitljivosti. Podaci o odobrenoj verziji i istorijske potvrde ostaju sačuvani.

Predaj kratak izveštaj sa obrađenim ID-jevima, putanjama primera, rezultatima simulacija i linkom ka novom PDF-u. Sledeće primere određuje korisnik.
