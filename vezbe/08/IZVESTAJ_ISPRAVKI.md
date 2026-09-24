# Izveštaj o ispravkama — vežbe 08

Brojevi stranica odnose se na izvorni `08_mos.pdf` (20 strana). Oznake `eq:...`, `sec:...`, `fig:...` i `tab:...` su stabilne oznake u novom LaTeX fajlu; vidljivu numeraciju određuje LaTeX. Negacije su proverene na slikama izvornog PDF-a: izgubljene crte iznad izraza u tekstualnoj ekstrakciji nisu prijavljene kao greške izvornika.

## 08-01 — str. 1–3, zadatak 1 → sec:1, eq:1.11

**Izvor:** krajnji izlazi pri ulazima 0 i VDD označeni su VOH i VOL i koriste se za MSNM.

**Dopuna:** razlikuju se krajnji V_H/V_L i garantovani V_OH=f(V_IL), V_O_L=f(V_IH). Izvorne procene 0.38 V i 0.43 V ostaju navedene kao aproksimacije. Garantovane margine u istom modelu bez korekcija kratkog kanala su 0.242474 V i 0.397739 V.

**Zašto i provera:** f(V_IL)=VDD−α/2=1.170930 V, f(V_IH)=sqrt(2αVDD/3)=0.215666 V; oduzimaju se od odgovarajućih ulaznih pragova. Oznake su usklađene sa vežbom 07. MIT [1] razlikuje izlazne granice od krajnjih napona i označava aproksimacije.

## 08-02 — str. 2, izbor korena → eq:1.9

**Izvor:** „uzeti samo pozitivni koren“.

**Ispravka:** bira se manji koren uz proveru omske oblasti i opsega između šina.

**Zašto:** za date parametre oba korena su pozitivna: približno 0.085567 V i 1.630712 V. Sam pozitivan znak nije dovoljan; veći koren je iznad napajanja 1.2 V i van pretpostavljene oblasti. Linearizovana procena 0.081301 V ostaje zasebno označena.

## 08-03 — str. 2, jednačine (1.2), (1.3) → eq:1.2, eq:1.3

**Izvor:** leva strana `(VDD−VOL)/RL`, iako se potom diferencira promenljivi izlaz vi.

**Ispravka:** `(VDD−vI)/RL`.

**Zašto i uticaj:** struja otpornika zavisi od trenutnog izlaza; diferenciranje konstante VOL ne bi dalo sledeću jednačinu. Ispravka vraća dosledno izvođenje VIL.

## 08-04 — str. 1–3, aproksimacije kratkog kanala → modeli, sec:1

**Izvor:** mali izlaz ili blizina praga uzeti su kao dovoljno opravdanje zanemarivanja članova sa EC L; predložena iteracija za VS.

**Dopuna:** potrebni su bezdimenzioni uslovi vI/(EC L)≪1 i (vU−VT)/(EC L)≪1. EC L nije zadat, pa tačnost zanemarivanja i tačan kratkokanalni VS nisu numerički određeni. Vrednost 0.652350 V navedena je isključivo za aproksimaciju bez tih korekcija.

**Uticaj:** izbegnuto izmišljanje parametra; svi brojni rezultati imaju naveden model. Izvorni interpolacioni model i relacija vsat=μEC/2 su sačuvani, uz jasno ograničenje njihove upotrebe.

## 08-05 — str. 4, numerička jednačina → eq:2.1

**Izvor:** `VOH=0.99−0.2 sqrt(VOH+0.88)`.

**Ispravka:** konstanta pre zaokruživanja je 0.9876166; rešenje je 0.733564 V.

**Vrsta i provera:** preciznost međurezultata, ne značajna teorijska greška. Zamenom se dobija VH+VT2(VH)=1.2 V. Izvorno 0.73 V ostaje pravilno zaokruženo.

## 08-06 — str. 5, odnos geometrija → eq:2.5

**Izvor:** `KR=1.7` iz jednačine (2.2).

**Ispravka:** direktna zamena zadatih parametara daje KR=4.49558.

**Zašto:** sa VU=0.733564 V, VI=0.1 V, VT2=0.410373 V, L=10⁻⁵ cm, μ=270 cm²/(Vs) i vsat=8·10⁶ cm/s, količnik struja po jediničnim geometrijama je 4.49558. Skripta nezavisno izračunava obe struje i proverava jednakost i režime rada. Vrednost 1.7 je ne zadovoljava; ne prenosi se u dimenzionisanje.

