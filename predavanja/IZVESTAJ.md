# Završni izveštaj rekonstrukcije predavanja

Završeno je **12 LaTeX Beamer prezentacija, 16:9, sa 620 izlaznih strana**.
Izvornih 314 PDF strana mapirano je na 620 pojedinačnih slajdova.
Svaki originalni slajd odgovara jednoj izlaznoj strani, uz očuvane granice,
redosled, ponavljanja, tekst, formule, tabele, kod i nastavne crteže.
Uklonjeni su samo dozvoljeni ponavljajući podaci i oznake.

## Prezentacije i dokazi pregleda

PDF i HTML linkovi rade nakon izgradnje i generisanja pregleda. Generisani
fajlovi ostaju u `build` direktorijumima, izuzetim iz Git-a.

| Predavanje | Izvorne PDF strane | Izlazne strane / očekivano | Prezentacija | Original i novi slajd | Evidencija |
|---|---:|---:|---|---|---|
| 01 | 19 | 37/37 | [PDF](01_logicke_funkcije/build/01_logicke_funkcije.pdf) | [Pregled](01_logicke_funkcije/build/pregled/index.html) | [Izveštaj](01_logicke_funkcije/provera/izvestaj.md) · [Greške originala](01_logicke_funkcije/provera/uocene_greske.md) |
| 02 | 27 | 54/54 | [PDF](02_sinteza_kombinacionih_mreza/build/02_sinteza_kombinacionih_mreza.pdf) | [Pregled](02_sinteza_kombinacionih_mreza/build/pregled/index.html) | [Izveštaj](02_sinteza_kombinacionih_mreza/provera/izvestaj.md) · [Greške originala](02_sinteza_kombinacionih_mreza/provera/uocene_greske.md) |
| 03 | 11 | 21/21 | [PDF](03_kola_srednjeg_stepena_integracije/build/03_kola_srednjeg_stepena_integracije.pdf) | [Pregled](03_kola_srednjeg_stepena_integracije/build/pregled/index.html) | [Izveštaj](03_kola_srednjeg_stepena_integracije/provera/izvestaj.md) · [Greške originala](03_kola_srednjeg_stepena_integracije/provera/uocene_greske.md) |
| 04 | 20 | 39/39 | [PDF](04_brojni_sistemi/build/04_brojni_sistemi.pdf) | [Pregled](04_brojni_sistemi/build/pregled/index.html) | [Izveštaj](04_brojni_sistemi/provera/izvestaj.md) · [Greške originala](04_brojni_sistemi/provera/uocene_greske.md) |
| 05 | 28 | 55/55 | [PDF](05_aritmeticke_operacije/build/05_aritmeticke_operacije.pdf) | [Pregled](05_aritmeticke_operacije/build/pregled/index.html) | [Izveštaj](05_aritmeticke_operacije/provera/izvestaj.md) · [Greške originala](05_aritmeticke_operacije/provera/uocene_greske.md) |
| 06 | 15 | 30/30 | [PDF](06_kodovi/build/06_kodovi.pdf) | [Pregled](06_kodovi/build/pregled/index.html) | [Izveštaj](06_kodovi/provera/izvestaj.md) · [Greške originala](06_kodovi/provera/uocene_greske.md) |
| 07 | 16 | 31/31 | [PDF](07_uvod_u_hdl/build/07_uvod_u_hdl.pdf) | [Pregled](07_uvod_u_hdl/build/pregled/index.html) | [Izveštaj](07_uvod_u_hdl/provera/izvestaj.md) · [Greške originala](07_uvod_u_hdl/provera/uocene_greske.md) |
| 08 | 34 | 67/67 | [PDF](08_elementi_analize_logickih_kola/build/08_elementi_analize_logickih_kola.pdf) | [Pregled](08_elementi_analize_logickih_kola/build/pregled/index.html) | [Izveštaj](08_elementi_analize_logickih_kola/provera/izvestaj.md) · [Greške originala](08_elementi_analize_logickih_kola/provera/uocene_greske.md) |
| 09_1 | 29 | 57/57 | [PDF](09_1_mos_logicka_kola/build/09_1_mos_logicka_kola.pdf) | [Pregled](09_1_mos_logicka_kola/build/pregled/index.html) | [Izveštaj](09_1_mos_logicka_kola/provera/izvestaj.md) · [Greške originala](09_1_mos_logicka_kola/provera/uocene_greske.md) |
| 09_2 | 31 | 62/62 | [PDF](09_2_mos_logicka_kola/build/09_2_mos_logicka_kola.pdf) | [Pregled](09_2_mos_logicka_kola/build/pregled/index.html) | [Izveštaj](09_2_mos_logicka_kola/provera/izvestaj.md) · [Greške originala](09_2_mos_logicka_kola/provera/uocene_greske.md) |
| 09_3 | 36 | 71/71 | [PDF](09_3_mos_logicka_kola/build/09_3_mos_logicka_kola.pdf) | [Pregled](09_3_mos_logicka_kola/build/pregled/index.html) | [Izveštaj](09_3_mos_logicka_kola/provera/izvestaj.md) · [Greške originala](09_3_mos_logicka_kola/provera/uocene_greske.md) |
| 10 | 48 | 96/96 | [PDF](10_logicka_kola_sa_bipolarnim_tranzistorima/build/10_logicka_kola_sa_bipolarnim_tranzistorima.pdf) | [Pregled](10_logicka_kola_sa_bipolarnim_tranzistorima/build/pregled/index.html) | [Izveštaj](10_logicka_kola_sa_bipolarnim_tranzistorima/provera/izvestaj.md) · [Greške originala](10_logicka_kola_sa_bipolarnim_tranzistorima/provera/uocene_greske.md) |
| **Ukupno** | **314** | **620/620** | | | |

