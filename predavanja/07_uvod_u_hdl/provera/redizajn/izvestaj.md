# Izveštaj redizajna — 07 Uvod u HDL

## Status i obuhvat

Kontrolna tačka: **2026-10-03**, status **`u_radu`**. Izgled i nastavni tekst beležaka obrađeni su za svih **31 slajdova**. Originalni PDF, svih 31 izdvojenih originalnih slajdova, početni LaTeX prikaz, novi slajdovi i 31 A4 prikaz beležaka pojedinačno su pregledani. **Šest grupa izvornih stručnih pitanja ostaje otvoreno**; konačno prihvatanje predavanja još nije moguće po odeljku 10.3 plana.

Početak je izričito odobren korisnikovim nalogom, zabeleženim u [odlukama](odluke.md). Odobrenje rezultata, stručnih promena i početka 08 nije dato. Ranija rekonstrukcija nije potvrda ovog redizajna; njena evidencija nije prepisana.

Original ima 16 PDF strana sa po dva slajda, uz praznu donju polovinu poslednje strane. Prezentacija zadržava **31 stranu i tačan niz `07-s001`–`07-s031`**; nema brisanja, deljenja, spajanja, novih razdelnika, overlay strana ni automatskog smanjivanja. A4 PDF ima **31 stranu**, po jednu za svaki ID, sa prikazom slajda i nastavnim beleškama. Autor **prof. dr Lazar Saranovac** i školska godina **2021/22** sačuvani su prema originalu. Tema je konkretna zamrznuta **`etf-v1`**, izbor **B**; dodato je lokalno tamnocrveno isticanje `#A32638`, bez izmene zajedničkih izvora teme. Originalni PDF je bajtno nepromenjen.

## Pokrivenost i glavne promene

[Mapa pokrivenosti](pokrivenost.md) prati **138/138 elemenata: 116 izvornih i 22 proverljive dopune**. Svaki ima konkretno sidro na slajdu, u njegovim beleškama ili na oba mesta. Potvrda pokrivenosti znači da sadržaj ima odredište; sporna stručna tačnost se posebno označava kao `problem` u [pregledu](pregled.json). Nijedno otvoreno pitanje nije sakriveno potvrdom pokrivenosti.

- Slajdovi s002–s004 i s009: urednije stavke i grupisanje pojmova; potpuna dodatna objašnjenja u beleškama.
- s005–s008: pregledniji prikaz programabilnih matrica, komponenti i JEDEC primera, sa razdvojenim oznakama, pinovima i vođicama. Svih 352 prikazanih bita ostaje vidljivo; originalno zaglavlje je potpuno sačuvano.
- s010/s011/s027: čitljiviji raspored ABEL/VHDL koda po kolonama, kontrolisani prelomi i razmaci. Promene u ABEL izvorima su isključivo razmaci i novi redovi; test vektori, uslovi i prioriteti su isti. Dugi naslovi/komentari uklonjeni iz projekcionog prikaza s010/s011 u potpunosti su objašnjeni u pripadajućim beleškama.
- s012/s018: precrtani CAD, VLSI i razvojni tokovi sa jasnim blokovima, nazivima, strelicama i povratnim putanjama.
- s013–s020: vidljive ključne definicije i rezultati; puni uklonjeni pasusi i primeri preneti u beleške. Izvorna istorijska poređenja zadržana su u kontekstu predavanja, bez proizvoljnog ažuriranja stručnih tvrdnji.
- s021–s026 i s028–s031: odvojeni tekst, šeme, kod, formule i tabele; povećani razmaci i jasnije poravnanje. Kod i sporne izvorne tvrdnje sačuvani su do odluke.

