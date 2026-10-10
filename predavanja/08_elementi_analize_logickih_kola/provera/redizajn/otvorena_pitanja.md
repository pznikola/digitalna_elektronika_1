# Predavanje 08 — stručni predlozi za odluku

Datum: 2026-10-03. Status: **12 grupa predloga čeka izričito korisnikovo odobrenje**. Ovo nisu komentari za projektovane slajdove ili beleške predavača. Izgled i nastavni tekst su obrađeni; zapisi navedeni ispod još nisu stručno ispravljeni.

[Prezentacija](../../build/08_elementi_analize_logickih_kola.pdf) · [Beleške](../../build/08_elementi_analize_logickih_kola_beleske.pdf) · [Original/pre/posle/beleške](../../build/redizajn/pregled/index.html) · [Izveštaj](izvestaj.md).

Svaki broj označava stabilni ID `08-sNNN`. Originalna PDF strana je `(NNN+1)//2`: neparni slajd je gornji, parni donji. Predlozi se odnose i na odgovarajuće jednačine u beleškama. Nijedan predlog nije automatski odobren; moguće je prihvatiti sve, određene oznake P01–P12 ili tražiti drugačiji zapis. Odobrenje ovih ispravki, prihvatanje cele prezentacije i dozvola za 09_1 tri su odvojene odluke.

## P01 — s011/s012: pretpostavka raspodele i pragovi

**Izvor:** s011 tvrdi da su verovatnoće logičke nule i jedinice jednake u digitalnom sistemu. To zavisi od signala i njegove upotrebe; nije opšte svojstvo. S012 najpre dopušta negativne ΔL/ΔH, a zatim kaže da je VIH „uvek” iznad i VIL „uvek” ispod polovine napajanja, pa odmah daje suprotan primer.

**Predlog s011:** „U ovom razmatranju pretpostavimo podjednaku verovatnoću pojave logičkih jedinica i nula.” Time tvrdnja ostaje vidljiva kao pretpostavka.

**Predlog s012:** „ΔL i ΔH ne moraju biti pozitivni. Zato VIH ne mora biti veće, niti VIL manje od polovine napona napajanja. Kod logičkih kola sa bipolarnim tranzistorima često je VIH manje od polovine napona napajanja.” Sačuvati definicije pragova i tabelu. Primer VCC=5 V, VIH=2 V već opovrgava „uvek”.

## P02 — s023: Tejlorov razvoj

**Izvor:** uz drugi izvod nedostaje `1/2!`, a linearno odsečen razvoj zapisan je kao tačna jednakost.

**Predlog:**

\[
f(V_{i1}+n)=f(V_{i1})+n f'(V_{i1})+\frac{n^2}{2!}f''(V_{i1})+\cdots,
\qquad f(V_{i1}+n)\approx f(V_{i1})+na,\quad a=f'(V_{i1}).
\]

Na slajdu navesti da je druga relacija aproksimacija za dovoljno mali šum i lokalno glatku karakteristiku. Primer `f(x)=x²` neposredno proverava koeficijent drugog reda.

## P03 — s030: najgori slučaj izlazne struje

**Izvor:** „minimalno IOHmax”; IOH je u prikazanoj referenci negativna struja, pa „minimalno” nije jednoznačno.

**Predlog:** „Najgori slučaj određujemo za najmanju garantovanu sposobnost davanja izlazne struje, odnosno najmanju dozvoljenu apsolutnu vrednost IOHmax uz zahtevani VOHmin.” Sačuvati izraze disipacije i objašnjenje referentnog smera. Ne menjati tabelarne vrednosti.

## P04 — s032: faktor grananja

**Izvor:** u NL imenilac nema apsolutnu vrednost, iako je IIL na s028 negativna. Izvorne vrednosti daju −40 umesto kapaciteta 40 ulaza.

**Predlog:**

\[
N_L=\left\lfloor\frac{|I_{OL\max}|}{|I_{IL\max}|}\right\rfloor,\qquad
N_H=\left\lfloor\frac{|I_{OH\max}|}{|I_{IH\max}|}\right\rfloor,\qquad N=\min(N_L,N_H).
\]

Objasniti da je N najveći dozvoljeni ceo broj istovetnih ulaza, uz garantovane najgore vrednosti. Za navedene struje: NL=40, NH=20, N=20. Topologija šeme ostaje ista.

## P05 — s042: jednačina kondenzatora

**Izvor:** `iC=duC/dt`, bez kapacitivnosti.

**Predlog:** `iC(t)=C·duC(t)/dt`, za konstantno C i prikazane usaglašene smerove. Ostale jednačine ostaju. Dimenzije: F·V/s=A; isto korišćenje faktora C već postoji u narednom izvođenju.

