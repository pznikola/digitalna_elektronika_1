# Predavanje 02 — SystemVerilog primeri

**Status: `ceka_odobrenje` · 2026-10-09.** Korisnik je odobrio izradu primera uz s021/s022/s051, oba tipa testbench-a, nazive i raspored. Novi rezultat čeka njegov pregled. Prethodno prihvatanje od 2026-10-05 odnosi se na arhiviranu verziju sa 62 strane; [zapis odobrenja](odobrenje_rezultata.json) ostaje neizmenjen.

## Obuhvat i prikaz

Prezentacija i beleške imaju **65 strana**: 54 originala + osam ranije odobrenih nastavaka + tri RTL dodatka. Svi prethodni ID-jevi i njihov međusobni redosled ostaju isti. Originalni PDF, istorijska mapa, zamrznuta tema etf-v1, autorstvo i godina 2021/22 nisu menjani. U katalogu ostaje 620 originalnih slajdova; sa postojećim nastavcima 02/03 i ovim dodacima ukupno je 634 projektovanih strana.

| Izabrani ID | Novi ID / strana | Dizajn i oba TB-a |
|---|---|---|
| 02-s021 | 02-s021-rtl01 / 25 | [mreza_zp](../../kodovi/primeri_sv/02-s021/README.md) — zbir proizvoda, tri I gejta i završni ILI |
| 02-s022 | 02-s022-rtl01 / 27 | [mreza_pz](../../kodovi/primeri_sv/02-s022/README.md) — proizvod pet potpunih zbirova |
| 02-s051 | 02-s051-rtl01 / 62 | [mreza_sa_hazardom](../../kodovi/primeri_sv/02-s051/README.md) — simulacioni model sa parametrom T |

Svaki novi slajd prikazuje ceo izvršivi izvor direktno preko `listings`: kod je levo, objašnjenje i klikabilni nazivi oba TB-a desno. Font koda je 9 pt; brojevi odgovaraju stvarnim linijama. Na s021/s022 par dodela invertora prikazan je u jednoj naredbi `assign`, uz sačuvanu topologiju. Prikazano je svih 16/18/16 linija izvora. Nema pune putanje dizajna iznad koda; oznake su **Testbench:** i **Testbench bez provere:**. Ne menja se monospaced font niti zajednička tema.

[Pregled novog s021](../../build/redizajn/pregled/novi/p-25.png), [s022](../../build/redizajn/pregled/novi/p-27.png), [s051](../../build/redizajn/pregled/novi/p-62.png). Šeme ranijih slajdova nisu precrtavane. Nema novih jezičkih ili stručnih ispravki originalnog gradiva.

## Model i testbench-ovi

S021 i s022 prate ulazne parove invertora i obe konkretne mreže, sa istim ulazima C, B, A i izlazom F. Nezavisna očekivanja iz funkcionalne tabele proveravaju svih osam binarnih kombinacija: F=1 za 011, 101 i 110. Posmatranje međusignala omogućeno je u VCD-u.

S051 zadržava izričitu pretpostavku originalnog slajda: kašnjenje ima samo invertor, a ostali gejtovi su idealno brzi. Za C=A=1 i pad B, BA odmah pada na 0, dok C·barB postaje 1 posle T. U fizičkom kolu svi gejtovi imaju kašnjenje; ovaj model izdvaja mehanizam hazarda. Korisnik je prihvatio objašnjenje porukom „onda u redu“. Na slajdu je vidljiva napomena da `assign #(T)` služi simulacionom primeru i ne zadaje fizička kašnjenja pri realnom RTL projektovanju.

Automatski TB hazarda proverava stacionarnu tabelu, lažnu nulu i oporavak dve instance: T=5 ns i T=7 ns. [Stvarni VCD zapisi oba simulatora](vcd_lazna_nula.json) potvrđuju oba trajanja. Studentski TB sa T=5 ns daje prvu lažnu nulu od **20 do 25 ns**. [Vremenski prikaz iz njegovog VCD-a](../../build/redizajn/systemverilog/s051_lazna_nula.png).

