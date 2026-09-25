# Uočene greške i nedoslednosti originala

Zapisi ostaju preneti bez prećutnog ispravljanja. Ovde su odvojene sumnje i
predlozi ispravki za celo predavanje. PDF strana je `(n+1)//2`,
neparni slajd je gore, parni dole; precizne lokacije su u `mapa.json`.

| Slajd | Izvorni zapis | Napomena / predlog |
|---|---|---|
| 3 | „dreja“ | Predlog „drejna“. |
| 4 | „dužina kanal“ | Predlog „dužina kanala“. Prazne ćelije CGCS/CGCD su sačuvane, nisu samovoljno dopunjavane nulama. |
| 6 | „prethodno stepen“ | Predlog „prethodni stepen“. |
| 10 | „kapacitvnosti“ | Predlog „kapacitivnosti“. |
| 11 | „ekvivalentana“ | Predlog „ekvivalentna“. |
| 11–13 | Odnos struja jednak odnosu pokretljivosti; tvrdnje o minimalnom kašnjenju i srednjem pragu | Jednakost sa μn/μp traži odgovarajuće pretpostavke modela i jednakih dimenzija; nije opšta za sve modele kratkog kanala. Statički i dinamički optimum se razlikuju, kao što sam slajd 12 navodi. Kompromis 2:1 sa slajda 13 ne garantuje istovremeno oba egzaktna optimuma za svaku tehnologiju. |
| 15 | „minizujemo“ | Predlog „minimizujemo“. |
| 17–19 | Promena značenja f_i | Na slajdu 17 to je odnos susednih ulaznih kapacitivnosti; na slajdu 19 f_i označava ukupno povećanje dimenzija i u izrazu se koristi f_(i+1)/f_i. Preporuka je razdvojiti oznake veličine stepena i njegovog fanout-a. |
| 19, 21 | „najblizi“ | Predlog „najbliži“. |
| 20 | „nema zatvorenu formu“ | U elementarnim funkcijama nema jednostavnog eksplicitnog izraza. Rešenje je moguće izraziti Lambertovom W funkcijom. Izvorna vrednost 3.6 je dobra aproksimacija pozitivnog korena za γ=1, potvrđena nezavisno. |
| 21 | U zbiru kašnjenja nema 1/γ | Odgovara dodatnoj aproksimaciji γ=1. U opštem izrazu sa slajda 19 faktor postoji. |
| 21–22 | Biranje najbližeg neparnog N | To je praktično pravilo za invertujući lanac, a ne dokaz diskretnog minimuma za svako opterećenje. Za strogu optimizaciju uporediti kašnjenja kandidata sa stvarnim završnim CL. |
| 22 | `tp=5Ntp0` | Izraz je tačan za γ=1 i svaki fanout jednak 4, uključujući završni CL. Ako se N samo zaokruži a CL ostaje zadat, poslednji odnos ne mora biti 4; treba zadržati stvarni završni odnos u sumi. |
| 23 | „nebaferisna“, „čije su tranzistora“, „osnovnom logikom kolu“ | Predlozi „nebaferisana“, „čiji su tranzistori“, „osnovnom logičkom kolu“. |
| 28–29 | „ukupnu ekvivalentnu širinu“ iz W/(1+1) | Preciznije je govoriti o ekvivalentnom odnosu W/L; tekst izvornika je zadržan. |

Nezavisna provera nalazi se u `kodovi/provera_logike.py`:
1007 računskih provera, uključujući istinitosne kombinacije i računske modele završnog dela. Vizuelna vernost vodi se zasebno u `pregled.json`.

Dopuna za slajdove 31–50:

- Slajd 31: „relaizaciju“ → predlog „realizaciju“.
- Slajd 32: „pojavlju“, „promenjive“, „komplementim“ → „pojavljuju“, „promenljive“, „komplementnim“.
- Slajd 35: najveći broj kola na putanji ne mora značiti najveće kašnjenje. Kritičnu putanju određuje zbir kašnjenja, uključujući tipove kola i opterećenja. Kontraprimer: dva kola po 10 jedinica kašnjenja sporija su od tri kola po 1 jedinicu.
- Slajd 37: W u izrazu CgW treba razumeti kao odgovarajuću ukupnu ulaznu širinu. Ako je W i dalje širina N tranzistora kao na slajdu 36, nedostaje faktor 3 pri definisanju krajnjeg opterećenja CgW_(N+1)=CL; odnos susednih širina nije pogođen tim faktorom.

Plus pre γinv na slajdu 40 postoji u izvorniku: potvrđen je renderovanjem na 400 dpi. Nije greška originala.

Dopuna 41–44:

- Slajd 41: „izvorom kapacitivnosti“ → predlog „izborom kapacitivnosti“.
- Slajd 43: u završnom izrazu Pi treba dosledno označiti Pinv; LEOR/POR treba LENOR/PNOR za nacrtano NILI kolo, a njegov FO ima indeks i+2 umesto ponovljenog i+1. Sve oznake izvornika su sačuvane.
- Slajd 44: Pinv=1/2 podrazumeva γinv=1/2, dok se ranije za neke približne proračune uzimalo γ≈1. Zadržati razliku modelskih pretpostavki pri korišćenju formula.

Dopuna 46–50:

- Slajd 46: „prouzrokvana“ → predlog „prouzrokovana“. Popis E tranzistora kao dva NMOS odgovara originalnoj šemi; nije zamenjen uobičajenom komplementarnom varijantom.
- Slajd 50: „a kao nije A“ → predlog „a ako nije A“.


Dopuna 51–71:

- Slajd 51: „trnazistora“ i „logičke logičke nule“ preneti su doslovno. Oznaka `VGTn` u uslovu `VGS=VGTn` odstupa od uobičajenog `VTn`; predlog proveriti i zameniti oznakom praga.
- Slajd 56: „logičko kolam“ → predlog „logičko kolo“.
- Slajd 59: prikazana mreža s prekidima vertikalnih podatkovnih vodova i gornjim vezama na A3 realizuje aritmetičko pomeranje udesno sa proširenjem znaka; ne treba je tumačiti kao proizvoljno pomeranje ulevo samo na osnovu šireg naslova. Četiri gornja spoja i tri prekida potvrđeni su na uvećanom originalu. Proverene su sve 64 kombinacije četvorobitnog ulaza i pomeraja.
- Slajd 62: naslov navodi `VI=−12 V`, ali crtež i pasus koriste `+12 V`. Predlog ispraviti znak u naslovu. Preneto je izvorno neslaganje. „će radi“ → „će raditi“.
- Slajd 63: „sa malom dinamičkom otpornosti“ → „sa malom dinamičkom otpornošću“.
- Slajd 67: zadatak ostaje otvoren sa `Y=?`; nezavisna provera prepoznaje XOR, ali odgovor nije dodat na slajd.
- Slajd 70: „tranzistora tranzistora“, „će vodi“, „je voditi“ ostaju doslovno; predlozi ukloniti dupliranje i koristiti „će voditi“.
- Slajd 71: „koje je“ → „koja je“. Završnu tvrdnju „sve funkcije ... moraju biti invertovane“ treba precizirati: izlazni invertor invertuje funkciju dinamičkog čvora, dok kaskadna standardna domino realizacija zahteva monoton porast izlaza tokom evaluacije i realizuje neinvertujuće funkcije ulaza bez dodatne logike. Tvrdnja originala je zadržana.
