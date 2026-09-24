# Izveštaj o ispravkama — vežbe 03

Vrsta izmene vidi se iz obrazloženja: računska/stručna greška, dopunsko pojašnjenje ili jezička i tipografska obrada. Stavke koje preciziraju konvenciju ili dodaju obrazloženje nisu predstavljene kao greške izvornika. Proračuni i promenjene formule dati su uz pojedinačne stavke; ponovljive provere su u [code/provera.py](code/provera.py). Izvorne oznake povezane su sa novim mestima u [inventaru](INVENTAR.md).

## Pojedinačne ispravke i pojašnjenja

### 03-01 — blok 32

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 81; `% Izvor DOCX: blok 32`.

**Izvor:** Broj D prikazan sa n cifara u osnovi r zapisujemo na sledeći način:

**Ispravka:** Broj $D$ sa $n$ cifara celog i $k$ cifara razlomljenog dela u osnovi $r$ zapisujemo kao:

**Obrazloženje i uticaj:** Broj cifara celog dela i ukupan broj cifara nisu ista veličina.

### 03-02 — blok 33

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 84; `% Izvor DOCX: blok 33`.

**Izvor:** $D_{r}$

**Ispravka:** \begin{equation}
D=(d_{n-1}\dots d_0.d_{-1}\dots d_{-k})_r
\end{equation}

**Obrazloženje i uticaj:** Dopunjen je nepotpun pozicioni zapis broja.

### 03-03 — blok 34

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 90; `% Izvor DOCX: blok 34`.

**Izvor:** gde su $d_{n - 1}d_{n - 2}\ldots d_{1}d_{0}.d_{- 1}d_{- 2}\ldots d_{- k + 1}d_{- k}$ cifre broja D u osnovi r. $D_{n - 1}$ nazivamo cifrom najveće težine u posmatranoj osnovi r. Skup vrednosti svake od cifara u brojnom sistemu r je:

**Ispravka:** gde su $d_i$ cifre broja $D$, a $d_{n-1}$ cifra najveće težine. Za osnovu važi $r\in\mathbb{Z}$, $r\ge2$, a skup dozvoljenih cifara je:

**Obrazloženje i uticaj:** Ispravljeno veliko D u oznaci cifre i eksplicitno naveden domen osnove.

### 03-04 — jednačina (1.1.1.3)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 143; `\label{eq:1.1.1.3}`.

**Izvor:** $\ \sum_{i = - k}^{n - 1}{d_{i}r^{i}} = \ \sum_{i = - K}^{N - 1}{d_{i}p^{i}}$

**Ispravka:** \sum_{i=-k}^{n-1}d_i r^i=\sum_{j=-K}^{N-1}e_j p^j

**Obrazloženje i uticaj:** Cifre istog broja u različitim osnovama uglavnom nisu jednake; druga predstava koristi e_j.

### 03-05 — jednačina (1.1.1.4)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 154; `\label{eq:1.1.1.4}`.

**Izvor:** $\ \sum_{i = - k}^{n - 1}{d_{i}r^{i}} = {(d_{- k}r^{- k} + \ d_{- k + 1}r^{- k + 1} + \ldots + \ d_{n - 2}r^{n - 2} + \ d_{n - 1}r^{n - 1})}_{10}$

**Ispravka:** D=\sum_{i=-k}^{n-1}d_i r^i=d_{-k}r^{-k}+\dots+d_0+\dots+d_{n-1}r^{n-1}

**Obrazloženje i uticaj:** Sažet raspored iste sume, bez promene sadržaja.

### 03-06 — jednačina (1.1.1.5)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 197; `\label{eq:1.1.1.5}`.

**Izvor:** ${(d_{n - 1}d_{n - 2}\ldots d_{1}d_{0})}_{r} = \ \sum_{i = 0}^{n - 1}{d_{i}r^{i}} = \ d_{0} + r(d_{1} + r(d_{2} + r(\ldots + r(d_{n - 2} + rd_{n - 1}))))\ $

**Ispravka:** I=\sum_{i=0}^{n-1}d_i r^i=d_0+r\bigl(d_1+r(d_2+\dots+r d_{n-1})\bigr)

**Obrazloženje i uticaj:** I označava ceo deo; Hornerov oblik zadržava sve cifre i omogućava čitljiv prelom.

### 03-07 — jednačina (1.1.1.6)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 221; `\label{eq:1.1.1.6}`.

**Izvor:** $D_{10} = {(o_{i}o_{i - 1}\ldots o_{1}o_{0})}_{r}\ $

**Ispravka:** I=(o_i o_{i-1}\dots o_1)_r

**Obrazloženje i uticaj:** Ostaci u algoritmu počinju od o_1, pa ne postoji o_0.

### 03-08 — blok 56

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 226; `% Izvor DOCX: blok 56`.

**Izvor:** Do algoritma za prebacivanje izlomljenog dela broja možemo doći na sličan način polazeći od jednačine (1.1.4).

**Ispravka:** Do algoritma za konverziju razlomljenog dela dolazimo iz jednačine~\eqref{eq:1.1.1.4}:

**Obrazloženje i uticaj:** Ispravljena nepostojeća referenca (1.1.4).

### 03-09 — jednačina (1.1.1.7)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 230; `\label{eq:1.1.1.7}`.

**Izvor:** ${(d_{- 1}d_{- 2}\ldots d_{- k + 1}d_{k})}_{r} = \ \sum_{i = - k}^{- 1}{d_{i}r^{i}} = \ r^{- 1}(d_{- 1} + r^{- 1}(d_{- 2} + r^{- 1}(\ldots + r^{- 1}(d_{- k + 1} + r^{- 1}d_{- k}))))\ $

