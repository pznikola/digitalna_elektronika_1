# Dokazi i pokrivenost — vežba 08

Pregled obuhvata ceo `08_mos.tex`, svih 20 izvornih PDF stranica, 38 numerisanih jednačina, sve nenumerisane izraze, četiri sadržinske tabele i 20 TikZ/Circuitikz crteža. Deset zadataka i sve postojeće pottačke/rešenja sačuvani su. `pregled_izvora.json` vezuje ručno izvođenje i praćenje priključaka za SHA256 svake jednačine i crteža. `audit_math.py` dodatno čita stvarne parametre, tabelarne vrednosti, Bulove izraze, MOS veze, upravljačke oznake i koordinate vremenskih dijagrama. Izmena neparsiranog izraza traži novi ručni pregled; prolazak brojeva u testu ne zamenjuje taj pregled.

## P0 — Model i njegove granice (`eq:model`, uvodni pasusi)

Dimenzije: B [A/V²], E [V], u,d [V], oba izraza daju [A]. Za u≤0 model zatvara kanal. Za d=0 omska struja je nula; na d=u oba izraza daju Bu²/[2(1+u/E)]. Izvod omskog izraza je B[u−d−d²/(2E)]/(1+d/E)². Nula je d*=E(sqrt(1+2u/E)−1)<u; na d=u izvod je −Bu²/[2E(1+u/E)²]<0, a izvod grane zasićenja nula. To je ograničenje zadatog interpolacionog modela, ne greška u računu kontinuiteta. Uvod zato ne tvrdi da opisuje fizički doslednu karakteristiku celog kratkog kanala. Granica d=u zadržana je kao konvencija izvornika; nije zamenjena drugim modelom bez zadatih tehnoloških parametara. Za E→∞ dobija se model kvadratnog zakona. Relacija vsat=μEC/2 obezbeđuje jednakost alternativnog zapisa struje zasićenja, ali se ne sme nezavisno nametnuti neusaglašenim brojnim podacima.

Primarni izvor: [MIT 6.012, MOSFETs II, slajdovi 1, 5, 14–16](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-fall-2009/33eea31f564b67fc47cd9c2796500669_MIT6_012F09_lec11.pdf) za uslove osnovnog modela, efekat podloge, p-kanal i ugrađeni kanal. Izvor ne služi potvrdi upravo zadate kratkokanalne interpolacije; njeno ograničenje dokazano je izvodom iznad.

## P1 — Pasivno opterećenje (`sec:1`, svih 11 jednačina)

Stvarni priključci slike 1: RL od VDD do M1.D i izlaza; M1.S i M1.B na masi; M1.G=vU. Zato je (D−y)/R=ID(x−T,y). U zasićenju i bez korekcije E, y=D−BR(x−T)²/2. Iz y′=−1 slede VIL=T+α i VOH=D−α/2, α=1/(BR). Za omsku granu F=(D−y)/R−B[(x−T)y−y²/2]=0 daje y′=−Fy_input/Fy_output. Postavljanje y′=−1 daje x=T−α+2y; zamenom αD=3y²/2, pa VOL=sqrt(2αD/3), VIH=T−α+2VOL. Krajnji niski nivo dobija se pri x=D: y²−2(D−T+α)y+2αD=0. Dva pozitivna korena nisu oba fizička. Niski je 0.0855668344 V, visoki 1.6307122354 V>D. Zanemarivanje y² daje 0.0813008130 V; nije identično kvadratnom korenu.

Skripta čita B0, W/L, R, D, T iz postavke, nezavisno rešava bilans, proverava oblast, izvod −1, svih pet redova tabele, četiri brojna izlaza/margine, α, B i aproksimativni VS. VOH−VIH=0.3977386746 V, VIL−VOL=0.2424739885 V; izvorne procene koriste krajnje nivoe. [MIT CMOS inverter, slajdovi 4–7](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-spring-2009/b96efcfa398f43f970ae4f36ac43456b_MIT6_012S09_lec11.pdf) razlikuje garantovane nivoe i margine. **Ograničenje 08-L01:** E nije zadat, pa brojni rezultati potpunog kratkokanalnog modela nisu određeni.

## P2 — Indukovani kanal (`sec:2`, svih pet jednačina)

M1.S/B=0, M2.D=VDD, M2.G=VGG, M2.S=vI, M2.B=0. Za VGG=VDD M2 je diodno vezan i provodan u zasićenju. VT2(y)=T0+γ(sqrt(y+2|φF|)−sqrt(2|φF|)) raste sa y. Jedinstveni koren y+VT2(y)=D je 0.7335643266 V. Iteracija ima |g′|=γ/[2sqrt(y+0.88)]<1 na celom fizičkom intervalu, pa početak 0.8 konvergira. Na y=0.1 V, u2=0.689626732 V i VT2=0.410373268 V. M1 je omski jer 0.1<0.333564327; M2 zasićen jer 1.1>u2. Deljenje stvarnih struja po W/L daje KR=4.495578304; 1.7 nije rešenje. cm/s, cm²/(Vs), μF/cm² i L=10⁻⁵ cm pretvoreni su pre računa. Kada se E=0.6 V nametne tačno uz relaciju vsat, KR=4.55177303. Podaci daju 2vsatL/μ=0.592592593 V, pa oba tumačenja moraju ostati označena.

