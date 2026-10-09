# Predavanje 03 — dorada prema odobrenoj prezentaciji 01

Datum: **2026-10-02**. Status: **ceka_odobrenje**. Tema: **etf-v1**, stil **B**.

Ponovo su upoređeni originalno predavanje, prethodno generisana prezentacija i novi prikaz svih **21/21 slajdova**. Raspored, razmaci, tabele i šeme usklađeni su sa odobrenom 01. Očuvani su broj, redosled i ID-jevi **03-s001–03-s021**, kao i svih **70/70 sadržajnih elemenata** originala, na slajdovima i u beleškama istog ID-ja. Prezentacioni PDF ima 21 stranu; prateći PDF beležaka takođe ima 21 stranu. Originalni PDF ima 11 strana i nije izmenjen.

Korisnikov nalog za ovu doradu i ranija stručna odluka za s004 evidentirani su u [odluke.md](odluke.md). Nalog odobrava rad na 03; nije prihvatanje završnog rezultata niti dozvola za 04. Predavanje 01 i zamrznuta zajednička tema nisu menjani.

## Šta je promenjeno

| Slajdovi | Rezultat dorade |
|---|---|
| s001 | Naslovna strana prati raspored odobrene 01, uz isto autorstvo i školsku godinu 2021/22. |
| s002–s003 | Ujednačene, pregledne tabele sa odvojenim naslovima i većim razmacima. Na s002 vraćeni su svi puni engleski nazivi stepena integracije; izvorni pragovi su očuvani. |
| s004 | Zadržana je korisnikom odobrena zamena NI sa I i jednakost F = ABC = A(BC). Neiskorišćeni ulazi i ključna jednačina istaknuti su tamnocrveno. |
| s005, s007–s008 | Poravnati su interni dekoder, apstraktni simboli i jednačine. Oznake selektora odvojene su od isprekidanog okvira; sačuvane su sve grane i tačke spojeva. |
| s006, s012 | Očuvani su nepotpuni crteži originala bez izmišljanja nedostajućih kola i vodova; objašnjenja su u beleškama. |
| s009 | Piramidalna šema više nije vertikalno potisnuta prema naslovu. Svi selektori, CS, četiri izlazna bloka i Y0–Y15 ostaju vidljivi. |
| s010 | Precrtana je izvorna matrična organizacija, sa vrstama/kolonama, svim njihovim izlazima i zajedničkim CS1/CS2. Reprezentativni završni blok i formula indeksa odvojeni su od matrice. Crvena strelica i prazan kružić izdvajaju polje; nisu električni vod ili spoj. |
| s011 | Svih šest prikaza dobilo je pojedinačne selektore i četiri izlazna izvoda. Sačuvani su svi nadcrti, kružići i relacije jednakosti/nejednakosti. Vraćen je nadcrt CS1 u trećem donjem simbolu koji je bio izostavljen u prethodnom crtežu. |
| s013–s015 | Interni MUX, simboli i prelazne strelice jasno su odvojeni. Izlazni ILI je spušten, a četiri izlazna voda I kola vođena su van tela simbola. Proširenje 16/1 prikazuje sve globalne i lokalne ulaze, zajedničke selektore i tačke njihovih grananja. |
| s016–s017 | Centrirani su naslovi funkcionalnih tabela, sa razmakom prema prvoj liniji. Tamnocrveno su istaknuti kod 00 i značenje GS; svi redovi tabela i cela prioritetska šema ostaju vidljivi. |
| s018 | Ujednačena je veličina I/ILI kola, razmaknute su ulazne oznake i izvod invertora. Vod invertor–I kolo izveden je sa pregibom ispred ulaznog priključka, izvan tela kola. |
| s019–s021 | Precrtani su simboli i proširene mreže kodera sa svim signalima. EI/EO, GS, A1/A0 i lokalni/globalni ulazi imaju odvojene oznake. Šema s020 je povećana radi čitljivosti; na s021 dve četvoroulazne ILI grane i lanac dozvole imaju zasebne vodove. |

