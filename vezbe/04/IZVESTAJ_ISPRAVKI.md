# Izveštaj o ispravkama — vežbe 04

Vrsta izmene vidi se iz obrazloženja: računska/stručna greška, dopunsko pojašnjenje ili jezička i tipografska obrada. Stavke koje preciziraju konvenciju ili dodaju obrazloženje nisu predstavljene kao greške izvornika. Proračuni i promenjene formule dati su uz pojedinačne stavke; ponovljive provere su u [code/provera.py](code/provera.py) i [code/rezultati.json](code/rezultati.json). Izvorne oznake povezane su sa novim mestima u [inventaru](INVENTAR.md).

## Pojedinačne ispravke i pojašnjenja

### 04-01 — blok 36

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 100; `% Izvor DOCX: blok 36`.

**Izvor:** gde c_{i} predstavlja cifru ulaznog prenosa. Cifra izlaznog prenosa c_{i+1 }uzima vrednost 1 ako je $x_{i}\  + \ y_{i}\  + c_{i}\  > r$ dok u suprotnom uzima vrednost 0.

**Ispravka:** Ulazni prenos je $c_i$. Izlazni prenos je $c_{i+1}=1$ ako je $x_i+y_i+c_i\ge r$, a inače je nula.

**Obrazloženje i uticaj:** Pri zbiru tačno jednakom osnovi takođe nastaje prenos; > zamenjeno sa ≥.

### 04-02 — blok 41

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 132; `% Izvor DOCX: blok 41`.

**Izvor:** gde b_{i} predstavlja cifru ulazne pozajmice. Cifra izlazne pozajmice b_{i+1 }uzima vrednost 1 ako je $x_{i} - \ y_{i} - c_{i}\  < r$ dok u suprotnom uzima vrednost 0.

**Ispravka:** Ulazna pozajmica je $b_i$. Izlazna pozajmica je $b_{i+1}=1$ ako je $x_i-y_i-b_i<0$, a inače je nula. Početna pozajmica je $b_0$, dok $b_{n+1}=1$ označava da je umanjenik manji od umanjioca (uz ulaznu pozajmicu).

**Obrazloženje i uticaj:** Ispravljeni su i pogrešna veličina c_i i pogrešna granica r; pozajmljuje se tek kada međurezultat postane negativan.

### 04-03 — blok 42

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 135; `% Izvor DOCX: blok 42`.

**Izvor:** U slučaju da brojevi X i Y nisu predstavljeni sa istim brojem cifara, pre realizacije operacije sabiranja potrebno je dodati vodeće nule ispred broja koji ima manje cifara kako bi se broj cifara izjednačio. Ukoliko brojevi X i Y sadrže razlomljeni deo, pre realizacije operacije oduzimanja neophodno je poravnati decimalne tačke.

**Ispravka:** Pre oduzimanja izjednačavamo broj cifara vodećim nulama i poravnavamo tačke. Ako je umanjenik manji od umanjioca, matematička razlika je negativna i nije predstavljiva kao neoznačen broj; zapis na ograničenoj širini predstavlja ostatak modulo $r^N$.

**Obrazloženje i uticaj:** Razdvojena negativna razlika i modularni rezultat neoznačenog oduzimanja.

### 04-04 — blok 45

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 148; `% Izvor DOCX: blok 45`.

**Izvor:** U slučaju operacije X - Y, ukoliko je |X| < |Y|, jasno je da će rezultat biti negativan, što znači da će bit najveće težine reultata operacije oduzimanja imati vrednost 1, dok će se apsolutna vrednost rezultata dobiti kao rezultat operacije |Y| - |X|.

**Ispravka:** Za sabiranje brojeva istog znaka sabiraju se apsolutne vrednosti i zadržava znak. Za suprotne znake oduzima se manja apsolutna vrednost od veće, a znak se preuzima od operanda veće apsolutne vrednosti. Oduzimanje $X-Y$ svodi se na $X+(-Y)$. Tvrdnja da iz $|X|<|Y|$ sledi $X-Y<0$ važi kada su $X$ i $Y$ nenegativni; nije opšte pravilo za označene operande.

**Obrazloženje i uticaj:** Izvorni uslov za znak razlike netačan je za proizvoljne označene brojeve.

### 04-05 — blok 47

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 156; `% Izvor DOCX: blok 47`.

**Izvor:** Sabiranje brojeva X = x_{n} x_{n-1} x_{n-2} … x_{1} x_{0} i Y = y_{n} y_{n-1} y_{n-2} … y_{1} datih u komplementu osnove se realizuje na skoro identičan način kao i sabiranje neoznačenih brojeva pri čemu je potrebno voditi računa prilikom ekstenzije znaka sabiraka. U okviru dobijenog rezultata se zadržava zahtevani broj cifara n dok se ostale cifre odbacuju.

**Ispravka:** Sabiranje u komplementu osnove izvodi se cifru po cifru, posle proširenja znaka na zadatu širinu $N$. Zadržava se $N$ cifara rezultata, tj. računa se modulo $r^N$. Kod zapisa sa $k$ razlomljenih cifara tačka se poravnava, a korak je $r^{-k}$.

**Obrazloženje i uticaj:** Usklađena je oznaka širine: izvor indeksira od 0 do n, a zatim pogrešno tvrdi da ima n cifara.

### 04-06 — blok 48

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 159; `% Izvor DOCX: blok 48`.

**Izvor:** Usled ograničenosti broja cifara, za razliku od realizacije operacije sabiranja u slučaju neoznačenih brojeva, prilikom sabiranja označenih brojeva može doći do prekoračenja (overflow - OF). Prekoračenje nastaje ukoliko su sabirci istog a zbir suprotnog znaka. Takođe, prekoračenje (overflow) se može identifikovati ukoliko su ulazni i izlazni prenos na poziciji bita znaka različiti. U slučaju binarnog brojnog sistema važi: OF = 1 ako je c_{n+1} ≠ c_{n}:

**Ispravka:** I neoznačena i označena aritmetika imaju ograničen opseg. Kod neoznačenog sabiranja prekoračenje označava izlazni prenos. Kod označenog sabiranja prekoračenje (OF) postoji ako tačan zbir izlazi iz opsega zadate predstave; za binarni KO to je slučaj kada su sabirci istog, a rezultat suprotnog znaka. Ekvivalentno, $\mathrm{OF}=c_{n+1}\oplus c_n$, gde je $n$ indeks bita znaka.

**Obrazloženje i uticaj:** Izvor netačno sugeriše da neoznačena aritmetika nema prekoračenje; kriterijum prenosa kroz bit znaka ograničen je na binarni KO.

### 04-07 — blok 52

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 185; `% Izvor DOCX: blok 52`.

**Izvor:** Sabiranje brojeva u komplementu maksimalne vrednosti se realizuje na sličan način kao i sabiranje brojeva u komplementu osnove. Konačan rezultat se dobija dodavanjem cifre izlaznog prenosa na zbir dobijen sabiranjem u

**Ispravka:** Sabiranje u komplementu maksimalne vrednosti izvodi se cifru po cifru. Izlazni prenos dodaje se na cifru najmanje težine (kružni prenos). Kod razlomljenih zapisa to znači dodavanje jedinice poslednjeg mesta, a ne celog broja 1.

**Obrazloženje i uticaj:** Dovršena prekinuta rečenica i preciziran povratni prenos za zapise sa tačkom.

### 04-08 — blok 56

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 215; `% Izvor DOCX: blok 56`.

**Izvor:** Množenje neoznačenih brojeva je moguće realizovati na isti način kao i množenje brojeva u decimalnom brojnom sistemu. Ukoliko činioci imaju decimalnu tačku, množenje se realizuje uklanjanjem decimalne tačke dok se u okviru dobijenog proizvoda decimalna tačka ubacuje na poziciju između cifara koja odgovara zbiru pozicija decimalnih tačaka činioca.

**Ispravka:** Pri množenju neoznačenih brojeva najpre privremeno uklanjamo tačke i množimo celobrojne kodne reči. Ako operandi imaju $k_X$ i $k_Y$ razlomljenih cifara, proizvod ima $k_X+k_Y$ razlomljenih cifara.

**Obrazloženje i uticaj:** Zamenjena neprecizna formulacija o zbiru „pozicija“ tačaka pravilom o broju razlomljenih cifara.

### 04-09 — blok 59

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 228; `% Izvor DOCX: blok 59`.

**Izvor:** Množenje označenih brojeva se realizuje na sličan način kao i množenje neoznačenih brojeva dok se sabiranje međurezultata realizuje po pravilima sabiranja predstave u kojoj su dati brojevi predstavljeni. Prilikom realizacije operacije sabiranja, u okviru pojedinačnih međurezultata, treba voditi računa o ekstenziji znaka sabiraka za jedno mesto i odbacivanju eventualnog viška cifara u poslednjem sabiranju. U dobijenim međurezultatima ne treba odbacivati eventualni višak cifara jer su ta sabiranja samo fragment ukupnog sabiranja na većem broju cifara. Takođe, ukoliko je cifra najveće težine broja sa kojim množimo negativna (pripada skupu {r/2,…,r-1}), poslednji sabirak je potrebno zameniti njegovom suprotnom vrednošću u osnovi u kojoj je predstavljen.

**Ispravka:** Za binarni KO broj $Y$ širine $N$ ima vrednost
\[Y=-y_{N-1}2^{N-1}+\sum_{i=0}^{N-2}y_i2^i.\]
Zato poslednji parcijalni proizvod ima negativnu težinu, dok se ostali sabiraju. Pre pomeranja i sabiranja svaki parcijalni proizvod proširuje se znakom na širinu rezultata; za dva $N$-bitna operanda puna širina proizvoda je $2N$. U međukoracima se ne sme izgubiti bit potreban za konačan rezultat. Za razlomljene operande na kraju vraćamo tačku. Pravilo o prostom negiranju poslednjeg parcijalnog proizvoda odnosi se na binarni KO; nije opšti algoritam za sve osnove i predstave.

**Obrazloženje i uticaj:** Izvor preširoko uopštava binarni algoritam množenja i ne određuje pouzdano širinu međurezultata.

### 04-10 — uvod — neparna osnova

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), celina navedena u naslovu stavke.

**Izvor:** Znak za osnovu 7 nije formalno definisan.

**Ispravka:** Dodata potpuna konvencija dekodiranja KO i KMV i neupotrebljene srednje reči KMV.

**Obrazloženje i uticaj:** Nijedan zadati operand nije neupotrebljena srednja reč; proračun je jednoznačan i proširenje čuva vrednost.

### 04-11 — blok 66

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 266; `% Izvor DOCX: blok 66`.

**Izvor:** * Izvršiti sabiranje neoznačenih brojeva brojnom u sistemu sa osnovom u kome su dati i odrediti sve cifre prenosa:

**Ispravka:** b) Izvršiti oduzimanje neoznačenih brojeva u osnovi u kojoj su dati i odrediti sve cifre pozajmice:

**Obrazloženje i uticaj:** U tački b pogrešno je pisalo sabiranje umesto oduzimanje.

### 04-12 — blok 70

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 285; `% Izvor DOCX: blok 70`.

**Izvor:** Izraz | Postupak | Rezultat
100.11_{2} + 10.01_{2} : |  | 0 | 0 | 1 |  | 1 | 0 | (ulazni prenos 0)
 | 1 | 0 | 0 | . | 1 | 1 | 
+ | 0 | 1 | 0 | . | 0 | 1 | 
 | 1 | 1 | 1 | . | 0 | 0 |  | 111.00_{2}
11111_{2} + 10011_{2} |  | 1 | 1 | 1 | 1 | 1 | 1 | (ulazni prenos 1)
 |  | 1 | 1 | 1 | 1 | 1 | 
+ |  | 1 | 0 | 0 | 1 | 1 | 
 | 1 | 1 | 0 | 0 | 1 | 1 |  | 110011_{2}
294_{10} + 42_{10} |  |  |  |  | 1 | 0 | 0 | (ulazni prenos 0)
 |  |  |  | 2 | 9 | 4 | 
+ |  |  |  | 0 | 4 | 2 | (dodata vodeća nula)
 |  |  |  | 3 | 3 | 6 |  | 336_{10}