**Ispravka:** F=(0.d_{-1}\dots d_{-k})_r=r^{-1}\bigl(d_{-1}+r^{-1}(d_{-2}+\dots+r^{-1}d_{-k})\bigr)

**Obrazloženje i uticaj:** Dodati 0 i tačka i ispravljen indeks poslednje cifre d_k u d_{-k}.

### 03-10 — blok 59

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 240; `% Izvor DOCX: blok 59`.

**Izvor:** * razlomljeni deo broja u osnovi 10 se pomnoži sa brojem r čime se dobija proizvod p_{1} gde s_{1} predstavlja ceo deo broja p_{1} a f_{1} predstavlja razlomljeni deo broja p_{1}
* ukoliko je f_{1 } različit od 0, u sledećem koraku se f_{1} množi sa r, čime se dobija proizvod p_{1} gde s_{2} predstavlja ceo deo broja p_{2} a f_{2} predstavlja razlomljeni deo broja p_{2}
* postupak se nastavlja sve dok razlomljeni deo f_{j} proizvoda p_{j} ne bude jednak 0 kada će s_{j }biti ceo deo proizvoda p_{j}
* cifre razlomljenog dela broja u osnovi r se dobijaju tako što se celi delovi proizvoda s_{j} čitaju u poretku u kom su i dobijeni, odnosno:

**Ispravka:** \begin{enumerate}[label=\arabic*),leftmargin=*]
\item Početni razlomljeni deo $f_0=F$ pomnoži se sa $r$: $p_1=rf_0=s_1+f_1$, gde je $s_1=\lfloor p_1\rfloor$ i $0\le f_1<1$.
\item Ako je $f_1\ne0$, izračuna se $p_2=rf_1=s_2+f_2$ i postupak se ponavlja.
\item Postupak se završava kada je $f_j=0$. Ako se neki ostatak ponovi, zapis je periodičan; za konačnu aproksimaciju unapred se zadaje broj cifara.
\item Cifre $s_1,s_2,\dots$ čitaju se redosledom računanja.
\end{enumerate}

**Obrazloženje i uticaj:** Ispravljen indeks p_1/p_2; algoritam ne mora da se završi nulom za razlomke koji imaju beskonačan zapis u ciljnoj osnovi.

### 03-11 — jednačina (1.1.1.8)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 249; `\label{eq:1.1.1.8}`.

**Izvor:** ${0.D}_{10} = {(s_{1}s_{2}\ldots s_{j - 1}s_{j})}_{r}\ $

**Ispravka:** F=(0.s_1s_2\dots s_j)_r

**Obrazloženje i uticaj:** Razlomljeni deo mora imati vodeću nulu i tačku.

### 03-12 — jednačina (1.1.1.9)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 260; `\label{eq:1.1.1.9}`.

**Izvor:** $D_{10} = o_{i}o_{i - 1}\ldots o_{1}o_{0}.{s_{1}s_{2}\ldots s_{j - 1}s_{j}}_{r}\ $

**Ispravka:** D=(o_io_{i-1}\dots o_1.s_1s_2\dots s_j)_r

**Obrazloženje i uticaj:** Usklađeno indeksiranje cifara celog i razlomljenog dela; konačan zapis važi kada se postupak završi.

### 03-13 — blok 64

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 269; `% Izvor DOCX: blok 64`.

**Izvor:** Algoritam za prebacivanje brojeva iz osnova koje su stepen broja 2 u brojni sistem čija je osnova takođe stepen broja 2, tj. $A_{2^{r_{1}}} \rightarrow$ $B_{r^{2}}$, se sastoji od sledećih koraka:

**Ispravka:** Za konverziju između osnova $2^{r_1}$ i $2^{r_2}$ koristi se binarni zapis kao međukorak:

**Obrazloženje i uticaj:** Ispravljena pogrešna oznaka ciljne osnove r² umesto 2^{r_2}.

### 03-14 — blok 65

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 272; `% Izvor DOCX: blok 65`.

**Izvor:** * broj A se prebaci u binarni zapis tako što se svaka cifra broja A prevodi u r_{1} binarnih cifara
* u odnosu na decimalnu tačku se grupišu binarne cifre u grupe od po r_{2} cifara
* binarne cifre u grupi od po r_{2} cifara se prevode u odgovarajuće cifre u osnovi r_{2}

**Ispravka:** \begin{enumerate}[label=\arabic*),leftmargin=*]
\item Svaku cifru polaznog zapisa prevesti u grupu od $r_1$ bita.
\item Od tačke grupisati bite u grupe od $r_2$ bita: ulevo za ceo, a udesno za razlomljeni deo. Nepotpune spoljne grupe dopuniti nulama.
\item Svaku grupu prevesti u jednu cifru osnove $2^{r_2}$.
\end{enumerate}

**Obrazloženje i uticaj:** Ispravljena ciljna osnova i dopunjeno pravilo dopunjavanja grupa nulama.

### 03-15 — jednačina (1.2.1.1)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 312; `\label{eq:1.2.1.1}`.

**Izvor:** $D\  \in \{ + \left( 2^{n - 1} - 1 \right),\ \ldots,\  + \left( 2^{n - 1} - 1 \right)\}$

**Ispravka:** D\in\{-(2^{n-1}-1),\dots,0,\dots,2^{n-1}-1\}

**Obrazloženje i uticaj:** Izvor ima pozitivnu donju i gornju granicu; donja granica mora biti negativna.

### 03-16 — blok 74

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 326; `% Izvor DOCX: blok 74`.

**Izvor:** Za brojni sistem sa osnovom r i datim brojem cifara n, predstava negativnog broja -D u komplementu maksimalne vrednosti se dobija na osnovu sledeće relacije:

**Ispravka:** Za nenegativnu apsolutnu vrednost $D$ i $n$ cifara u osnovi $r$, kodna reč negativnog broja u komplementu maksimalne vrednosti (KMV) dobija se kao:

**Obrazloženje i uticaj:** Razdvojena je matematička vrednost od njene kodne reči; D je apsolutna vrednost.

### 03-17 — jednačina (1.2.2.1)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 330; `\label{eq:1.2.2.1}`.

**Izvor:** $- D \equiv M - \ D$

**Ispravka:** \operatorname{KMV}_n(-D)=M-D

**Obrazloženje i uticaj:** Oznaka funkcije kodiranja izbegava tumačenje kodne reči kao obične jednake nenegativne vrednosti.

### 03-18 — jednačina (1.2.2.4)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 373; `\label{eq:1.2.2.4}`.

**Izvor:** $D\  \in \{ - \left( \frac{r^{n}}{2} - 1 \right),\ \ldots, + \left( \frac{r^{n}}{2} - 1 \right)\}$

**Ispravka:** D\in\left\{-\left(\frac{r^n}{2}-1\right),\dots,\frac{r^n}{2}-1\right\},\qquad r\ \text{parno}

**Obrazloženje i uticaj:** Izvorna formula celobrojnog opsega zahteva parnu osnovu; primenjena je na osnove 2, 8, 10 i 16.

### 03-19 — blok 85

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 383; `% Izvor DOCX: blok 85`.

**Izvor:** U slučaju binarnog brojnog sistema (r = 2) ova predstava se naziva komplement jedinice ili prvi komplement. Tada, na osnovu relacije 1.2.2.3, možemo izvesti zaključak da se biti predstave negativnog broja D, u komplementu maksimalne vrednosti, dobijaju komplementiranjem bita d_{n-1}d_{n-2}…d_{1}d_{0} negativnog broja D, odnosno:

**Ispravka:** U binarnom sistemu ($r=2$) ovo je komplement jedinice, odnosno prvi komplement. Biti kodne reči za negativni broj dobijaju se komplementiranjem bita njegove apsolutne vrednosti:

**Obrazloženje i uticaj:** Komplementiraju se biti apsolutne vrednosti, a ne već negativno kodiranog broja.

### 03-20 — jednačina (1.2.3.1)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 402; `\label{eq:1.2.3.1}`.

**Izvor:** $- D \equiv M - \ D + 1$

**Ispravka:** \operatorname{KO}_n(-D)=(-D)\bmod r^n

**Obrazloženje i uticaj:** Operacija modulo neophodna je i za D=0: r^n se odbacuje na širini od n cifara.

### 03-21 — jednačina (1.2.3.2)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 413; `\label{eq:1.2.3.2}`.

**Izvor:** $- D \equiv {- D}_{KMV} + 1$

**Ispravka:** \operatorname{KO}_n(-D)=\bigl(\operatorname{KMV}_n(-D)+1\bigr)\bmod r^n

**Obrazloženje i uticaj:** Dodavanje jedinice obavlja se na celoj reči i rezultat se svodi na n cifara.

### 03-22 — blok 92

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 418; `% Izvor DOCX: blok 92`.

**Izvor:** Jednačina 1.3.2.1 se može tumačiti i na sledeći način: Ukoliko je negativna vrednost -D predstavljena na nivou cifara jednaka -d_{n-1}d_{n-2}…d_{1}d_{0} i ako je maksimalna vrednost M predstavljena na novu cifara jednaka mm…mm tada za cifre negativnog broja D važi:

**Ispravka:** Najpre se svaka cifra apsolutne vrednosti zameni cifrom $r-1-d_i$, a zatim se celoj reči doda jedinica. Prenos se propagira od cifre najmanje težine:

**Obrazloženje i uticaj:** Izvor pogrešno dodaje 1 svakoj cifri nezavisno; to ne implementira komplement osnove.

### 03-23 — jednačina (1.2.3.3)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 422; `\label{eq:1.2.3.3}`.

**Izvor:** $\overline{d_{i}} \equiv m - \ d_{i} + 1 = r - \ d_{i}$

**Ispravka:** \begin{aligned}c_0&=1,\\ e_i&=(r-1-d_i+c_i)\bmod r,\\ c_{i+1}&=\left\lfloor\frac{r-1-d_i+c_i}{r}\right\rfloor,\quad i=0,\dots,n-1.\end{aligned}

**Obrazloženje i uticaj:** Ispravna rekurzija sa prenosom umesto netačne relacije e_i=r-d_i.

### 03-24 — jednačina (1.2.3.4)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 433; `\label{eq:1.2.3.4}`.

**Izvor:** $D\  \in \{ - \frac{r^{n}}{2},\ \ldots, + \left( \frac{r^{n}}{2} - 1 \right)\}$

**Ispravka:** D\in\left\{-\frac{r^n}{2},\dots,\frac{r^n}{2}-1\right\},\qquad r\ \text{parno}

**Obrazloženje i uticaj:** Eksplicitno ograničenje na parne osnove; sprečava primenu polucelih granica u neparnoj osnovi.

### 03-25 — blok 97

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 443; `% Izvor DOCX: blok 97`.

**Izvor:** U slučaju binarnog brojnog sistema (r = 2) ova predstava se naziva komplement dvojke ili drugi komplement. Tada, na osnovu relacije 2.2.2.3, možemo izvesti zaključak da se biti predstave negativnog broja D, u komplementu osnove, dobijaju komplementiranjem bita d_{n-1}d_{n-2}…d_{1}d_{0} negativnog broja D sa dodatkom 1, odnosno:

**Ispravka:** Za $r=2$ ovo je komplement dvojke, odnosno drugi komplement. Komplementiraju se biti apsolutne vrednosti i celoj reči se doda jedinica, uz odbacivanje izlaznog prenosa:

**Obrazloženje i uticaj:** Ispravljena referenca i terminologija apsolutne vrednosti.

### 03-26 — uvod, nakon 1.2.3

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), celina navedena u naslovu stavke.

**Izvor:** Ofset je samo naveden u spisku, bez definicije.

**Ispravka:** Dodate definicije ofseta i skaliranja zapisa sa fiksnom tačkom.

**Obrazloženje i uticaj:** Dopuna omogućava razumevanje navedenih predstava i zadataka sa oktalnim razlomcima.

### 03-27 — jednačina (2.1.1)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 500; `\label{eq:2.1.1}`.

**Izvor:** ${1001.0101}_{2}\  = \mathbf{1} \bullet 2^{3} + \mathbf{0} \bullet 2^{2} + \mathbf{0} \bullet 2^{1} + \mathbf{1} \bullet 2^{0} + \mathbf{0} \bullet 2^{- 1} + \mathbf{1} \bullet 2^{- 2} + \mathbf{0} \bullet 2^{- 3} + 1 \bullet 2^{- 4} = {9.3125}_{10}$

**Ispravka:** (1001.0101)_2=2^3+2^0+2^{-2}+2^{-4}=9.3125

**Obrazloženje i uticaj:** Uklonjeni su samo nulti sabirci, radi čitljivosti.

### 03-28 — jednačina (2.1.2)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 503; `\label{eq:2.1.2}`.

**Izvor:** ${137.21}_{8} = \mathbf{1} \bullet 8^{2} + \mathbf{3} \bullet 8^{1} + 7 \bullet 8^{0} + 2 \bullet 8^{- 1} + \mathbf{1} \bullet 8^{- 2} = {95.265625}_{10}$

**Ispravka:** (137.21)_8=8^2+3\cdot8+7+2\cdot8^{-1}+8^{-2}=95.265625

**Obrazloženje i uticaj:** Zadržan tačan razvoj i rezultat.

### 03-29 — jednačina (2.1.3)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 506; `\label{eq:2.1.3}`.

**Izvor:** ${1E0.2A}_{16} = \mathbf{1} \bullet 16^{2} + \mathbf{14} \bullet 16^{1} + \mathbf{0} \bullet 16^{0} + \mathbf{2} \bullet 16^{- 1} + \mathbf{10} \bullet 16^{- 2} = {480.16406}_{10}$

**Ispravka:** (1E0.2A)_{16}=16^2+14\cdot16+2\cdot16^{-1}+10\cdot16^{-2}=480.1640625

**Obrazloženje i uticaj:** 480.16406 je zaokružena vrednost, a izvor je označava znakom jednakosti; dodat tačan završetak.

### 03-30 — jednačina (2.1.4)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 509; `\label{eq:2.1.4}`.

**Izvor:** $\ \ \ \ {254.61}_{7} = \mathbf{2} \bullet 7^{2} + 5 \bullet 7^{1} + \mathbf{4} \bullet 7^{0} + \mathbf{\ 6} \bullet 7^{- 1} + \mathbf{1} \bullet 7^{- 2} = {137.8776}_{10}\ $

**Ispravka:** (254.61)_7=2\cdot7^2+5\cdot7+4+\frac67+\frac1{49}=137+\frac{43}{49}\approx137.877551

**Obrazloženje i uticaj:** 137.8776 je aproksimacija; zadržana je tačna racionalna vrednost.

### 03-31 — blok 108

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 514; `% Izvor DOCX: blok 108`.

**Izvor:** * Broj 13.375_{10} je moguće konvertovati iz decimalnog u binarni brojni sistem na osnovu algoritma opisanog u 0. Na osnovu tog algoritma najpre je neophodno izvršiti konverziju celog dela broja a zatim razlomljenog i na kraju sabrati dobijene rezultate. Proces konvertovanja celog dela je:

**Ispravka:** b) Za broj $(13.375)_{10}$ primenjujemo postupak iz odeljka~\ref{sec:1.1.2}, posebno na ceo i razlomljeni deo. Za ceo deo dobijamo:

**Obrazloženje i uticaj:** Uklonjena pokvarena Word referenca „0“.

### 03-32 — blok 112

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 550; `% Izvor DOCX: blok 112`.

**Izvor:** Na osnovu prikazane procedure dobijamo da je razlomljeni deo broja u binarnom brojnom sistemu jednak 111.

**Ispravka:** Razlomljeni deo je $(0.011)_2$, jer se izdvojeni celi delovi proizvoda čitaju redom: 0, 1, 1.

**Obrazloženje i uticaj:** Tabela množenja daje 011, a ne 111.

### 03-33 — blok 113

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 553; `% Izvor DOCX: blok 113`.

**Izvor:** Na osnovu prikazanog postupka i dobijenih rezultata dobijamo da je ekvivalentna predstava broja 13.375_{10} u binarnom brojnom sistemu jednaka 1101.111

**Ispravka:** \begin{equation}
(13.375)_{10}=(1101.011)_2
\end{equation}

**Obrazloženje i uticaj:** Ispravka konverzije: 0.011₂=3/8, dok je 0.111₂=7/8.

### 03-34 — blok 117

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 577; `% Izvor DOCX: blok 117`.

**Izvor:** * drugi korak algoritma se ne implementira je je u pitanju nulti stepen broja 2. To znači da (2.3.5) predstavlja predstavu broja 614.24_{8} u binarnom brojnom sistemu

**Ispravka:** Za ciljnu osnovu $2=2^1$ svaka grupa ima jedan bit, pa dodatno grupisanje nije potrebno. Rezultat je dat jednačinom~\eqref{eq:2.1.5}.