Na aktivnom predavanju lokalno je primenjena tamnocrvena **#A32638** za nastavna isticanja, prema odluci iz plana i prezentaciji 01. Fontovi ostaju postojeći. Boja nije proglašena zvaničnom ETF bojom; tema `etf-v1` nije menjana. Oznake šema su najmanje 9 pt, bez skaliranja celog slajda ili dodatnih overlay strana. Razmaci su uređeni rasporedom i eksplicitnim završavanjem pasusa, bez negativnog potiskivanja sadržaja.

Izmenjeni uređivi crteži: `dekoder_jezgro.tex`, `s009_piramidalni_dekoder.tex`, `s010_matricni_dekoder.tex`, `s011_polariteti_izlaza.tex`, `s011_polariteti_selekcije.tex`, `mux_jezgro.tex`, `s015_mux_16_u_1.tex`, `prioritetno_jezgro.tex`, `s018_minimalniji_koder.tex`, `koder_prioriteta_simbol.tex`, `s019_koder_16_ulaza.tex` i `s021_koder_sa_enable_lancem.tex`. Svaki je pregledan prema originalnoj topologiji, indeksima i negacijama, a ne samo prema izgledu.

## Beleške i pokrivenost

Svaki slajd ima zaseban izvor beležaka i smislen naslov uz stabilni ID. PDF beležaka sadrži novi prikaz slajda, ID i detaljno objašnjenje. Pregledane su sve 21 strane u punoj veličini. Dopunska izvođenja označena su odvojeno od izvornog sadržaja.

| Slajdovi | Detalji u beleškama |
|---|---|
| s001–s003 | Poreklo materijala, približnost integracionih granica, puni nazivi, veza sa PCB i izbor pakovanja. |
| s004 | Izvorna NI formulacija i invertorski slučaj, poreklo odobrene ispravke i detaljno objašnjenje asocijativnosti I. |
| s005–s008 | Mintermi, težine selektora, indeksi, izbor komponente i aktivni nivo CS. Na s006 dopunsko F = Y0 + Y3 nije pripisano originalu. |
| s009–s010 | Indeksiranje većih mreža, tri nivoa piramide, dvodimenziona i trodimenziona selekcija, poređenje 18/21 komponenti i mogućnost kombinovanih struktura. |
| s011–s012 | Razlika između aktivnog nivoa i negacije, dvostruka negacija i funkcionalni odnos demultipleksera prema dekoderu. |
| s013–s015 | Izbor podatkovnih grana, poređenje sa dekoderom, izvođenje vrednosti 1/0/0/1 i mapiranje 16 ulaza u proširenom MUX-u. |
| s016–s018 | Primena kodera u procesorskim sistemima, dvosmislenost koda 00, potiskivanje nižih prioriteta; na s018 dopunske jednačine A1, A0 i GS. |
| s019–s021 | Izbor validnih nižih bitova, tri slučaja EI/EO, izvorna alternativa neuslovljenog GS, uslovi direktnog spajanja izlaza sa visokom impedansom i konvencije priključaka. |

Definicije, rezultati, uslovi, tabele i nastavne šeme ostaju na slajdovima. U projektovanom PDF-u nema uredničkih komentara o procesu obrade ili greškama originala.

Precizna mapa svih 70 elemenata, sa odredištima na slajdu i u beleškama i opisom promene, nalazi se u [pokrivenost.md](pokrivenost.md) i [pokrivenost.json](pokrivenost.json). Nezavisni [inventar.json](inventar.json) na s006 sada tačno navodi izvornu funkciju, umesto prethodne pogrešne tvrdnje da original eksplicitno prikazuje F = Y0 + Y3.

## Provere i stručne odluke

Uspešno su izvršeni:

```bash
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije all
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije review
make -C predavanja LECTURE=03_kola_srednjeg_stepena_integracije check
python3 predavanja/03_kola_srednjeg_stepena_integracije/kodovi/provera_logike.py
git diff --check
```

`review` gradi i prateći PDF beležaka iz istih izvora. `check` daje **PROVERENO**: broj, redosled i ID-jevi su očuvani, svih 70 sadržajnih elemenata ima provereno odredište, a svih 21 potvrda povezuje aktuelne izvore, slajd i beleške. LuaLaTeX logovi oba nastavna PDF-a nemaju upozorenja, `Overfull`, nedostajuće znakove ili greške kompilacije. [Završni review log](../../build/dorada-2026-10-02/review-zavrsno.log) i [check log](../../build/dorada-2026-10-02/check-zavrsno.log) čuvaju rezultate.