5325_{7} + 4163_{7} |  |  | 1 | 0 | 1 | 1 | 0 | (ulazni prenos 0)
 |  |  | 5 | 3 | 2 | 5 | 
+ |  |  | 4 | 1 | 6 | 3 | 
 |  | 1 | 2 | 5 | 2 | 1 |  | 12521_{7}
AF3.50_{16} + FB2.B9_{16} |  | 1 | 1 | 0 | 1 |  | 0 | 0 | (ulazni prenos 0)
 |  | A | F | 3 | . | 5 | 0 | 
+ |  | F | B | 2 | . | B | 9 | 
 | 1 | A | A | 6 | . | 0 | 9 |  | 1AA6.09_{16}
26417_{8} + 13140_{8} |  |  |  | 1 | 0 | 0 | 0 | 0 | (ulazni prenos 0)
 |  |  | 2 | 6 | 4 | 1 | 7 | 
+ |  |  | 1 | 3 | 1 | 4 | 0 | 
 |  |  | 4 | 1 | 5 | 5 | 7 |  | 41557_{8}

**Ispravka:** \begin{longtable}{p{0.33\linewidth} p{0.36\linewidth} p{0.23\linewidth}}\toprule
Izraz & Postupak & Rezultat\\\midrule\endhead
$(100.11)_{2}+(10.01)_{2}$ & $\begin{array}{r}\text{c}:\ 000110\\100.11\\+010.01\\\hline 111.00\end{array}$ & $111.00$\\[5pt]
$(11111)_{2}+(10011)_{2}+1$ & $\begin{array}{r}\text{c}:\ 111111\\11111\\+10011\\\hline 10011\end{array}$ & $110011$\\[5pt]
$(294)_{10}+(42)_{10}$ & $\begin{array}{r}\text{c}:\ 0100\\294\\+042\\\hline 336\end{array}$ & $336$\\[5pt]
$(5325)_{7}+(4163)_{7}$ & $\begin{array}{r}\text{c}:\ 10110\\5325\\+4163\\\hline 2521\end{array}$ & $12521$\\[5pt]
$(AF3.50)_{16}+(FB2.B9)_{16}$ & $\begin{array}{r}\text{c}:\ 110100\\AF3.50\\+FB2.B9\\\hline AA6.09\end{array}$ & $1AA6.09$\\[5pt]
$(26417)_{8}+(13140)_{8}$ & $\begin{array}{r}\text{c}:\ 010000\\26417\\+13140\\\hline 41557\end{array}$ & $41557$\\[5pt]
\bottomrule\end{longtable}

**Obrazloženje i uticaj:** Ponovo izračunate sve cifre prenosa/pozajmice. Kod 436₈−627₈ tačna razlika je −171₈; ostatak 607₈ na tri cifre uz izlaznu pozajmicu nije neoznačena pozitivna razlika. Ostali tačni krajnji rezultati zadržani su; uklonjene su pogrešne oznake „prenos“ u tabeli oduzimanja.

### 04-13 — blok 72

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 309; `% Izvor DOCX: blok 72`.

**Izvor:** Izraz | Postupak | Rezultat
110101_{2} - 10110_{2} |  | 1 | 1 | 1 | 1 | 0 | 0 | (ulazna pozajmica 0)
 | 1 | 1 | 0 | 1 | 0 | 1 | 
- | 0 | 1 | 0 | 1 | 1 | 0 | 
 | 0 | 1 | 1 | 1 | 1 | 1 |  | 11111_{2}
100010_{2} - 10010_{2} |  | 1 | 1 | 1 | 1 | 1 | 1 | (ulazni prenos 1)
 | 1 | 0 | 0 | 0 | 1 | 0 | 
- | 0 | 1 | 0 | 0 | 1 | 0 | 
 | 0 | 0 | 1 | 1 | 1 | 1 |  | 001111_{2}
25.2_{10} - 2.8_{10} |  |  |  | 0 | 1 |  | 0 | (ulazni prenos 0)
 |  |  | 2 | 5 | . | 2 | 
- |  |  | 0 | 2 | . | 8 | 
 |  |  | 2 | 2 | . | 4 |  | 22.4_{10}
436_{8} - 627_{8} |  |  |  | 1 | 0 | 1 | 0 | (ulazni prenos 0)
 |  |  |  | 4 | 3 | 6 | 
- |  |  |  | 6 | 2 | 7 | 
. | 7 | 7 | 7 | 6 | 0 | 7 |  | 777607_{8}
FB.2B9_{16} – AF.350_{16} |  | 0 | 1 | 1 |  | 0 | 0 | 0 | (ulazni prenos 0)
 |  | F | B | . | 2 | B | 9 | 
- |  | A | F | . | 3 | 5 | 0 | 
 |  | 4 | B | . | F | 6 | 9 |  | 4B.F69_{16}
26417_{8} - 13140_{8} |  |  |  | 0 | 0 | 1 | 0 | 0 | (ulazni prenos 0)
 |  |  | 2 | 6 | 4 | 1 | 7 | 
- |  |  | 1 | 3 | 1 | 4 | 0 | 
 |  |  | 1 | 3 | 2 | 5 | 7 |  | 13257_{8}

**Ispravka:** \begin{longtable}{p{0.33\linewidth} p{0.36\linewidth} p{0.23\linewidth}}\toprule
Izraz & Postupak & Rezultat\\\midrule\endhead
$(110101)_{2}-(10110)_{2}$ & $\begin{array}{r}\text{b}:\ 0111100\\110101\\-010110\\\hline 011111\end{array}$ & $\begin{array}{r}011111\\b_{N}=0\end{array}$\\[5pt]
$(100010)_{2}-(10010)_{2}-1$ & $\begin{array}{r}\text{b}:\ 0111111\\100010\\-010010\\\hline 001111\end{array}$ & $\begin{array}{r}001111\\b_{N}=0\end{array}$\\[5pt]
$(25.2)_{10}-(2.8)_{10}$ & $\begin{array}{r}\text{b}:\ 0010\\25.2\\-02.8\\\hline 22.4\end{array}$ & $\begin{array}{r}22.4\\b_{N}=0\end{array}$\\[5pt]
$(436)_{8}-(627)_{8}$ & $\begin{array}{r}\text{b}:\ 1010\\436\\-627\\\hline 607\end{array}$ & $\begin{array}{r}-171\\b_{N}=1\end{array}$\\[5pt]
$(FB.2B9)_{16}-(AF.350)_{16}$ & $\begin{array}{r}\text{b}:\ 011000\\FB.2B9\\-AF.350\\\hline 4B.F69\end{array}$ & $\begin{array}{r}4B.F69\\b_{N}=0\end{array}$\\[5pt]
$(26417)_{8}-(13140)_{8}$ & $\begin{array}{r}\text{b}:\ 000100\\26417\\-13140\\\hline 13257\end{array}$ & $\begin{array}{r}13257\\b_{N}=0\end{array}$\\[5pt]
\bottomrule\end{longtable}

**Obrazloženje i uticaj:** Ponovo izračunate sve cifre prenosa/pozajmice. Kod 436₈−627₈ tačna razlika je −171₈; ostatak 607₈ na tri cifre uz izlaznu pozajmicu nije neoznačena pozitivna razlika. Ostali tačni krajnji rezultati zadržani su; uklonjene su pogrešne oznake „prenos“ u tabeli oduzimanja.

### 04-14 — blok 79

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 358; `% Izvor DOCX: blok 79`.

**Izvor:** Izraz | Postupak | Rezultat
Znak | Apsolutna vrednost
A + B | + (jer su oba broja pozitivna) |  |  | 0 | 0 | 1 | 0 | 0 | 
 |  | 1 | 0 | 0 | 1 | 0 | 
+ |  | 0 | 1 | 0 | 1 | 0 | 
 |  | 1 | 1 | 1 | 0 | 0 |  | 011100_{ZA}
B – A | - (jer je B < A) |  |  | 1 | 0 | 0 | 0 | 0 | 
 |  | 1 | 0 | 0 | 1 | 0 | A
- |  | 0 | 1 | 0 | 1 | 0 | B
 |  | 0 | 1 | 0 | 0 | 0 |  | 101000_{ZA}
A – B | + (jer je B < A) |  |  | 1 | 0 | 0 | 0 | 0 | 
 |  | 1 | 0 | 0 | 1 | 0 | A
- |  | 0 | 1 | 0 | 1 | 0 | B
 |  | 0 | 1 | 0 | 0 | 0 |  | 001000_{ZA}
–B – A | -
(-(B+A)) |  |  | 1 | 0 | 1 | 0 | 0 | 
 |  | 1 | 0 | 0 | 1 | 0 | A
+ |  | 0 | 1 | 0 | 1 | 0 | B
 |  | 1 | 1 | 1 | 0 | 0 |  | 111100_{ZA}
C – A | Za samostalni rad
C – D
A – 2B | -
(Množenje sa 2 podrazumeva pomeranje bita za jedno mesto u levo. Zbog toga važi da je 2B ˃ A, odnosno da je rezultat negativan ) |  |  | 0 | 0 | 1 | 0 | 0 | 
 |  | 1 | 0 | 1 | 0 | 0 | 2B
- |  | 1 | 0 | 0 | 1 | 0 | A
 |  | 0 | 0 | 0 | 1 | 0 |  | 100010_{ZA}
A – B + C – D | Za samostalni rad

**Ispravka:** \begin{longtable}{p{0.2\linewidth} p{0.48\linewidth} p{0.24\linewidth}}\toprule
Izraz & Postupak nad apsolutnim vrednostima & Rezultat\\\midrule\endhead
$A+B$ & Znak $+$; $|R|=10010+01010$ & $011100_{\mathrm{ZA}}$\\[5pt]
$B-A$ & Znak $-$; $|R|=10010-01010$ & $101000_{\mathrm{ZA}}$\\[5pt]
$A-B$ & Znak $+$; $|R|=10010-01010$ & $001000_{\mathrm{ZA}}$\\[5pt]
$-B-A$ & Znak $-$; $|R|=10010+01010$ & $111100_{\mathrm{ZA}}$\\[5pt]
$C-A$ & \multicolumn{2}{c}{Za samostalni rad}\\[5pt]
$C-D$ & \multicolumn{2}{c}{Za samostalni rad}\\[5pt]
$A-2B$ & Znak $-$; $|R|=10100-10010$ & $100010_{\mathrm{ZA}}$\\[5pt]
$A-B+C-D$ & \multicolumn{2}{c}{Za samostalni rad}\\[5pt]
\bottomrule\end{longtable}

**Obrazloženje i uticaj:** Sačuvana su sva prikazana rešenja i sva tri označena nerešena izraza. Usklađeni međurezultati i izbegnuto mešanje aritmetike nad znakom i apsolutnom vrednošću.

### 04-15 — blok 87

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 419; `% Izvor DOCX: blok 87`.

**Izvor:** Izraz | Postupak | Rezultat
010_{2} +0011_{2} |  |  | 0 | 0 | 1 | 0 | 0 | 
 |  |  | 0 | 0 | 1 | 0 | 
+ |  |  | 0 | 0 | 1 | 1 | 
 |  | 0 | 0 | 1 | 0 | 1 |  | 0101_{2} OF = 0
11_{2} +110_{2} |  |  | 1 | 1 | 1 | 0 | 0 | 
 |  |  | 1 | 1 | 1 | 1 | 
+ |  |  | 1 | 1 | 1 | 0 | 
 |  | 1 | 1 | 1 | 0 | 1 |  | 1101_{2}
OF = 0
0110_{2} +1011_{2} |  |  | 1 | 1 | 1 | 0 | 0 | 
 |  |  | 0 | 1 | 1 | 0 | 
+ |  |  | 1 | 0 | 1 | 1 | 
 |  | 1 | 0 | 0 | 0 | 1 |  | 0001_{2} OF = 0
1100_{2} +0101_{2} |  |  | 1 | 1 | 0 | 0 | 0 | 
 |  |  | 1 | 1 | 0 | 0 | 
+ |  |  | 0 | 1 | 0 | 1 | 
 |  | 1 | 0 | 0 | 0 | 1 |  | 0001_{2}
OF = 0
0101_{2} +0110_{2} |  |  | 0 | 1 | 0 | 0 | 0 | 
 |  |  | 0 | 1 | 0 | 1 | 