**Obrazloženje i uticaj:** Binarna osnova je prvi, a ne nulti stepen broja 2; ispravljena referenca.

### 03-35 — jednačina (2.1.6)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 586; `\label{eq:2.1.6}`.

**Izvor:** ${A3B.4F}_{8}\  = 1010\ 0011\ 1011\ .\ 0100\ 1111$

**Ispravka:** (A3B.4F)_{16}=(1010\,0011\,1011.0100\,1111)_2

**Obrazloženje i uticaj:** Izvor pogrešno navodi osnovu 8 za heksadecimalni broj.

### 03-36 — jednačina (2.1.7)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 597; `\label{eq:2.1.7}`.

**Izvor:** ${254.61}_{7}\  = {137.8776}_{10}\  = 10001001.\ 1110000$

**Ispravka:** (254.61)_7=137+\frac{43}{49}=\bigl(10001001.\overline{111000001010011100101}\bigr)_2

**Obrazloženje i uticaj:** Razlomak 43/49 ima period od 21 bita. Konačan niz iz izvornika nije tačno jednak broju.

### 03-37 — blok 133

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 665; `% Izvor DOCX: blok 133`.

**Izvor:** Gde su rešenja jednačine r_{1} = -2 i r_{2} = 7. Pošto osnova ne može biti negativna, dobija se da je osnova sistema u kojem je zadata jednačina r=7

**Ispravka:** Rešenja su $r=-2$ i $r=7$. Osnova mora biti ceo broj veći od najveće korišćene cifre (5), pa je jedina dozvoljena osnova $r=7$.

**Obrazloženje i uticaj:** Uslov nije samo pozitivnost osnove, već i r≥2 i dozvoljenost svih cifara.

### 03-38 — jednačina (2.3.1)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 711; `\label{eq:2.3.1}`.

**Izvor:** $\{ - \left( 2^{7 - 1} - 1 \right),\  + \left( 2^{7 - 1} - 1 \right)\}$

**Ispravka:** \{-(2^{7-1}-1),\dots,2^{7-1}-1\}

**Obrazloženje i uticaj:** Dodate tri tačke: izvorni zapis navodi samo dva krajnja elementa umesto celog skupa.

### 03-39 — blok 146

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 766; `% Izvor DOCX: blok 146`.

**Izvor:** * Algoritam prebacivanje brojeva predstavljenih koristeći predstavu znak i apsolutna vrednost u osnovu 10 uključuje sledeće korake:

**Ispravka:** c) U svakom zadatom zapisu prvi bit je bit znaka, a preostali biti predstavljaju apsolutnu vrednost. Prva dva broja imaju šest bita; pri proširenju na sedam bita zadržava se znak i dodaje nula ispred apsolutne vrednosti:

**Obrazloženje i uticaj:** Izvor bez objašnjenja menja širinu zapisa; kod znak–apsolutna vrednost ne koristi obično ponavljanje bita znaka.

### 03-40 — jednačina (2.3.10)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 770; `\label{eq:2.3.10}`.

**Izvor:** $1001110\  = - 14$

**Ispravka:** (101110)_{\mathrm{ZA}}=(1001110)_{\mathrm{ZA}}=-14

**Obrazloženje i uticaj:** Prikazan izvorni šestobitni zapis i ekvivalentan sedmobitni zapis.

### 03-41 — jednačina (2.3.11)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 773; `\label{eq:2.3.11}`.

**Izvor:** $0010100 = 20\ \ \ $

**Ispravka:** (010100)_{\mathrm{ZA}}=(0010100)_{\mathrm{ZA}}=20

**Obrazloženje i uticaj:** Prikazano proširenje šestobitnog pozitivnog zapisa.

### 03-42 — jednačina (2.4.7)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 862; `\label{eq:2.4.7}`.

**Izvor:** $\ \ \ \ \ \ \ \ 1 \equiv 9999 - 1 = 9998_{KMV}$

**Ispravka:** -1 \equiv 9999 - 1 = 9998_{KMV}

**Obrazloženje i uticaj:** Predstavlja se suprotna vrednost broja +1, pa leva strana mora biti −1; kodna reč pripada odgovarajućoj predstavi.

### 03-43 — jednačina (2.4.15)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 904; `\label{eq:2.4.15}`.

**Izvor:** $\ \ \ \ \ \ \ \ 1 \equiv FFFF - 1 = {FFFE}_{KMV}$

**Ispravka:** -1 \equiv FFFF - 1 = {FFFE}_{KMV}

**Obrazloženje i uticaj:** Predstavlja se suprotna vrednost broja +1, pa leva strana mora biti −1; kodna reč pripada odgovarajućoj predstavi.

### 03-44 — jednačina (2.4.23)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 947; `\label{eq:2.4.23}`.

**Izvor:** $\ \ \ \ \ \ \ \ \ \ 1 \equiv 7777 - 1 = 7776_{KMV}$

**Ispravka:** -1 \equiv 7777 - 1 = 7776_{KMV}

**Obrazloženje i uticaj:** Predstavlja se suprotna vrednost broja +1, pa leva strana mora biti −1; kodna reč pripada odgovarajućoj predstavi.

### 03-45 — jednačina (2.4.31)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 989; `\label{eq:2.4.31}`.

**Izvor:** $\ \ \ \ \ \ \ \ \ 1 \equiv 1111 - 1 = 1110_{KMV}$

**Ispravka:** -1 \equiv 1111 - 1 = 1110_{KMV}

**Obrazloženje i uticaj:** Predstavlja se suprotna vrednost broja +1, pa leva strana mora biti −1; kodna reč pripada odgovarajućoj predstavi.

