# Predavanje 03 — beleške kao pomoć predavaču

Datum: **2026-10-02**. Status: **ceka_odobrenje**. Tema: zamrznuta **etf-v1**, stil **B**.

Pročitani su aktuelni PLAN_PREDAVANJA.md, svih **21 originalnih slajdova** sa 11 PDF strana, izvori postojećih slajdova i njihove beleške. Svaki originalni i generisani slajd upoređen je vizuelno. Prepisani su izvori `beleske/s001.tex`–`s021.tex` prema novom koraku 6: samo ono što predavač treba dodatno da objasni, bez uredničkih naslova, porekla, istorije ispravki ili korisnikovih odluka u nastavnom tekstu.

**Slajdovi, crteži, tabele, kod, glavni izvor i prezentacioni PDF ostali su nepromenjeni.** Originalni PDF i tema su neizmenjeni. Broj, redosled i ID-jevi **03-s001–03-s021** očuvani su. Projekcija ima 21 stranu; nove beleške imaju 21 A4 stranu, sa prikazom slajda, njegovim ID-jem i naslovom. S001 nema dodatnog teksta i nije veštački popunjen.

## Sadržaj beležaka i pokrivenost

Preneti su svi nastavni detalji skraćeni na slajdovima. Dopune objašnjavaju formule, međukorake, rad kola, uslove i tipične zabune. Formule koje su vidljive koriste se samo kao oslonac izvođenja; tabele i tekst slajdova nisu ponovo prepisani. Vidljive ključne definicije, uslovi, rezultati i ilustracije ostaju očuvani.

[Mapa pokrivenosti](pokrivenost.md) i [inventar](inventar.json) sada obuhvataju **91/91 proveren element**: 70 ranije popisanih izvornih elemenata, zasebno izdvojen tačan izvorni NI invertorski slučaj na s004 i 20 blokova dopunskog objašnjenja. Za taj izvorni slučaj dodat je `03-s004:e04`; njegova sadržina već je postojala u ranijim beleškama, sada bez istorije odobravanja. Dopune imaju sidra `03-s002:d01`–`03-s021:d01`. Sva stara nevidljiva sidra i `\BeleskeID` veze sačuvani su. Odredišta u beleškama vode samo do stvarnog nastavnog sadržaja istog ID-ja.

Poreklo izvornog sadržaja, razlika prema dopunama, stručne provere i izdvojena urednička evidencija nalaze se u [evidencija_beleski.json](evidencija_beleski.json). Taj fajl ne sadrži drugu kopiju teksta beležaka. Jedini izvor njihovog nastavnog teksta ostaje `beleske/sNNN.tex`.

