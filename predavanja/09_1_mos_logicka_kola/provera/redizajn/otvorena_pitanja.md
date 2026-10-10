# Otvorena stručna pitanja — 09_1

Datum: 2026-10-03. Status svih predloga: **čeka odluku korisnika; nije primenjeno**. Ovo su nedoslednosti izvornog predavanja, a ne dozvola za promenu njegovih formula. Predavanje zato ostaje `u_radu`. Korisnik može odobriti pojedinačni predlog ili zatražiti obrazloženo zadržavanje izvornog zapisa.

Izvor za svaki sNNN: originalni PDF `09 1 MOS logicka kola.pdf`, strana `(NNN+1)//2`, gornji slajd za neparni NNN, donji za parni. Slajdovi i beleške ne sadrže ove uredničke komentare. Računski protivprimeri su u [postojećoj proveri](../../kodovi/provera_logike.py); izvedeni predlozi dodatno su provereni u [dokazu](dokazi_ispravki.md). Ilustrativni parametri dokaza nisu novi podaci prezentacije.

## P01 — Ujednačavanje stručnih oznaka (s004, s042, s043, s044, s049, s051, s053)

Predlog: `V_T → V_Tn` u modifikovanom nMOS modelu s004; `V_Tn.L → V_Tn,L` na s042; `T1 → T_D` na s043; `k_n.D → k_n,D` na s044; `T2 → T_L` na s049; `V_Tn,D1 → V_Tn,D` na s051; `V_Tn,L → V_Tn,D` u desnoj strani prvog diferenciranog reda s053 (sada u beleškama). Potonji indeks pripada struji pogonskog tranzistora, što se vidi u polaznoj jednačini. Oznake se proveravaju prema susednim relacijama i imenima na šemama.

## P02 — Granica dugog kanala (s014)

Izvor: `V_I=V_Tn+√(2V_DD/(k_n R_L))`, zajedno sa istim izrazom u uslovu za treću oblast. Izraz izostavlja pad izlaznog napona u ravnoteži struja. Predlog, za `x=V_I−V_Tn`:

```text
(k_n R_L/2)x² + x − V_DD = 0
V_I = V_Tn + (√(1+2k_n R_L V_DD)−1)/(k_n R_L).
```

Istim izrazom zameniti i levi član uslova `< V_DD`. Pri `V_DD=5 V`, `V_Tn=1 V`, `k_n R_L=1/V`, izvor daje 4,162 V, dok granica koja zadovoljava i `V_O=V_I−V_Tn` i ravnotežu daje 3,317 V. Ako je namerna gruba aproksimacija, alternativno navesti njen dodatni uslov i koristiti približnu jednakost.

## P03 — Uslov zanemarivanja kratkog kanala (s020)

Izvor: `V_O < L_n E_Cn`. Sam znak `<` ne čini količnik u imeniocu zanemarljivim. Predlog: `V_O ≪ L_n E_Cn`, uz jasno navođenje da se koristi aproksimacija. Na primer, za odnos 0,5 faktor `1/(1+0,5)` iznosi 2/3, a ne približno 1.

## P04 — Opseg tvrdnje o zasićenju tokom pražnjenja (s029 i beleške s030)

Izvor proverava srednji izlazni nivo, ali zaključuje da zasićenje važi tokom celog pražnjenja. Predlog: ograničiti zaključak na **interval do nivoa na kojem se meri kašnjenje**. Provera `V_DSsat < V_DD/2` ne obezbeđuje zasićenje i posle pada ispod tog graničnog napona. Ne menjaju se krive niti RC rezultat `t_p≈0,69R_n C_L`; precizira se domen njegove upotrebe.

## P05 — Decimalne aproksimacije (s033)

Predlog: `5/6 ≈ 0,833` i `7/9 ≈ 0,778`, umesto izvornih jednakosti sa 0,833 i 0,777. Drugi broj je zaokružen na tri decimale. Integralni izrazi se ne menjaju.

## P06 — Oznaka upravljačkog napona pMOS krive (s034)

Kolo i objašnjenje koriste `V_SG`, a kriva nosi `V_GS`. Predlog: oznaku uz porodicu krivih promeniti u `V_SG`. Sačuvati izvornu osu `V_SD`, smer prelaza i sve koeficijente.

## P07 — Jednaki parametri i Δ=0 (s041)

Izvor bezuslovno tvrdi da jednačina nema rešenje za `k_n,L=k_n,D`. Za jednake k, kvadratna jednačina svodi se na `−Δ² k_n,L=0`: nema rešenja kada je `Δ≠0`, ali pri `Δ=0` postaje identitet. Predlog: odvojiti ta dva slučaja. Identitet ne određuje jednu izdvojenu tačku nagiba −1; ne sme biti proglašen jednačinom bez rešenja.