+ |  |  | 0 | 1 | 1 | 0 | 
 |  | 0 | 1 | 0 | 1 | 1 |  | 1011_{2}
OF = 1
1101_{2} +1011_{2} |  |  | 1 | 1 | 1 | 1 | 0 | 
 |  |  | 1 | 1 | 0 | 1 | 
+ |  |  | 1 | 0 | 1 | 1 | 
 |  | 1 | 1 | 0 | 0 | 0 |  | 1000_{2}
OF = 0
1.0_{2} +10.1_{2} |  | 1 | 1 | 0 | 0 |  | 0 | 
 |  | 1 | 1 | 0 | . | 1 | 
+ |  | 1 | 1 | 1 | . | 0 | 
 | 1 | 1 | 0 | 1 | . | 1 |  | 101.0_{2}
OF = 0
435_{10} + 834_{10} |  |  | 1 | 1 | 0 | 0 | 0 | 
 |  |  | 0 | 4 | 3 | 5 | 
+ |  |  | 9 | 8 | 3 | 4 | 
 |  | 1 | 0 | 2 | 6 | 9 |  | 0269_{10}
OF = 0
A32F_{16} + 476_{16} |  |  | 0 | 0 | 0 | 1 | 0 | 
 |  |  | A | 3 | 2 | F | 
+ |  |  | 0 | 4 | 7 | 6 | 
 |  | 0 | A | 7 | A | 5 |  | A7A5_{16}
OF = 0
324_{7} + 365_{7} |  |  | 1 | 1 | 1 | 1 | 0 | 
 |  |  | 0 | 3 | 2 | 4 | 
+ |  |  | 6 | 3 | 6 | 5 | 
 |  | 0 | 0 | 0 | 2 | 2 |  | 0022_{7}
OF = 0

**Ispravka:** \begin{longtable}{p{0.34\linewidth} p{0.34\linewidth} p{0.23\linewidth}}\toprule
Izraz & Sabiranje kodnih reči & Rezultat\\\midrule\endhead
$(010)_{2}+(0011)_{2}$ & $\begin{array}{r}c:\ 00100\\0010\\+0011\\\hline 0101\end{array}$ & $0101$\newline OF = 0\\[5pt]
$(11)_{2}+(110)_{2}$ & $\begin{array}{r}c:\ 11100\\1111\\+1110\\\hline 1101\end{array}$ & $1101$\newline OF = 0\\[5pt]
$(0110)_{2}+(1011)_{2}$ & $\begin{array}{r}c:\ 11100\\0110\\+1011\\\hline 0001\end{array}$ & $0001$\newline OF = 0\\[5pt]
$(1100)_{2}+(0101)_{2}$ & $\begin{array}{r}c:\ 11000\\1100\\+0101\\\hline 0001\end{array}$ & $0001$\newline OF = 0\\[5pt]
$(0101)_{2}+(0110)_{2}$ & $\begin{array}{r}c:\ 01000\\0101\\+0110\\\hline 1011\end{array}$ & $1011$\newline OF = 1\\[5pt]
$(1101)_{2}+(1011)_{2}$ & $\begin{array}{r}c:\ 11110\\1101\\+1011\\\hline 1000\end{array}$ & $1000$\newline OF = 0\\[5pt]
$(1.0)_{2}+(10.1)_{2}$ & $\begin{array}{r}c:\ 11000\\111.0\\+110.1\\\hline 101.1\end{array}$ & $101.1$\newline OF = 0\\[5pt]
$(435)_{10}+(834)_{10}$ & $\begin{array}{r}c:\ 11000\\0435\\+9834\\\hline 0269\end{array}$ & $0269$\newline OF = 0\\[5pt]
$(A32F)_{16}+(476)_{16}$ & $\begin{array}{r}c:\ 00010\\A32F\\+0476\\\hline A7A5\end{array}$ & $A7A5$\newline OF = 0\\[5pt]
$(324)_{7}+(365)_{7}$ & $\begin{array}{r}c:\ 11110\\0324\\+6365\\\hline 0022\end{array}$ & $0022$\newline OF = 0\\[5pt]
\bottomrule\end{longtable}

**Obrazloženje i uticaj:** Sve tabele ponovo su izvedene na četiri cifre, uz dekodiranje na izvornoj širini, proširenje znaka, negiranje umanjioca i kružni prenos za KMV. Detaljne pojedinačne razlike nalaze se u posebnom pregledu ispod.

### 04-16 — blok 89

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 451; `% Izvor DOCX: blok 89`.

**Izvor:** Izraz | Postupak | Rezultat
010_{2} −1101_{2} |  |  | 0 | 0 | 1 | 0 | 0 | 
 |  |  | 0 | 0 | 1 | 0 | 
+ |  |  | 0 | 0 | 1 | 1 | -1101_{2}
 |  | 0 | 0 | 1 | 0 | 1 |  | 0101_{2} OF = 0
11_{2} −010_{2} |  |  | 1 | 1 | 1 | 0 | 0 | 
 |  |  | 1 | 1 | 1 | 1 | 
+ |  |  | 1 | 1 | 1 | 0 | -0010_{2}
 |  | 1 | 1 | 1 | 0 | 1 |  | 1101_{2}
OF = 0
0110_{2} −0101_{2} |  |  | 1 | 1 | 1 | 0 | 0 | 
 |  |  | 0 | 1 | 1 | 0 | 
+ |  |  | 1 | 0 | 1 | 1 | −0101_{2}
 |  | 1 | 0 | 0 | 0 | 1 |  | 0001_{2} OF = 0
1100_{2} −1011_{2} |  |  | 1 | 1 | 0 | 0 | 0 | 
 |  |  | 1 | 1 | 0 | 0 | 
+ |  |  | 0 | 1 | 0 | 1 | −1011_{2}
 |  | 1 | 0 | 0 | 0 | 1 |  | 0001_{2}
OF = 0
01.01_{2} −10.10_{2} |  | 1 | 1 | 0 |  | 0 | 0 | 
 |  | 0 | 1 | . | 0 | 1 | 
+ |  | 0 | 1 | . | 1 | 0 | −10.10_{2}
 | 1 | 1 | 0 | . | 1 | 1 |  | 10.11_{2}
OF = 1
1101_{2} −0101_{2} |  |  | 1 | 1 | 1 | 1 | 0 | 
 |  |  | 1 | 1 | 0 | 1 | 
+ |  |  | 1 | 0 | 1 | 1 | −0101_{2}
 |  | 1 | 1 | 0 | 0 | 0 |  | 1000_{2}
OF = 0
10_{2} −011_{2} |  |  | 1 | 1 | 0 | 0 | 0 | 
 |  |  | 1 | 1 | 1 | 0 | 
+ |  |  | 1 | 1 | 0 | 1 | -0011_{2}
 |  | 1 | 1 | 0 | 1 | 1 |  | 1011_{2}
OF = 0
435_{10} − 166_{10} |  |  | 1 | 1 | 0 | 0 | 0 | 
 |  |  | 0 | 4 | 3 | 5 | 
+ |  |  | 9 | 8 | 3 | 4 | -0166_{10}
 |  | 1 | 0 | 2 | 6 | 9 |  | 0269_{10}
OF = 0
A32F_{16} − 524_{16} |  |  | 1 | 0 | 1 | 1 | 0 | 
 |  |  | A | 3 | 2 | F | 
+ |  |  | F | A | D | C | − 524_{16}
 |  | 1 | 9 | E | 0 | B |  | 9E0B_{16}
OF = 0
8135_{16} − FA3B_{16} |  |  | 0 | 0 | 0 | 0 | 0 | 
 |  |  | 8 | 1 | 3 | 5 | 
+ |  |  | 0 | 5 | C | 5 | − FA3B_{16}
 |  | 0 | 8 | 6 | F | B |  | 86FB_{16}
OF = 0
364_{7} − 302_{7} |  |  | 0 | 0 | 0 | 0 | 0 | 
 |  |  | 6 | 3 | 5 | 4 | 
+ |  |  | 6 | 3 | 6 | 5 | − 302_{7}
 |  | 1 | 6 | 0 | 6 | 2 |  | 6062_{7}
OF = 0

**Ispravka:** \begin{longtable}{p{0.34\linewidth} p{0.34\linewidth} p{0.23\linewidth}}\toprule
Izraz & Sabiranje kodnih reči & Rezultat\\\midrule\endhead
$(010)_{2}-(1101)_{2}$ & $\begin{array}{r}c:\ 00100\\0010\\+0011\\\hline 0101\end{array}$ & $0101$\newline OF = 0\\[5pt]
$(11)_{2}-(010)_{2}$ & $\begin{array}{r}c:\ 11100\\1111\\+1110\\\hline 1101\end{array}$ & $1101$\newline OF = 0\\[5pt]
$(0110)_{2}-(0101)_{2}$ & $\begin{array}{r}c:\ 11100\\0110\\+1011\\\hline 0001\end{array}$ & $0001$\newline OF = 0\\[5pt]
$(1100)_{2}-(1011)_{2}$ & $\begin{array}{r}c:\ 11000\\1100\\+0101\\\hline 0001\end{array}$ & $0001$\newline OF = 0\\[5pt]
$(01.01)_{2}-(10.10)_{2}$ & $\begin{array}{r}c:\ 01000\\01.01\\+01.10\\\hline 10.11\end{array}$ & $10.11$\newline OF = 1\\[5pt]
$(1101)_{2}-(0101)_{2}$ & $\begin{array}{r}c:\ 11110\\1101\\+1011\\\hline 1000\end{array}$ & $1000$\newline OF = 0\\[5pt]
$(10)_{2}-(011)_{2}$ & $\begin{array}{r}c:\ 11000\\1110\\+1101\\\hline 1011\end{array}$ & $1011$\newline OF = 0\\[5pt]
$(435)_{10}-(166)_{10}$ & $\begin{array}{r}c:\ 11000\\0435\\+9834\\\hline 0269\end{array}$ & $0269$\newline OF = 0\\[5pt]
$(A32F)_{16}-(524)_{16}$ & $\begin{array}{r}c:\ 10110\\A32F\\+FADC\\\hline 9E0B\end{array}$ & $9E0B$\newline OF = 0\\[5pt]
$(8135)_{16}-(FA3B)_{16}$ & $\begin{array}{r}c:\ 00000\\8135\\+05C5\\\hline 86FA\end{array}$ & $86FA$\newline OF = 0\\[5pt]
$(364)_{7}-(302)_{7}$ & $\begin{array}{r}c:\ 11110\\6364\\+6365\\\hline 6062\end{array}$ & $6062$\newline OF = 0\\[5pt]
\bottomrule\end{longtable}

**Obrazloženje i uticaj:** Sve tabele ponovo su izvedene na četiri cifre, uz dekodiranje na izvornoj širini, proširenje znaka, negiranje umanjioca i kružni prenos za KMV. Detaljne pojedinačne razlike nalaze se u posebnom pregledu ispod.

### 04-17 — blok 97

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 518; `% Izvor DOCX: blok 97`.

**Izvor:** Izraz | Postupak | Rezultat
010_{2} +0011_{2} |  |  | 0 | 0 | 1 | 0 | 0 | 
 |  |  | 0 | 0 | 1 | 0 | 
+ |  |  | 0 | 0 | 1 | 1 | 
 |  | 0 | 0 | 1 | 0 | 1 | 
+ |  |  |  |  |  | 0 | 
 |  |  | 0 | 1 | 0 | 1 |  | 0101_{2} OF = 0
11_{2} +110_{2} |  |  | 1 | 1 | 1 | 0 | 0 | 
 |  |  | 1 | 1 | 1 | 1 | 
+ |  |  | 1 | 1 | 1 | 0 | 
 |  | 1 | 1 | 1 | 0 | 1 | 
+ |  |  |  |  |  | 1 | 
 |  |  | 1 | 1 | 1 | 0 |  | 1110_{2}
OF = 0
0110_{2} +1011_{2} |  |  | 1 | 1 | 1 | 0 | 0 | 
 |  |  | 0 | 1 | 1 | 0 | 
+ |  |  | 1 | 0 | 1 | 1 | 
 |  | 1 | 0 | 0 | 0 | 1 | 