## 08-07 — str. 4–5, parametri modela → napomena posle eq:2.5

**Izvor:** istovremeno zadati vsat, μ, L i EC L.

**Nalaz:** iz 2vsatL/μ proizlazi 0.592593 V, a zadato je 0.6 V. Ako se EC L=0.6 V i relacija modela nametnu tačno, KR=4.55177.

**Vrsta i uticaj:** malo neslaganje zaokruženih parametara (oko 1.25% u KR). Oba tumačenja su izložena; nema proizvoljne promene podataka.

## 08-08 — str. 5, zadatak 2b → eq:2.3

**Izvor:** traži „minimalnu vrednost“, a rezultat je stroga nejednakost bez brojnog završetka.

**Ispravka/dopuna:** VGG>1.700827 V; ta vrednost je donja granica, ne dostignuti minimum za strogo omski rad. VH=VDD=1.2 V.

**Zašto:** maksimalni VT2 na 0≤vI≤VDD iznosi VT2(VDD)=0.500827 V. Dopunjen je postojeći postupak numeričkim rezultatom, bez dodavanja rešenja novom zadatku.

## 08-09 — str. 6, efekat podloge → eq:3.9

**Izvor:** nedostaju završne apsolutne vrednosti u korenima `sqrt(VSB+2|φF)−sqrt(2φF)`.

**Ispravka:** `sqrt(VSB+2|φF|)−sqrt(2|φF|)`.

**Zašto:** koristi se pozitivna veličina 2|φF|, kao u zadatku 2. Primarni MOS izvor [2] potvrđuje zavisnost praga od polarizacije podloge.

## 08-10 — str. 6, visoki izlaz → sec:3

**Izvor:** VOH=5 V bez zadatog napajanja.

**Ispravka:** VH=VDD, uz VT2(vI)<0 u celom opsegu. Nisu dati dovoljni podaci za numeričke margine.

**Zašto:** kada M1 ne vodi, opterećenje puni izlaz do napajanja samo ako ostaje provodno. Ako efekat podloge podigne prag iznad nule, analiziraju se drugačije oblasti; to je sada navedeno.

## 08-11 — str. 6–7, (3.1)–(3.3) → eq:3.1–eq:3.3

**Izvor:** `(VGS2−|VT2|)VDS2`, zatim `−|VT2|(VDD−VI)` i `−2|VT2|(VDD−VI)`.

**Ispravka:** za negativan prag i VGS2=0 prenapon je `−VT2=|VT2|=t>0`; članovi su pozitivni `t d` i `2t d`, gde d=VDD−vI.

**Zašto i uticaj:** izvorna desna strana jednačine (3.3) bila bi negativna za svaki d>0, dok je leva nenegativna. Ispravljeni bilans je KR(vU−VT1)²=2td−d². Sve izvedene jednačine i granice ponovo su izračunate.

## 08-12 — str. 7, tekst i (3.4) → eq:3.4

**Izvor:** „za VU≈VI“ u diskusiji blizu VIL; `VI=KR(VIL−VT1)+|VT2|+VDD`.

**Ispravka:** analizira se ulaz blizu VIL i visok izlaz; `vI=VDD−t+KR(VIL−VT1)`.

**Zašto:** diferenciranje ispravljenog bilansa uz vI′=−1 daje d=t−KR(VIL−VT1). Stari izraz daje izlaz iznad napajanja. Simbolička provera u SymPy potvrđuje novi izraz i zajedničko rešenje sistema.

## 08-13 — str. 7, (3.5) → eq:3.5

**Izvor:** imenilac struje zasićenja `−|VT2|+EC L2`.

**Ispravka:** `|VT2|+EC L2`.

**Zašto:** prenapon opteretnog tranzistora je pozitivan t. Izraz (3.6) izvornika, pisan kao `VT2²/(1−VT2/(EC L2))` sa **negativnim** VT2, već ima ispravan znak; ta jednačina nije prijavljena kao pogrešna nego prepisana kao Q=t²/(1+t/E2).

## 08-14 — str. 7–8, (3.6)–(3.8) → sec:3