### 03-46 — jednačina (2.5.7)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1068; `\label{eq:2.5.7}`.

**Izvor:** $\ \ \ \ \ \ \ \ 1 \equiv 10000 - 1 = 9999_{KMV} = 9998_{KMV} + 1$

**Ispravka:** -1 \equiv 10000 - 1 = 9999_{KO} = 9998_{KMV} + 1

**Obrazloženje i uticaj:** Predstavlja se suprotna vrednost broja +1, pa leva strana mora biti −1; kodna reč pripada odgovarajućoj predstavi.

### 03-47 — jednačina (2.5.15)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1110; `\label{eq:2.5.15}`.

**Izvor:** $\ \ \ \ \ \ \ \ 1 \equiv 10000 - 1 = {FFFF}_{KO} = {FFFE}_{KMV} + 1$

**Ispravka:** -1 \equiv 10000 - 1 = {FFFF}_{KO} = {FFFE}_{KMV} + 1

**Obrazloženje i uticaj:** Predstavlja se suprotna vrednost broja +1, pa leva strana mora biti −1; kodna reč pripada odgovarajućoj predstavi.

### 03-48 — jednačina (2.5.23)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1153; `\label{eq:2.5.23}`.

**Izvor:** $\ \ \ \ \ \ \ \ \ \ 1 \equiv 10000 - 1 = 7777_{KO} = 7776_{KMV} + 1$

**Ispravka:** -1 \equiv 10000 - 1 = 7777_{KO} = 7776_{KMV} + 1

**Obrazloženje i uticaj:** Predstavlja se suprotna vrednost broja +1, pa leva strana mora biti −1; kodna reč pripada odgovarajućoj predstavi.

### 03-49 — jednačina (2.5.31)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1195; `\label{eq:2.5.31}`.

**Izvor:** $\ \ \ \ \ \ \ \ \ 1 \equiv 1111 - 1 = 1111_{KO} = 1110_{KMV} + 1$

**Ispravka:** -1 \equiv 1111 - 1 = 1111_{KO} = 1110_{KMV} + 1

**Obrazloženje i uticaj:** Predstavlja se suprotna vrednost broja +1, pa leva strana mora biti −1; kodna reč pripada odgovarajućoj predstavi.

### 03-50 — jednačina (2.4.19)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 935; `\label{eq:2.4.19}`.

**Izvor:** $\ \ \ \  - 27.40 \equiv 77.77\  - 27.40 = {50.37}_{KMV}$

**Ispravka:** -(24.70)_8\ \longmapsto\ (77.77)_8-(24.70)_8=(53.07)_{8,\mathrm{KMV}}

**Obrazloženje i uticaj:** U postavci je 24.70, a rešenje greškom koristi 27.40; ispravljeno prema postavci.

### 03-51 — jednačina (2.4.29)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 983; `\label{eq:2.4.29}`.

**Izvor:** $\ \ \ \ \ \ \ 11\  \equiv 1111 - 11 = 1100_{KMV}$

**Ispravka:** -(11)_2\ \longmapsto\ (1111)_2-(0011)_2=(1100)_{2,\mathrm{KMV}}

**Obrazloženje i uticaj:** Nedostajao je znak minus ispred broja čija se suprotna vrednost traži.

### 03-52 — blok 175

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1026; `% Izvor DOCX: blok 175`.

**Izvor:** * Provera da li se zadati broj nalazi u skupu brojeva koje je moguće predstaviti na datom broju cifara n – koristimo (1.3.2.4). Ukoliko je broj moguće predstaviti koristeći n cifara u posmatranom brojnom sistemu, prelazimo na korak 2
* Koristimo formulu (1.3.2.1) da bi dobili predstavu negativnog broja

**Ispravka:** Prvo se proveri pripadnost opsegu iz~\eqref{eq:1.2.3.4}, a zatim se koristi formula~\eqref{eq:1.2.3.1}.

**Obrazloženje i uticaj:** Ispravljene nepostojeće reference 1.3.2.4 i 1.3.2.1.

### 03-53 — jednačina (2.5.3)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1056; `\label{eq:2.5.3}`.

**Izvor:** $\ \ \ \  - 1952 \equiv 10000 - 1952 = 8049_{KO} = 8047_{KMV} + 1$

**Ispravka:** -1952\ \longmapsto\ 10000-1952=8048_{\mathrm{KO}}=8047_{\mathrm{KMV}}+1

**Obrazloženje i uticaj:** 10000−1952=8048, a ne 8049.

### 03-54 — jednačina (2.5.6)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1065; `\label{eq:2.5.6}`.

**Izvor:** $\ \ \ \ \ \ \ 0 \equiv 10000 - 0 = 0000_{KO} = 9999_{KMV} + 1$

**Ispravka:** 0\ \longmapsto\ (10000-0)\bmod10000=0000_{\mathrm{KO}}

**Obrazloženje i uticaj:** Zadržavaju se četiri cifre; obična jednakost 10000=0000 nije tačna.

### 03-55 — jednačina (2.5.10)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1087; `\label{eq:2.5.10}`.

**Izvor:** $\{ - {8FFF}_{16},{7FFF}_{16}\ \ldots,\ {7FFE}_{16},\ {7FFF}_{16}\ \}$

**Ispravka:** \{-(8000)_{16},-(7FFF)_{16},\dots,(7FFE)_{16},(7FFF)_{16}\}

**Obrazloženje i uticaj:** Donja granica je −8000₁₆, a ne −8FFF₁₆; vraćen minus drugom elementu.

### 03-56 — jednačina (2.5.14)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1107; `\label{eq:2.5.14}`.

**Izvor:** $\ \ \ \ \ \ \ 0 \equiv 10000 - 0 = 0000_{KO} = {FFFF}_{KMV} + 1$