+ |  |  |  |  |  | 1 | 
 |  |  | 0 | 0 | 1 | 0 |  | 0010_{2} OF = 0
1100_{2} +0101_{2} |  |  | 1 | 1 | 0 | 0 | 0 | 
 |  |  | 1 | 1 | 0 | 0 | 
+ |  |  | 0 | 1 | 0 | 1 | 
 |  | 1 | 0 | 0 | 0 | 1 | 
+ |  |  |  |  |  | 1 | 
 |  |  | 0 | 0 | 1 | 0 |  | 0010_{2}
OF = 0
0101_{2} +0110_{2} |  |  | 0 | 1 | 0 | 0 | 0 | 
 |  |  | 0 | 1 | 0 | 1 | 
+ |  |  | 0 | 1 | 1 | 0 | 
 |  | 0 | 1 | 0 | 1 | 1 | 
+ |  |  |  |  |  | 0 | 
 |  |  | 1 | 0 | 1 | 1 |  | 1011_{2}
OF = 1
1101_{2} +1011_{2} |  |  | 1 | 1 | 1 | 1 | 0 | 
 |  |  | 1 | 1 | 0 | 1 | 
+ |  |  | 1 | 0 | 1 | 1 | 
 |  | 1 | 1 | 0 | 0 | 0 | 
+ |  |  |  |  |  | 1 | 
 |  |  | 1 | 0 | 0 | 1 |  | 1001_{2}
OF = 0
1.0_{2} +10.1_{2} |  | 1 | 1 | 0 | 0 |  | 0 | 
 |  | 1 | 1 | 0 | . | 1 | 
+ |  | 1 | 1 | 1 | . | 0 | 
 | 1 | 1 | 0 | 1 | . | 1 | 
+ |  |  |  |  |  | 1 | 
 |  | 1 | 1 | 0 | . | 0 |  | 110.0_{2}
OF = 0
435_{10} + 834_{10} |  |  | 1 | 1 | 0 | 0 | 0 | 
 |  |  | 0 | 4 | 3 | 5 | 
+ |  |  | 9 | 8 | 3 | 4 | 
 |  | 1 | 0 | 2 | 6 | 9 | 
+ |  |  |  |  |  | 1 | 
 |  |  | 0 | 2 | 7 | 0 |  | 0270_{10}
OF = 0
A32F_{16} + 476_{16} |  |  | 0 | 0 | 0 | 1 | 0 | 
 |  |  | A | 3 | 2 | F | 
+ |  |  | 0 | 4 | 7 | 6 | 
 |  | 0 | A | 7 | A | 5 | 
+ |  |  |  |  |  | 0 | 
 |  |  | A | 7 | A | 5 |  | A7A5_{16}
OF = 0
324_{7} + 365_{7} |  |  | 1 | 1 | 1 | 1 | 0 | 
 |  |  | 0 | 3 | 2 | 4 | 
+ |  |  | 6 | 3 | 6 | 5 | 
 |  | 1 | 0 | 0 | 2 | 2 | 
+ |  |  |  |  |  | 1 | 
 |  |  | 0 | 0 | 2 | 3 |  | 0023_{7}
OF = 0

**Ispravka:** \begin{longtable}{p{0.34\linewidth} p{0.34\linewidth} p{0.23\linewidth}}\toprule
Izraz & Sabiranje kodnih reči & Rezultat\\\midrule\endhead
$(010)_{2}+(0011)_{2}$ & $\begin{array}{r}c:\ 00100\\0010\\+0011\\\hline 0101\\+0000\\\hline 0101\end{array}$ & $0101$\newline OF = 0\\[5pt]
$(11)_{2}+(110)_{2}$ & $\begin{array}{r}c:\ 00000\\0000\\+1110\\\hline 1110\\+0000\\\hline 1110\end{array}$ & $1110$\newline OF = 0\\[5pt]
$(0110)_{2}+(1011)_{2}$ & $\begin{array}{r}c:\ 11100\\0110\\+1011\\\hline 0001\\+0001\\\hline 0010\end{array}$ & $0010$\newline OF = 0\\[5pt]
$(1100)_{2}+(0101)_{2}$ & $\begin{array}{r}c:\ 11000\\1100\\+0101\\\hline 0001\\+0001\\\hline 0010\end{array}$ & $0010$\newline OF = 0\\[5pt]
$(0101)_{2}+(0110)_{2}$ & $\begin{array}{r}c:\ 01000\\0101\\+0110\\\hline 1011\\+0000\\\hline 1011\end{array}$ & $1011$\newline OF = 1\\[5pt]
$(1101)_{2}+(1011)_{2}$ & $\begin{array}{r}c:\ 11110\\1101\\+1011\\\hline 1000\\+0001\\\hline 1001\end{array}$ & $1001$\newline OF = 0\\[5pt]
$(1.0)_{2}+(10.1)_{2}$ & $\begin{array}{r}c:\ 11000\\111.0\\+110.1\\\hline 101.1\\+000.1\\\hline 110.0\end{array}$ & $110.0$\newline OF = 0\\[5pt]
$(435)_{10}+(834)_{10}$ & $\begin{array}{r}c:\ 11000\\0435\\+9834\\\hline 0269\\+0001\\\hline 0270\end{array}$ & $0270$\newline OF = 0\\[5pt]
$(A32F)_{16}+(476)_{16}$ & $\begin{array}{r}c:\ 00010\\A32F\\+0476\\\hline A7A5\\+0000\\\hline A7A5\end{array}$ & $A7A5$\newline OF = 0\\[5pt]
$(324)_{7}+(365)_{7}$ & $\begin{array}{r}c:\ 11110\\0324\\+6365\\\hline 0022\\+0001\\\hline 0023\end{array}$ & $0023$\newline OF = 0\\[5pt]
\bottomrule\end{longtable}

**Obrazloženje i uticaj:** Sve tabele ponovo su izvedene na četiri cifre, uz dekodiranje na izvornoj širini, proširenje znaka, negiranje umanjioca i kružni prenos za KMV. Detaljne pojedinačne razlike nalaze se u posebnom pregledu ispod.

### 04-18 — blok 99

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 550; `% Izvor DOCX: blok 99`.

**Izvor:** Izraz | Postupak | Rezultat
010_{2} −1101_{2} |  |  | 0 | 0 | 1 | 0 | 0 | 
 |  |  | 0 | 0 | 1 | 0 | 
+ |  |  | 0 | 0 | 1 | 0 | -1101_{2}
 |  | 0 | 0 | 1 | 0 | 0 | 
 |  |  |  |  |  | 0 | 
 |  |  | 0 | 1 | 0 | 0 |  | 0100_{2} OF = 0
11_{2} −010_{2} |  |  | 1 | 1 | 1 | 1 | 0 | 
 |  |  | 1 | 1 | 1 | 1 | 
+ |  |  | 1 | 1 | 0 | 1 | -0010_{2}
 |  | 1 | 1 | 1 | 0 | 0 | 
 |  |  |  |  |  | 1 | 
 |  |  | 1 | 1 | 0 | 1 |  | 1101_{2}
OF = 0
0110_{2} −0101_{2} |  |  | 1 | 1 | 1 | 0 | 0 | 
 |  |  | 0 | 1 | 1 | 0 | 
+ |  |  | 1 | 0 | 1 | 0 | −0101_{2}
 |  | 1 | 0 | 0 | 0 | 0 | 
 |  |  |  |  |  | 1 | 
 |  |  | 0 | 1 | 0 | 1 |  | 0001_{2} OF = 0
1100_{2} −1011_{2} |  |  | 1 | 1 | 0 | 0 | 0 | 
 |  |  | 1 | 1 | 0 | 0 | 
+ |  |  | 0 | 1 | 0 | 0 | −1011_{2}
 |  | 1 | 0 | 0 | 0 | 1 | 
 |  |  |  |  |  | 1 | 
 |  |  | 0 | 0 | 1 | 0 |  | 0001_{2}
OF = 0
01.01_{2} −10.10_{2} |  | 1 | 1 | 0 |  | 1 | 0 | 
 |  | 0 | 1 | . | 0 | 1 | 
+ |  | 0 | 1 | . | 0 | 1 | −10.10_{2}
 | 0 | 1 | 0 | . | 1 | 0 | 
 |  |  |  |  |  | 0 | 
 |  | 1 | 0 | . | 1 | 0 |  | 10.10_{2}
OF = 1
1101_{2} −0101_{2} |  |  | 1 | 0 | 0 | 0 | 0 | 
 |  |  | 1 | 1 | 0 | 1 | 
+ |  |  | 1 | 0 | 1 | 0 | −0101_{2}
 |  | 1 | 0 | 1 | 1 | 1 | 
 |  |  |  |  |  | 1 | 
 |  |  | 1 | 0 | 0 | 0 |  | 1000_{2}
OF = 0
10_{2} −011_{2} |  |  | 1 | 1 | 0 | 0 | 0 | 
 |  |  | 1 | 1 | 1 | 0 | 
+ |  |  | 1 | 1 | 0 | 0 | -0011_{2}
 |  | 1 | 1 | 0 | 1 | 0 | 
 |  |  |  |  |  | 1 | 
 |  |  | 1 | 0 | 1 | 1 |  | 1011_{2}
OF = 0
435_{10} − 166_{10} |  |  | 1 | 1 | 0 | 0 | 0 | 
 |  |  | 0 | 4 | 3 | 5 | 
+ |  |  | 9 | 8 | 3 | 3 | -0166_{10}
 |  | 1 | 0 | 2 | 6 | 8 | 
 |  |  |  |  |  | 1 | 
 |  |  | 0 | 2 | 6 | 9 |  | 0269_{10}
OF = 0
A32F_{16} − 524_{16} |  |  | 1 | 0 | 1 | 1 | 0 | 
 |  |  | A | 3 | 2 | F | 
+ |  |  | F | A | D | B | − 524_{16}
 |  | 1 | 9 | E | 0 | A | 
 |  |  |  |  |  | 1 | 
 |  |  | 9 | E | 0 | B |  | 9E0B_{16}
OF = 0
8135_{16} − FA3B_{16} |  |  | 0 | 0 | 0 | 0 | 0 | 
 |  |  | 8 | 1 | 3 | 5 | 
+ |  |  | 0 | 5 | C | 5 | − FA3B_{16}
 |  | 0 | 8 | 6 | F | B | 
 |  |  |  |  |  | 0 | 
 |  |  | 8 | 6 | F | B |  | 86FB_{16}
OF = 0
364_{7} − 302_{7} |  |  | 1 | 1 | 1 | 1 | 0 | 
 |  |  | 6 | 3 | 5 | 4 | 
+ |  |  | 6 | 3 | 6 | 4 | − 302_{7}
 |  | 1 | 6 | 0 | 6 | 1 | 
 |  |  |  |  |  | 1 | 
 |  |  | 6 | 0 | 6 | 2 |  | 6062_{7}
OF = 0