Precrtani/uređeni vektorski crteži: **s005, s006, s007, s011, s012, s018, s021, s022 i s029**. Na s007 očuvana je puna PAL organizacija: 32 kolone, 64 reda, osam grupa, sedam proizvoda za ILI kolo i zaseban proizvod za omogućavanje izlaza, svih 20 brojeva pinova i šest povratnih IO putanja. Pojedinačni redni indeksi objedinjeni su u vidljive raspone uz potpuno objašnjenje numeracije u beleškama. Vodovi ka različitim ILI ulazima odvojeni su; spoljašnji vod I1 odmaknut je od oznake O1, a I10 od O8. Na s021/s029 grananja imaju tačke spoja, ukrštanja bez spoja nemaju tačku i vodovi ne prelaze preko kapija.

Reprezentativna poređenja original/pre/posle/beleške: [PAL s007](../../build/redizajn/pregled/index.html#07-s007), [CAD s012](../../build/redizajn/pregled/index.html#07-s012), [tekst s013](../../build/redizajn/pregled/index.html#07-s013), [šema i kod s021](../../build/redizajn/pregled/index.html#07-s021), [SR sprega s029](../../build/redizajn/pregled/index.html#07-s029).

## Beleške i preneti sadržaj

Beleške su jedan LaTeX izvor po slajdu u `beleske/sNNN.tex`, sa istim ID-jem i nevidljivim sidrima. Sadrže **samo dodatni nastavni tekst**, bez istorije redizajna, poređenja verzija, odobrenja, rezultata provera, izvornog broja PDF strane ili obaveznih uredničkih naslova. Ključne definicije, ilustracije, rezultati i uslovi ostaju na slajdovima. s001 ima samo vezu sa ID-jem, jer nema dodatnog sadržaja.

Naredna tabela navodi detalje objašnjene u beleškama; sažeti oslonci mogu ostati vidljivi. Tačna razlika između prenetog sadržaja i dopune, odredišta i dokazi nalaze se u [evidenciji beležaka](evidencija_beleski.json), [inventaru](inventar.json) i [mapi](pokrivenost.json), bez druge kopije teksta beležaka.

| ID | Dodatno objašnjen izvorni sadržaj |
|---|---|
| 07-s002 | Električna šema, realizacija, sinteza/simulacija i Schematic Capture; CAD, EDA/ECAD, PCB sa punim nazivima. Sličnost sa programskim jezicima, objektni i konkurentni koncepti; opis hardvera naspram posla procesora. |
| 07-s003 | Računar i različiti programi ne menjaju fizičke veze; izuzimanje memorija iz poređenja. Prelazak sa malog/srednjeg na viši stepen integracije i ograničenje teme na kombinacione mreže. |
| 07-s005 | Šta učestvuje u Y, koliko proizvoda m postoji, koliko ulaza ima I kolo. Šta učestvuje u F, koliko članova i ulaza ima ILI kolo. |
| 07-s007 | Indeksi kolona 0–31; svih 64 rednih indeksa 0–63 po osam grupa; redni indeksi u beleškama, rasponi vidljivi. I1–I10, O1/O8, IO2–IO7 i svi brojevi pinova; namenski ulazi/izlazi i deljeni IO. Navodnici uz „bilo koja“ i primer jednostavne programabilne komponente. |
| 07-s009 | Početak razvoja 80-ih radi lakog generisanja, simulacije, verifikacije i dokumentovanosti čitljivog koda. Razvoj složenijih jezika, prenosivost, ponovno korišćenje, simulacija, sinteza i analiza. |
| 07-s010 | Naslov and1 o instanciranju/hijerarhiji i komentar o pinovima šematskog simbola/interfejsa. Naslov Dual Priority Encoder; komentari Input and output pins i Set definitions. |
| 07-s011 | Naslov modula „12 to 4 multiplexer“. |
| 07-s013 | 1. Jezik za simulaciono modelovanje: nivo detalja, gejtovi do mikroprocesora/čipova, porast/pad/kašnjenja/funkcija. Modeli kao gradivni blokovi većih kola kroz šeme, blok dijagrame i VHDL opis sistema. |
| 07-s014 | 2. Unos dizajna za sintezu/simulaciju; Pascal/C/C++, strukturiran dizajn i kontrola/podaci. Istovremeni događaji i rad hardvera; iskustvo sa PALASM/ABEL/CUPL naspram softverskih jezika. 3. Testbench: specifikacija performansi, pobude/očekivani izlazi tokom vremena; nedovoljno korišćena mogućnost, paralelni razvoj. |
| 07-s015 | 4. Netlist Language: visok nivo unosa i niskonivojska komunikacija, strukturalni opis, zamena/dopuna EDIF-a. 5. Standard: očuvanje koncepta kroz nove alate, savremeni alati i baza iskustva drugih inženjera. Veliki jezik, lak početak prema potrebama, postepeno napredne funkcije. |
| 07-s016 | Specifikacija visokog nivoa, performanse/interfejsi, tim, top-down, testbench prihvatanja i prosleđivanje deklaracija/zahteva. Unos detalja, ploča/funkcionalne šeme/VHDL; sintetizabilan stil; kombinacija drugih metoda i alata. |
| 07-s017 | Simulacija funkcionalnih/vremenskih zahteva: prethodni testbench, opis za sintezu i model posle sinteze. Dokumentacija, struktura/konfiguracije i izvorni iskaz o DoD-u i podizvođačima u istorijskom kontekstu predavanja. Šeme ostaju korisne, posebno blok dijagrami; kombinovanje sa VHDL-om. |
| 07-s018 | Unos VHDL/šeme/blok dijagrami i putanje simulacija/sinteza/uređaj. Razvoj testa prema zahtevima; tekst ili grafički talasni oblici kao izvor testbench-a. Model posle rutiranja; dobavljač uređaja/treća strana, generisani VHDL sa vremenskim napomenama i sistemska simulacija. |
| 07-s019 | Verilog simulacija/sinteza; Gateway sredinom 1980-ih, de fakto ASIC biblioteke i istorijska prednost dostupnosti. VITAL: standardni zapis kašnjenja, izrada VHDL modela iz Verilog biblioteka. PLI/Open Verilog International: izvan HDL-a, C i brzina/teško izražive funkcije. VHDL/IEEE1076, konfiguracije/biblioteke/veliki projekti; funkcionalna sličnost, Verilog-C i VHDL-Pascal/Ada. |
| 07-s020 | Prelazak sa jednog na drugi; smisao rasprave o karakteristikama i slobodno vreme. |

Ostale beleške razjašnjavaju samo potrebne oznake, rad matrica, pinove i testove, topologiju kola, međukorake punog sabiranja, signale/promеnljive, delta cikluse i odnos liste osetljivosti i WAIT naredbe. Dopune su proverene prema originalnom gradivu, računskim rezultatima ili navedenoj primarnoj dokumentaciji. Beleške s027/s028/s031 ne predstavljaju neispravne izvorne programe kao provereno ispravne realizacije.

## Jezičke ispravke i stručne odluke

| ID | Izvorni zapis → novi zapis | Razlog |
|---|---|---|
| s006 | `Fild Programmable Gate Array` → `Field Programmable Gate Array` | Ispravljena očigledna slovna greška u originalu i prethodnom LaTeX-u, bez promene značenja naziva FPGA. |
| s019, beleške | `Gatevai Design Automation` → `Gateway Design Automation` | Ispravljena slovna greška u nazivu kompanije; naziv potvrđuje [Computer History Museum](https://computerhistory.org/profile/philip-moorby/). |
| s002–s020, beleške | Razmaknute reči i skraćenice oštećene izvlačenjem teksta; pravopisna interpunkcija | Puni nastavni tekst prepisan prema stvarnim PDF prikazima, bez prenošenja OCR razmaka i bez promene stručnog smisla. |

Stručni predlozi **nisu primenjeni**. Konkretni kodovi, dokazi, preporuka i tražena odluka nalaze se u [otvorenim pitanjima](otvorena_pitanja.md):

| ID | Predmet odluke |
|---|---|
| s006 | Razdvajanje CPLD/FPGA grupa i pun naziv EEPROM. |
| s023 | Nedostajuća otvorena zagrada u `[SIGNAL]`. |
| s027 | Neispravan VHDL prioritetni enkoder: signalne zastavice izazivaju delta oscilaciju. Pripremljen ceo kod sa lokalnim promenljivama; 256 kombinacija prolazi. |
| s028 | Oba BIT literala i smer porta B koji se dodeljuje i čita. |
| s030 | Preciziranje signalne dodele naspram trenutne dodele promenljivoj. |
| s031 | Dva BIT literala i odluka da li treći proces ostaje primer zadržavanja stanja ili postaje potpuni kombinacioni MUX. |

## Provere i ograničenja

Stvarne komande i izlazni kodovi sačuvani su u [provere.txt](provere.txt):

| Komanda | Rezultat |
|---|---|
| `make -C predavanja all LECTURE=07_uvod_u_hdl` | Izlaz 0; 31 prezentaciona strana. |
| `make -C predavanja notes LECTURE=07_uvod_u_hdl` | Izlaz 0; 31 A4 strana sa tačnim ID-jevima. |
| `make -C predavanja review LECTURE=07_uvod_u_hdl` | Izlaz 0; original/pre/posle/beleške za svih 31 ID-jeva. |
| `python3 predavanja/07_uvod_u_hdl/kodovi/provera_logike.py` | Izlaz 0; 352 JEDEC bita, četiri AND testa, 256 ABEL prioriteta, 12 MUX testova, osam sabiranja, osam kombinacija šeme s021, isti dataflow izrazi, četiri SR koraka i reprodukovana izvorna oscilacija. |
| `make -C predavanja check LECTURE=07_uvod_u_hdl` | **NEZAVRŠENO**, izlaz `make` 2 / provera 1; samo sedam nepotvrđenih stručnih kategorija na šest ID-jeva. |

Jedina prijavljena ograničenja `check` su s006/tekst, s006/crtezi, s023/kod, s027/kod, s028/kod, s030/tekst i s031/kod. **Nema prijavljenih problema broja/redosleda/ID-jeva, pokrivenosti, nedostajućih resursa ili zastarelih potvrda.** Izgradnja oba PDF-a nema greške, prekoračenja prostora, upozorenja o fontovima, nedostajuće znakove ili nerešene reference. Automatske provere nisu zamenile stvarni pregled.

Svih **31/31 slajdova i 31/31 beležaka vizuelno je pregledano** u punoj veličini. Potvrde su vezane za aktuelne izvore i renderovane stranice. **25 ID-jeva potpuno je potvrđeno; šest ima nerešene stručne kategorije.** Beleške su pregledane zbog potpunosti prenetih detalja, upotrebljivosti u izlaganju, stručne tačnosti, odsustva nepotrebnog ponavljanja i uredničke evidencije.

Dodatni stvarni GHDL dokazi su u [hdl_dokazi.txt](hdl_dokazi.txt). Ispravni kompletni izvorni primeri s021, s024 i s029 prolaze analizu sa `--std=08`. Izvorne greške s027/s028/s031 stvarno su reprodukovane. [Predlog s027](predlozi/s027_prioritet.vhd) zasebno je simuliran na svih 256 kombinacija; predlozi s028 i izolovani literali s031 prolaze sintaksnu analizu. Ovi rezultati ne daju korisnikovo odobrenje za primenu. Metasintaksni obrasci s023/s030 i nepotpuni isečci s025/s026 nisu predstavljeni kao samostalni izvršivi programi. Alati i zajednička tema nisu menjani.

Početni prikaz, njegovi izvori i original sačuvani su u [arhivi](pocetni_prikaz.tar.gz); **105 fajlova** bajtno je upoređeno sa početnim snapshotom. Digest početnog stanja iz manifesta je `3df9ccb56923e6b9c77bafc2a277be4d0484e836e522ef808fc86098fd62f92f`.

## Isporuka i nastavak

- [Prezentacioni PDF](../../build/07_uvod_u_hdl.pdf).
- [A4 PDF beležaka](../../build/07_uvod_u_hdl_beleske.pdf).
- [Uporedni pregled svih ID-jeva](../../build/redizajn/pregled/index.html).
- [Glavni LaTeX izvor](../../07_uvod_u_hdl.tex) i [beleške po slajdu](../../beleske/).
- [Predlozi koji čekaju odluku](otvorena_pitanja.md).

Izlazi u `build/` se ne verzionišu. Ponovna izgradnja radi se gornjim komandama za **samo 07**. Ako je početni prikaz obrisan iz `build/`, prvo vratiti arhivu:

```bash
mkdir -p predavanja/07_uvod_u_hdl/build/redizajn
tar -xzf predavanja/07_uvod_u_hdl/provera/redizajn/pocetni_prikaz.tar.gz -C predavanja/07_uvod_u_hdl/build/redizajn
make -C predavanja all LECTURE=07_uvod_u_hdl
make -C predavanja notes LECTURE=07_uvod_u_hdl
make -C predavanja review LECTURE=07_uvod_u_hdl
make -C predavanja check LECTURE=07_uvod_u_hdl
```

**Poslednji završen korak:** raspored, beleške, pokrivenost, pojedinačni pregled i kontrolna tačka. **Sledeća dozvoljena radnja:** korisnik odlučuje o šest konkretnih grupa stručnih predloga za ovu verziju 07. Zatim primeniti samo odobrene promene, dopuniti pogođene beleške, uskladiti računska očekivanja sa dokazima i obnoviti pogođene prikaze/potvrde. Ponoviti `notes`, `review`, `check`; tek tada može `ceka_odobrenje`. Nepogođene aktuelne potvrde koriste se bez ponavljanja završene analize. Svaka izmena beležaka poništava njihove pogođene potvrde. Prelazak na 08 traži zasebnu stvarnu korisnikovu poruku.

## Kontrolne sume ove verzije

- [Originalni PDF](<../../../07 Uvod u HDL.pdf>): `321ce3dd5052f7eab982430e29715feb8044b6f69e74a458a18f1356ddbbc6cc`.
- [Manifest teme](<../../../_zajednicko/etf-v1/manifest.json>): `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41`.
- [Manifest redizajna](<manifest.json>): `1d9268712a2860efde2a574e956cdcd0adcce58ed7354de16cdabe3dbd6108e3`.
- [Izgradnja](<izgradnja.json>): `ea1669564881126e3d9568d66d931bfcb7602cbf1b8d9dbf71c5ee26061123cf`.
- [Potvrde pregleda](<pregled.json>): `1dcfc8b1fcac77d1948afaacd10c3bb49e2d1107fbcba32342025e79e3238be0`.
- [Inventar](<inventar.json>): `fa61252f7532538d141ec0031ce245ccd63fbf976477c13dd53fb2650c6a72c5`.
- [Mapa pokrivenosti](<pokrivenost.json>): `03ebb0377c4afefa3d2d6823c976ee65862d007aecfca6077d3e7d63f376618a`.
- [Poreklo i dokazi beležaka](<evidencija_beleski.json>): `bd0d9c77b5b6433ead872621ec9e66fd858a655792fb3a586a5e72a3583a8869`.
- [HDL dokazi](<hdl_dokazi.txt>): `089614184c069d0fb7a448c70aab2a0472bed65df9fc9464f6eba43ed893a60e`.
- [Zapis provera](<provere.txt>): `40e5357f73c8f61cf25eb0ebf01f224f1ed906ce745e6cf7fb6085c2f24c71a4`.
- [Početni prikaz](<pocetni_prikaz.tar.gz>): `7113a2a0971f6446ae2f3885d08719b53e9d0d474c8f6b8690d3807352aeac5e`.
- [Prezentacioni PDF](<../../build/07_uvod_u_hdl.pdf>): `371ad77b2067be17691c875d56fade638fa8fd36fa9c2e546f9da3dbf96e404a`.
- [PDF beležaka](<../../build/07_uvod_u_hdl_beleske.pdf>): `47b396e99f8fa39e44f06b878cc9ce3ae3af06117848c6b521de53c6dd4d5a91`.