**Izvor:** diferencira se uz zanemarenu zavisnost praga od izlaza, što nije odmah izrečeno.

**Dopuna:** prag se eksplicitno zamrzava na VT2(VDD) ili VT02 u odgovarajućoj oblasti. Inače se mora uključiti njegov izvod. Dodati su zatvoreni izrazi za pragove, fizički koren VL i uslovi diskriminanta; numerički parametri nisu izmišljeni.

## 08-15 — str. 8–9, PMOS oblasti → eq:4.1 i fig:4.1

**Izvor:** VSG>VTP uz VTP<0; VSD>VSG−VTP; tekst završava sa VI<VU+VTP.

**Ispravka:** VSG>|VTP|, VSD≥VSG−|VTP| i vI≤vU+|VTP|.

**Zašto:** dosledno se koriste pozitivni naponi PMOS tranzistora. Izvorna slika već ima ispravnu gornju pravu sa +|VTP|; tekst je bio u sukobu sa njom. Granice označene jednakošću i neprovodne oblasti proverene su zasebno.

## 08-16 — str. 9, ECN LN → sec:4

**Izvor:** ECN LN=0.4 V.

**Ispravka:** `(24/4 V/μm)·0.1 μm=0.6 V`.

**Uticaj:** izbačena je zamena NMOS imenioca netačnom konstantom. Potpuna izvorna jednačina struja rešena je numerički: VS=0.611288 V za Wp=400 nm i 0.537965 V za Wp=100 nm. Prvo zaokruživanje 0.61 V ostaje; drugo je 0.54 V umesto 0.53 V.

## 08-17 — str. 9, zajednički vsat → eq:4.2

**Dopuna:** isti vsat i Cox za NMOS/PMOS predstavljaju pretpostavku izvorne jednačine, a nisu automatski posledica jednakih dužina. Ako nisu jednaki, potreban je njihov odnos. Rešenja su proverena u (VTN,VDD−|VTP|) i imaju jednake struje.

## 08-18 — str. 10–11, statički CMOS → sec:5

**Izvor:** „barY“ kao običan tekst, nejasno poređenje minimalnosti realizacija.

**Ispravka/dopuna:** dosledna negacija Y; 8 tranzistora uz dostupne negacije, 10 sa izlaznim invertorom uz direktne ulaze, naspram 16 sa četiri ulazna invertora. Minimalnost je ograničena na komplementarnu statičku CMOS porodicu. Sva 16 ulazna stanja proverena su na PDN/PUN.

## 08-19 — str. 12, opis podmreže PM4 → sec:6

**Izvor:** na kraju objašnjenja PUN kaže da C i D čine paralelnu vezu.

**Ispravka:** C i D su paralelni u PDN, a redni u PUN. PM1 je A, PM2=B sa grupom CD, PM3=B, PM4=CD, PM5=C, PM6=D.

**Zašto:** dualnost serija/paralela i uslov da PDN i PUN vode za komplementarne skupove ulaza. Izvorna tranzistorska slika je ispravna; tekst je usklađen sa njom. Hierarhijski crtež čuva sve podmreže.

## 08-20 — str. 14–15, širine → eq:7.2

**Izvor:** `WP=min{R1,R2}`; dva puta „power-down“ i PDN umesto PUN u završnom objašnjenju.

**Ispravka:** `wP,worst=min(w1,w2)`; pull-down/pull-up i odgovarajuće mreže.

**Zašto:** širina ne može biti minimum otpornosti. Kada samo jedan paralelni tranzistor vodi, najgori slučaj daje najuži tranzistor. Oba uključena daju zbir širina. Proverene putanje: NMOS A i BC/BD imaju ekvivalent 1; PMOS AB i ACD imaju ekvivalent 2. Dimenzije 1,2,2,2 i 4,4,8,8 ostaju iste.

## 08-21 — str. 14–15, apsolutno dimenzionisanje → sec:7

**Dopuna:** vrednosti su normalizovani W/L u odnosu na referentni invertor, sa zajedničkom dužinom kanala. Bez zadate reference, opterećenja i ciljanog kašnjenja ne postoji jedinstveno apsolutno dimenzionisanje. Sačuvana je izvorna praktična raspodela otpornosti.

## 08-22 — str. 16–17, domino izlaz → eq:8.2 i fig:8.2