**Ispravka:** \begin{longtable}{p{0.34\linewidth} p{0.34\linewidth} p{0.23\linewidth}}\toprule
Izraz & Sabiranje kodnih reči & Rezultat\\\midrule\endhead
$(010)_{2}-(1101)_{2}$ & $\begin{array}{r}c:\ 00100\\0010\\+0010\\\hline 0100\\+0000\\\hline 0100\end{array}$ & $0100$\newline OF = 0\\[5pt]
$(11)_{2}-(010)_{2}$ & $\begin{array}{r}c:\ 00000\\0000\\+1101\\\hline 1101\\+0000\\\hline 1101\end{array}$ & $1101$\newline OF = 0\\[5pt]
$(0110)_{2}-(0101)_{2}$ & $\begin{array}{r}c:\ 11100\\0110\\+1010\\\hline 0000\\+0001\\\hline 0001\end{array}$ & $0001$\newline OF = 0\\[5pt]
$(1100)_{2}-(1011)_{2}$ & $\begin{array}{r}c:\ 11000\\1100\\+0100\\\hline 0000\\+0001\\\hline 0001\end{array}$ & $0001$\newline OF = 0\\[5pt]
$(01.01)_{2}-(10.10)_{2}$ & $\begin{array}{r}c:\ 01010\\01.01\\+01.01\\\hline 10.10\\+00.00\\\hline 10.10\end{array}$ & $10.10$\newline OF = 1\\[5pt]
$(1101)_{2}-(0101)_{2}$ & $\begin{array}{r}c:\ 10000\\1101\\+1010\\\hline 0111\\+0001\\\hline 1000\end{array}$ & $1000$\newline OF = 0\\[5pt]
$(10)_{2}-(011)_{2}$ & $\begin{array}{r}c:\ 11000\\1110\\+1100\\\hline 1010\\+0001\\\hline 1011\end{array}$ & $1011$\newline OF = 0\\[5pt]
$(435)_{10}-(166)_{10}$ & $\begin{array}{r}c:\ 11000\\0435\\+9833\\\hline 0268\\+0001\\\hline 0269\end{array}$ & $0269$\newline OF = 0\\[5pt]
$(A32F)_{16}-(524)_{16}$ & $\begin{array}{r}c:\ 10110\\A32F\\+FADB\\\hline 9E0A\\+0001\\\hline 9E0B\end{array}$ & $9E0B$\newline OF = 0\\[5pt]
$(8135)_{16}-(FA3B)_{16}$ & $\begin{array}{r}c:\ 00000\\8135\\+05C4\\\hline 86F9\\+0000\\\hline 86F9\end{array}$ & $86F9$\newline OF = 0\\[5pt]
$(364)_{7}-(302)_{7}$ & $\begin{array}{r}c:\ 11110\\6364\\+6364\\\hline 6061\\+0001\\\hline 6062\end{array}$ & $6062$\newline OF = 0\\[5pt]
\bottomrule\end{longtable}

**Obrazloženje i uticaj:** Sve tabele ponovo su izvedene na četiri cifre, uz dekodiranje na izvornoj širini, proširenje znaka, negiranje umanjioca i kružni prenos za KMV. Detaljne pojedinačne razlike nalaze se u posebnom pregledu ispod.

### 04-19 — zadatak 2.3, 1.0+10.1, osnova 2

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), celina navedena u naslovu stavke.

**Izvor:** 101.0_{2}
OF = 0

**Ispravka:** 101.1, OF=0

**Obrazloženje i uticaj:** Ispravljena krajnja kodna reč nezavisnim dekodiranjem i ponovnim kodiranjem tačnog rezultata.

### 04-20 — zadatak 2.3, 8135−FA3B, osnova 16

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), celina navedena u naslovu stavke.

**Izvor:** 86FB_{16}
OF = 0

**Ispravka:** 86FA, OF=0

**Obrazloženje i uticaj:** Ispravljena krajnja kodna reč nezavisnim dekodiranjem i ponovnim kodiranjem tačnog rezultata.

### 04-21 — zadatak 2.4, 8135−FA3B, osnova 16

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), celina navedena u naslovu stavke.

**Izvor:** 86FB_{16}
OF = 0

**Ispravka:** 86F9, OF=0

**Obrazloženje i uticaj:** Ispravljena krajnja kodna reč nezavisnim dekodiranjem i ponovnim kodiranjem tačnog rezultata.

### 04-22 — blok 108

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 626; `% Izvor DOCX: blok 108`.

**Izvor:** Izraz | Postupak | Rezultat
10110_{2} × 01010_{2} | I |  |  |  |  |  | 0 | 0 | 0 | 0 | 0 | (10110_{2} × 0_{2})
 |  |  |  | 1 | 0 | 1 | 1 | 0 |  | (10110_{2} × 1_{2})
 |  |  | 0 | 0 | 0 | 0 | 0 |  |  | (10110_{2} × 0_{2})
 |  | 1 | 0 | 1 | 1 | 0 |  |  |  | (10110_{2} × 1_{2})
+ | 0 | 0 | 0 | 0 | 0 |  |  |  |  | (10110_{2} × 0_{2})
 | 0 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 0 |  | 011011100_{2}
II |  |  |  |  |  | 0 | 0 | 0 | 0 | 0 | (početni zbir 0)
+ |  |  |  |  | 0 | 0 | 0 | 0 | 0 | (10110_{2} × 0_{2})
 |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 
+ |  |  |  | 1 | 0 | 1 | 1 | 0 |  | (10110_{2} × 1_{2})
 |  |  |  | 1 | 0 | 1 | 1 | 0 | 0 | 
+ |  |  | 0 | 0 | 0 | 0 | 0 |  |  | (10110_{2} × 0_{2})
 |  |  | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 
+ |  | 1 | 0 | 1 | 1 | 0 |  |  |  | (10110_{2} × 1_{2})
 |  | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 
+ | 0 | 0 | 0 | 0 | 0 |  |  |  |  | (10110_{2} × 0_{2})
 | 0 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 
110.01_{2} × 10.111_{2} | I |  |  |  |  |  | 1 | 1 | 0 | 0 | 1 | (11001_{2} × 1_{2})
 |  |  |  | 1 | 1 | 0 | 0 | 1 |  | (11001_{2} × 1_{2})
 |  |  | 1 | 1 | 0 | 0 | 1 |  |  | (11001_{2} × 1_{2})
 |  | 0 | 0 | 0 | 0 | 0 |  |  |  | (11001_{2} × 0_{2})
+ | 1 | 1 | 0 | 0 | 1 |  |  |  |  | (11001_{2} × 1_{2})
1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |  | 10001.11111_{2}
II |  |  |  |  |  | 0 | 0 | 0 | 0 | 0 | (početni zbir 0)
+ |  |  |  |  | 1 | 1 | 0 | 0 | 1 | (11001_{2} × 1_{2})
 |  |  |  |  | 1 | 1 | 0 | 0 | 1 | 
+ |  |  |  | 1 | 1 | 0 | 0 | 1 |  | (11001_{2} × 1_{2})
 |  |  | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 
+ |  |  | 1 | 1 | 0 | 0 | 1 |  |  | (11001_{2} × 1_{2})
 |  | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 
+ |  | 0 | 0 | 0 | 0 | 0 |  |  |  | (11001_{2} × 0_{2})
 |  | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 
+ | 1 | 1 | 0 | 0 | 1 |  |  |  |  | (11001_{2} × 1_{2})
1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 
0110.1_{2} × 1.0110_{2} | I |  |  |  |  |  | 0 | 0 | 0 | 0 | 0 | (11001_{2} × 0_{2})
 |  |  |  | 1 | 1 | 0 | 0 | 1 |  | (11001_{2} × 1_{2})
 |  |  | 1 | 1 | 0 | 0 | 1 |  |  | (11001_{2} × 1_{2})
 |  | 0 | 0 | 0 | 0 | 0 |  |  |  | (11001_{2} × 0_{2})
+ | 1 | 1 | 0 | 0 | 1 |  |  |  |  | (11001_{2} × 1_{2})
1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |  | 1000.11110_{2}
II |  |  |  |  |  | 0 | 0 | 0 | 0 | 0 | (početni zbir 0)
+ |  |  |  |  | 0 | 0 | 0 | 0 | 0 | (0110.1_{2} × 0_{2})
 |  |  |  |  | 0 | 0 | 0 | 0 | 0 | 
+ |  |  |  | 0 | 1 | 1 | 0 | 1 |  | (0110.1_{2} × 1_{2})
 |  |  | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 
+ |  |  | 0 | 1 | 1 | 0 | 1 |  |  | (0110.1_{2} × 1_{2})
 |  | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 
+ |  | 0 | 0 | 0 | 0 | 0 |  |  |  | (0110.1_{2} × 0_{2})
 |  | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 
+ | 0 | 1 | 1 | 0 | 1 |  |  |  |  | (0110.1_{2} × 1_{2})
 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 |

**Ispravka:** \noindent\textbf{$(10110)_{2}\times (01010)_{2}$}\par
\begin{longtable}{ccccc}\toprule
$j$ & $y_j$ & Težina & I: parcijalni proizvod & II: međuzbir\\\midrule\endhead
0 & 0 & 1 & $0000000000$ & $0000000000$\\[5pt]
1 & 1 & 2 & $0000101100$ & $0000101100$\\[5pt]
2 & 0 & 4 & $0000000000$ & $0000101100$\\[5pt]
3 & 1 & 8 & $0010110000$ & $0011011100$\\[5pt]
4 & 0 & 16 & $0000000000$ & $0011011100$\\[5pt]
\bottomrule\end{longtable}
\begin{equation}
(10110)_{2}\times (01010)_{2}=(0011011100)_{2}
\end{equation}
\noindent\textbf{$(110.01)_{2}\times (10.111)_{2}$}\par
\begin{longtable}{ccccc}\toprule
$j$ & $y_j$ & Težina & I: parcijalni proizvod & II: međuzbir\\\midrule\endhead
0 & 1 & 1 & $0000011001$ & $0000011001$\\[5pt]
1 & 1 & 2 & $0000110010$ & $0001001011$\\[5pt]
2 & 1 & 4 & $0001100100$ & $0010101111$\\[5pt]
3 & 0 & 8 & $0000000000$ & $0010101111$\\[5pt]
4 & 1 & 16 & $0110010000$ & $1000111111$\\[5pt]
\bottomrule\end{longtable}
\begin{equation}
(110.01)_{2}\times (10.111)_{2}=(10001.11111)_{2}
\end{equation}
\noindent\textbf{$(0110.1)_{2}\times (1.0110)_{2}$}\par
\begin{longtable}{ccccc}\toprule
$j$ & $y_j$ & Težina & I: parcijalni proizvod & II: međuzbir\\\midrule\endhead
0 & 0 & 1 & $0000000000$ & $0000000000$\\[5pt]
1 & 1 & 2 & $0000011010$ & $0000011010$\\[5pt]
2 & 1 & 4 & $0000110100$ & $0001001110$\\[5pt]
3 & 0 & 8 & $0000000000$ & $0001001110$\\[5pt]
4 & 1 & 16 & $0011010000$ & $0100011110$\\[5pt]
\bottomrule\end{longtable}
\begin{equation}
(0110.1)_{2}\times (1.0110)_{2}=(01000.11110)_{2}
\end{equation}

**Obrazloženje i uticaj:** Sačuvana oba načina računanja: svi pomereni parcijalni proizvodi (I) i svaki međuzbir (II). Ispravljeni kopirani pogrešni množenici u trećem primeru i pogrešni međurezultati; puna širina proizvoda dva petobitna broja je deset bita. Vrednosti tačnih krajnjih rezultata ostaju iste.

### 04-23 — blok 110

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 684; `% Izvor DOCX: blok 110`.

**Izvor:** Izraz | Postupak | Rezultat
10110_{2} × 01010_{2} | I |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | (10110_{2} × 0_{2} + EZ[NOTE EZ – Ekstenzija znaka])
 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 |  | (10110_{2} × 1_{2} + EZ)
 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  | (10110_{2} × 0_{2} + EZ)
 | 1 | 1 | 0 | 1 | 1 | 0 |  |  |  | (10110_{2} × 1_{2} + EZ)
+ | 0 | 0 | 0 | 0 | 0 |  |  |  |  | (10110_{2} × 0_{2} + EZ)
1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |  | 110011100_{2}
II |  |  |  |  |  | 0 | 0 | 0 | 0 | 0 | (početni zbir 0)
+ |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | (10110_{2} × 0_{2} + EZ)
 |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | (EZ)
+ |  |  | 1 | 1 | 0 | 1 | 1 | 0 |  | (10110_{2} × 1_{2} + EZ)
 |  | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | (EZ)
+ |  | 0 | 0 | 0 | 0 | 0 | 0 |  |  | (10110_{2} × 0_{2} + EZ)
 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | (EZ)
+ | 1 | 1 | 0 | 1 | 1 | 0 |  |  |  | (10110_{2} × 1_{2} + EZ)
1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | (EZ)
0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  | (10110_{2} × 0_{2} + EZ)
1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 
110.01_{2}× 10.111_{2} | I |  | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | (11001_{2} × 1_{2} + EZ)
 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |  | (11001_{2} × 1_{2} + EZ)
 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |  |  | (11001_{2} × 1_{2} + EZ)
 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  | (11001_{2} × 0_{2} + EZ)