**Ispravka:** 0\ \longmapsto\ (10000_{16}-0)\bmod16^4=0000_{\mathrm{KO}}

**Obrazloženje i uticaj:** Eksplicitno odbacivanje izlaznog prenosa za nulu.

### 03-57 — jednačina (2.5.17)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1126; `\label{eq:2.5.17}`.

**Izvor:** $\{ - 2048,\  - 2047,\ldots,\ 2046,\ 2047\ \rbrack$

**Ispravka:** \{-2048,-2047,\dots,2046,2047\}

**Obrazloženje i uticaj:** Ispravljena završna zagrada skupa.

### 03-58 — jednačina (2.5.19)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1141; `\label{eq:2.5.19}`.

**Izvor:** $\ \ \ \  - 27.40 \equiv 100.00\  - 27.40 = {50.40}_{KO} = {50.37}_{KMV} + 1$

**Ispravka:** -(24.70)_8\ \longmapsto\ (100.00)_8-(24.70)_8=(53.10)_{8,\mathrm{KO}}

**Obrazloženje i uticaj:** Postavka koristi 24.70; za prelaz iz KMV 53.07 dodaje se 0.01₈, jedinica poslednjeg mesta.

### 03-59 — jednačina (2.5.22)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1150; `\label{eq:2.5.22}`.

**Izvor:** $\ \ \ \ \ \ \ \ \ 0\  \equiv 10000 - 0 = 0000_{KO} = 7777_{KMV} + 1$

**Ispravka:** 0\ \longmapsto\ (10000_8-0)\bmod8^4=0000_{\mathrm{KO}}

**Obrazloženje i uticaj:** Eksplicitna širina četiri cifre.

### 03-60 — jednačina (2.5.28)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1186; `\label{eq:2.5.28}`.

**Izvor:** $\ \ \ \  - 0101 \equiv 1000 - 0101 = 1011_{KO} = 1010_{KMV} + 1$

**Ispravka:** -(0101)_2\ \longmapsto\ (10000)_2-(0101)_2=(1011)_{2,\mathrm{KO}}

**Obrazloženje i uticaj:** Minuend mora biti 10000₂=2⁴, a ne 1000₂.

### 03-61 — jednačina (2.5.29)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1189; `\label{eq:2.5.29}`.

**Izvor:** $\ \ \ \ \ \ \ 11\  \equiv 1111 - 11 = 1101_{KO} = 1100_{KMV} + 1$

**Ispravka:** -(11)_2\ \longmapsto\ (10000)_2-(0011)_2=(1101)_{2,\mathrm{KO}}

**Obrazloženje i uticaj:** Ispravljen predznak i minuend komplementa osnove.

### 03-62 — jednačina (2.5.30)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1192; `\label{eq:2.5.30}`.

**Izvor:** $\ \ \ \ \ \ \ \ \ 0 \equiv 1111 - 0 = 0000_{KO} = 1111_{KMV} + 1$

**Ispravka:** 0\ \longmapsto\ (10000_2-0)\bmod2^4=0000_{\mathrm{KO}}

**Obrazloženje i uticaj:** Komplement osnove nule daje nulu nakon odbacivanja izlaznog prenosa.

### 03-63 — jednačina (2.5.31)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1195; `\label{eq:2.5.31}`.

**Izvor:** $\ \ \ \ \ \ \ \ \ 1 \equiv 1111 - 1 = 1111_{KO} = 1110_{KMV} + 1$

**Ispravka:** -(1)_2\ \longmapsto\ (10000)_2-(0001)_2=(1111)_{2,\mathrm{KO}}

**Obrazloženje i uticaj:** Ispravljen predznak i minuend 2⁴.

### 03-64 — zadatak 2.6, konvencija

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), celina navedena u naslovu stavke.

**Izvor:** Nije eksplicitno rečeno da su operandi već kodirane reči.

**Ispravka:** Dodata napomena o kodiranim operandima i spoljašnjoj negaciji.

**Obrazloženje i uticaj:** Čuva smisao izvornog rešenja −54→0045, bez pogrešnog predstavljanja decimalnog broja −54.

### 03-65 — jednačina (2.6.8)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1360; `\label{eq:2.6.8}`.

**Izvor:** $38_{8} \equiv 0038_{8 - KMV}$

**Ispravka:** (36)_8\ \longmapsto\ (0036)_{8,\mathrm{KMV}}

**Obrazloženje i uticaj:** Cifra 8 ne postoji u oktalnom sistemu; postavka i objašnjenje daju 36.

### 03-66 — blok 230

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1407; `% Izvor DOCX: blok 230`.

**Izvor:** d) Odrediti broj iste apsolutne vrednosti ali suprotnog znaka za sledeće binarne brojeve date u drugom komplementu sa 3 bita. Rezultate predstaviti u drugom koplementu sa 6 bita:

**Ispravka:** b) Odrediti suprotne vrednosti sledećih trobitnih brojeva datih u drugom komplementu. Rezultate predstaviti u drugom komplementu sa šest bita:

**Obrazloženje i uticaj:** Ispravljena oznaka tačke d) u b).

### 03-67 — jednačina (2.7.5)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1469; `\label{eq:2.7.5}`.

**Izvor:** $00000001 \equiv 00000000$

**Ispravka:** 1\ \longmapsto\ 00000001

**Obrazloženje i uticaj:** Kodna reč broja 1 nije 00000000.

### 03-68 — jednačina (2.7.6)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1480; `\label{eq:2.7.6}`.

**Izvor:** $- \ 01111111 \equiv 11111111 - 01111111 + 1 = 10000000$

**Ispravka:** -128\ \longmapsto\ (-128)\bmod256=128=(10000000)_2