## P08 — Izvod i oba rezultata za omsko opterećenje (s044/s045)

Desna strana je `k_D V_O(2V_I−2V_TD−V_O)`. Pri `dV_O/dV_I=−1`, njen izvod je `k_D(4V_O−2V_I+2V_TD)`, a ne `k_D(2V_O−2V_I+2V_TD)`. Predlog: vratiti izgubljenu dvojku i ponoviti završnu zamenu i korene.

Za kraći zapis u dokazu definišimo `ρ=k_L/k_D`, `A=V_C−V_TL`, `B=V_C−V_DD−V_TL=Δ`. U prezentaciji se mogu zadržati pune izvorne oznake:

```text
V_I = V_TD + 2V_O − ρ(A−V_O)
(3+ρ)V_O² = ρ(A²−B²)
V_O(IH) = √[ρ(A²−B²)/(3+ρ)]
V_IH = V_TD + (2+ρ)V_O(IH) − ρA.
```

Ovo su rezultati u usvojenom dugokanalnom modelu, uz proveru oblasti rada oba tranzistora. Izvorni rezultati s045 ne zadovoljavaju početnu ravnotežu; sam izbor drugog znaka izvornog korena nije dovoljan.

## P09 — Ponovljeni izraz logičke nule (s046/s047)

Iz definicije `Δ=V_C−V_DD−V_Tn,L` sledi `V_DD+2Δ=2V_C−V_DD−2V_Tn,L`. Predlog: dodati nedostajuću dvojku uz `V_Tn,L` u drugom zapisu `V_OL` na oba slajda. Prvi zapis i dokaz poništavanja zajedničkog faktora širina ostaju isti.

## P10 — Zamena u početnu jednačinu (s051)

Posle zamene jednačine 2 u jednačinu 1, desni koeficijent je `k_L²/k_D`, a ne `k_L`. Predlog:

```text
k_L(V_DD−V_O−V_TL)² = (k_L²/k_D)(V_DD−V_O−V_TL)².
```

Izvorni upitnici predstavljaju nastavno pitanje. Mogu ostati kao poziv da se protumači dobijeni uslov, uz ispravljenu relaciju. Ovo nije identitet za proizvoljan odnos parametara.

## P11 — Izuzetak konstantnog pojačanja (s052)

Izvor tvrdi da nema tačke nagiba −1, a zatim daje `a=−√(k_D/k_L)`. Pri `k_D=k_L`, nagib je −1 u celoj razmatranoj linearnoj oblasti. Predlog: uvodnu tvrdnju izričito vezati za **slučaj logičkog kola `k_D>k_L`**, već naveden na kraju slajda, i objasniti degenerisani slučaj jednakih parametara. Linearna karakteristika se ne menja.

## P12 — Izvod i rezultati za zasićeno opterećenje (s053/s054)

Ista izgubljena dvojka kao P08, zajedno sa pogrešnim indeksom praga u prvom redu diferenciranja (P01). Predlog: ispraviti sve međukorake i oba rezultata. Za `ρ=k_L/k_D`, `A=V_DD−V_TL`:

```text
2k_L(A−V_O) = k_D(4V_O−2V_I+2V_TD)
V_I = V_TD + 2V_O − ρ(A−V_O)
V_O(IH) = A√[ρ/(3+ρ)]
V_IH = V_TD + A[(2+ρ)√(ρ/(3+ρ))−ρ].
```

Proveriti i uslove oblasti; rezultati nisu univerzalni izvan pretpostavljenog režima. Izvorni koreni s054 ne zadovoljavaju početnu ravnotežu.

## P13 — Visoki ulaz u imeniocu VOL (s055)

Prethodni red koristi `V_OH−V_Tn,D`, a s050 daje `V_OH=V_DD−V_Tn,L`. Predlog:

```text
V_OL ≈ (1/2)(k_n,L/k_n,D)(V_DD−V_Tn,L)²
       / (V_DD−V_Tn,L−V_Tn,D).
```

Zadržati aproksimaciju malog `V_OL`, navesti pozitivan imenilac i proveriti da dobijena tačka ostaje u omskoj oblasti pogonskog tranzistora.

## Razrešeno poređenjem sa originalom — s027

Dodatna zatvorena zagrada u prvom `I_OL` postojala je u polaznom LaTeX-u. Vizuelni pregled originalnog slajda pokazuje jedan zatvoren par zagrada. LaTeX je usklađen sa PDF-om bez menjanja formule ili traženja stručnog odobrenja. Istorijski `uocene_greske.md` ostaje arhiva rekonstrukcije; njegov unos za s027 nije dokaz greške originala.