+ | 0 | 0 | 1 | 1 | 1 |  |  |  |  | (11001_{2} × 1_{2} → DK[NOTE DK – Drugi komplement])
1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |  | 0001.11111_{2}
II |  |  |  |  |  | 0 | 0 | 0 | 0 | 0 | (početni zbir 0)
+ |  |  |  | 1 | 1 | 1 | 0 | 0 | 1 | (11001_{2} × 1_{2} + EZ)
 |  |  | 1 | 1 | 1 | 1 | 0 | 0 | 1 | (EZ)
+ |  |  | 1 | 1 | 1 | 0 | 0 | 1 |  | (11001_{2} × 1_{2} + EZ)
 |  | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | (EZ)
+ |  | 1 | 1 | 1 | 0 | 0 | 1 |  |  | (11001_{2} × 1_{2} + EZ)
 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | (EZ)
+ | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  | (11001_{2} × 0_{2} + EZ)
1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | (EZ)
0 | 0 | 0 | 1 | 1 | 1 |  |  |  |  | (11001_{2} × 1_{2} -> DK)
1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 
0110.1_{2}× 1.0110_{2} | I |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | (01101_{2} × 0_{2})
 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |  | (01101_{2} × 1_{2})
 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |  |  | (01101_{2} × 1_{2})
 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  | (01101_{2} × 0_{2})
+ | 1 | 0 | 0 | 1 | 1 |  |  |  |  | (01101_{2} × 1_{2} -> DK)
1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |  | 1011.11110_{2}
II |  |  |  |  |  | 0 | 0 | 0 | 0 | 0 | (početni zbir 0)
+ |  |  |  | 0 | 0 | 0 | 0 | 0 | 0 | (0110.1_{2} × 0_{2})
 |  |  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
+ |  |  | 0 | 0 | 1 | 1 | 0 | 1 |  | (0110.1_{2} × 1_{2})
 |  | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 
+ |  | 0 | 0 | 1 | 1 | 0 | 1 |  |  | (0110.1_{2} × 1_{2})
 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 
+ | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  | (0110.1_{2} × 0_{2})
0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 
1 | 1 | 0 | 0 | 1 | 1 |  |  |  |  | (0110.1_{2} × 1_{2})
1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |

**Ispravka:** \noindent\textbf{$(10110)_{2}\times (01010)_{2}$}\par
\begin{longtable}{ccccc}\toprule
$j$ & $y_j$ & Težina & I: parcijalni proizvod & II: međuzbir\\\midrule\endhead
0 & 0 & 1 & $0000000000$ & $0000000000$\\[5pt]
1 & 1 & 2 & $1111101100$ & $1111101100$\\[5pt]
2 & 0 & 4 & $0000000000$ & $1111101100$\\[5pt]
3 & 1 & 8 & $1110110000$ & $1110011100$\\[5pt]
4 & 0 & -16 & $0000000000$ & $1110011100$\\[5pt]
\bottomrule\end{longtable}
\begin{equation}
(10110)_{2}\times (01010)_{2}=(1110011100)_{2}\quad(\mathrm{KO})
\end{equation}
\noindent\textbf{$(110.01)_{2}\times (10.111)_{2}$}\par
\begin{longtable}{ccccc}\toprule
$j$ & $y_j$ & Težina & I: parcijalni proizvod & II: međuzbir\\\midrule\endhead
0 & 1 & 1 & $1111111001$ & $1111111001$\\[5pt]
1 & 1 & 2 & $1111110010$ & $1111101011$\\[5pt]
2 & 1 & 4 & $1111100100$ & $1111001111$\\[5pt]
3 & 0 & 8 & $0000000000$ & $1111001111$\\[5pt]
4 & 1 & -16 & $0001110000$ & $0000111111$\\[5pt]
\bottomrule\end{longtable}
\begin{equation}
(110.01)_{2}\times (10.111)_{2}=(00001.11111)_{2}\quad(\mathrm{KO})
\end{equation}
\noindent\textbf{$(0110.1)_{2}\times (1.0110)_{2}$}\par
\begin{longtable}{ccccc}\toprule
$j$ & $y_j$ & Težina & I: parcijalni proizvod & II: međuzbir\\\midrule\endhead
0 & 0 & 1 & $0000000000$ & $0000000000$\\[5pt]
1 & 1 & 2 & $0000011010$ & $0000011010$\\[5pt]
2 & 1 & 4 & $0000110100$ & $0001001110$\\[5pt]
3 & 0 & 8 & $0000000000$ & $0001001110$\\[5pt]
4 & 1 & -16 & $1100110000$ & $1101111110$\\[5pt]
\bottomrule\end{longtable}
\begin{equation}
(0110.1)_{2}\times (1.0110)_{2}=(11011.11110)_{2}\quad(\mathrm{KO})
\end{equation}

**Obrazloženje i uticaj:** Sačuvana oba načina računanja: svi pomereni parcijalni proizvodi (I) i svaki međuzbir (II). Ispravljeni kopirani pogrešni množenici u trećem primeru i pogrešni međurezultati; puna širina proizvoda dva petobitna broja je deset bita. Vrednosti tačnih krajnjih rezultata ostaju iste.

### 04-24 — blok 116

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 760; `% Izvor DOCX: blok 116`.

**Izvor:** Izraz | Postupak | Rezultat
11010111/1011 |  | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | : | 1 | 0 | 1 | 1 | = 10011
- | 1 | 0 | 1 | 1 |  |  |  |  | 1011_{2} × 1
 | 0 | 0 | 1 | 0 | 0 |  |  |  | Dopisana cifra 0
- |  | 0 | 0 | 0 | 0 |  |  |  | 1011_{2} × 0
 |  |  | 1 | 0 | 0 | 1 |  |  | Dopisana cifra 1
- |  |  | 0 | 0 | 0 | 0 |  |  | 1011_{2} × 0
 |  |  | 1 | 0 | 0 | 1 | 1 |  | Dopisana cifra 1
- |  |  |  | 1 | 0 | 1 | 1 |  | 1011_{2} × 1
 |  |  |  | 1 | 0 | 0 | 0 | 1 | Dopisana cifra 1
- |  |  |  |  | 1 | 0 | 1 | 1 | 1011_{2} × 1
 |  |  |  |  |  | 1 | 1 | 0 | Ostatak | 10011_{2}
1001101001/101 |  | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | : | 1 | 0 | 1 | = 01111011
- | 0 | 0 | 0 |  |  |  |  |  |  |  | 101_{2} × 0
 | 1 | 0 | 0 | 1 |  |  |  |  |  |  | Dopisana cifra 1
- |  | 1 | 0 | 1 |  |  |  |  |  |  | 101_{2} × 1
 |  | 1 | 0 | 0 | 1 |  |  |  |  |  | Dopisana cifra 1
- |  |  | 1 | 0 | 1 |  |  |  |  |  | 101_{2} × 1
 |  |  | 1 | 0 | 0 | 0 |  |  |  |  | Dopisana cifra 0
- |  |  |  | 1 | 0 | 1 |  |  |  |  | 101_{2} × 1
 |  |  |  | 0 | 1 | 1 | 1 |  |  |  | Dopisana cifra 1
- |  |  |  |  | 1 | 0 | 1 |  |  |  | 101_{2} × 1
 |  |  |  |  | 0 | 1 | 0 | 0 |  |  | Dopisana cifra 0
- |  |  |  |  |  | 0 | 0 | 0 |  |  | 101_{2} × 0
 |  |  |  |  |  | 1 | 0 | 0 | 0 |  | Dopisana cifra 0
- |  |  |  |  |  |  | 1 | 0 | 1 |  | 101_{2} × 1
 |  |  |  |  |  |  | 0 | 1 | 1 | 1 | Dopisana cifra 1
- |  |  |  |  |  |  |  | 1 | 0 | 1 | 101_{2} × 1
 |  |  |  |  |  |  |  |  | 1 | 0 | Ostatak | 1111011_{2}
10001011/1101 |  | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | : | 1 | 1 | 0 | 1 | = 01010
- | 0 | 0 | 0 | 0 |  |  |  |  |  | 1101_{2} × 0
 | 1 | 0 | 0 | 0 | 1 |  |  |  |  | Dopisana cifra 1
- |  | 1 | 1 | 0 | 1 |  |  |  |  | 1101_{2} × 1
 |  | 0 | 1 | 0 | 0 | 0 |  |  |  | Dopisana cifra 0
- |  |  | 0 | 0 | 0 | 0 |  |  |  | 1101_{2} × 0
 |  |  | 1 | 0 | 0 | 0 | 1 |  |  | Dopisana cifra 1
- |  |  |  | 1 | 1 | 0 | 1 |  |  | 1101_{2} × 1
 |  |  |  | 0 | 1 | 0 | 0 | 1 |  | Dopisana cifra 1
- |  |  |  |  | 0 | 0 | 0 | 0 |  | 1101_{2} × 0
 |  |  |  |  | 1 | 0 | 0 | 1 |  | Ostatak | 01010_{2}

**Ispravka:** \noindent\textbf{$11010111:1011$}\par
\begin{longtable}{ccccc}\toprule
Korak & Dopisani bit & Pre oduzimanja & Bit količnika & Ostatak\\\midrule\endhead
1 & 1 & $1$ & 0 & $1$\\[5pt]
2 & 1 & $11$ & 0 & $11$\\[5pt]
3 & 0 & $110$ & 0 & $110$\\[5pt]
4 & 1 & $1101$ & 1 & $10$\\[5pt]
5 & 0 & $100$ & 0 & $100$\\[5pt]
6 & 1 & $1001$ & 0 & $1001$\\[5pt]
7 & 1 & $10011$ & 1 & $1000$\\[5pt]
8 & 1 & $10001$ & 1 & $110$\\[5pt]
\bottomrule\end{longtable}
\begin{equation}
(11010111)_2=(1011)_2\cdot(10011)_2+(110)_2
\end{equation}
\noindent\textbf{$1001101001:101$}\par
\begin{longtable}{ccccc}\toprule
Korak & Dopisani bit & Pre oduzimanja & Bit količnika & Ostatak\\\midrule\endhead
1 & 1 & $1$ & 0 & $1$\\[5pt]
2 & 0 & $10$ & 0 & $10$\\[5pt]
3 & 0 & $100$ & 0 & $100$\\[5pt]
4 & 1 & $1001$ & 1 & $100$\\[5pt]
5 & 1 & $1001$ & 1 & $100$\\[5pt]
6 & 0 & $1000$ & 1 & $11$\\[5pt]
7 & 1 & $111$ & 1 & $10$\\[5pt]
8 & 0 & $100$ & 0 & $100$\\[5pt]
9 & 0 & $1000$ & 1 & $11$\\[5pt]
10 & 1 & $111$ & 1 & $10$\\[5pt]
\bottomrule\end{longtable}
\begin{equation}
(1001101001)_2=(101)_2\cdot(1111011)_2+(10)_2
\end{equation}
\noindent\textbf{$10001011:1101$}\par
\begin{longtable}{ccccc}\toprule
Korak & Dopisani bit & Pre oduzimanja & Bit količnika & Ostatak\\\midrule\endhead
1 & 1 & $1$ & 0 & $1$\\[5pt]
2 & 0 & $10$ & 0 & $10$\\[5pt]
3 & 0 & $100$ & 0 & $100$\\[5pt]
4 & 0 & $1000$ & 0 & $1000$\\[5pt]
5 & 1 & $10001$ & 1 & $100$\\[5pt]
6 & 0 & $1000$ & 0 & $1000$\\[5pt]
7 & 1 & $10001$ & 1 & $100$\\[5pt]
8 & 1 & $1001$ & 0 & $1001$\\[5pt]
\bottomrule\end{longtable}
\begin{equation}
(10001011)_2=(1101)_2\cdot(1010)_2+(1001)_2
\end{equation}

**Obrazloženje i uticaj:** Sva tri postupka deljenja preneta su korak po korak, uz eksplicitno navođenje ostatka: 110₂, 10₂ i 1001₂. Izvorna poslednja kolona navodi samo celobrojni količnik.

### 04-25 — blok 124

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 868; `% Izvor DOCX: blok 124`.

**Izvor:** * Odrediti vrednosti X, Y i Z:

**Ispravka:** a) Odrediti $X$ i $Y$. Za $X$ koristiti pet heksadecimalnih cifara, od toga dve razlomljene; za $Y$ zadržati šest ternarnih cifara:

**Obrazloženje i uticaj:** Z nije zadat nigde u izvorniku. Širine nisu navedene: uvedene su eksplicitne konvencije; 9³=3⁶ prirodno određuje širinu Y.

### 04-26 — blok 125

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 871; `% Izvor DOCX: blok 125`.

**Izvor:** X_(16KO )=  − 13.3125₁₀

  Y_(3KMV ) = 520_(9KO)

**Ispravka:** \begin{equation}
X_{16,\mathrm{KO}}=-13.3125_{10}
\end{equation}
\begin{equation}
Y_{3,\mathrm{KMV}}=(520)_{9,\mathrm{KO}}
\end{equation}

**Obrazloženje i uticaj:** Jednačine su prepisane iz izvornika u standardan matematički zapis; bez dodavanja rešenja.

### 04-27 — blok 126

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 880; `% Izvor DOCX: blok 126`.

**Izvor:** b) Naznačiti da li je dati iskaz tačan ili netačn, ukoliko je na raspolaganju 5 cifara

**Ispravka:** b) Naznačiti da li je sledeći iskaz tačan, uz pet bita za rezultate:

**Obrazloženje i uticaj:** Ispravljena gramatika i precizirana binarna širina.

### 04-28 — blok 127

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 883; `% Izvor DOCX: blok 127`.

**Izvor:** []

**Ispravka:** \begin{equation}
(10011)_{\mathrm{KMV}}+(11111)_{\mathrm{KMV}}=(10111)_{\mathrm{ZA}}-(01011)_{\mathrm{ZA}}
\end{equation}

**Obrazloženje i uticaj:** Formula iz WMF slike preneta kao izmenjiva jednačina; ovo je iskaz čiju tačnost student proverava, pa se njegova eventualna netačnost ne ispravlja.

### 04-29 — blok 129

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 894; `% Izvor DOCX: blok 129`.

**Izvor:** c) Naznačiti da li su dati iskazi tačni ili netačni, ukoliko je na raspolaganju proizvoljan broj cifara

**Ispravka:** c) Naznačiti da li su sledeći iskazi tačni, uz dovoljan broj cifara za rezultate:

**Obrazloženje i uticaj:** Sačuvan smisao provere iskaza; ispravljena gramatička formulacija.

### 04-30 — blok 130

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 897; `% Izvor DOCX: blok 130`.

**Izvor:** []

  []

**Ispravka:** \begin{equation}
(243)_{5,\mathrm{KO}}+(304)_{5,\mathrm{KO}}>(10100)_{2,\mathrm{KO}}\cdot(111000)_{2,\mathrm{KO}}
\end{equation}
\begin{equation}
(F243)_{16,\mathrm{KMV}}-(F279)_{16,\mathrm{KMV}}=(111100)_{\mathrm{ZA}}-(100111)_{\mathrm{ZA}}
\end{equation}

**Obrazloženje i uticaj:** Obe formule iz WMF slika prenete bez gubitka indeksa. Iskazi ostaju zadaci bez rešenja.

### 04-31 — blok 133

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 916; `% Izvor DOCX: blok 133`.

**Izvor:** * [IMAGE /tmp/de1-work/04/media/image4.png]Na slici 3.3.1 je predstavljen jedan dvobitni komparator. Realizovati četvorobitni komparator isključivo korišćenjem komparatora predstavljenog na slici i I, ILI i NI logičkih kola.

**Ispravka:** a) Na slici~\ref{fig:comp2} prikazan je dvobitni komparator. Realizovati četvorobitni komparator korišćenjem takvih komparatora i I, ILI i NI logičkih kola.

**Obrazloženje i uticaj:** Slika odvojena od teksta i povezana automatskom referencom.

### 04-32 — jednačina (3.3.1)

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 933; `\label{eq:3.3.1}`.

**Izvor:** RES=max(A, 2B, C/2)

**Ispravka:** \mathrm{RES}=\max\bigl(A,2B,\lfloor C/2\rfloor\bigr)

**Obrazloženje i uticaj:** Petobitni izlaz je celobrojan; deljenje sa 2 definiše se logičkim pomeranjem udesno. Izvor ne precizira odsecanje polovine za neparno C.

### 04-33 — blok 139

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 947; `% Izvor DOCX: blok 139`.

**Izvor:** * [IMAGE /tmp/de1-work/04/media/image5.png]Na slici 3.3.2 je predstavljena realizacija četvorobitnog komparatora korišćenjem dvobitnog komparatora sa slike 7 i I/ILI logičkih kola

**Ispravka:** a) Višu polovinu brojeva poredimo komparatorom H, a nižu komparatorom L. Ako su njihove zastavice $G$, $L$ i $E$ redom „veće“, „manje“ i „jednako“, važi
\[G=G_H+E_HG_L,\qquad E=E_HE_L,\qquad L=\overline{G+E}.\]
Realizacija je prikazana na slici~\ref{fig:comp4}. Završni NILI može se realizovati ILI kolom i NI kolom sa spojenim ulazima, pa se poštuje zadati skup kola.

**Obrazloženje i uticaj:** Dodata objašnjenja veza i izlaznih funkcija; ispravljena pogrešna referenca „slika 7“.

### 04-34 — blok 141

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 958; `% Izvor DOCX: blok 141`.

**Izvor:** * Na slici 3.3.3 je prikazana realizacija funkcije RES korišćenjem četvorobitnih komparatora.

**Ispravka:** b) Neka je $X=A$, $Y=\lfloor C/2\rfloor$ i $Z=2B$. Prvi četvorobitni komparator i multiplekser određuju $M=\max(X,Y)$. Drugi poredi $M$ sa $Z_{3:0}$. Petobitni izlaz bira $Z$ kada je $Z_4=1$ ili $Z_{3:0}>M$, a inače bira $0M$. Tako visoki bit broja $2B$ ne može biti izgubljen.

**Obrazloženje i uticaj:** Dopunjeno objašnjenje petobitnog poređenja sa četvorobitnim komparatorima.

### 04-35 — blok 144

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 972; `% Izvor DOCX: blok 144`.

**Izvor:** * Realizovati sabirač dva dvobitna binarna broja korišćenjem minimalnog broja osnovnih logičkih kola
* Korišćenjem sabirača iz tačke a) realizovati logičku funkciju:

**Ispravka:** \begin{enumerate}[label=\alph*),leftmargin=*]
\item Realizovati sabirač dva neoznačena dvobitna broja $A=(a_1a_0)_2$ i $B=(b_1b_0)_2$, minimizovanjem izlaznih funkcija. Prikazati i realizaciju kada su dostupna XOR kola.
\item Korišćenjem sabirača iz tačke a realizovati funkciju:
\end{enumerate}

**Obrazloženje i uticaj:** Definisani su ulazi i dozvoljena XOR varijanta; „minimalan broj kola“ zavisi od toga da li je XOR osnovni element.

### 04-36 — blok 147

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 992; `% Izvor DOCX: blok 147`.

**Izvor:** * Tabela 3.4.1 predstavlja funkcionalnu tabelu sabirača sa dva dvobitna ulaza.

**Ispravka:** a) Tabela~\ref{tab:adder} prikazuje sve ulazne kombinacije i zbir $S=A+B$.

**Obrazloženje i uticaj:** Ispravljena veza između oznaka ulaza tabele i šeme.

### 04-37 — tabela 3.4.1

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), celina navedena u naslovu stavke.

**Izvor:** Ulazi su a3,a2,a1,a0, a dalji tekst koristi a1,a0,b1,b0.

**Ispravka:** Kolone preimenovane u a1,a0,b1,b0, uz istih 16 redova.

**Obrazloženje i uticaj:** Tabela i izvedene funkcije sada koriste istu konvenciju.

### 04-38 — blok 149

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1032; `% Izvor DOCX: blok 149`.

**Izvor:** Na osnovu tabele 3.4.1 popunjavamo Karnoove karte, za svaki od izlaza posebno, kako bi izveli funkcije izlaza u minimalnoj formi. Na slici 3.4.1 je prikazan sadržaj Karnoove karte za svaki od izlaza dvoulaznog dvobitnog sabirača.

**Ispravka:** Iz tabele~\ref{tab:adder} popunjavamo Karnoove karte sa slike~\ref{fig:kmap}. Redovi su $a_1a_0$, a kolone $b_1b_0$, u Grejovom redosledu 00, 01, 11, 10.

**Obrazloženje i uticaj:** Preciziran raspored promenljivih u kartama.

### 04-39 — blok 151

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1041; `% Izvor DOCX: blok 151`.

**Izvor:** Za realizaciju funkcija izlaznih signala ćemo koristiti formu ZP koja se generiše preklapanjem oblasti koje su na slici 10 uokvirene plavim pravougaonicima. Dobijene funkcije su:

**Ispravka:** Grupisanjem jedinica dobijamo sledeće minimalne sume proizvoda:

**Obrazloženje i uticaj:** Uklonjena pogrešna referenca na sliku 10.

### 04-40 — jednačina (3.4.2)

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1045; `\label{eq:3.4.2}`.

**Izvor:** $s_{0} = \ b_{0}\overline{a_{0}}$ + $a_{0}\overline{b_{0}}$

**Ispravka:** s_0=\bar a_0b_0+a_0\bar b_0

**Obrazloženje i uticaj:** Ujednačena matematička notacija, zadržana funkcija.

### 04-41 — jednačina (3.4.3)

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1048; `\label{eq:3.4.3}`.

**Izvor:** $s_{1} = \ $ $a_{1}\overline{a_{0}}\overline{b_{1}} + a_{1}\overline{b_{1}}\overline{b_{0}} + \overline{a_{1}}\ \overline{a_{0}}b_{1} + b_{1}\overline{b_{0}}\ \overline{a_{1}} + \ \overline{a_{1}}a_{0}\overline{b_{1}}b_{0} + \ a_{1}a_{0}b_{1}b_{0}$

**Ispravka:** \begin{aligned}s_1={}&a_1\bar a_0\bar b_1+a_1\bar b_1\bar b_0+\bar a_1\bar a_0b_1\\&+\bar a_1b_1\bar b_0+\bar a_1a_0\bar b_1b_0+a_1a_0b_1b_0.\end{aligned}

**Obrazloženje i uticaj:** Funkcija proverena za svih 16 kombinacija; raspoređena u dva reda radi čitljivosti.

### 04-42 — jednačina (3.4.5)

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1060; `\label{eq:3.4.5}`.

**Izvor:** $s_{0} = \ $ $a_{0} \oplus b_{0}$

**Ispravka:** s_0=a_0\oplus b_0

**Obrazloženje i uticaj:** Uklonjeno razdvajanje jedne formule na više Word matematičkih objekata.

### 04-43 — jednačina (3.4.6)

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1063; `\label{eq:3.4.6}`.

**Izvor:** $s_{1} = \ $ $a_{0}b_{0} \oplus (a_{1}b_{1})$

**Ispravka:** s_1=(a_1\oplus b_1)\oplus(a_0b_0)

**Obrazloženje i uticaj:** U izvorniku stoji a0b0 XOR (a1b1), što nije bit zbira; potreban je XOR viših bita.

### 04-44 — blok 153

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1056; `% Izvor DOCX: blok 153`.

**Izvor:** Funkcije (3.4.2 – 3.4.4) se mogu realizovati u još minimalnijoj formi ukoliko su na raspolaganju XOR kola. Uprošćene funkcije su

**Ispravka:** Kada su na raspolaganju XOR kola, dobijamo kompaktniju realizaciju. Zajednički signal $p_1=a_1\oplus b_1$ koristi se i za $s_1$ i za prenos:

**Obrazloženje i uticaj:** Izbegnuta neodređena formulacija „još minimalnija forma“ i omogućeno deljenje zajedničkog signala.

### 04-45 — jednačina (3.4.7)

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1066; `\label{eq:3.4.7}`.

**Izvor:** $s_{2} = \ b_{1}a_{1} + a_{0}b_{0}(b_{1} + a_{1})$

**Ispravka:** s_2=a_1b_1+(a_0b_0)(a_1+b_1)=a_1b_1+(a_0b_0)p_1