## P06 — s043: struja otpornika i stacionarno stanje RC kola

**Izvor:** `(uC−uo)/R`, iako su u ovoj vezi `uo=uC`; sledeći izraz `(uC−U0)/R` ima obrnut znak za označeni smer struje. Intuitivni pasus dopušta da napon kondenzatora pređe preko U0, pa se vrati. U ovom pasivnom RC kolu pri konstantnoj pobudi odziv je monoton.

**Predlog vidljivog izraza:**

\[
i_R(t)=i_C(t)=\frac{u_i(t)-u_C(t)}R,
\qquad \lim_{u_C\to U_0}i_R=\lim_{u_C\to U_0}\frac{U_0-u_C}R=0.
\]

**Predlog celog intuitivnog objašnjenja u beleškama:** „Pre promene ulazni napon U0 smatra se dovoljno dugo prisutnim. Ako je napon kondenzatora manji od U0, struja ga puni; ako je veći, struja suprotnog smera ga prazni. U oba slučaja razlika napona eksponencijalno opada, bez prelaska preko U0. U idealnom modelu napon teži U0 asimptotski, a struja teži nuli. U stacionarnom stanju važe iC=0 i uC=U0.” Sačuvati objašnjenje da je beskonačno vreme idealizacija dovoljnog prethodnog trajanja.

Sadašnje beleške prenose i izvorni problematični intuitivni argument, sa jezičkim ispravkama. On nije prećutno uklonjen ili proglašen tačnim. Predlog se odobrava kao celina: znak, izrazi i objašnjenje monotonosti.

## P07 — s047/s048/s055/s056/s058/s060/s061/s066/s067: dosledni indeksi

**Izvor:** mešanje slova `o`, velikog `O` i cifre `0`, kao i `C/c`, za iste veličine.

**Predlog:** izlazni napon svuda označiti `u_o`, početnu konstantnu vrednost `U_0`, napon i struju kondenzatora `u_C`, `i_C`, a struju otpornika `i_R`. Sačuvati različite fizičke veličine; ne vršiti slepu globalnu zamenu. Na s047/s048 i u amplitudi odziva s056 `U_o` postaje `U_0`; na s055/s058/s060/s061/s066 izlazno `u_0` postaje `u_o`. Na šemi s067 izlazno `u_O(t)` uskladiti sa `u_o(t)` u jednačinama. Proveriti iste oznake u njihovim beleškama.

Na s058 u ponovljenom opštem obrascu u beleškama početni trenutak `t_0⁺` uskladiti sa `t_1⁺`, kao u prvom obrascu. **Ne ispravljati namerno pogrešan postupak s058 i njegovo `uo=VOL`**: to je nastavni primer pogrešnog izbora intervala, razrešen na s059/s061.

## P08 — s054: integrali, početni uslov i uslov aproksimacije

**Izvor:** integrali nemaju diferencijal; početni uslov nije naveden, a aproksimacija nije ograničena uslovom važenja.

**Predlog:** u beleškama dati tačnu vezu

\[
u_C(t)=u_C(t_0)+\frac1C\int_{t_0}^{t}i_C(s)\,ds.
\]

Na slajdu, uz postojeći tok izvođenja, prikazati

\[
i_C\approx\frac{u_i}R,\qquad
u_o(t)\approx\frac1{RC}\int_{t_0}^{t}u_i(s)\,ds,
\]

uz vidljive uslove `uo(t0)=0` i zanemarljiv `uo` u odnosu na `ui` tokom posmatranog intervala. Beleške objašnjavaju i slučaj nenultog početnog napona: u aproksimaciji se integralu dodaje `uo(t0)`. Za sinusoidalnu analizu integratorski režim odgovara `ωRC≫1`; za početak skoka aproksimacija važi na dovoljno kratkom intervalu. Šema i crtež ostaju.

## P09 — s056: izlaz diferencijatora i aproksimacija

**Izvor:** završno `ui=uR`, iako je u šemi `uo=uR`.

**Predlog završnog reda:**

\[
u_o(t)=u_R(t)=Ri_R(t)\approx RC\frac{du_i(t)}{dt}.
\]

Uz približni rezultat jasno navesti režim `ωRC≪1`, odnosno promene ulaza spore u odnosu na RC. Aproksimaciju ne primenjivati na samu idealnu skokovitu ivicu. Egzaktan eksponencijalni odziv na skok ostaje prikazan iznad i nije uslovljen ovom aproksimacijom.

## P10 — s059: dva međukoraka superpozicije