**Obrazloženje i uticaj:** Apsolutna vrednost 128 ima zapis 10000000; izvor koristi 01111111 i daje netačnu jednakost.

### 03-69 — blok 245

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1485; `% Izvor DOCX: blok 245`.

**Izvor:** -127:

**Ispravka:** 127:

**Obrazloženje i uticaj:** Postavka traži +127, a rešenje greškom navodi −127.

### 03-70 — jednačina (2.7.8)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1489; `\label{eq:2.7.8}`.

**Izvor:** $- \ 01111110 \equiv 11111111 - 01111110 + 1 = 011111111$

**Ispravka:** 127\ \longmapsto\ (01111111)_2

**Obrazloženje i uticaj:** Ispravljen znak, broj bita i sama konverzija broja +127.

### 03-71 — blok 247

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1494; `% Izvor DOCX: blok 247`.

**Izvor:** -128: Nije moguće prikazati jer izlazi iz skupa

**Ispravka:** 128: nije moguće predstaviti na osam bita u drugom komplementu, čiji je opseg $[-128,127]$.

**Obrazloženje i uticaj:** Van opsega je +128; −128 je dozvoljena donja granica.

### 03-72 — blok 248

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1497; `% Izvor DOCX: blok 248`.

**Izvor:** b) Potrebno je prvo odraditi suprotnu vrednost datog broja na širini od 3 bita, a zatim u zavisnosti od cifre najveće težine, uraditi odgovarajuću ekstenziju znaka

**Ispravka:** b) Najpre proširimo znak sa tri na šest bita, a zatim odredimo drugi komplement na šest bita. Time postupak ostaje ispravan i za najmanji trobitni broj $100_2=-4$, čija suprotna vrednost ne staje na tri bita.

**Obrazloženje i uticaj:** Negiranje pre proširenja može da prekorači opseg; uveden opšti ispravan redosled.

### 03-73 — jednačina (2.7.9)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1501; `\label{eq:2.7.9}`.

**Izvor:** $- \ 101 \equiv 111 - 101 + 1 = 011 = 000011$

**Ispravka:** -(111101)_{2,\mathrm{KO}}\ \longmapsto\ (000011)_{2,\mathrm{KO}}

**Obrazloženje i uticaj:** Rezultat je isti kao u izvorniku, a postupak koristi prvo proširenje pa negiranje.

### 03-74 — jednačina (2.7.10)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1504; `\label{eq:2.7.10}`.

**Izvor:** $- \ 011 \equiv 111 - 011 + 1 = 101 = 111101$

**Ispravka:** -(000011)_{2,\mathrm{KO}}\ \longmapsto\ (111101)_{2,\mathrm{KO}}

**Obrazloženje i uticaj:** Rezultat je isti kao u izvorniku, a postupak koristi prvo proširenje pa negiranje.

### 03-75 — jednačina (2.7.11)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1507; `\label{eq:2.7.11}`.

**Izvor:** $- \ 111 \equiv 111 - 111 + 1 = 001 = 000001$

**Ispravka:** -(111111)_{2,\mathrm{KO}}\ \longmapsto\ (000001)_{2,\mathrm{KO}}

**Obrazloženje i uticaj:** Rezultat je isti kao u izvorniku, a postupak koristi prvo proširenje pa negiranje.

### 03-76 — jednačina (2.7.12)

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1510; `\label{eq:2.7.12}`.

**Izvor:** $- \ 001 \equiv 111 - 001 + 1 = 111 = 111111$

**Ispravka:** -(000001)_{2,\mathrm{KO}}\ \longmapsto\ (111111)_{2,\mathrm{KO}}

**Obrazloženje i uticaj:** Rezultat je isti kao u izvorniku, a postupak koristi prvo proširenje pa negiranje.

### 03-77 — zadatak 2.7 b, poslednji operand

**Novo mesto:** [LaTeX](03_brojni_sistemi_i_predstave_binarnih_brojeva.tex), red 1394; `\label{sec:2.7}`.

**Izvor:** Rešenje za 000 nedostaje.

**Ispravka:** −000 → 000000.

**Obrazloženje i uticaj:** Dopunjen izostavljeni operand postojećeg rešenog zadatka.

## Jezik, oznake i prelom

Ujednačeni su izrazi „razlomljeni deo“, „proširenje znaka“, nazivi predstava, razmaci, interpunkcija i dijakritika. Ispravljene su tipografske greške navedene u tekstu (npr. „ne promenjen“, „ospegu“, „prebaivanje“). Ručne reference zamenjene su automatskim; Word tabele za raspored jednačina zamenjene su matematičkim okruženjima. Naslovna strana i autorstvo usklađeni su sa vežbama 01 i 02 po dogovoru.

## Provera

`make check` proverava konverzije preko racionalnih brojeva, komplementne kodne reči i opsege, proširenja, granične vrednosti i uslove zadataka za samostalni rad. Period 43/49 proverava se tačno, bez aritmetike sa pokretnom tačkom.

U zadacima za samostalni rad rešenja nisu dodata u studentski tekst. Proverena je rešivost i dozvoljenost osnova u kontrolnoj skripti.

## Dodatna provera izgleda nakon konverzije

Diskretna siva linija razdvaja susedne redove podataka. Uz `\toprule`, `\midrule` i `\bottomrule` ne dodaje se druga, tanka linija. Vidljivi tekst „oprule“ bio je artefakt konverzije: Python je početak `\toprule` protumačio kao tabulator (`\t`). Ispravljen je LaTeX zapis komande; sama komanda iz paketa booktabs crta gornju ivicu tabele i ne treba da se vidi kao tekst. Ovo su ispravke nastalog LaTeX dokumenta, a ne greške DOCX izvornika.