Studentski TB-ovi sadrže samo jednostavan uzastopni niz dodela, čekanja, VCD i završetak. Nemaju očekivane rezultate, assert, fatal ili PASS. Student može promeniti ulaze, trajanja i T i ponovo pokrenuti `run_student`; automatske provere ostaju u odvojenom TB-u. Linkovi u PDF-u prate GitHub putanje kao u vežbama; lokalni fajlovi i komande su dostupni preko README-a svakog primera.

## Beleške i pokrivenost

Dodate su beleške samo za tri nova ID-ja. Objašnjavaju paralelno značenje više dodela u `assign`, posmatranje međusignala, redove u kojima potpuni zbir daje nulu i vremenski tok hazarda. Ne sadrže istoriju rada, odluke ili rezultate provera. Nijedan detalj sa ranijih slajdova nije uklonjen ili dodatno premešten u beleške.

[Mapa pokrivenosti](pokrivenost.md) ima **241/241 potvrđen element**: 231 raniji + deset elemenata dopuna. **105 elemenata** ima odredište u beleškama. Nastavno poreklo, razlika dopuna i izvornog materijala, stvarne odluke i dokazi ostaju u [evidenciji beležaka](evidencija_beleski.json) i [odlukama](odluke.md). Tekst beležaka postoji samo u odgovarajućim `.tex` fajlovima.

## Pregled i provere

Pregledani su originalni i aktuelni s021/s022/s051, njihove formule i šeme, svi izvori novih dizajna i oba TB-a. Stvarno su pregledani tri nova projekciona slajda i njihove cele A4 strane: sadržaj, oznake, brojevi linija, linkovi, razmaci i nastavna objašnjenja. Nema preklapanja, odsecanja ili izostavljenog koda; oba LaTeX loga nemaju greške, upozorenja ili prekoračenja prostora.

[Poređenje sa prethodnom odobrenom verzijom](poredjenje_rtl_dodataka.json) potvrđuje **62/62 identična projekciona prikaza i 62/62 identična A4 tela**. Izvori njihovih slajdova i beležaka takođe su isti. Na 38 pomerenih A4 strana promenjen je samo broj u podnožju; sva promenjena podnožja pregledana su [zajedno](../../build/redizajn/pregled/pregled_podnozja.png). Prethodni stvarni sadržinski pregled ostaje osnova za neizmenjene slajdove; nove potvrde beleže ovu proveru razlike, bez tvrdnje da je ponovljena njihova cela analiza.

Sve sledeće komande završavaju kodom 0:

```sh
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza notes
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza review
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza check-sv HDL_LOCAL=1
make -C predavanja LECTURE=02_sinteza_kombinacionih_mreza check
make -C predavanja test
make -C predavanja test-redizajn
```

**check: PROVERENO.** Svi ID-jevi, njihov redosled, beleške, odredišta sadržaja i trenutne potvrde su usklađeni. Postojeća nezavisna računska provera prolazi. **12 simulacija** (tri primera × dva TB-a × dva simulatora) završava uspešno; automatski TB-ovi daju PASS, studentski završavaju i daju VCD. Simulacije su izvršene lokalno u instaliranim Verilator-u i Icarus-u; Docker pokretanje nije korišćeno u ovoj sesiji. Verzije su u zapisima svake simulacije.

**49 regresionih testova** i integraciona proba prolaze. [Tri namerno pogrešne realizacije](negativne_provere_rtl.json), proverene u privremenim kopijama, automatski TB-ovi odbijaju: pogrešan polaritet proizvoda, OR umesto završnog AND i uklonjeno kašnjenje invertora.