**Izvor:** završni izlaz na slici 8.2 označen Y, iako tačka b) traži Z=Ȳ.

**Ispravka:** Z=AB+CD. Sve crte negacije sa slike 8.1 i početnog izraza pažljivo su prenete; P·CD=CD provereno je za svih 16 kombinacija.

## 08-23 — str. 16–18, dinamička logika → sec:8–sec:9

**Dopuna:** logička funkcija dinamičkog čvora važi tokom evaluacije uz pamćenje pražnjenja. Tokom pretpunjenja izlaz je 1. Domino ulazi moraju biti stabilni ili monotono rastući tokom evaluacije [3]. Dodati su zanemareni efekti (curenje, kašnjenja i raspodela naelektrisanja), bez njihovog proizvoljnog kvantifikovanja.

**Provera:** događajna simulacija svih ivica zadatog dijagrama potvrđuje da pad C ne puni Y do narednog CLK=0. Izvorni oblik Y je bio ispravan i ostao je sačuvan.

## 08-24 — str. 19, tabela 10.1, red 0101 → tab:10.1

**Izvor:** Y=0.

**Ispravka:** Y=1.

**Zašto:** A=0 bira donju granu, C=0 bira B=1. Isto sledi iz (10.1) i iz tabele 10.2. Svih 16 redova nezavisno je provereno; ostali redovi tabele 10.1 su ispravni.

## 08-25 — str. 20, visoka impedansa i drugi izraz → sec:10

**Dopuna/ispravka:** Z označava odsustvo aktivnog pogona, ne Bulovu vrednost. TG bira i prosleđuje odabrani izvor; proverena su sva 24 slučaja za ABC i D∈{0,1,Z}. U drugom Šenonovom razlaganju uklonjena je suvišna završna zagrada. Obe realizacije Y=AC+BC proverene su za svih osam kombinacija. Navedeno je da potrebni invertori komplementarnih upravljanja nisu uključeni u broj TG tranzistora.

## Jezik i grafika

Na str. 1–20 ispravljeni su izrazi „obzirom“, „prekidni napon“ (ujednačen „napon praga“), „inertorski“, „direknu“, „indentifikuju“, „javalja“, „pribizno“, padeži, slaganje i duplirane reči. Oštećena dijakritika ekstrakcije rekonstruisana je vizuelnom proverom PDF-a. Izvorni simboli fizičkih veličina dobili su dosledne indekse i jedinice. Sve šeme i dijagrami su izmenjivi TikZ/Circuitikz izvori. Izvorna slika 9.1 razdvojena je na šemu i ulazni dijagram radi čitljivosti. Tabele imaju tanke razdelnike podataka, bez udvojenih linija uz zaglavlje.

## Ponovljive provere i primarni izvori

`make check` proverava MOS struje i oblasti, racionalne otpornosti putanja, simboličko diferenciranje za zadatak 3, sve male logičke tabele, propagaciju visoke impedanse i vremenske događaje. Ne zamenjuje proveru konkretnog tehnološkog modela SPICE simulacijom.

1. [MIT 6.012, Lecture 11 — CMOS inverter, Spring 2009, slajdovi 4–7](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-spring-2009/b96efcfa398f43f970ae4f36ac43456b_MIT6_012S09_lec11.pdf): garantovani naponski nivoi, nagibi i margine šuma.
2. [MIT 6.012, MOSFETs II; Large Signal Models, Fall 2009](https://www.ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2009/33eea31f564b67fc47cd9c2796500669_MIT6_012F09_lec11.pdf): efekat podloge i oblasti rada MOS tranzistora; uslovi korišćenja pojednostavljenih modela.
3. [David Harris, Advanced Domino Circuit Design, slajdovi 3–7](https://pages.hmc.edu/harris/research/advanceddomino.pdf): pretpunjenje, evaluacija i monotoni ulazi.

## Završna provera crteža

Na šemama zadataka 1–3 podloga MOS tranzistora eksplicitno je povezana preko priključka bulk. Povećane su oznake složenih mreža, a brojevi dimenzija pomereni od oznaka upravljanja. Dijagram oblasti rada čuva ilustrativnu karakteristiku prenosa i koristi izdvojenu legendu. Izvozi šema ograničeni su na površinu crteža. Ove korekcije odnose se na konverziju i čitljivost; ne prijavljuju se kao greške izvornika.