## Rezultat završne provere

`make -C predavanja check` završen je izlaznim kodom 0; svih 12 predavanja
ima rezultat `PROVERENO`. Ova komanda uključuje izgradnju svih prezentacija,
računske provere, proveru mapiranja i generisanje uporednih pregleda.
Potvrđeno je sledeće:

- Izvorni PDF-ovi imaju iste SHA-256 kontrolne sume kao početni inventari.
- Postoji 620 izvora slajdova, sa tačnim eksplicitnim redosledom uključivanja.
- Zapis stvarno poslatih PDF strana odgovara svim izvornim oznakama.
- Nema nedostajućih resursa, prekoračenja prostora, nedostajućih znakova ili nerešenih referenci.
- Svih 620 slajdova pojedinačno je sadržinski i vizuelno pregledano.
- Potvrde pregleda imaju aktuelne kontrolne sume originalnih i novih prikaza.
- Nezavisne računske provere svih predavanja prolaze.

`make -C predavanja test` prolazi **20 testova alata**. Obuhvaćeni su
izostavljen i dupliran slajd, promenjen redosled, dodatna overlay strana,
dva slajda na strani i samo jedan na poslednjoj, nedostajuće podnožje,
sadržaj dostupan samo kao slika, zastarele potvrde, promenjeni resursi
i neispravan keš renderovanih strana.

Mapiranje i inventar sadržaja nalaze se u `provera/mapa.json` svakog
predavanja, a potvrde kategorija i kontrolne sume u `provera/pregled.json`.
HTML poređenje prikazuje originalne isečke, nove slajdove i kandidate za
tekstualne razlike. Tekstualno ili pikselno poklapanje nije korišćeno kao
zamena za sadržinski i vizuelni pregled.

## Vernost prenosa i greške originala

Potvrđena je vernost prenosa. To nije potvrda da su svi izvorni stručni i
računski iskazi tačni. Otkrivene slovne, računske i stručne greške sačuvane
su na odgovarajućim slajdovima, a zasebno zabeležene u dokumentima
`provera/uocene_greske.md`, sa lokacijom, izvornim zapisom, obrazloženjem i
predlogom ispravke. Sopstvene greške prepisivanja ispravljene su pre pregleda.

Sve nastavne tabele, Karnoove karte, šeme, dijagrami i prikazani kod imaju
uređive tekstualne izvore. Fotografije i snimci interfejsa izdvojeni su iz
originala kada nose nastavnu informaciju. Nijedan originalni slajd nije
prenesen kao celovita slika umesto rekonstrukcije.

Originalni PDF-ovi ostali su na postojećim putanjama. Rad na predavanjima
nije menjao postojeće izmene u `vezbe`.

## Dalje uređivanje

Komande i verzije zavisnosti su u [README.md](README.md), a pravila prenosa
u [PREDAVANJA.md](../PREDAVANJA.md). Posle promene sadržaja pokrenuti izgradnju
i uporedni pregled, proveriti izmenjene prikaze i tek zatim obnoviti njihove
potvrde. Stroga provera odbija potvrde čiji se prikaz promenio.