| Slajd | Izvorni detalji dodatno objašnjeni u beleškama | Dopunsko izvođenje ili razjašnjenje |
|---|---|---|
| 03-s001 | Nema; naslov i autorstvo ostaju vidljivi. | Bez dodatnog teksta. |
| 03-s002 | Različite brojčane granice u literaturi. | Razlika brojanja tranzistora i kapija; približnost klasifikacije. |
| 03-s003 | Puni engleski naziv PCB i veza sa vodovima ploče. Dostupna pakovanja i podaci o njima nalaze se u proizvođačkom opisu. | Razlika funkcije i kućišta, tumačenje fizičkih pinova prema konkretnoj komponenti. |
| 03-s004 | Smanjenje potrebnih čipova zavisi od dostupnih kola iste vrste. Neodređeni ulazi mogu nepovoljno uticati na aktivni deo mreže. Funkcionalno jednaka zamena daje putanju kroz dva kola umesto jednog. NI kolo sa spojenim ulazima ostvaruje invertor. | Brojanje četiri I2 i preostalog invertora; idempotentnost I i inverzija NI. |
| 03-s005 | Adresni ulazi često se označavaju slovom A. | Dokaz jednog aktivnog minterma; primer adrese 10 i sinteza preko minterma. |
| 03-s006 | Izvorni sadržaj ostaje vidljiv; beleške razrađuju njegov smisao. | Izvođenje F=Y0+Y3 i prepoznavanje EXNILI funkcije za četiri kombinacije. |
| 03-s007 | Bez oznaka unutar komponente nije moguće pouzdano rekonstruisati rešenje zadatka ili ispita. | Formula k=2S1+S0 i posledica zamene uloga selektora. |
| 03-s008 | Izvorni sadržaj ostaje vidljiv; beleške razrađuju njegov smisao. | Izvođenje Yk=CS mk; razlikovanje neaktivne nule i visoke impedanse. |
| 03-s009 | Mogućnost drugačijeg rasporeda selektora; ime piramide prati oblik i grananje. Proširenjem raste broj nivoa i kaskadno kašnjenje. | Indeks 4g+k, primer 1011→11 i brojanje komponenti 1+4+16. |
| 03-s010 | Trodimenzioni izbor zahteva tri CS uslova. Svako od 16 polja ima izlazni blok; izdvojeni prikaz pokazuje samo jedan. Prednost pri većim kapacitetima, zahtev za specifičnijim komponentama i kombinovanje struktura. | Razlaganje i/j/k, primer indeksa 39, razlika označenog polja i električkog spoja. |
| 03-s011 | Uobičajena upotreba simbola sa negacionim kružićima. | Tumačenje m_k, dvostruka negacija i različiti uslovi prvih i trećeg CS simbola. |
| 03-s012 | Izvorni sadržaj ostaje vidljiv; beleške razrađuju njegov smisao. | Jednačine Yk=I mk, primer adrese 10 za oba nivoa I i tumačenje dozvole kao podatka. |
| 03-s013 | Broj podatkovnih ulaza veći od broja izlaza; smer izbora obrnut demultiplekseru. | Pun izraz Z za četiri podatkovna ulaza, mintermi i primer adrese 01. |
| 03-s014 | U nekim situacijama MUX omogućava jednostavniju realizaciju od dekodera. Vrednosti funkcije dovode se na ulaze kojima odgovaraju selektovani potpuni proizvodi. | Uvrštavanje 1,0,0,1 u izraz multipleksera; dokaz iste funkcije. |
| 03-s015 | Izvorni sadržaj ostaje vidljiv; beleške razrađuju njegov smisao. | Uslovljeni izlaz Z=CS Z0; mapiranje stabla 4g+k, primer I13 i broj pet MUX-ova. |
| 03-s016 | Upotreba u složenim i procesorskim digitalnim sistemima. | X kao nevažna vrednost, prioritet i valjanost adrese uz GS. |
| 03-s017 | Direktno crtanje iz preglednih uslova bez zahteva da realizacija bude minimalna. | Međusignali P3–P0, koderske jednačine i primer I2/I1. |
| 03-s018 | Izvorni sadržaj ostaje vidljiv; beleške razrađuju njegov smisao. | Algebarsko izvođenje A1/A0/GS pomoću X+barX Y=X+Y i objašnjenje prioriteta. |
| 03-s019 | Niži bitovi iz neizabrane grupe daju logički pogrešan kod, pored električkog problema direktnog spoja. Dodatne dozvole služe identifikaciji validnih nižih bitova i njihovom logičkom objedinjavanju. | Globalni indeks 4g+k i kontraprimer I12/I7 protiv spajanja neuslovljenih kodova. |
| 03-s020 | Alternativa u kojoj GS nije uslovljen EI. Potpuno tumačenje sva tri slučaja prenosa dozvole. Zašto inverzija ne odgovara EO ni za uslovljeni ni za neuslovljeni GS. | H kao lokalni zahtev, GS=EI H i EO=EI barH sa potpunim slučajevima. |
| 03-s021 | Direktno povezivanje izvodljivo je sa visokom impedansom neaktivnih izlaza. Nema jednog strogo jedinstvenog rasporeda MSI simbola; uobičajeno razdvajanje ulaza i izlaza. | Primer I10/I5/I1, slučaj bez zahteva i uslov jedinstvenog drajvera visoke impedanse. |