Računska provera potvrđuje obe tabele kodera za svih 16 ulaznih stanja, dekoder/MUX, svih 64 adresa dekodera, svih **65.536** stanja proširenog kodera i odobrenu zamenu I3 sa dva I2. Automatika ne potvrđuje izgled sama: ručno su upoređeni svi originalni i prethodni slajdovi, sve formule, tabele, šeme, novi prikazi i beleške.

Nema novih nerešenih stručnih predloga koji blokiraju pregled. Ranija korisnikova odluka za s004 ostaje sprovedena. Vraćanje CS priključaka na s010 i nadcrta CS1 na s011 ispravlja odstupanja prethodnih crteža od originala. S006 i s012 ostaju izvorno nepotpuni; njihova dopuna nije izmišljena. Jezičke ispravke iz prve obrade, poput „Integration“, „komponenti“, „tri“ i „prikazan samo jedan“, zadržane su; nije menjana stručna vrednost izvornog teksta.

## Izlazi, poređenja i otisci

- [Prezentacioni PDF — 21 slajd](../../build/03_kola_srednjeg_stepena_integracije.pdf).
- [PDF beležaka — 21 strana](../../build/03_kola_srednjeg_stepena_integracije_beleske.pdf).
- [Uporedni pregled original / polazni prikaz / novo / beleške](../../build/redizajn/pregled/index.html).
- [Poređenje pre i posle ove dorade — šest reprezentativnih slajdova](../../build/dorada-2026-10-02/poredjenje-pre-posle.pdf): s002, s010, s011, s015, s018 i s021.
- [Cela prezentacija pre ove dorade](../../build/dorada-2026-10-02/pre-03_kola_srednjeg_stepena_integracije.pdf) i [arhiva tadašnjih izvora](../../build/dorada-2026-10-02/izvori-pre.tar.gz).
- [Prvobitno polazno stanje rekonstrukcije](pocetno_stanje.tar.gz), sačuvano van ignorisanog `build/`, i [prethodni izveštaj 2026-10-01](istorija/izvestaj-2026-10-01.md).
- [Manifest](manifest.json), [stvarne zavisnosti i izlazi izgradnje](izgradnja.json) i [pojedinačne potvrde pregleda](pregled.json).

| Resurs | SHA-256 |
|---|---|
| Originalni PDF | `5e68d267ca2f60c1ccdf073c2579fd64a4b05278955cc3d3f920cc54e123fd86` |
| Zamrznuti manifest etf-v1 | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |
| Manifest redizajna 03 | `043cfd60fc37b3776983018ddca3b715e03d99d8c679ea1e8de9df4306469213` |
| Zapis izgradnje | `f957be77aa44fd04114d1e4e17a3e34045ebb519a2dda162c805eec500feadab` |
| Potvrde pregleda | `1e48a859ed9e9d18a36713a219f3744f95d22c06130eda21ac0d8790de09cbac` |
| Prezentacioni PDF | `4bcf5f421b2d32586028a3683d572bbf8077ca9ac088927a3e76180722cec9b9` |
| PDF beležaka | `9c5fefeef69c1499565d9d03c32858d36752b94be9677bd17112fc9b1c46c641` |
| PDF pre ove dorade | `4b0df764040eb7b9f5c00b73d2cae5d3a4be62f3b32889a6455a6b8627be7c4a` |
| Arhiva polazne rekonstrukcije | `c811bbc07e38b5d35989ebd68889bcdb657b518e0b035fae2e502bbbc2547d15` |

## Sledeći korak

Korisnik pregleda predati PDF 03 i beleške. Status je **ceka_odobrenje**; odobrenje rezultata i dozvola početka 04 evidentiraju se zasebno, na osnovu stvarne korisnikove poruke. **04 nije započeto.** Predavanje 01 je odobreno, a rezultat 02 čeka zasebno prihvatanje.

Naredni agent čita ovaj izveštaj i centralnu evidenciju, proverava otiske i nastavlja samo od stvarno potrebne dorade. Analiza i pregled ove verzije 03 su završeni; ne ponavljaju se ako relevantni izvori, zavisnosti i beleške ostanu isti i korisnik ne traži novu izmenu. Promena poništava samo pogođene potvrde, uključujući beleške.