**Izvor:** `uo=uo1+uo1` umesto sabiranja dva različita odziva; potom `VOH−(VOH+VOL)` umesto `VOH−(VOH−VOL)`.

**Predlog za t≥t2:**

\[
u_o=u_{o1}+u_{o2},
\]
\[
u_o=V_{OH}-(V_{OH}-V_{OL})+(V_{OH}-V_{OL})\left(e^{-(t-t_2)/\tau}-e^{-(t-t_1)/\tau}\right).
\]

Sačuvati postojeći ispravan završni izraz

\[
u_o=V_{OL}+(V_{OH}-V_{OL})(1-e^{-(t_2-t_1)/\tau})e^{-(t-t_2)/\tau}.
\]

Provera koristi nenulto VOL, tako da se greška ne sakrije. Superpozicija i postupak po intervalima sa s061 daju isti ispravan rezultat.

## P11 — s064: kontinuitet struje kalema

**Izvor:** „Da bi se struja kroz induktivnost promenila potreban je beskonačno veliki napon”. To bi isključilo i običnu postepenu promenu.

**Predlog:** „Da bi se struja kroz induktivnost trenutno promenila, potreban je beskonačno veliki napon.” Ostaje `uL=L·diL/dt`; konačan napon daje konačnu brzinu promene. Šema i stacionarni uslovi ostaju.

## P12 — s067: nenulto početno stanje kompenzovanog razdelnika

**Izvor:** ulazni dijagram polazi od VOL, a početni izraz `uo(t0⁺)=C1/(C1+C2)·ui(t0⁺)` pretpostavlja nenapunjene kondenzatore / nulti prethodni nivo. Nije opšti izraz za prethodno stacionarno nenulto VOL.

**Preporučeni predlog:** zadržati dijagrame i uvesti `kR=R2/(R1+R2)`, `kC=C1/(C1+C2)`. Za skok sa VOL na VOH posle stacionarnog stanja:

\[
u_o(t_0^+)=k_RV_{OL}+k_C(V_{OH}-V_{OL}),\qquad
u_o(\infty)=k_RV_{OH}.
\]

U beleškama dati

\[
u_o(t)=k_RV_{OH}+(k_C-k_R)(V_{OH}-V_{OL})e^{-(t-t_0)/\tau},
\quad \tau=\frac{R1R2}{R1+R2}(C1+C2).
\]

Uslov za kompenzaciju i dalje je `kC=kR`, odnosno `C1R1=C2R2`; međukorake i poređenje podkompenzacije/prekompenzacije sačuvati. Alternativa je izričito ograničiti sadašnje izvođenje na VOL=0 i odgovarajuće nulto prethodno stanje, ali to zahteva usklađivanje početnih nivoa dijagrama. Preporučena je opšta verzija iznad, bez gubitka nastavnog slučaja.

## Provera predloga i izvori

- Izvorni PDF i postojeća evidencija [uočenih grešaka rekonstrukcije](../uocene_greske.md) pregledani su; istorijska evidencija nije prepisana.
- Postojeći `kodovi/provera_logike.py` nezavisno proverava margine, struje/fan-out, 72 RC/CR stanja, kontinuitet, promenu početnog trenutka, impulsnu superpoziciju, RL i odnos za kompenzaciju. Prolazak tih proračuna **ne potvrđuje pogrešne zapise sa slajdova**.
- Dodatno su provereni Tejlorov koeficijent na polinomu, znak struje i monotonost RC odziva, dva opsega aproksimacije i odziv kompenzovanog razdelnika pri nenultom početnom stanju. Konkretni rezultati su u [provera_predloga.json](provera_predloga.json).
- Definicije pragova, garantovanih izlaznih struja i kataloških uslova: [Texas Instruments — Understanding and Interpreting Standard-Logic Data Sheets](https://www.ti.com/lit/an/szza036c/szza036c.pdf).
- RC vremenska konstanta i eksponencijalni odziv: [Analog Devices — RC Intro](https://wiki.analog.com/university/courses/engineering_discovery/lab_2).
- Dopune beležaka o lokalnom razdvajanju napajanja: [Analog Devices — MT-101, Decoupling Techniques](https://www.analog.com/media/en/training-seminars/tutorials/MT-101.pdf).

Posle odluke primeniti samo odobrene predloge na njihove slajdove i beleške, ponoviti `all`, `notes`, `review`, pregledati sve pogođene prikaze i obnoviti njihove otiske/potvrde. Tek kada `check` prođe bez otvorenih sadržinskih problema, promeniti status u `ceka_odobrenje`. Početak 09_1 čeka zaseban nalog.