## Poređenje sa prethodnim beleškama

| Primer | Pre | Posle |
|---|---|---|
| s001 | Objašnjenje naslovnog slajda i urednički zapis autorstva. | Samo ID; PDF prikazuje slajd i naslov. |
| s004 | Opis korisnikove odluke i istorije NI/I izmene. | Izvođenje zamene I3 sa dva I2, uslovi uštede čipova, tačan NI invertorski slučaj i pravilo neiskorišćenih ulaza. |
| s006/s012 | Opis nedostajućih delova originalnog crteža. | Funkcionalno izvođenje iz datih oznaka i formule; crtež nije dopisivan. |
| s017/s018 | Sažetak prioritetske šeme i izdvojeni naslov dopune. | Međusignali P3–P0, njihove koderske jednačine i algebarsko pojednostavljenje. |
| s020 | Sažeto prepričavanje uloga EI/EO i GS. | Potpuna tri slučaja, EO=EI·barH, kontraprimer inverzije GS i alternativa neuslovljenog GS. |

Uporedni prikaz originala, početnog LaTeX prikaza, postojećeg slajda i novih beležaka dostupan je u [HTML pregledu](../../build/redizajn/pregled/index.html). Prethodni izveštaj, inventar, mapa, manifest, zapis izgradnje i potvrde sačuvani su u [istorijskoj evidenciji](istorija/pre-dorade-beleski-2026-10-02/izvestaj.md). Oni opisuju prethodnu verziju i ne potvrđuju nove beleške.

## Stručne i jezičke ispravke

Ranija korisnikova odluka za s004 ostaje važeća: I kola i F=ABC=A(BC). Nema nove stručne promene projektovanog sadržaja. Tačan izvorni NI invertorski slučaj objašnjen je neposredno, uz razlikovanje od ponovljenih ulaza I kola. Odobrenje i istorija ostaju u [odluke.md](odluke.md) i arhiviranom izveštaju.

S006 i s012 zadržavaju postojeće nepotpune prikaze. Jednačine u beleškama stručno su izvođenje njihovih formula i definicija; nisu tvrdnja da nevidljivi vodovi postoje u originalu. S011 zadržava sve izvorne negacije; objašnjeno je zašto treći simbol nije ekvivalentan.

Jezički su uređene rečenice beležaka, bez promene značenja. Ranije evidentirane slovne ispravke i korisnikove odluke ostaju u istoriji. **Nema otvorenih stručnih pitanja za ovu doradu 03.** Nalog za pisanje beležaka nije odobrenje njihovog rezultata.

## Dokazi provere

Uspešno izvršene komande iz korena repozitorijuma (izlazni kod 0):

```bash
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije notes
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije review
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije check
python3 predavanja/03_kola_srednjeg_stepena_integracije/kodovi/provera_logike.py
git diff --check
```

[Notes log](../../build/redizajn/provera-beleski/notes.log), [review log](../../build/redizajn/provera-beleski/review.log) i [check log](../../build/redizajn/provera-beleski/check.log) čuvaju završne rezultate. `check` daje **PROVERENO** za 21/21 slajd, 21/21 blok beležaka i 91/91 element pokrivenosti. Provereni su isti broj i redosled slajdova, tačni ID-jevi, veza svake beleške sa odgovarajućim slajdom, aktualnost izvora, prikaza i korišćene teme. Oba LaTeX loga su bez upozorenja, Overfull/Underfull poruka, nedostajućih znakova i grešaka.