**Obrazloženje i uticaj:** Dodato ekvivalentno faktorisanje koje deli p1 sa bitom s1; provereno iscrpno.

### 04-46 — blok 155

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1071; `% Izvor DOCX: blok 155`.

**Izvor:** [IMAGE /tmp/de1-work/04/media/image7.png]Na slici 3.4.2 je prikazana realizacija dvoulaznog dvobitnog sabirača, sa ulazima A(a_{1}a_{0}) i B(b_{1}b_{0}), dobijena na osnovu funkcija (3.4.5– 3.4.7).

**Ispravka:** Na slici~\ref{fig:adder} prikazana je realizacija sa tri XOR, tri I i jednim ILI kolom. Ulazi su $A=(a_1a_0)_2$ i $B=(b_1b_0)_2$.

**Obrazloženje i uticaj:** Šema koristi ispravljenu funkciju s1 i zajednički p1.

### 04-47 — jednačina (3.4.9)

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1099; `\label{eq:3.4.9}`.

**Izvor:** X=S(B+1)

**Ispravka:** S=A+1,\qquad X=S(B+1)

**Obrazloženje i uticaj:** S je izlaz sabirača kome se dovode A i konstanta 1; definicija nedostaje uz izvornu jednačinu.

### 04-48 — blok 164

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1119; `% Izvor DOCX: blok 164`.

**Izvor:** | ako je B = 0, tada je X=S | (3.4.10)
 | ako je B = 1, tada je X = 2S | (3.4.11)
 | ako je B = 2, tada je X = 3S
Ako je B = 3, tada je X = 4S | (3.4.12)
(3.4.13)

**Ispravka:** \begin{equation}\label{eq:3.4.10}
B=0\quad\Longrightarrow\quad X=S
\end{equation}
\begin{equation}\label{eq:3.4.11}
B=1\quad\Longrightarrow\quad X=2S
\end{equation}
\begin{equation}\label{eq:3.4.12}
B=2\quad\Longrightarrow\quad X=3S
\end{equation}
\begin{equation}\label{eq:3.4.13}
B=3\quad\Longrightarrow\quad X=4S
\end{equation}

**Obrazloženje i uticaj:** Razdvojene četiri grane koje su delom spojene u jednoj Word ćeliji; sačuvan svaki slučaj.

### 04-49 — blok 165

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1134; `% Izvor DOCX: blok 165`.

**Izvor:** [IMAGE /tmp/de1-work/04/media/image8.png]Dakle, vrednost dvobitnog broja B(b_{1}b_{0}) određuje koja od funkcija (S, 2S, 3S ili 4S) će biti dodeljena funkciji X. Ovakva (selekciona) logika se najlakše realizuje korišćenjem multipleksera 4/1. Pre nego predstavimo način povezivanja multipleksera, neophodno je prodiskutovati o širini ulaznih i izlaznih linija multipleksera. U prethodnoj tački smo videli da je za predtavljanje rezltata sabiranja dva dvobitna broja potrebno minimum 3 bita zbog toga što je najveći broj koji se dobija sabiranjem dva neoznačena dvobitna broja jednak 6. Pošto je u slučaju realizacije ove tačke zadatka na jedan ulaz sabirača (ulaz A) doveden neoznačeni dvobitni broj A(a_{1}a_{0}) a na drugi ulaz (ulaz B) konstanta 1 (b_{1}b_{0} = 01), jasno je da se kao najveća vrednost rezultata sabiranja može obiti broj 4. Množenjem ovog rezultata sa brojem 2 (2.24), najveći broj koji se može dobiti u slučaju B=1 je 8 i za predstavu ovog rezltata nam je potrebno 4 bita. U slučaju množenja izlaza sabirača S sa 3, najveći rezultat koji možemo dobiti je 12, što se takođe može predstaviti sa 4 bita, dok je u slučaju množenja izlaza sabirača sa brojem 4 najveći očekivani rezultat 16 za čiju predstavu nam je potrebno 5 bita. Pošto su širine ulaznih i izlaznih linija određene rezultatom za čiju predstavu nam je potrebno najviše bita, jasno je da moramo uzeti multiplekser čija je širina ulaznih i izlaznih linija jednaka 5. Opisani multiplekser je predstavljen na slici 3.4.3

**Ispravka:** Vrednost $B=(b_1b_0)_2$ bira jedan od ulaza $S,2S,3S,4S$ multipleksera 4/1. Pošto je $1\le S=A+1\le4$, maksimalne vrednosti ovih ulaza su 4, 8, 12 i 16. Zato svi podatkovni ulazi i izlaz multipleksera imaju pet bita; kraći zapisi dopunjavaju se vodećim nulama. Multiplekser je prikazan na slici~\ref{fig:mux4}.

**Obrazloženje i uticaj:** Sačuvano celokupno obrazloženje širina, uklonjene tipografske greške i pogrešna referenca 2.24.

### 04-50 — blok 167

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1143; `% Izvor DOCX: blok 167`.

**Izvor:** Pre nego predstavimo način na koji je multiplekser iskorišćen za realizaciju logike opisane sa (3.4.8 do 3.4.9) potrebno je izvršiti analizu načina za generisanje ulaznih signala D_{0}, D_{1}, D_{2} i D_{3}. Generisanje signala opisanih u (3.4.10), (3.4.11) i (3.4.13) se realizuje jednostavnim pomeranjem za 0, 1 i 2 mesta u levo, respektivno. Međutim, za generisanje ulaznog signala D_{2} (za slučaj B = 2) nije moguće koristiti vrednost dobijenu na izlazu sabirača već je potrebno realizovati kombinacionu mrežu koja se dobija na osnovu sadržaja kobinacione tabele 3.4.2

**Ispravka:** Ulazi $D_0=S$, $D_1=2S$ i $D_3=4S$ dobijaju se pomeranjem i dopunjavanjem nulama. Ulaz $D_2=3(A+1)$ može se dobiti i sabiranjem $S+2S$; ovde ga realizujemo direktno iz dvobitnog ulaza $A$, prema tabeli~\ref{tab:triS}.

**Obrazloženje i uticaj:** Izvor netačno tvrdi da nije moguće koristiti vrednost izlaza sabirača; direktna kombinaciona realizacija jeste izbor, a ne jedina mogućnost.

### 04-51 — blok 169

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1163; `% Izvor DOCX: blok 169`.

**Izvor:** Na osnovu Tabele 3.4.3 dobijamo funkcije izlaznih signala kombinacione mreže (ulazni signali multipleksera)

**Ispravka:** Iz tabele~\ref{tab:triS} dobijamo:

**Obrazloženje i uticaj:** Ispravljena referenca na tabelu 3.4.3 umesto 3.4.2.

### 04-52 — blok 170

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1166; `% Izvor DOCX: blok 170`.

**Izvor:** | $D_{2 - 4} = 0$ | (3.4.14)
 | $D_{2 - 3} = a_{1}$ | (3.4.15)
 | $D_{2 - 2} = a_{0}$
$D_{2 - 1} = \overline{a_{1}}$ | (3.4.16)
(3.4.17)
 | $D_{2 - 0} = \overline{a_{0}}$ | (3.4.18)

**Ispravka:** \begin{equation}\label{eq:3.4.14}
D_{2,4}=0
\end{equation}
\begin{equation}\label{eq:3.4.15}
D_{2,3}=a_1
\end{equation}
\begin{equation}\label{eq:3.4.16}
D_{2,2}=a_0
\end{equation}
\begin{equation}\label{eq:3.4.17}
D_{2,1}=\bar a_1
\end{equation}
\begin{equation}\label{eq:3.4.18}
D_{2,0}=\bar a_0
\end{equation}

**Obrazloženje i uticaj:** Svaka bit-funkcija ima sopstvenu oznaku; svih četiri izlaznih reči provereno prema 3(A+1).

### 04-53 — blok 171

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1184; `% Izvor DOCX: blok 171`.

**Izvor:** Na slici 3.4.4 je je predstavljen deo kombinacione mreže koji realizuje funkciju X.

**Ispravka:** Na slici~\ref{fig:x} prikazano je generisanje funkcije $X$.

**Obrazloženje i uticaj:** Ispravljeno ponavljanje „je je“ i referenca.

### 04-54 — blok 173

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1193; `% Izvor DOCX: blok 173`.

**Izvor:** Za realizaciju kompletne funkcije (3.4.1) neophodno je implementirati logiku koja na osnovu poređenja dva neoznačena dvobitna broja A i B generiše izlaznu funkciju Y, tj. ukoliko je $A < B$ funkcija Y uzima vrednost X dok u suprotnom uzima vrednost 2X. Za realizaciju logike proeđenja dva neoznačena binarna broja, koristićemo komparator (kao u prethodnom zadatku) koji realizuje funkcionalnost poređenja dva neoznačena broja. Rezultat poređenja ($A\  > B$) ćemo iskoristiti kao selekcioni signal multipleksera 2/1 kojim se definiše vrednost funkcije Y. Množenje sa 2 smo realizovali koristeći istu logiku kao i u slučaju generisanja signala X.

**Ispravka:** Za konačan izlaz, šestobitni multiplekser bira $0X$ kada je $A\le B$, odnosno $X0=2X$ kada je $A>B$. Zatim se svih šest izlaznih bita maskira signalom $\overline{E}$, gde je $E=(A=B)$. Time je pri jednakosti izlaz nula, što je zasebna grana zadate funkcije. Šestobitna unutrašnja putanja omogućava neposredno pomeranje celog petobitnog $X$; za dozvoljene parove $A\ne B$ najveća izlazna vrednost je 24, pa je najviši izlazni bit uvek nula.

**Obrazloženje i uticaj:** Izvorni tekst izostavlja granu jednakosti iako je šema sadrži. Dopunjena maska i obrazložena širina izlaza.

### 04-55 — blok 174

**Novo mesto:** [LaTeX](04_aritmeticke_operacije.tex), red 1196; `% Izvor DOCX: blok 174`.

**Izvor:** Na slici 3.4.4 je predstavljena implementirana kombinaciona mreža.

**Ispravka:** Kompletna realizacija prikazana je na slici~\ref{fig:y}.

**Obrazloženje i uticaj:** Otklonjena duplirana oznaka slike 3.4.4.

## Jezik, oznake i prelom

Ujednačeni su izrazi „razlomljeni deo“, „proširenje znaka“, nazivi predstava, razmaci, interpunkcija i dijakritika. Ispravljene su tipografske greške navedene u tekstu (npr. „ne promenjen“, „ospegu“, „prebaivanje“). Ručne reference zamenjene su automatskim; Word tabele za raspored jednačina zamenjene su matematičkim okruženjima. Naslovna strana i autorstvo usklađeni su sa vežbama 01 i 02 po dogovoru.

## Provera i ograničenja

`make check` proverava sve prenose, pozajmice, parcijalne proizvode, međuzbirove, količnike i ostatke iz `code/rezultati.json`, kao i veze rezultata sa LaTeX tekstom. Svi ulazi dvobitnog sabirača i obe složene funkcije proveravaju se iscrpno.

Postavka samostalnog zadatka 3.2 je dopunjena širinom zapisa X, jer ga izvor ne određuje; to je jasno navedena urednička pretpostavka. Netačni iskazi dati radi studentske provere ostaju nepromenjeni. Rešenja samostalnih zadataka 3.1, 3.2, 3.5 i 3.6 nisu dodata. Postojeća rešenja 3.3 i 3.4 su preneta.

## Dodatna provera izgleda nakon konverzije

Diskretna siva linija razdvaja susedne redove podataka. Uz `\toprule`, `\midrule` i `\bottomrule` ne dodaje se druga, tanka linija. Vidljivi tekst „oprule“ bio je artefakt konverzije: Python je početak `\toprule` protumačio kao tabulator (`\t`). Ispravljen je LaTeX zapis komande; sama komanda iz paketa booktabs crta gornju ivicu tabele i ne treba da se vidi kao tekst. Ovo su ispravke nastalog LaTeX dokumenta, a ne greške DOCX izvornika.

Karnoove karte imaju tačno četiri reda i četiri kolone; mreža je usklađena sa skalom koordinata. Razmaknute su ulazne oznake logičkih kola i oznake grana D₂/D₃ na slici realizacije proizvoda. Funkcije su proverene za sve ulaze.