Alati podržavaju odobrene RTL dodatke odvojeno od podela originala, njihove beleške i uporedni kontekst, zavisnosti dizajna/pomoćnih modula/oba TB-a i važenje simulacionih potvrda. Uveden je `check-sv`; detalji su u [tehničkom uputstvu](../../../_alati/REDIZAJN.md). Izmena izvora, TB-a, VCD-a ili simulatora poništava odgovarajući dokaz. Provere ne daju odobrenje rezultata.

[Notes log](../../build/redizajn/rtl-primeri-2026-10-09/notes.log), [review](../../build/redizajn/rtl-primeri-2026-10-09/review.log), [check-sv](../../build/redizajn/rtl-primeri-2026-10-09/check-sv.log), [check](../../build/redizajn/rtl-primeri-2026-10-09/check.log), [regresioni testovi](../../build/redizajn/rtl-primeri-2026-10-09/tests.log), [integraciona proba](../../build/redizajn/rtl-primeri-2026-10-09/integration.log).

## Isporuka i sledeći korak

- [Prezentacija — 65 slajdova](../../build/02_sinteza_kombinacionih_mreza.pdf); RTL dodaci su na stranama **25, 27 i 62**.
- [PDF beležaka — 65 A4 strana](../../build/02_sinteza_kombinacionih_mreza_beleske.pdf).
- [Uporedni pregled](../../build/redizajn/pregled/index.html).

Nema otvorenih stručnih pitanja. Sledeći korak je korisnikov pregled ovih dodataka; on određuje sledeće primere. Nalog i odluke o konkretnim izmenama ne predstavljaju prihvatanje cele nove isporuke niti menjaju odobrenja drugih predavanja.

Prethodna evidencija, izvori, alati i [izveštaj](istorija/pre-rtl-primera-2026-10-09/izvestaj.md) sačuvani su u `istorija/pre-rtl-primera-2026-10-09/`; prihvaćeni izlazi su u `build/redizajn/pre-rtl-primera-2026-10-09/`. Generisani izlazi, logovi i simulacije ostaju u ignorisanom `build/`; obnavljaju se navedenim komandama.

## SHA-256 pregledane verzije

| Resurs | Otisak |
|---|---|
| Originalni PDF | `f631914c9f32a0472f4fa3af11115abaadb9316dfcf6f1528cd91ef4d28868f4` |
| Istorijska mapa | `b2c8e07fa123a40da68c8b89b1b1c6ce88112e90c7417792cdec341d60136ca2` |
| Manifest | `250a3e227875e5a2608041b74c9fdc33a56b22ae80d5e447e5cbaee19311aa83` |
| Odobrenje RTL dodataka | `535888756f8b93c35be3fc7dc41ffe3b60f140566a374dc8d7d8eaf8449b02c5` |
| Prethodno odobrenje rezultata | `d66d9546852d11ec4a54b7c6a327eaf20de4c50aca3a88f8e01bab3651bcb790` |
| Manifest teme | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |
| Prezentacioni PDF | `c31175c869e2cde5dfbcbc9687fd6501f4102a31927e58f9d54163c661fe7ed6` |
| PDF beležaka | `e6edb257294d9242b5ef60eac401fdfe4c520f56a6925fd472ac6fa9997951c2` |
| Zapis izgradnje | `64afb1d09d951160b423c8bf748cf7e13d1b2d750ed21af11af2af768aa9f6a3` |
| Potvrde pregleda | `43baddbbe55449c58440050e5766f82ee7aa9854a8cfb027c33e96e228f3fa87` |
| Evidencija beležaka | `dbf9365b3f3d65905136f57fecabeb8b2b5112b159c33c8b6d722be08f03106a` |
| Poređenje 62 prethodna para | `9c45b2a33f96efcc982e51fd564c50ca1e3223ddfa787199b78bbae45ee599e1` |
| VCD dokaz hazarda | `39eac3eeeb680cadab28a03f68ab62f92141a6390b6e6804c4c8c1c138155480` |