Postojeća računska provera potvrđuje obe funkcionalne tabele kodera za svih 16 stanja, dekoder/MUX, svih 64 adrese i svih 65.536 stanja proširenog kodera. Dodatno je tokom ove dorade enumeracijom provereno **14 grupa izvođenja kroz 1.048.959 slučajeva**, uključujući svih 16 adresa i 65.536 ulaznih podataka stabla MUX 16/1, minterme, negacije, prioritetne međusignale, EO i konkretne primere. Rezultati i granice tih provera su u [evidenciji](evidencija_beleski.json); one proveravaju izvedene izraze, ne dokazuju automatski izgled šema.

Zato su posebno pregledani svi originalni i generisani slajdovi i **svaka nova A4 strana u punoj veličini**: formule, tekst, oznake, tabele, topologija, pokrivenost i upotrebljivost za predavača. Beleške su čitljive, bez preklapanja, odsecanja ili nepotrebnog prepisivanja vidljivog teksta. S020 sadrži ceo argument, ne samo rezime. Tek posle pregleda obnovljena je [21 potvrda](pregled.json), vezana za stvarno pregledane izvore i prikaze. Otisci potvrđuju da su original, slajdovi i projekcija ostali identični stanju pre ovog zadatka.

## Isporuka i kontrolne sume

- [Prezentacioni PDF — nepromenjen, 21 slajd](../../build/03_kola_srednjeg_stepena_integracije.pdf).
- [Novi PDF beležaka — 21 A4 strana](../../build/03_kola_srednjeg_stepena_integracije_beleske.pdf).
- [Uporedni pregled](../../build/redizajn/pregled/index.html).
- [Izvori beležaka](../../beleske/s001.tex), [manifest](manifest.json), [zapis izgradnje](izgradnja.json), [potvrde](pregled.json), [poreklo i dokazi](evidencija_beleski.json).

Izlazi u `build/` ne verzionišu se; ponovo se grade gore navedenim komandama iz sačuvanih izvora. Izvori, evidencija i istorija ostaju van tog foldera.

| Resurs | SHA-256 |
|---|---|
| Originalni PDF | `5e68d267ca2f60c1ccdf073c2579fd64a4b05278955cc3d3f920cc54e123fd86` |
| Manifest redizajna | `043cfd60fc37b3776983018ddca3b715e03d99d8c679ea1e8de9df4306469213` |
| Zapis izgradnje | `fbe022a68b9f3cd17057d2df9c55fe2ca3d7a738d773df8bfc2a17d296c4b1b1` |
| Potvrde pregleda | `3ec10952831f676fcf9c654ddb37cd802403e244879901ae481bdd5a91d24740` |
| Prezentacioni PDF | `4bcf5f421b2d32586028a3683d572bbf8077ca9ac088927a3e76180722cec9b9` |
| PDF beležaka | `7b5b67c09c00da4d1fb1ce6a0dcde8a055c85b5dff8230e3fd9a68405c5e7e56` |
| Evidencija beležaka | `2a8318a532e68b33501629547b9dc3f7a1481169d1f30016b73337fb0e332deb` |
| Manifest teme etf-v1 | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |
| Arhiva polazne rekonstrukcije | `c811bbc07e38b5d35989ebd68889bcdb657b518e0b035fae2e502bbbc2547d15` |

## Nastavak rada

Poslednji završen korak: sadržinski i vizuelni pregled svih beležaka, obnova potvrda i završni `check: PROVERENO`. Sledeća radnja je **korisnikov pregled i prihvatanje novih beležaka 03**. Status ostaje `ceka_odobrenje`; rezultat 03 nije samostalno odobren od agenta.

Ovaj zadatak ne otvara drugo predavanje. Ranija dozvola za 04 evidentirana je zasebno u centralnom statusu; ovo nije nova dozvola niti obrada 04. Početak 05 nije odobren. Naredni agent proverava ovu evidenciju i relevantne otiske; ne ponavlja završen pregled nepromenjene verzije bez novog naloga. Naknadna izmena beležaka poništava pogođene potvrde i zahteva pregled pogođenog prikaza, `notes`, `review` i `check`.