Omski uslov za M2: D−y<VGG−y−VT2(y), tj. VGG>D+VT2(y). Maksimum na [0,D] je na D i daje strogu granicu VGG>1.700827472 V. Pri isključenom M1 i takvom VGG visoki izlaz dostiže D. **Ograničenje 08-L02:** međusobno zaokruženi parametri; izbor tumačenja mora pratiti rezultat.

## P3 — Ugrađeni kanal (`sec:3`, svih deset jednačina)

M2.G kratko spojen sa M2.S; obe podloge na masi. Za negativni prag u2=−VT2=t>0, ne −|VT2|. Visoka oblast: d=D−y, I1,sat=I2,lin. Uz male korekcije i zamrznuti t dobija se K(x−T1)²=2td−d². Diferenciranje uz y′=−1 daje K(x−T1)=t−d. Iz sistema u=t/sqrt(K(K+1)), d=t[1−sqrt(K/(K+1))]. Niski izlaz: I1,lin=I2,sat, odnosno K[2(x−T1)y−y²]=Q, Q=t0²/(1+t0/E2). Nagib −1 daje x−T1=2y, pa y=sqrt(Q/(3K)). Pri ulazu VH manji koren je VH−T1−sqrt((VH−T1)²−Q/K). Zanemarivanje y² daje Q/[2K(VH−T1)]. Svaka od ovih jednakosti proverena je simboličkom zamenom u početni bilans i ponovnim diferenciranjem.

Zamrzavanje praga isključuje dt/dy=−γ/[2sqrt(y+2|φF|)], što je dodatna aproksimacija, a ne identitet efekta podloge. Na visokom pragu treba proveriti M1 zasićen/M2 omski; na niskom su oblasti obrnute. Za VH=D potreban je negativan VT2 u celom opsegu i isključen M1. **Ograničenje 08-L03:** nisu zadati D, geometrije i tehnološki parametri; pozitivnost diskriminanta i oblasti ne mogu se brojno potvrditi. Simbolički rezultat je uslovan.

## P4 — CMOS invertor (`sec:4`, obe jednačine, tabela i slika)

Za PMOS pozitivni VSG=D−x, VSD=D−y daju zasićenje D−y≥D−x−|TP|, tj. y≤x+|TP|. NMOS: y≥x−TN. Neprovodni uslovi su x≤TN i x≥D−|TP|. U preklopljenom intervalu oba su zasićena na x=y=VS. Prave na slici imaju odgovarajuće preseke/smerove; brojevi I–V označavaju oblasti duž shematske karakteristike, ne sve tačke ravni. Pri isključenom jednom tranzistoru, drugi dovodi izlaz na odgovarajuću šinu. Bez modulacije dužine kanala zajednička oblast zasićenja pri VS nema jednoznačan y, otuda vertikalni segment. Shematska crna linija nije brojno rešenje tačke b).

U tački b), iz jednakih vsat i Cox sledi (x−0.4)²/(x+0.2)=r(0.8−x)²/(3.2−x). Leva strana raste, desna opada na (0.4,0.8), pa postoji jedinstveni koren. Stvarne dimenzije i redovi tabele provereni su zamenom: r=4 daje 0.6112880845, r=1 daje 0.5379653116 V. E_n=(24/4)·0.1=0.6 V, E_p=2.4 V. **Ograničenje 08-L04:** bez odnosa vsat,n Cox,n / (vsat,p Cox,p), jednakost korišćena u izvorniku je dodatna pretpostavka.

## P5–P7 — Statičke mreže, dualnost i širine (`sec:5`–`sec:7`)

`switch_graph` čita svaki nmos/pmos simbol, D/S priključke, upravljački tekst i nacrtane ortogonalne segmente. Spaja završetke i T-spojeve; ukrštanje unutrašnjosti vodova samo po sebi nije spoj. U svim kombinacijama ulaza traži putanju izlaz–masa i izlaz–napajanje. Svaka promena neparsiranog detalja dodatno obara SHA proveru. Podmreže sa stvarnim imenima tranzistora:

- Z5 PDN m1–m2 sa gejtovima ¬A,¬B paralelno m3–m4 sa ¬C,¬D. Kompletno kolo: PUN (m5 ∥ m6) redno (m7 ∥ m8); PDN (m9–m10) ∥ (m11–m12). Daje Y=(A+B)(C+D); dve mreže uvek vode komplementarno.
- Z5b PUN (m13–m14) ∥ (m15–m16), PDN (m17 ∥ m18) redno (m19 ∥ m20), svi gejtovi direktni. Y1=¬((A+B)(C+D)), pa završni CMOS invertor vraća Y. **Veza Y1→inv.input sada je neprekidna.** Brojanje 8/10/16 i donja granica 2(4+1)=10 važe u eksplicitno navedenoj acikličnoj dualnoj CMOS biblioteci.
- Z6 PDN m21 ∥ [m22–(m23 ∥ m24)] i u kompletnom kolu m29 ∥ [m30–(m31 ∥ m32)]. PUN m25–[m26 ∥ (m27–m28)]. PDN=A+B(C+D); PUN=¬A(¬B+¬C¬D). Stablo PM1=A, PM2=ostatak, PM3=B, PM4=CD, PM5=C, PM6=D dosledno menja seriju/paralelu.
- Z7 ista mreža m33–m40, dimenzionisana m41–m48. Stvarne oznake w_p=(4,4,8,8), w_n=(1,2,2,2). Sve jednostavne provodne putanje izdvajaju se iz nacrtanog grafa; otpori ∑1/w ne prelaze 1 za PDN i 1/2 za PUN, a granice se dostižu. Dodatne paralelne provodne grane samo smanjuju otpor. U ekvivalentnoj slici m49–m50 i m52∥m53 daju rednu harmonijsku širinu i najgori minimum (za samo jedan uključen). Kada su oba paralelna uključena širine se sabiraju. R∝1/w je aproksimacija pri uporedivim naponima i istoj tehnologiji, ne pun MOS model. **08-L05:** nema jedinstvenih apsolutnih dimenzija bez reference, opterećenja i kriterijuma; sačuvano je jedno normalizovano rešenje.

## P8–P9 — Dinamička logika (`sec:8`–`sec:9`)

Početni izraz i svaki korak (8.1) čitaju se iz TeX-a i proveravaju za svih 16 ulaza. Identitet P·CD=CD daje Y=¬(AB+CD). Slika Z8: m55 PMOS pretpunjenje, PDN (m56–m57)∥(m58–m59), m60 NMOS evaluacija. Precharge vodi samo za CLK=0; foot dozvoljava pražnjenje samo za CLK=1. Domino m61–m64, m65–m68 i m69–m72 sa inverterima daju P=AB, Q=CD, Z=P+Q. Jednako označeni vodovi znače električku vezu. Ne postoji provodna putanja između šina za bilo koju stabilnu binarnu kombinaciju.

Slika Z9: m73 pretpunjenje, m74(C) redno (m75(A)∥m76(B)), m77 evaluacija. Stvarne ulazne polilinije imaju CLK=1 na [1,2),[3,4),[5,6),[7,8),[9,10); B raste na 1.5, C pada na 7.5, A=0. Te brojke označavaju isključivo relativne koordinate crteža, ne fizičke vremenske jedinice. Događajni automat puni samo kada vodi PMOS, prazni samo kada postoji PDN putanja, inače pamti. Na svim otvorenim intervalima između svih nacrtanih događaja odgovara stvarnoj izlaznoj poliliniji. U 7.5 Y ostaje 0, u 8 postaje 1; poslednja evaluacija ga ne prazni. Kašnjenje/curenje/raspodela naelektrisanja nisu dati ni kvantifikovani.

[Harris, Advanced Domino Circuit Design, slajdovi 3–8](https://pages.hmc.edu/harris/research/advanceddomino.pdf) potvrđuje pretpunjenje, evaluaciju, problem pada posle pražnjenja i ulogu izlaznog invertora. Pad ne izaziva sam pražnjenje: samo ne može poništiti ranije pražnjenje. Tvrdnje važe u idealnom modelu i uz monotonost/stabilnost ulaza tokom evaluacije.

## P10 — Transmisioni gejtovi (`sec:10`, tri jednačine i obe tabele)

Na stvarnim simbolima gornja oznaka upravlja NMOS-om, donja njegovim PMOS parom. Prva grupa prosleđuje C za B=1, D za B=0; druga D za C=1, B za C=0; treća P za A=1, Q za A=0. Putanje i objedinjeni izlazi ručno su ispraćeni, izvor crteža vezan je SHA otiskom. Skripta čita svih šest parova upravljačkih/data oznaka: u svakoj grupi tačno jedan TG provodi, a upravljanja su komplementarna. Svih 16 redova tabele i sva 24 slučaja D∈{0,1,Z} slažu se sa tim prosleđivanjem. Z se ne pretvara u broj. Red 0101 mora dati 1. Oba stvarna Šenonova niza algebarski su proverena za svih osam ulaza, a četiri TG na slici sinteze daju Q=BC, Y=A?C:Q=(A+B)C. Broj osam MOS isključuje eventualne invertore upravljanja. Naelektrisanje i trajanje zadržavanja pri Z nisu određeni.
