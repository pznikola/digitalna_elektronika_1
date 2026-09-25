# Izveštaj o ispravkama — vežbe 05

Vrsta izmene vidi se iz obrazloženja: računska/stručna greška, dopunsko pojašnjenje ili jezička i tipografska obrada. Stavke koje preciziraju konvenciju ili dodaju obrazloženje nisu predstavljene kao greške izvornika. Proračuni i promenjene formule dati su uz pojedinačne stavke; ponovljive provere su u [code/provera.py](code/provera.py). Izvorne oznake povezane su sa novim mestima u [inventaru](INVENTAR.md).

## Pojedinačne ispravke i pojašnjenja

### 05-01 — blok 29

**Novo mesto:** [LaTeX](05_kodovi.tex), red 108; `% Izvor DOCX: blok 29`.

**Izvor:** BCD8421, ili skraćeno BCD, predstavlja binarni težinski kod koji svaku cifru broja datog u decimalnom brojmo sistemu predstavlja na 4. Deo naziva 8421 označava težinu svakog od bita binarne predstave polazeći od cifre najveće težine. Tabela 1.1.1.1. ilustruje kodnu reč za svaku od cifara

**Ispravka:** BCD8421 (skraćeno BCD) svaku decimalnu cifru predstavlja sa četiri bita, težina 8, 4, 2 i 1, redom od najvišeg bita. Tabela~\ref{tab:bcd} prikazuje dozvoljene kodne reči; preostalih šest četvorobitnih kombinacija nije dozvoljeno.

**Obrazloženje i uticaj:** Dovršena prekinuta definicija „predstavlja na 4“ i definisana dozvoljenost kodnih reči.

### 05-02 — blok 32

**Novo mesto:** [LaTeX](05_kodovi.tex), red 141; `% Izvor DOCX: blok 32`.

**Izvor:** Dakle, u slučaju kodovanja broja datog u decimalnom brojnom sistemu, odgovarajuću binarnu predstavu u kodu BCD8421 dobijamo tako što svaku od cifara kodujemo koristeći tabelu 1.1.1.1

**Ispravka:** Za kodovanje decimalnog broja svaka cifra se zasebno zamenjuje četvorobitnom reči iz tabele~\ref{tab:bcd}.

**Obrazloženje i uticaj:** Referenca je sada automatska; sačuvan postupak kodovanja.

### 05-03 — blok 34

**Novo mesto:** [LaTeX](05_kodovi.tex), red 149; `% Izvor DOCX: blok 34`.

**Izvor:** Kao i BCD kod, i ovaj kod predstavlja svaku od cifara na 4 bita. Međutim, sadržaj tabele koja ilustruje kodovanje svake od cifara decimalne predstave broja, je drugačiji i prikazan je u okviru tabele 1.1.1.2

**Ispravka:** Kod BCD2421 takođe koristi četiri bita po decimalnoj cifri, ali njihove težine su 2, 4, 2 i 1. Izbor kodnih reči u tabeli~\ref{tab:2421} čini kod samokomplementarnim.

**Obrazloženje i uticaj:** Precizirane težine i izbor jedne od mogućih reči iste težinske vrednosti.

### 05-04 — blok 37

**Novo mesto:** [LaTeX](05_kodovi.tex), red 184; `% Izvor DOCX: blok 37`.

**Izvor:** Na osnovu sadržaja tabele 1.1.1.2 možemo zaključiti da se cifre 0-4 koduju na isti način kao i u slučaju BCD koda. Međutim, kodne reči cifara 5-9 se dobijaju komplementiranjem cifara simetričnih u odnosu na crvenu osu simetrije (sredinu tabele). U opštem slučaju, kodovi kod kojih su predstave cifara u donjoj polovini tabele simetrični u odnosu na cifre iz gornje gornje polovine, spadaju u kategoriju komplementarnih kodova.

**Ispravka:** Za cifre od 0 do 4 reči se poklapaju sa BCD8421. Reč cifre $9-d$ dobija se komplementiranjem sva četiri bita reči cifre $d$. Ovo je svojstvo samokomplementarnosti; samo vizuelna simetrija tabele nije dovoljna definicija.

**Obrazloženje i uticaj:** Precizirana bitovska komplementarnost. Vizuelna osa izvornika naknadno je obnovljena u tabeli; prvobitna ekstrakcija nije je uključivala.

### 05-05 — blok 40

**Novo mesto:** [LaTeX](05_kodovi.tex), red 196; `% Izvor DOCX: blok 40`.

**Izvor:** Kao i BCD kodovi (BCD8421 i BCD2421) i ovaj kod na 4 bita predstavlja svaku od cifara broja datog u decimalnom zapisu. Međutim, ovaj težinski kod zsvaku od cifara koduje koristeći kodne reči predstavljene u tabeli 1.1.2.1

**Ispravka:** Kod „više 3“ je netežinski kod. Svaka decimalna cifra $d$ koduje se četvorobitnim binarnim zapisom broja $d+3$, prema tabeli~\ref{tab:excess}.

**Obrazloženje i uticaj:** U izvorniku je netačno nazvan težinskim kodom.

### 05-06 — blok 43

**Novo mesto:** [LaTeX](05_kodovi.tex), red 229; `% Izvor DOCX: blok 43`.

**Izvor:** Kao što se iz tabele 1.1.2.1 može primetiti, i ovaj kod spada u grupu komplementarnih kodova i izveden je iz BCD koda dodavanjem broja 3 na svaku od cifara.

**Ispravka:** Kod je samokomplementaran: $15-(d+3)=(9-d)+3$. Pri dekodiranju se od binarne vrednosti svake dozvoljene četvorobitne reči oduzima 3.

**Obrazloženje i uticaj:** Obrazložena samokomplementarnost i razlika između binarne vrednosti reči i decimalne cifre.

### 05-07 — blok 45

**Novo mesto:** [LaTeX](05_kodovi.tex), red 237; `% Izvor DOCX: blok 45`.

**Izvor:** Za razliku od prethodnih kodova, koji su svaku od cifara decimalnog broja kodovali koristeći jasno definisanu tabelu kodnih reči, Gray-ov kod se može primeniti za kodovanje proizvoljnih brojeva. Glavna karakteristika Gray-ovog binarnog koda je da se kodne reči, koje odgovaraju susednim brojevima, razlikuju samo za jedan bit. Ova karakteristika je itekako značajna u sintezi digitalnih sistema kada treba sprečiti pojavu gličeva.

**Ispravka:** Reflektovani binarni Grejov kod predstavlja cele nenegativne brojeve zadate širine. Uzastopne kodne reči razlikuju se u tačno jednom bitu. To smanjuje neodređenost očitavanja pri prelazu između susednih vrednosti; ne garantuje odsustvo svih gličeva u proizvoljnoj kombinacionoj mreži.

**Obrazloženje i uticaj:** Ograničena preširoka tvrdnja da Grejov kod sprečava gličeve uopšte.

### 05-08 — blok 54

**Novo mesto:** [LaTeX](05_kodovi.tex), red 378; `% Izvor DOCX: blok 54`.

**Izvor:** n | n - 1 | n - 2 | … | 1 | 0
0 | b_{n-1} | b_{n-2} | … | b_{1} | b_{0}
 | c_{n}_{-1} = 0$\bigoplus$ b_{n-1} | c_{n}_{-2} = b_{n-1}$\bigoplus$ b_{n-2} | … | c_{1} = b_{2}$\bigoplus$ b_{1} | c_{0} = b_{1}$\bigoplus$ b_{0}

**Ispravka:** \begin{equation}
g_{n-1}=b_{n-1},\qquad g_i=b_{i+1}\oplus b_i\quad(0\le i<n-1).
\end{equation}

**Obrazloženje i uticaj:** Tabela algoritma sa nezgrapnim indeksima zamenjena ekvivalentnim eksplicitnim pravilom za sve pozicije.

### 05-09 — blok 55

**Novo mesto:** [LaTeX](05_kodovi.tex), red 384; `% Izvor DOCX: blok 55`.

**Izvor:** Na osnovu kodne reči c_(n-1)c_(n-2)…c₁c₀ date u Gray-ovom binarnog kodu moguće je odrediti binarnu vrednost b_(n-1)b_(n-2)…b₁b₀ ukoliko pratimo sledeći set koraka:

**Ispravka:** Za dekodiranje Grejove reči $g_{n-1}\dots g_0$ u binarnu reč $b_{n-1}\dots b_0$ koristimo sledeći postupak:

**Obrazloženje i uticaj:** Ujednačene oznake i ispravljen padež.

### 05-10 — blok 57

**Novo mesto:** [LaTeX](05_kodovi.tex), red 396; `% Izvor DOCX: blok 57`.

**Izvor:** n - 1 | n - 2 | … | 1 | 0
c_{n-1} | c_{n-2} | … | c_{1} | c_{0}
b_{n}_{-1} = c_{n-1} | b_{n}_{-2} = b_{n-1}$\bigoplus$ c_{n-2} | … | b_{1} = b_{2}$\bigoplus$ c_{1} | c_{0} = b_{1}$\bigoplus$ c_{0}

**Ispravka:** \begin{equation}
b_{n-1}=g_{n-1},\qquad b_i=b_{i+1}\oplus g_i\quad(i=n-2,\dots,0).
\end{equation}

**Obrazloženje i uticaj:** U poslednjoj koloni izvornika netačno stoji c0=b1 XOR c0; na levoj strani mora biti b0.

### 05-11 — blok 59

**Novo mesto:** [LaTeX](05_kodovi.tex), red 407; `% Izvor DOCX: blok 59`.

**Izvor:** Slično kao i u slučaju ostalih BCD kodova, i u slučaju GrayBCD koda se svaka od cifara broja koduje koristeći tabelu kodnih reči. Sadržaj tabele kodnih reči dat je u okviru tabele 1.1.2.3.

**Ispravka:** Za decimalne cifre koristićemo ciklični Grejov kod iz tabele~\ref{tab:graybcd}. Svaka decimalna cifra koduje se zasebno.

**Obrazloženje i uticaj:** Precizirano koja varijanta decimalnog Grejovog koda se koristi.

### 05-12 — blok 62

**Novo mesto:** [LaTeX](05_kodovi.tex), red 440; `% Izvor DOCX: blok 62`.

**Izvor:** Poređenjem tabele 1.1.2.3 i 1.1.2.2 možemo zaključiti da kodne reči odgovaraju binarnom Gray-ovom kodu.

**Ispravka:** Za cifre 0–8 reči se poklapaju sa početkom reflektovanog binarnog Grejovog koda. Za cifru 9 koristi se 1000, a ne 1101. Time su i prelazi $8\to9$ i $9\to0$ jednobitni; ovaj kod nije samo prvih deset reči standardnog binarnog Grejovog koda.

**Obrazloženje i uticaj:** Izvor tvrdi da se sve reči poklapaju; upravo reč cifre 9 razlikuje ova dva koda.

### 05-13 — blok 64

**Novo mesto:** [LaTeX](05_kodovi.tex), red 447; `% Izvor DOCX: blok 64`.

**Izvor:** Kodovi za detekciju greške su bazirani na osobini koja umogućava da usled bilo koje nepravilnosti rada digitalnog sistema dobijemo kodnu reč koja ne pripada skupu kodnih reči, odnosno da nije moguće detektovati podatak. Na primeru komunikacije dva digitalna sistema, pokušaćemo da ilustrujemo ideju na kojoj su bazirani kodovi za detekciju grešaka.

**Ispravka:** Kodovi za detekciju grešaka koriste skup dozvoljenih reči koji ne obuhvata sve binarne kombinacije. Promena bita može dovesti do nedozvoljene reči i time otkriti grešku. Koji oblici greške se garantovano otkrivaju zavisi od minimalnog Hamingovog rastojanja; ne mogu se otkriti sve proizvoljne promene.

**Obrazloženje i uticaj:** Izvor neosnovano tvrdi da bilo koja nepravilnost daje nedozvoljenu reč.

### 05-14 — blok 65

**Novo mesto:** [LaTeX](05_kodovi.tex), red 450; `% Izvor DOCX: blok 65`.

**Izvor:** [IMAGE /tmp/de1-work/05/media/image7.png]Na slici je prikazan digitalni sistem koji šalje podatke (Transmiter) i sistem koji prima podatke (Receiver). Između dva digitalna sistema je uspostavljen komunikacioni kanal (Channel).

**Ispravka:** Na slici~\ref{fig:channel} predajnik šalje kodnu reč kroz komunikacioni kanal, a prijemnik prima reč koja zbog smetnji može biti izmenjena.
\begin{figure}[!htbp]\centering
\includegraphics[width=0.9\linewidth]{Uvod/kanal}
\caption{Prenos kodne reči kroz kanal sa smetnjom.}\label{fig:channel}
\end{figure}

**Obrazloženje i uticaj:** Ponovo nacrtana cela komunikaciona šema, uključujući Word oblike koje automatska ekstrakcija ne prenosi.

### 05-15 — blok 71

**Novo mesto:** [LaTeX](05_kodovi.tex), red 483; `% Izvor DOCX: blok 71`.

**Izvor:** U slučaju skupa binarnih vrednosti, definiše se i minimalno Hamingovo rastojanje H_{dmin} kao minimalna vrednost d između svih parova tog skupa. Dakle, ukoliko skup binarnih vrednosti predstavlja BCD kod, dobijamo sledeće vrednosti Hamingovog rastojanja:

**Ispravka:** Minimalno Hamingovo rastojanje $d_{\min}$ je najmanje rastojanje između dve \emph{različite} dozvoljene reči. Tabela~\ref{tab:distances} prikazuje primere za BCD8421.

**Obrazloženje i uticaj:** Isključeno je poređenje kodne reči sa samom sobom; ono bi uvek dalo nulu.

### 05-16 — blok 73

**Novo mesto:** [LaTeX](05_kodovi.tex), red 489; `% Izvor DOCX: blok 73`.

**Izvor:** Hamingovo rastojanje
d(0000, 0001) = 1 | d(0001,0000) = 1
d(0000, 0010) = 1 | d(0001,0010) = 2
d(0000, 0011) = 2 | d(0001,0011) = 1
d(0000, 0100) = 1 | d(0001,0100) = 2
d(0000, 0101) = 2 | d(0001,0101) = 2
d(0000, 0110) = 2 | …
d(0000, 0111) = 3 | 
d(0000, 1000) = 1 | 
d(0000, 1001) = 2 |

**Ispravka:** \begin{table}[!htbp]\centering\caption{Primeri Hamingovih rastojanja u BCD kodu.}\label{tab:distances}
\begin{adjustbox}{max width=\linewidth}\begin{tabular}{cc}\toprule
Prva grupa & Druga grupa\\\midrule
$d(0000,0001)=1$ & $d(0001,0000)=1$\\
$d(0000,0010)=1$ & $d(0001,0010)=2$\\
$d(0000,0011)=2$ & $d(0001,0011)=1$\\
$d(0000,0100)=1$ & $d(0001,0100)=2$\\
$d(0000,0101)=2$ & $d(0001,0101)=1$\\
$d(0000,0110)=2$ & $\cdots$\\
$d(0000,0111)=3$ & \\
$d(0000,1000)=1$ & \\
$d(0000,1001)=2$ & \\
\bottomrule\end{tabular}\end{adjustbox}
\end{table}

**Obrazloženje i uticaj:** Ispravljeno d(0001,0101)=1 umesto 2. Svi ostali navedeni parovi provereni brojanjem različitih bita.

### 05-17 — blok 74

**Novo mesto:** [LaTeX](05_kodovi.tex), red 514; `% Izvor DOCX: blok 74`.

**Izvor:** Sa stanovišta mehanizma detekcije greške i skupa kodnih reči, minimalno Hamingovo rastojanje određuje minimalan broj bita koje je potrebno promeniti da bi se dobila sledeća reč iz skupa kodnih reči. Drugim rečima, minimalno Hamingovo rastojanja umanjeno za jedan definiše broj bita koje je moguće promeniti a da dobijena vrednost ne predstavlja kodnu reč. Ukoliko je minimalno Hamingovo rastojanje jednako 1, ne postoji mogućnost promene nijednog od bita a da budemo sigurni da neće doći do prelaska na neku definisanu kodnu reč. Dakle, ne postoji mogućnost detekcije greške. Osobina detekcije greške je karakteristika kodova sa Hamingovim rastojanjem 2 i više.

**Ispravka:** Kod rastojanja $d_{\min}$ garantovano detektuje svaku grešku koja menja najviše $d_{\min}-1$ bita, ako se koristi samo detekcija. Za $d_{\min}=1$ nema garancije detekcije proizvoljne jednobitne greške, iako se neke konkretne greške mogu detektovati. Za korekciju do $t$ grešaka potrebno je $d_{\min}\ge2t+1$.

**Obrazloženje i uticaj:** Razlikovane su garantovana detekcija i mogućnost detekcije pojedinih slučajeva.

### 05-18 — blok 75

**Novo mesto:** [LaTeX](05_kodovi.tex), red 517; `% Izvor DOCX: blok 75`.

**Izvor:** U opštem slučaju, za kod sa minimalnim hamingovim rastojanjem H_{dmin}, važi:

**Ispravka:** Za istovremenu korekciju do $n_c$ grešaka i detekciju do ukupno $n_d$ grešaka, uz $n_d\ge n_c$, dovoljan i za garanciju zasnovanu na rastojanju potreban uslov je:

**Obrazloženje i uticaj:** Jasno definisano da n_d označava ukupan broj detektovanih grešaka, uključujući one koje se koriguju.

### 05-19 — jednačina (1.1.3.2)

**Novo mesto:** [LaTeX](05_kodovi.tex), red 521; `\label{eq:1.1.3.2}`.

**Izvor:** $H_{dmin} = 2n_{c} + n_{d} + 1$

**Ispravka:** d_{\min}\ge n_c+n_d+1,\qquad n_d\ge n_c.

**Obrazloženje i uticaj:** Izvor meša broj dodatno detektovanih i ukupno detektovanih grešaka, i koristi jednakost umesto uslova. Za dodatni broj s=n_d−n_c ekvivalentno je d_min≥2n_c+s+1.

### 05-20 — blok 78

**Novo mesto:** [LaTeX](05_kodovi.tex), red 531; `% Izvor DOCX: blok 78`.

**Izvor:** * n_{c} – broj grešaka koje je moguće korigovati
* n_{d} – broj grešaka koje je moguće detektovati

**Ispravka:** \begin{itemize}[leftmargin=*]
\item $n_c$: najveći broj grešaka koje se garantovano koriguju;
\item $n_d$: najveći ukupan broj grešaka koje se garantovano detektuju u istom režimu.
\end{itemize}
Da bi reč sa najviše $n_d$ grešaka bila pogrešno korigovana u drugu reč udaljenu najviše $n_c$, dve dozvoljene reči morale bi biti udaljene najviše $n_c+n_d$, što navedeni uslov isključuje.

**Obrazloženje i uticaj:** Dodata kratka provera uslova trougaonom nejednakošću Hamingovog rastojanja.

### 05-21 — blok 83

**Novo mesto:** [LaTeX](05_kodovi.tex), red 573; `% Izvor DOCX: blok 83`.

**Izvor:** Zbog toga što je minimalno Hamingovo rastojanje u slučaju parne i neparne parnosti jednako 2, ovaj kod nema mogućnost korekcije već samo detekcije greške

**Ispravka:** Za fiksnu dužinu poruke oba koda imaju $d_{\min}=2$. Otkrivaju svaku grešku sa neparnim brojem promenjenih bita, ali ne i greške sa parnim brojem. Sam bit parnosti ne određuje položaj greške i ne omogućava njenu korekciju.

**Obrazloženje i uticaj:** Precizirana granica sposobnosti detekcije i uslov iste dužine reči.

### 05-22 — blok 85

**Novo mesto:** [LaTeX](05_kodovi.tex), red 581; `% Izvor DOCX: blok 85`.

**Izvor:** Hamingov kod omogućava detektovanje do dve greške u bitima i korekciju jednog bita. Realizuje se dodavanjem redudantnih (kontrolnih) bita na informacione bite i to tačno na odgovarajuće pozicije. Kontrolni biti predstavljaju bite parnosti koji kontrolišu odgovarajuće bite poruke. Broj kontrolnih bita r u zavisnosti od broja informacionih bita m je definisan sledećom relacijom:

**Ispravka:** Osnovni Hamingov kod ima $d_{\min}=3$: koriguje jednu grešku, ili detektuje do dve greške kada se koristi samo detekcija. Sam sindrom ne razlikuje svaku dvobitnu grešku od jednobitne. Za istovremenu korekciju jedne i detekciju dve greške dodaje se opšti bit parnosti, čime se dobija prošireni kod sa $d_{\min}=4$. Broj kontrolnih bita $r$ za $m$ informacionih bita mora zadovoljiti:

**Obrazloženje i uticaj:** Razdvojeni osnovni Hamingov kod i SECDED; izvor ne navodi da su dve mogućnosti osnovnog koda alternativne.

### 05-23 — jednačina (1.1.3.4)

**Novo mesto:** [LaTeX](05_kodovi.tex), red 596; `\label{eq:1.1.3.4}`.

**Izvor:** $n = 2^{r} - 1$

**Ispravka:** n=m+r\le2^r-1

**Obrazloženje i uticaj:** Jednakost n=2^r−1 važi za pun kod, a ne za sve skraćene kodove koji zadovoljavaju prethodnu nejednakost.

### 05-24 — jednačina (1.1.3.5)

**Novo mesto:** [LaTeX](05_kodovi.tex), red 607; `\label{eq:1.1.3.5}`.

**Izvor:** $m = 2^{r} - r - 1$

**Ispravka:** m_{\max}=2^r-r-1

**Obrazloženje i uticaj:** Označeno da formula daje maksimalan broj informacionih bita.

### 05-25 — blok 97

**Novo mesto:** [LaTeX](05_kodovi.tex), red 658; `% Izvor DOCX: blok 97`.

**Izvor:** 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1
1111 | 1110 | 1101 | 1100 | 1011 | 1010 | 1001 | 1000 | 0111 | 0110 | 0101 | 0100 | 0011 | 0010 | 0001
D_{10} | D_{9} | D_{8} | D_{7} | D_{6} | D_{5} | D_{4} | C_{4} | D_{3} | D_{2} | D_{1} | C_{4} | D_{0} | C_{2} | C_{1}

**Ispravka:** \begin{center}\begin{adjustbox}{max width=\linewidth}
\begin{tabular}{ccccccccccccccc}\toprule
15 & 14 & 13 & 12 & 11 & 10 & 9 & 8 & 7 & 6 & 5 & 4 & 3 & 2 & 1 \\
\midrule
1111 & 1110 & 1101 & 1100 & 1011 & 1010 & 1001 & 1000 & 0111 & 0110 & 0101 & 0100 & 0011 & 0010 & 0001 \\
D\textsubscript{10} & D\textsubscript{9} & D\textsubscript{8} & D\textsubscript{7} & D\textsubscript{6} & D\textsubscript{5} & D\textsubscript{4} & C\textsubscript{8} & D\textsubscript{3} & D\textsubscript{2} & D\textsubscript{1} & C\textsubscript{4} & D\textsubscript{0} & C\textsubscript{2} & C\textsubscript{1} \\
\bottomrule\end{tabular}\end{adjustbox}\end{center}

**Obrazloženje i uticaj:** Na poziciji 8 mora biti C8, a ne drugi C4. Preostale pozicije i podaci zadržani su.

### 05-26 — blok 99

**Novo mesto:** [LaTeX](05_kodovi.tex), red 676; `% Izvor DOCX: blok 99`.

**Izvor:** 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1
1111 | 1110 | 1101 | 1100 | 1011 | 1010 | 1001 | 1000 | 0111 | 0110 | 0101 | 0100 | 0011 | 0010 | 0001
D_{10} | D_{9} | D_{8} | D_{7} | D_{6} | D_{5} | D_{4} | C_{4} | D_{3} | D_{2} | D_{1} | C_{4} | D_{0} | C_{2} | C_{1}

**Ispravka:** \begin{center}\begin{adjustbox}{max width=\linewidth}
\begin{tabular}{ccccccccccccccc}\toprule
15 & 14 & 13 & 12 & 11 & 10 & 9 & 8 & 7 & 6 & 5 & 4 & 3 & 2 & 1 \\
\midrule
1111 & 1110 & 1101 & 1100 & 1011 & 1010 & 1001 & 1000 & 0111 & 0110 & 0101 & 0100 & 0011 & 0010 & 0001 \\
D\textsubscript{10} & D\textsubscript{9} & D\textsubscript{8} & D\textsubscript{7} & D\textsubscript{6} & D\textsubscript{5} & D\textsubscript{4} & C\textsubscript{8} & D\textsubscript{3} & D\textsubscript{2} & D\textsubscript{1} & C\textsubscript{4} & D\textsubscript{0} & C\textsubscript{2} & C\textsubscript{1} \\
\bottomrule\end{tabular}\end{adjustbox}\end{center}

**Obrazloženje i uticaj:** Na poziciji 8 mora biti C8, a ne drugi C4. Preostale pozicije i podaci zadržani su.

### 05-27 — blok 100

**Novo mesto:** [LaTeX](05_kodovi.tex), red 699; `% Izvor DOCX: blok 100`.

**Izvor:** [IMAGE /tmp/de1-work/05/media/image10.png]Drugi način za analizu Hammingovog koda je kroz Venove dijagrame. Na slici je prikazan Venov dijagram za slučaj Hamingovog koda čija je dužina kodne reči jednaka 7 i koji ima 3 kontrolna bita.

**Ispravka:** Za Hamingov kod dužine 7, Venov dijagram na slici~\ref{fig:venn} prikazuje koje kontrolne grupe sadrže pojedine pozicije. Oznake $d_3,d_5,d_6,d_7$ ovde sadrže \emph{pozicije u reči}, dok $D_0,\dots,D_{10}$ u prethodnim tabelama označavaju redne brojeve informacionih bita.

**Obrazloženje i uticaj:** Razjašnjene dve konvencije označavanja informacionih bita.

### 05-28 — blok 102

**Novo mesto:** [LaTeX](05_kodovi.tex), red 708; `% Izvor DOCX: blok 102`.

**Izvor:** Jedan od načina za identifikaciju bita na kome je došlo do greške jeste analizom sadržaja kontrolnih bita. Ako se svakom kontrolnom bitu koji pokazuje da nije došlo do greške pridruži 0, a svakom kontrolnom bitu koji ukazuje da je bilo greške pridruži 1, čitanjem dobijenog koda moguće je utvrditi na kom bitu je došlo do greške.

**Ispravka:** Sindrom se dobija ponovnim izračunavanjem parnosti svake kontrolne grupe: $s_j=0$ ako provera prolazi, a $s_j=1$ ako ne prolazi. Za najviše jednu grešku broj $(s_4s_2s_1)_2$ daje njenu poziciju. Nulti sindrom znači da su provere zadovoljene; bez ograničenja broja grešaka to nije dokaz da greške nema.

**Obrazloženje i uticaj:** Sindrom nije isto što i sadržaj kontrolnih bita; navedena pretpostavka jedne greške.

### 05-29 — blok 107

**Novo mesto:** [LaTeX](05_kodovi.tex), red 733; `% Izvor DOCX: blok 107`.

**Izvor:** Za svaki od pomenutih kodova odrediti težinske koeficijente bita

**Ispravka:** Navesti težine bita za težinske kodove i obrazložiti zašto ostali navedeni kodovi nemaju takve fiksne težine.

**Obrazloženje i uticaj:** Netežinskim kodovima nije moguće dodeliti obične konstantne težine koje direktno daju vrednost cifre.

### 05-30 — blok 112

**Istorijska odluka, zamenjena nalazima 05-A12 i 05-A13:** po naknadnom zahtevu korisnika sada su i postavka i prvi red rešenja za broj 43, a međukoraci binarnog Grejovog kodovanja vraćeni su. Raniji zapis ispod sačuvan je radi sledljivosti.

**Novo mesto:** [LaTeX](05_kodovi.tex), red 759; `% Izvor DOCX: blok 112`.

**Izvor:** Broj | BCD | BCD2421 | Više 3 | Gray BCD | Gray binarni
43 | 0100 0011 | 0100 0011 | 0111 0110 | 0001 0010 | 0101011_{2} = 111110
0 | 0000 | 0000 | 0011 | 0000 | 00000_{2} = 0000
15 | 0001 0101 | 0001 1011 | 0100 1000 | 0001 0111 | 01111_{2} = 1000
49 | 0100 1001 | 0100 1111 | 0111 1100 | 0110 1000 | 0110001_{2} = 101001
62 | 0110 0010 | 1100 0010 | 1001 0101 | 0101 0011 | 0111110_{2} = 100001

**Ispravka:** \begin{center}
\begin{adjustbox}{max width=\linewidth}\begin{tabular}{cccccc}\toprule
Broj & BCD & BCD2421 & Više 3 & Grej BCD & Grej binarni\\\midrule
13 & 0001 0011 & 0001 0011 & 0100 0110 & 0001 0010 & 001011\\
0 & 0000 & 0000 & 0011 & 0000 & 000000\\
15 & 0001 0101 & 0001 1011 & 0100 1000 & 0001 0111 & 001000\\
49 & 0100 1001 & 0100 1111 & 0111 1100 & 0110 1000 & 101001\\
62 & 0110 0010 & 1100 0010 & 1001 0101 & 0101 0011 & 100001\\
\bottomrule\end{tabular}\end{adjustbox}
\end{center}

**Obrazloženje i uticaj:** Prva postavljena vrednost je 13, ali izvorna tabela većinom rešava 43. Ispravljen ceo prvi red; binarni Grejovi zapisi ujednačeni na šest bita.

### 05-31 — blok 113

**Novo mesto:** [LaTeX](05_kodovi.tex), red 777; `% Izvor DOCX: blok 113`.

**Izvor:** * Prilikom tumačenja binarnih brojeva kao decimalnih brojeva datih u određenom kodu, potrebno je obratiti pažnju na to da li dobijeni kodovi pripadaju kodnim rečima. Ukoliko pripadaju, moguće je odrediti decimalnu vrednost dok u suprotnom to nije moguće. U slučaju transofrmacije kodne reči koja sadrži decimalnu tačku i BCD predstava, cifre se posmatraju u odnosu na decimalnu tačku. U slučaju Gray-ovog binarnog koda, decimalna tačka se zanemaruje pa se nakon konverzije dodaje na odgovarajuće mesto.

**Ispravka:** Kodovi decimalnih cifara grupišu se u četvorke od tačke ulevo i udesno; nepotpune spoljne grupe dopunjuju se nulama. Svaka grupa mora biti dozvoljena kodna reč. Za binarni Grejov kod ovde koristimo zapis sa fiksnom tačkom: dekodiramo ceo izvorni niz i zadržavamo izvorni broj razlomljenih bita. U tom postupku se razlomljeni deo ne dopunjava nulama radi grupisanja.

**Obrazloženje i uticaj:** Razdvojena pravila grupisanja decimalnih kodova i dekodiranja binarnog Grejovog zapisa; desno dopunjavanje Grejove reči nije uopšte neutralno.

### 05-32 — blok 114

**Novo mesto:** [LaTeX](05_kodovi.tex), red 780; `% Izvor DOCX: blok 114`.

**Izvor:** Broj | BCD | BCD2421 | Više 3 | Gray BCD | Gray binarni
00101001.10010100 | 29.94 | x | x | x | 110001.000110 = 49.09375
10010011.11101010 | x | x | x | x | 11100010.1011001=
226.6953125
1011.10100100 | x | x | 8.71 | x | 1101.001110 = 13.21875

**Ispravka:** \begin{center}
\begin{adjustbox}{max width=\linewidth}\begin{tabular}{cccccc}\toprule
Izvorna reč & BCD & BCD2421 & Više 3 & Grej BCD & Grej binarni\\\midrule
101001.100101 & 29.94 & -- & -- & -- & \shortstack{110001.000110\\49.09375}\\
10010011.1110101 & -- & -- & -- & -- & \shortstack{11100010.1011001\\226.6953125}\\
1011.101001 & -- & -- & 8.71 & -- & \shortstack{1101.001110\\13.21875}\\
\bottomrule\end{tabular}\end{adjustbox}
\end{center}

**Obrazloženje i uticaj:** Zadržani tačni numerički rezultati, ali prvi stupac sada sadrži izvorne bitove, pa se dopuna za BCD ne primenjuje pogrešno i na Grejov kod. Crta označava nedozvoljenu reč.

### 05-33 — blok 120

**Novo mesto:** [LaTeX](05_kodovi.tex), red 815; `% Izvor DOCX: blok 120`.

**Izvor:** Sabiranje BCD brojeva se realizuje na nivou binarnih BCD cifara, tj. sabirajući BCD cifru sa BCD cifrom. Ukoliko je neka od BCD cifara veća od 1001 (tj. 9), tada je potrebno dodati na tu cifru vrednost korekcije 0110 (tj. 6).

**Ispravka:** Sabiraju se po dve BCD cifre sa ulaznim decimalnim prenosom. Ako puni binarni zbir prelazi 9, tj. ako je četvorobitni rezultat veći od 1001 \emph{ili} postoji izlazni binarni prenos, dodaje se korekcija 0110. Zatim se cifra i decimalni prenos prosleđuju u sledeći korak.

**Obrazloženje i uticaj:** Izvor izostavlja korekciju kada postoji prenos iz četvorobitnog sabiranja, a donja četiri bita nisu veća od 9.

### 05-34 — blok 121

**Istorijski prikaz, zamenjen nalazom 05-A15:** sažeta tabela je čuvala rezultate po ciframa, ali nije prenela sve pisane međukorake izvornika. Tvrdnja ispod da je prenet svaki korak bila je preširoka. Sada je vraćen pisani postupak.

**Novo mesto:** [LaTeX](05_kodovi.tex), red 818; `% Izvor DOCX: blok 121`.

**Izvor:** Izraz | Postupak | Rezultat
34 + 13 |  | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 
 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 
 |  |  |  | 0 | 0 | 1 | 1 | 1 | Nema korekcije
 | 0 | 0 | 1 | 1 |  |  |  |  | 
 | 0 | 0 | 0 | 1 |  |  |  |  | 
 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | Nema korekcije | 47_{BCD}
35 + 86 |  |  |  | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 
 |  |  | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 
 |  |  |  |  |  |  | 1 | 0 | 1 | 1 | 
 |  |  |  |  |  |  |  | 1 | 1 | 0 | Korekcija
 |  |  |  |  |  | 1 | 0 | 0 | 0 | 1 | 
 |  |  | 0 | 0 | 1 | 1 |  |  |  |  | 
 |  |  | 1 | 0 | 0 | 0 |  |  |  |  | 
 |  |  | 1 | 1 | 0 | 0 |  |  |  |  | 
 |  |  |  | 1 | 1 | 0 |  |  |  |  | Korekcija
 |  | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |  | 121_{BCD}
1026 + 192 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 
 |  |  |  | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 
 |  |  |  |  |  |  |  |  |  |  | 0 | 1 | 0 | 0 | 0 | 
 |  |  |  |  |  |  |  | 0 | 0 | 1 | 0 |  |  |  |  | 
 |  |  |  |  |  |  |  | 1 | 0 | 0 | 1 |  |  |  |  | 
 |  |  |  |  |  |  |  | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 
 |  |  |  |  |  |  |  | 0 | 1 | 1 | 0 |  |  |  |  | Korekcija
 |  |  |  |  |  |  | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 
 |  |  |  | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  | 
 |  |  |  | 0 | 0 | 0 | 1 |  |  |  |  |  |  |  |  | 
 |  |  | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 
0 | 0 | 0 | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 
0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 |  | 1218_{BCD}
529 + 432 |  |  |  |  | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 
 |  |  |  | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 
 |  |  |  |  |  |  |  |  |  |  |  | 1 | 0 | 1 | 1 | 
 |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 1 | 0 | Korekcija
 |  |  |  |  |  |  |  |  |  |  | 1 | 0 | 0 | 0 | 1 | 
 |  |  |  |  |  |  |  | 0 | 0 | 1 | 0 |  |  |  |  | 
 |  |  |  |  |  |  |  | 0 | 0 | 1 | 1 |  |  |  |  | 
 |  |  |  |  |  |  | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 
 |  |  |  | 0 | 1 | 0 | 1 |  |  |  |  |  |  |  |  | 
 |  |  |  | 0 | 1 | 0 | 0 |  |  |  |  |  |  |  |  | 
 |  |  |  | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 961_{BCD}

**Ispravka:** \noindent\textbf{$34+13$}\par
\begin{center}
\begin{adjustbox}{max width=\linewidth}\begin{tabular}{cccccccc}\toprule
Poz. & $a_i$ & $b_i$ & $c_i$ & Binarni zbir & Korekcija & BCD cifra & $c_{i+1}$\\\midrule
0 & 4 & 3 & 0 & 00111 & 0000 & 0111 & 0\\
1 & 3 & 1 & 0 & 00100 & 0000 & 0100 & 0\\
\bottomrule\end{tabular}\end{adjustbox}
\end{center}
\begin{equation}
34+13=47\quad\longleftrightarrow\quad \mathtt{0100\,0111}
\end{equation}
\noindent\textbf{$35+86$}\par
\begin{center}
\begin{adjustbox}{max width=\linewidth}\begin{tabular}{cccccccc}\toprule
Poz. & $a_i$ & $b_i$ & $c_i$ & Binarni zbir & Korekcija & BCD cifra & $c_{i+1}$\\\midrule
0 & 5 & 6 & 0 & 01011 & 0110 & 0001 & 1\\
1 & 3 & 8 & 1 & 01100 & 0110 & 0010 & 1\\
\bottomrule\end{tabular}\end{adjustbox}
\end{center}
\begin{equation}
35+86=121\quad\longleftrightarrow\quad \mathtt{0001\,0010\,0001}
\end{equation}
\noindent\textbf{$1026+192$}\par
\begin{center}
\begin{adjustbox}{max width=\linewidth}\begin{tabular}{cccccccc}\toprule
Poz. & $a_i$ & $b_i$ & $c_i$ & Binarni zbir & Korekcija & BCD cifra & $c_{i+1}$\\\midrule
0 & 6 & 2 & 0 & 01000 & 0000 & 1000 & 0\\
1 & 2 & 9 & 0 & 01011 & 0110 & 0001 & 1\\
2 & 0 & 1 & 1 & 00010 & 0000 & 0010 & 0\\
3 & 1 & 0 & 0 & 00001 & 0000 & 0001 & 0\\
\bottomrule\end{tabular}\end{adjustbox}
\end{center}
\begin{equation}
1026+192=1218\quad\longleftrightarrow\quad \mathtt{0001\,0010\,0001\,1000}
\end{equation}
\noindent\textbf{$529+432$}\par
\begin{center}
\begin{adjustbox}{max width=\linewidth}\begin{tabular}{cccccccc}\toprule
Poz. & $a_i$ & $b_i$ & $c_i$ & Binarni zbir & Korekcija & BCD cifra & $c_{i+1}$\\\midrule
0 & 9 & 2 & 0 & 01011 & 0110 & 0001 & 1\\
1 & 2 & 3 & 1 & 00110 & 0000 & 0110 & 0\\
2 & 5 & 4 & 0 & 01001 & 0000 & 1001 & 0\\
\bottomrule\end{tabular}\end{adjustbox}
\end{center}
\begin{equation}
529+432=961\quad\longleftrightarrow\quad \mathtt{1001\,0110\,0001}
\end{equation}

**Obrazloženje i uticaj:** Prenet svaki korak BCD sabiranja, korekcija i prenos; sačuvani rezultati 47, 121, 1218 i 961. Izvorni mešoviti bitni prikaz zamenjen čitljivom tabelom po decimalnim pozicijama.

### 05-35 — zadatak 2.3 b, tabela suseda

**Dopunjeno nalazom 05-A16:** ispravni susedi i rezultati zadržani su, a vraćeni su izostavljeni međukoraci dekodovanja i isticanje bitova.

**Novo mesto:** [LaTeX](05_kodovi.tex), celina navedena u naslovu stavke.

**Izvor:** Tabela među rečima rastojanja 1 sadrži samu reč broja 23 (rastojanje 0), kao i nedozvoljene reči bez dosledne oznake.

**Ispravka:** Za svaki kod navedena je svaka reč nastala promenom jednog bita, uz ispravnu decimalnu vrednost ili oznaku „Nedozvoljena reč“.

**Obrazloženje i uticaj:** Iscrpna provera svih osam promena za decimalne kodove i svih pet promena za binarni Grejov kod; sačuvana početna širina.

### 05-36 — blok 136

**Novo mesto:** [LaTeX](05_kodovi.tex), red 1048; `% Izvor DOCX: blok 136`.

**Izvor:** * Na osnovu relacije 1.1.3 važi da je u slučaju minimalnog hamingovog rastojanja 4 moguće:

**Ispravka:** a) Za $d_{\min}=4$ važe sledeće mogućnosti:

**Obrazloženje i uticaj:** Referenca na odeljak zamenjena direktno primenjenim uslovom.

### 05-37 — blok 137

**Novo mesto:** [LaTeX](05_kodovi.tex), red 1051; `% Izvor DOCX: blok 137`.

**Izvor:** * (n_{c} = 0; n_{d} = 3) detekcija trobitnih grešaka bez korekcije
* (n_{c} = 0; n_{d} = 2) detekcija dvobitnih grešaka bez korekcije
* (n_{c} = 1; n_{d} = 1) korekcija 1bitne geške i detekcija 1bitne greške

**Ispravka:** \begin{itemize}[leftmargin=*]
\item Samo detekcija: garantovano se otkrivaju sve jednobitne, dvobitne i trobitne greške; za četvorobitne nema opšte garancije.
\item Samo korekcija: garantovano se koriguje jedna greška; za dve, tri ili četiri nema garancije korekcije.
\item Istovremeno: jedna greška se koriguje, a do dve se detektuju ($n_c=1$, $n_d=2$).
\end{itemize}

**Obrazloženje i uticaj:** Ispravljeno značenje dodatne detekcije: kod rastojanja 4 podržava SECDED. Garantovana detekcija do tri obuhvata i izvorno zasebno navedenu detekciju do dve.

### 05-38 — blok 138

**Novo mesto:** [LaTeX](05_kodovi.tex), red 1058; `% Izvor DOCX: blok 138`.

**Izvor:** * Na osnovu relacije 1.1.3 važi da je u slučaju minimalnog Hamingovog rastojanja 5 moguće:

**Ispravka:** b) Za $d_{\min}=5$ važe sledeće mogućnosti:

**Obrazloženje i uticaj:** Ujednačen prikaz dve tačke zadatka.

### 05-39 — blok 139

**Novo mesto:** [LaTeX](05_kodovi.tex), red 1061; `% Izvor DOCX: blok 139`.

**Izvor:** * (n_{c} = 0; n_{d} = 4) detekcija četvorobitnih grešaka bez korekcije
* (n_{c} = 0; n_{d} = 3) detekcija trobitnih grešaka bez korekcije
* (n_{c} = 1; n_{d} = 2) detekcija dvobitnih grešaka i korekcija jednobitne greške
* (n_{c} = 2; n_{d} = 0) korekcija dvobitne geške i bez detekcije dodatnih grešaka

**Ispravka:** \begin{itemize}[leftmargin=*]
\item Samo detekcija: garantovano se otkrivaju sve greške sa jednom, dve, tri ili četiri promenjena bita.
\item Samo korekcija: garantovano se koriguju do dve greške.
\item Istovremeno: mogu se korigovati do jedne i detektovati do tri greške, ili korigovati do dve i detektovati do dve ($n_c=n_d=2$), bez garancije detekcije dodatnih trobitnih grešaka u drugom režimu.
\end{itemize}

**Obrazloženje i uticaj:** Ispravljena terminologija ukupnog i dodatnog broja grešaka, uz odgovor za sve tražene težine od 1 do 4.

### 05-40 — blok 148

**Novo mesto:** [LaTeX](05_kodovi.tex), red 1123; `% Izvor DOCX: blok 148`.

**Izvor:** * Minimalno Hamingovo rastojanje iznosi 2 za oba koda
* Na osnovu relacija 2.3.1 ni jedan od kodova ne podržava mogućnost korekcije već samo mogućnost detekcije greške

**Ispravka:** b) Za fiksnu dužinu reči oba koda imaju minimalno rastojanje 2.\par c) Oba otkrivaju svaku promenu neparnog broja bita, a ne otkrivaju parne promene. Ne omogućavaju određivanje položaja ni korekciju jedne greške.

**Obrazloženje i uticaj:** Uklonjena nepostojeća referenca 2.3.1 i precizirana sposobnost detekcije.

### 05-41 — blok 150

**Novo mesto:** [LaTeX](05_kodovi.tex), red 1131; `% Izvor DOCX: blok 150`.

**Izvor:** * Izvršiti korekciju greške u prijemu ako je primljena sekvenca d_{7}d_{6}d_{5}c_{4}d_{3}d_{2}c_{1}c_{0} = 1011100 kodirana Hamming-ovim kodom sa tri kontrolna bita koji proveravaju parnu parnost
* Zaštiti originalnu sekvencu iz prethodne tačke sa kodom sa Hamming-ovim rastojanjem 4.
* Koliki je maksimalni broj informacionih bita u kodnoj reči datoj u Hamming-ovom kodu sa minimalnim Hamming-ovim rastojanjem 3 ako imamo ukupno 5 kontrolnih bita.

**Ispravka:** \begin{enumerate}[label=\alph*),leftmargin=*]
\item Ispraviti jednu grešku u primljenoj reči $d_7d_6d_5c_4d_3c_2c_1=1011100$, kodiranoj Hamingovim kodom sa tri kontrolna bita parne parnosti. Pretpostaviti da je promenjen najviše jedan bit.
\item Istu informacionu poruku zaštititi kodom minimalnog rastojanja 4.
\item Odrediti maksimalan broj informacionih bita za Hamingov kod minimalnog rastojanja 3 sa pet kontrolnih bita.
\end{enumerate}

**Obrazloženje i uticaj:** Izvor nabraja osam pozicija za sedmobitnu reč i koristi nepostojeći c0. Ispravljen raspored i eksplicitna pretpostavka korekcije jedne greške.

### 05-42 — blok 153

**Novo mesto:** [LaTeX](05_kodovi.tex), red 1149; `% Izvor DOCX: blok 153`.

**Izvor:** * 1011100 – bit c_{1} ukazuje na grešku jer je broj jedinica neparan a kontrolni bit ima vrednost 0
* 1011100 - bit c_{2} ne ukazuje na grešku jer je broj jedinica na mestima koje kontroliše paran a kontrolni bit ima vrednost 0
* 1011100 - bit c_{4} ukazuje na grešku jer je broj jedinica na mestima koje kontroliše paran a kontrolni bit ima vrednost 1

**Ispravka:** \begin{align*}
s_1&=c_1\oplus d_3\oplus d_5\oplus d_7=0\oplus1\oplus1\oplus1=1,\\
s_2&=c_2\oplus d_3\oplus d_6\oplus d_7=0\oplus1\oplus0\oplus1=0,\\
s_4&=c_4\oplus d_5\oplus d_6\oplus d_7=1\oplus1\oplus0\oplus1=1.
\end{align*}

**Obrazloženje i uticaj:** Svaka provera sada uključuje i kontrolni bit; izračunati su biti sindroma, a ne nove vrednosti kontrolnih bita.

### 05-43 — blok 154

**Novo mesto:** [LaTeX](05_kodovi.tex), red 1156; `% Izvor DOCX: blok 154`.

**Izvor:** Kako bi detektovali gde je došlo do greške neophodno je da na ispod kontrolnih bita koji su detektovali grešku upišemo 1 a ispod kontrolnih bita koji nisu detektovali grešku upišemo nulu a zatim pročitamo tako dobijeni kod. Dakle, c_{4}c_{2}c_{1} = 101 ukazuje da se greška desila na poziciji 5 i da je ispravna sekvenca zapravo 1001100.

**Ispravka:** Sindrom je $(s_4s_2s_1)_2=(101)_2=5$. Menja se bit na poziciji 5, pa je ispravljena reč $1001100$. Ponovna provera daje sindrom 000.

**Obrazloženje i uticaj:** Izvor pogrešno zapisuje sindrom kao c4c2c1, iako primljeni kontrolni biti imaju sadržaj 100.

### 05-44 — blok 155

**Novo mesto:** [LaTeX](05_kodovi.tex), red 1159; `% Izvor DOCX: blok 155`.

**Izvor:** [IMAGE /tmp/de1-work/05/media/image10.png]Drugi način za utvrđivanje pozicije na kojoj je došlo do greške jeste analizom Venovog dijagrama sa slike 2.6.1

**Ispravka:** Isti zaključak dobijamo pomoću Venovog dijagrama sa slike~\ref{fig:venn-task}.

**Obrazloženje i uticaj:** Zamenjena ručna referenca i prenet izmenjivi crtež.

### 05-45 — blok 157

**Novo mesto:** [LaTeX](05_kodovi.tex), red 1168; `% Izvor DOCX: blok 157`.

**Izvor:** Sa slike 2.6.1 se vidi da biti c_{4} i c_{1} zajedno kontrolišu bite d_{7} i d_{5} tako da oni predstavljaju kandidate za bite na kojima je došlo do greške. Pošto bit c_{2} kontroliše bit d_{7} jasno je da on nije pogrešan i zbog toga bit d_{5} ostaje jedini mogući bit na kome je došlo do greške.

**Ispravka:** Pozicije 5 i 7 pripadaju i grupi $c_1$ i grupi $c_4$. Pozicija 7 pripada i grupi $c_2$, čija provera prolazi. Uz pretpostavku jedne greške preostaje pozicija 5.

**Obrazloženje i uticaj:** Obrazloženje važi uz ograničenje jedne greške, što je sada navedeno.

### 05-46 — blok 37

**Novo mesto:** [LaTeX](05_kodovi.tex), red 184; `% Izvor DOCX: blok 37`.

**Izvor:** Na osnovu sadržaja tabele 1.1.1.2 možemo zaključiti da se cifre 0-4 koduju na isti način kao i u slučaju BCD koda. Međutim, kodne reči cifara 5-9 se dobijaju komplementiranjem cifara simetričnih u odnosu na crvenu osu simetrije (sredinu tabele). U opštem slučaju, kodovi kod kojih su predstave cifara u donjoj polovini tabele simetrični u odnosu na cifre iz gornje gornje polovine, spadaju u kategoriju komplementarnih kodova.

**Ispravka:** Jednako obojeni redovi u tabeli~\ref{tab:2421} nalaze se na jednakom rastojanju od crvene horizontalne ose. Njihove kodne reči su bit po bit komplementarne: $c(9-d)=\overline{c(d)}$. Parovi su $0\leftrightarrow9$, $1\leftrightarrow8$, $2\leftrightarrow7$, $3\leftrightarrow6$, $4\leftrightarrow5$. To je antisimetrija vrednosti bita ($0\leftrightarrow1$), odnosno samokomplementarnost koda. Za cifre 0–4 kod se poklapa sa BCD8421.

**Obrazloženje i uticaj:** Dopuna prenosa: vraćena crvena horizontalna osa i vizuelno uparivanje komplementarnih redova; osa je postojala u Word crtežu, ali nije bila preneta ekstrakcijom.

### 05-47 — blok 50

**Novo mesto:** [LaTeX](05_kodovi.tex), red 270; `% Izvor DOCX: blok 50`.

**Izvor:** Cifra | Korak
I | II | III | IV
n = 1 | n = 2 | n = 3 | n = 4
0 | 0 | 00 | 000 | 0000
1 | 1 | 01 | 001 | 0001
2 |  | 11 | 011 | 0011
3 |  | 10 | 010 | 0010
4 |  |  | 110 | 0110
5 |  |  | 111 | 0111
6 |  |  | 101 | 0101
7 |  |  | 100 | 0100
8 |  |  |  | 1100
9 |  |  |  | 1101
10 |  |  |  | 1111
11 |  |  |  | 1110
12 |  |  |  | 1010
13 |  |  |  | 1011
14 |  |  |  | 1001
15 |  |  |  | 1000

**Ispravka:** \begin{table}[!htbp]\centering\caption{Reflektovana konstrukcija Grejovog koda od jednog do četiri bita.}\label{tab:graybuild}
\begin{minipage}[t]{.24\linewidth}\centering$n=1$

\begin{tabular}{cc}\toprule
$i$ & $g_0$\\
\midrule
0 & \texttt{0}\\
1 & \texttt{1}\\
\bottomrule\end{tabular}
\end{minipage}\hfill
\begin{minipage}[t]{.24\linewidth}\centering$n=2$

\setlength{\tabcolsep}{3pt}\begin{tabular}{cccc}\toprule
$i$ & $g_{1}$ & $g_0$ & red\\
\midrule
0 & \textcolor{Primary}{\texttt{0}} & \cellcolor{blue!8}\texttt{0} & $\downarrow$\\
1 & \textcolor{Primary}{\texttt{0}} & \cellcolor{blue!8}\texttt{1} & $\downarrow$\\
\arrayrulecolor{red!70!black}\specialrule{.6pt}{2pt}{2pt}\arrayrulecolor{black}
2 & \textcolor{Primary}{\texttt{1}} & \cellcolor{orange!12}\texttt{1} & $\uparrow$\\
3 & \textcolor{Primary}{\texttt{1}} & \cellcolor{orange!12}\texttt{0} & $\uparrow$\\
\bottomrule\end{tabular}
\end{minipage}\hfill
\begin{minipage}[t]{.24\linewidth}\centering$n=3$

\setlength{\tabcolsep}{3pt}\begin{tabular}{cccc}\toprule
$i$ & $g_{2}$ & $g_{1}\dots g_0$ & red\\
\midrule
0 & \textcolor{Primary}{\texttt{0}} & \cellcolor{blue!8}\texttt{00} & $\downarrow$\\
1 & \textcolor{Primary}{\texttt{0}} & \cellcolor{blue!8}\texttt{01} & $\downarrow$\\
2 & \textcolor{Primary}{\texttt{0}} & \cellcolor{blue!8}\texttt{11} & $\downarrow$\\
3 & \textcolor{Primary}{\texttt{0}} & \cellcolor{blue!8}\texttt{10} & $\downarrow$\\
\arrayrulecolor{red!70!black}\specialrule{.6pt}{2pt}{2pt}\arrayrulecolor{black}
4 & \textcolor{Primary}{\texttt{1}} & \cellcolor{orange!12}\texttt{10} & $\uparrow$\\
5 & \textcolor{Primary}{\texttt{1}} & \cellcolor{orange!12}\texttt{11} & $\uparrow$\\
6 & \textcolor{Primary}{\texttt{1}} & \cellcolor{orange!12}\texttt{01} & $\uparrow$\\
7 & \textcolor{Primary}{\texttt{1}} & \cellcolor{orange!12}\texttt{00} & $\uparrow$\\
\bottomrule\end{tabular}
\end{minipage}\hfill
\begin{minipage}[t]{.24\linewidth}\centering$n=4$

\setlength{\tabcolsep}{3pt}\begin{tabular}{cccc}\toprule
$i$ & $g_{3}$ & $g_{2}\dots g_0$ & red\\
\midrule
0 & \textcolor{Primary}{\texttt{0}} & \cellcolor{blue!8}\texttt{000} & $\downarrow$\\
1 & \textcolor{Primary}{\texttt{0}} & \cellcolor{blue!8}\texttt{001} & $\downarrow$\\
2 & \textcolor{Primary}{\texttt{0}} & \cellcolor{blue!8}\texttt{011} & $\downarrow$\\
3 & \textcolor{Primary}{\texttt{0}} & \cellcolor{blue!8}\texttt{010} & $\downarrow$\\
4 & \textcolor{Primary}{\texttt{0}} & \cellcolor{blue!8}\texttt{110} & $\downarrow$\\
5 & \textcolor{Primary}{\texttt{0}} & \cellcolor{blue!8}\texttt{111} & $\downarrow$\\
6 & \textcolor{Primary}{\texttt{0}} & \cellcolor{blue!8}\texttt{101} & $\downarrow$\\
7 & \textcolor{Primary}{\texttt{0}} & \cellcolor{blue!8}\texttt{100} & $\downarrow$\\
\arrayrulecolor{red!70!black}\specialrule{.6pt}{2pt}{2pt}\arrayrulecolor{black}
8 & \textcolor{Primary}{\texttt{1}} & \cellcolor{orange!12}\texttt{100} & $\uparrow$\\
9 & \textcolor{Primary}{\texttt{1}} & \cellcolor{orange!12}\texttt{101} & $\uparrow$\\
10 & \textcolor{Primary}{\texttt{1}} & \cellcolor{orange!12}\texttt{111} & $\uparrow$\\
11 & \textcolor{Primary}{\texttt{1}} & \cellcolor{orange!12}\texttt{110} & $\uparrow$\\
12 & \textcolor{Primary}{\texttt{1}} & \cellcolor{orange!12}\texttt{010} & $\uparrow$\\
13 & \textcolor{Primary}{\texttt{1}} & \cellcolor{orange!12}\texttt{011} & $\uparrow$\\
14 & \textcolor{Primary}{\texttt{1}} & \cellcolor{orange!12}\texttt{001} & $\uparrow$\\
15 & \textcolor{Primary}{\texttt{1}} & \cellcolor{orange!12}\texttt{000} & $\uparrow$\\
\bottomrule\end{tabular}
\end{minipage}
\par\medskip\small Plavi bit je novi MSB. Donji biti se prepisuju redom ($\downarrow$), a zatim obrnutim redom ($\uparrow$). Crvena linija je osa refleksije svakog koraka.
\end{table}

**Obrazloženje i uticaj:** Dopuna prenosa: originalna tabela je prikazivala korake refleksije, ne samo završne reči. Sada su odvojeni novi MSB, prethodni niz, smer čitanja i osa svakog koraka. Provereno g(i)=i XOR (i>>1).

## Jezik, oznake i prelom

Ujednačeni su izrazi „razlomljeni deo“, „proširenje znaka“, nazivi predstava, razmaci, interpunkcija i dijakritika. Ispravljene su tipografske greške navedene u tekstu (npr. „ne promenjen“, „ospegu“, „prebaivanje“). Ručne reference zamenjene su automatskim; Word tabele za raspored jednačina zamenjene su matematičkim okruženjima. Naslovna strana i autorstvo usklađeni su sa vežbama 01 i 02 po dogovoru.

## Provere

Kontrolna skripta proverava sve kodne tabele, cikličnost decimalnog Grejovog koda, konverzije i sve susede broja 23, sve parnosti, 200 kombinacija BCD cifara sa ulaznim prenosom, svih 16 poruka Hamingovog (7,4) koda i sve pojedinačne greške. Za prošireni (8,4) kod proverava i sve dvobitne greške.

## Stručni izvor

Razlika između korekcije jedne greške i istovremene detekcije dve proverena je u izvornom radu: [R. W. Hamming, Error Detecting and Error Correcting Codes, 1950](https://ineffectivetheory.com/edu/papers/hamming-codes-1950.pdf), odeljci 3 i 4. Rezultati konkretnih primera ponovo su nezavisno izračunati.

## Napomena o sadržaju

Izvorni Word sadržaj navodi „Zadatke za samostalni rad“, ali u telu dokumenta posle zadatka 2.6 takva celina ne postoji. Ta zastarela stavka nije preneta u automatski sadržaj; nijedan postojeći zadatak nije izostavljen. Dva prazna Word naslova uklonjena su iz numeracije.

## Dopune vizuelnog prenosa

Vraćene su oznake horizontalne ose i upareni redovi BCD2421 tabele (izvor 1.1.1.2), i postupak refleksije u svakom koraku Grejove konstrukcije (izvor 1.1.2.2). Slika Hamingovih kocki sada eksplicitno sadrži 1, 4 i 12 ivica; oznake su pomerene van putanja ivica. To su ispravke konverzije, ne greške izvorne teorije.

## Dodatna provera izgleda nakon konverzije

Diskretna siva linija razdvaja susedne redove podataka. Uz `\toprule`, `\midrule` i `\bottomrule` ne dodaje se druga, tanka linija. Vidljivi tekst „oprule“ bio je artefakt konverzije: Python je početak `\toprule` protumačio kao tabulator (`\t`). Ispravljen je LaTeX zapis komande; sama komanda iz paketa booktabs crta gornju ivicu tabele i ne treba da se vidi kao tekst. Ovo su ispravke nastalog LaTeX dokumenta, a ne greške DOCX izvornika.

Dodatno su ujednačeni nazivi „Grejov“ i „Hamingov“ u blokovima 44, 48, 59 i 123; u bloku 66 opis kanala koristi termine predajnik i prijemnik umesto mešavine srpskih i engleskih naziva. Tabele sa simetrijom i slika Hamingovog rastojanja opisane su zasebno u ovom izveštaju.

## Ponovna potpuna provera — 25. 9. 2026.

Ranija istorija iznad je sačuvana. Novi nalazi odnose se na stanje LaTeX-a pri početku ove provere. Tačni tekstualni zapisi pre/posle nalaze se i u [nalazi_05_tekst.json](../PROVERA/nalazi_05_tekst.json); trajna mesta ispod određena su DOCX blokom ili LaTeX oznakom. [Dokazi](code/PREGLED_DOKAZA.md) razdvajaju dedukciju, iscrpne provere i usvojene pretpostavke.

### 05-A01 — vrste kodova nisu disjunktna klasifikacija

**Mesto:** blok 24, odeljak 1.1. **Pre:** „binarni kodovi se mogu razvrstati u 4 grupe“. **Posle:** navedene su razmatrane vrste uz objašnjenje preklapanja. **Vrsta:** stručno pojašnjenje. Težinski kod takođe može imati detekciju greške (npr. težine 1,1,1,1 i reči sa tačno dve jedinice); klasifikacija po nameni i po težinama nije ista. Nijedna kodna tabela nije promenjena.

### 05-A02 — nepotpuno obrazloženje netežinskosti

**Mesto:** blok 112, zadatak 1a. **Pre:** „0011 ... predstavlja nulu i ne može se tumačiti običnim nenegativnim pozicionim težinama“. **Posle:** izvedena su dva protivrečna sistema za prve četiri kodne reči. **Vrsta:** stručna dopuna dokaza. Samo jedna reč za nulu ne isključuje sve fiksne težine; novi dokaz isključuje čak i proizvoljne realne aditivne težine za date višebitne kodove. Kod „više 3“ zahteva w₀=1,w₁=2 i w₀+w₁=0, a oba Grejova koda w₁=1 i w₁=3. Rezultati konverzija ostaju isti. Ponovo provereno direktnom zamenom svih navedenih reči.

### 05-A03 — pretpostavke razlomljenog kodnog zapisa

**Mesto:** blokovi 109/113, zadatak 1b i `tab:dekodiranje`. **Pre:** nepotpune grupe se „dopunjuju nulama“, a konvencija fiksne tačke uvedena tek u rešenju. **Posle:** pretpostavke jasno navedene uz postavku; objašnjeno da to nije opšte produžavanje kodnih reči uz očuvanje vrednosti. **Vrsta:** ograničenje nepotpune postavke, dopuna. Npr. 0000 nije nula koda „više 3“. Binarni Grejov kod ne definiše sam po sebi nezavisno kodovanje dva dela oko tačke. Sa izričito usvojenom konvencijom svi postojeći rezultati ostaju tačni; provereni tačnom racionalnom aritmetikom. Bez nje problem nema jednoznačno tumačenje.

### 05-A04 — širina određuje sve jednobitne susede

**Mesto:** blok 132, zadatak 3b, `tab:susedi-*`. **Pre:** širine su bile samo vidljive u tabelama. **Posle:** izričito osam bita za dve decimalne cifre i pet za binarni Grejov kod. **Vrsta:** dopunska pretpostavka. Dodavanje vodećeg bita proširuje skup mogućih jednobitnih promena. Sve 37 prikazane reči ponovo su proverene i nijedna vrednost nije promenjena.

### 05-A05 — formiranje i provera kontrolnog bita

**Mesto:** blokovi 85/92/98, uvod o Hamingovom kodu. **Pre:** kontrolni bit „predstavlja njihov bit parnosti“ uz grupu koja sadrži i njega; nije neposredno naglašeno da se r odnosi na osnovni kod. **Posle:** razlikuju se izbor bita prema ostalim bitovima i provera cele grupe; r je pre opšte parnosti, numeracija ide zdesna nalevo. **Vrsta:** stručno pojašnjenje, uklanjanje mogućeg kružnog tumačenja. Matrica ima jedinične kolone na stepenima dvojke. Sve stvarne kontrolne grupe i pozicije automatski su pročitane i proverene; nema promene sindroma ni konačnih reči. Primarni izvor ponovo pročitan: Hamming (1950), odeljak 3, str. 150–153; opšta parnost odeljak 4, str. 153–154.

### 05-A06 — nazivi, reference i prelomi tabela

**Mesto:** blokovi 93,95,97,99,112,114,121,132,147. **Pre:** 17 sadržinskih tabela bilo je bez naslova/broja, uz odvojene nazive kodova i ponovljene naslove sabiranja. **Posle:** `\captionof{table}` i jedinstvene oznake; naslov ostaje uz tabelu, sabiranja su imenovana u naslovu, susedne liste imaju vertikalni razmak. Dodate oznake za šest ranije neoznačenih jednačina, bez promene njihovih izraza. **Vrsta:** formatiranje. Uvodni naslov „Više 3“ više nije sam na dnu stranice; plivajuća BCD2421 tabela ostaje pre nove teorijske celine. Nema tankih duplih linija uz naglašene granice. Svih 17 konačnih stranica pregledano je posle poslednje izgradnje.

### 05-A07 — jezik i oznake

**Mesta:** blokovi 48,53,56,67,89,111,127,139,144,146,158. „s desna na levo“ → „zdesna nalevo“, „zaštiti“ → „zaštititi“, „sa parnom/neparnom parnosti“ → „parnošću“, „do jedne“ → „jedna“, automatskim referencama dodat naziv odeljka. „Bit najveće težine“ u netežinskom kodu zamenjen je krajnjim levim bitom; matematičke promenljive i eksponenti pravilno su složeni. U zadatku 6b H_d=4 zamenjeno je preciznim d_min=4. **Vrsta:** jezička/terminološka. Ponovni pregled potvrdio da značenje postavki nije izmenjeno.

### Ponovna potvrda ranijih ispravki i vizuelnih zahteva

Provereni su i ostaju ispravni: d(0001,0101)=1, decimalni Grejov kod za 9, osnovni Hamingov kod kao SEC ili samo detekcija dve greške, prošireni SECDED, sindrom 101 → pozicija 5, 1001100 i 10011001. BCD2421 osa i svi parovi boja su očuvani. Grejova tabela prikazuje sva četiri koraka i razlikuje refleksiju donjih bita od komplementiranja MSB-a. Kocke imaju kompletne jedinstvene skupove 1/4/12 ivica, bez preklopljenih oznaka; četiri slikovna izvora nisu precrtavana tokom ove provere. Venove grupe proverene su iz stvarnih koordinata krugova i oznaka.

Automatska provera sada vezuje rezultate za stvarne ćelije/formule, uključuje sve 2048 poruke prikazane konstrukcije (15,11) sa svim pojedinačnim i dvobitnim greškama, i sve maske greške za (7,4)/(8,4). Broj uspešnih računskih provera nije zamena za zasebno dokumentovan teorijski i vizuelni pregled.

## Dopune prema izvornim tabelama i primedbama — 25. 9. 2026.

### 05-A08 — različiti biti u Tabeli 6

**Mesto pre/posle:** DOCX blok 73, XML tabela 8 (brojanje od nule); `tab:distances`, Tabela 6. **Pre:** svih 14 izraza bilo je bez istaknutih različitih bita, iako DOCX koristi crveno označavanje. **Posle:** različite pozicije u obe reči označene su tamnoplavom bojom i podebljanjem (`\istaknutbit`). **Vrsta:** propust pri prenosu grafičkog objašnjenja. Boja prati postojeću boju Primary; podebljanje pomaže i pri štampi u sivim tonovima. Obeležena su oba bita svakog različitog para, uključujući poslednju nulu u drugoj reči izraza d(0001,0000), koju izvornik nije obojio. Ranije ispravljen rezultat d(0001,0101)=1 ostaje. **Provera:** za svaki par automatski se porede skupovi označenih pozicija sa mestima razlike, kao i broj razlika sa prikazanim rastojanjem. Vrednosti reči i rezultati nisu promenjeni.

### 05-A09 — dodatni biti parnosti u Tabeli 7

**Mesto pre/posle:** DOCX blok 81, XML tabela 10; `tab:parity3`, Tabela 7. **Pre:** sve cifre imale su isti izgled. **Posle:** samo četvrti, dodati bit u kolonama parne i neparne parnosti istaknut je kao u Tabeli 6. **Vrsta:** propust pri prenosu označavanja iz DOCX-a. **Provera:** svih osam poruka ima neobeležena tri informaciona bita i po jedan označen završni bit u obe kodne reči; ponovo je proverena parnost svih 16 reči. Nema promene vrednosti.

### 05-A10 — strelice kontrolnih grupa u Tabeli 11

**Mesto pre/posle:** DOCX blok 99, XML tabela 17, dno 10. strane; `tab:raspored-provera`, Tabela 11, i povezana `tab:grupe`. **Pre:** ostao je samo raspored pozicija, bez strelica iz originala. **Posle:** TikZ vodovi ispod tabele vode od svakog kontrolnog bita do pripadajućih informacionih pozicija. Kontrolne ćelije i strelice imaju usklađene boje; različite grupe su vertikalno razmaknute. **Vrsta:** grafički propust pri prenosu. Original prikazuje strelice za C₁, C₂ i C₄; dopunjena je i grupa C₈ da svih 15 pozicija i četiri kontrole budu prikazani dosledno. Grupa obuhvata i svoj kontrolni bit, od kog vod polazi; strelice pokazuju preostalih sedam pozicija.

**Obrazloženje/provera:** za kontrolu p∈{1,2,4,8} cilj i pripada grupi ako i AND p ≠ 0. Iz LaTeX-a se čitaju položaji svih 15 priključnih oznaka i četiri liste od po sedam ciljeva, pa porede sa ovim pravilom i Tabelom 12. Ručno je ispraćeno da svaka vodoravna linija polazi od odgovarajuće kontrolne ćelije i da su sve strelice izvučene naviše do pravilnih kolona. Postojeći raspored C/D i vrednosti nisu menjani. Tabela sa svim strelicama ostaje u jednom bloku na stranici.

### 05-A11 — oznaka d₃ u Venovom dijagramu

**Mesto pre/posle:** `Images/Uvod/ven.tex`, `fig:venn`, Slika 3. **Pre:** centar oznake d₃ bio je na (0; 0,9), pa je njen donji deo dodirivao gornju kružnicu grupe c₄. **Posle:** centar je (0; 1,15). **Vrsta:** grafička ispravka. **Provera:** pregled izvoza i konačne stranice potvrđuje slobodan razmak; oznaka i dalje pripada c₁∩c₂, van c₄. Za leve/desne krugove kvadrat rastojanja je 0,8²+0,65²=1,0625 < 1,65²=2,7225, a za donji je 2,05²=4,2025 > 2,7225. Sve ostale oznake i geometrija ostaju isti; ažuriran je otisak pregledanog izvora.

### 05-A12 — usklađivanje prvog primera na broj 43

**Mesto pre/posle:** DOCX blokovi 106 i 112, `sec:2.1`, `tab:kodiranje`, prvi red Tabele 13; raniji nalaz 05-30. **Izvorna nedoslednost:** postavka navodi 13, a prvi red rešenja broj 43; kolona Grej BCD čak zadržava kod za 13. Ranija konverzija je sve uskladila na 13 prema postavci. **Sada, po izričitom zahtevu korisnika:** i postavka i rešenje koriste 43. **Vrsta:** razrešenje nedoslednosti izvornika prema potvrđenoj nameri korisnika, uz stručnu ispravku jedne izvorne kodne reči.

**Proverene vrednosti za 43:** BCD8421 `0100 0011`; BCD2421 `0100 0011`; „više 3“ `0111 0110`; Grej BCD `0110 0010`; binarni Grej `111110`. Cifre 4 i 3 koduju se zasebno prema odgovarajućim tabelama. Posebno, izvorno `0001 0010` u Grej BCD koloni koduje 13, pa je zamenjeno sa `0110 0010`. Za binarni Grej važi 43=101011₂ i 101011 XOR 010101=111110. Ažurirani su ulaz i svih pet rezultata u dokumentu i računskom prilogu; preostala četiri primera nisu promenjena. Provera sada vezuje i spisak operanada iz postavke sa redovima tabele, a ne samo rezultate međusobno.

### 05-A13 — vraćen početni binarni zapis u Tabeli 13

**Mesto pre/posle:** DOCX blok 112, kolona „Gray binarni“; `tab:kodiranje`. **Pre:** prikazivana je samo konačna Grejova reč. **Posle:** svaki red prikazuje početni šestobitni binarni zapis i strelicu ka šestobitnoj Grejovoj reči. Po dodatnom zahtevu kolona je proširena na 4,3 cm da ceo prelaz stane u jedan red, bez prelamanja. Indeks 2 označava binarni broj, a oznaka G kodnu reč; značenje je navedeno ispod tabele. **Vrsta:** izgubljen didaktički međukorak tokom konverzije. Strelica zamenjuje izvorni znak jednakosti između zapisa različitog značenja.

**Provereni prelazi:** `101011→111110`, `000000→000000`, `001111→001000`, `110001→101001`, `111110→100001`, redom za 43, 0, 15, 49 i 62. Za svaki stvarno prikazan početni zapis proverena je decimalna vrednost i formula g=b XOR (b>>1). Ujednačene vodeće nule ne menjaju brojeve. Tabela zadržava sve ostale kolone i diskretne razdelnike redova.

**Ponovna provera ove dopune:** `make -C vezbe/05` i `make -C vezbe/05 check` uspešni (256.515 računskih/logičkih provera), kao i `structure.py 05`. Konačni dokument i dalje ima 17 stranica. Promenjene stranice pregledane su pojedinačno, uz poređenje ostalih rendera sa prethodnim PDF-om. Prethodni zapis čiste izgradnje ostaje istorijski; ova dopuna je proverena redovnom izgradnjom i novim vizuelnim pregledom.

### 05-A14 — binarna i decimalna predstava u istom redu Tabele 14

**Mesto pre/posle:** DOCX blok 114, `tab:dekodiranje`, kolona „Grej binarni“. **Pre:** dekodirani binarni zapis i njegova decimalna vrednost bili su prelomljeni u dva reda komandom `\shortstack`. **Posle:** kolona ima zadatu širinu 6,3 cm, a oba zapisa povezana su znakom jednakosti u jednom redu, uz oznake osnova 2 i 10. Razmak uz ivice ćelija ove tabele smanjen je na 4 pt da tabela ostane unutar margina. **Vrsta:** poboljšanje čitljivosti po zahtevu korisnika.

**Obrazloženje i provera:** binarni i decimalni zapis predstavljaju istu dekodiranu vrednost; jedinstven red čini tu vezu neposrednom. Nijedan bit niti računski rezultat nije promenjen. Postojeći parser prilagođen je novom prikazu, uz očuvane nezavisne provere sva tri dekodovanja i tačnih racionalnih vrednosti. `make -C vezbe/05`, `make -C vezbe/05 check` (256.515 provera) i `structure.py 05` prolaze; nova stranica pregledana je na 140 dpi, bez prelamanja ili prekoračenja širine tabele.

### 05-A15 — vraćeni pisani međukoraci BCD sabiranja u zadatku 2.2

**Mesto pre/posle:** DOCX blok 121, XML tabela 20 sa ugnježdenim tabelama 21–24 (indeksi od nule), izvorne strane 13–14; `sec:2.2`, `tab:zbir-1`, `tab:zbir-2`, `tab:zbir-3`, `tab:zbir-4` i jednačine `eq:bcd-zbir-1`–`eq:bcd-zbir-4`.

**Pre:** četiri sažete tabele prikazivale su po jedan red za decimalnu poziciju: cifre, ulazni prenos, zbir, korekciju i rezultat. To jeste prenosilo brojčane rezultate, ali je uklonilo originalni pisani postupak, položaj korekcije i nastajanje međurezultata. **Posle:** svako sabiranje ponovo ima poravnate bitove početnih sabiraka, obradu zdesna nalevo, crte sabiranja, nekorigovani zbir, dodavanje 0110 gde je potrebno i korigovani međurezultat. Već dobijene niže BCD cifre ostaju vidljive. Ulazni prenos je posebno ispisan na pravom bitnom mestu; prenos i korekcija istaknuti su plavom bojom. Nulti viši delovi poravnati su vodećim nulama.

**Vrsta i razlog:** propust u prenosu didaktičkih detalja; ranija zamena originala previše sažetim tabelama bila je nepotrebna. U okviru pisanog računa horizontalne crte označavaju sabiranje; odvojene decimalne pozicije imaju dodatni vertikalni razmak. Svaka tabela ostaje sa svojim naslovom i završnom jednačinom. Oznake i konačni rezultati 47, 121, 1218 i 961 nisu promenjeni.

**Provera:** sva četiri postupka ukupno imaju 11 decimalnih pozicija i 44 računska reda (6, 11, 15 i 12), uključujući četiri korekcije 0110 i tri eksplicitna ulazna prenosa 1. Iz stvarnog LaTeX-a provereni su svaki bit, prazne pozicije, širina, operator, prenos, poravnanje korekcije, prepisani niži deo i odluka o korekciji. Rezultati su izvedeni iz operanada postavke i provereni konačnim jednakostima. Na privremenim kopijama promena bita međuzbira i zamena 0110 sa 0111 pravilno obaraju proveru. Izvorne stranice upoređene su vizuelno i preko Word XML-a; dodatni eksplicitni redovi prenosa pojašnjavaju prenose koji su u originalu sadržani u prethodnom međurezultatu.

### 05-A16 — vraćeni koraci i označavanje u zadatku 2.3

**Mesto pre/posle:** DOCX blokovi 128–132, XML tabela 25, izvorna strana 14; `sec:2.3`, `tab:susedi-bcd`, `tab:susedi-2421`, `tab:susedi-excess`, `tab:susedi-graybcd`, `tab:susedi-gray`.

**Pre:** u 2.3a različiti biti ostali su neobeleženi; u 2.3b tabele su sadržale samo promenjenu reč i konačnu decimalnu vrednost. Posebno je nestao izvorni korak Grej → običan binarni zapis → decimalna vrednost. **Posle:** različite pozicije u sva tri para 2.3a ponovo su istaknute. Svaki sused u 2.3b ima broj promenjenog bita i obojen upravo taj bit; decimalne četvorke su vizuelno razdvojene. Za dozvoljene decimalne kodove prikazano je dekodovanje obe četvorke u cifre, a za nedozvoljene navedena konkretna nevažeća četvorka. Kod binarnog Grejovog koda vraćen je početni prelaz 23₁₀=10111₂→11100_G, kao i oba koraka za svih pet suseda, u jednom redu.

**Vrsta i razlog:** izgubljeni didaktički detalji pri konverziji. Dekodovanje obe decimalne cifre i numeracija promenjenog bita predstavljaju dodatna pojašnjenja, dok su binarni međuzapisi Grejovih suseda prisutni u izvorniku. Ranije ispravke pogrešnih/nedozvoljenih reči ostaju: sama početna reč 23 nije sused na rastojanju 1; odgovarajući Grej BCD sused je 0011 0000 → 20. Promene ne vraćaju tu grešku. „Na osnovu odeljku“ ispravljeno je u „Na osnovu odeljka“. Naslov rešenja ostaje uz uvod i prikazane korake.

**Provera:** ostaje svih 37 jedinstvenih jednobitnih suseda (četiri puta osam i pet binarnih Grejovih). Za svaki red provereni su bitni indeks, istaknuta pozicija, rastojanje 1, dozvoljenost i sve prikazane faze dekodovanja. Pet binarnih prelaza, u redosledu tabele, glasi 01100_G→01000₂=8, 10100_G→11000₂=24, 11000_G→10000₂=16, 11110_G→10100₂=20, 11101_G→10110₂=22. Vodeća nula u prvom binarnom rezultatu čuva zadatu širinu pet bita. Privremene promene binarnog međukoraka i izostavljanje oznake promenjenog bita pravilno obaraju proveru.

**Ponovna potvrda 05-A15/A16:** lokalna izgradnja, 256.757 računskih/logičkih provera i strukturna provera prolaze. Vizuelno su pregledane fizičke stranice 2 i 12–17 na 130 dpi (sadržaj i stranice čiji se prelom promenio); preostalih deset identično je prethodno potvrđenom PDF-u na 110 dpi. Dokument ostaje na 17 stranica. [Zapis provere prikaza](code/provera_prikaza.json) sadrži otiske izvora, poređenje stranica i četiri provereno otkrivene namerne greške. Ovo je redovna izgradnja ove dopune; istorijska čista izgradnja nije predstavljena kao provera nove verzije.

### 05-A17 — razmak između postupka i objašnjenja u tabelama 15–18

**Mesto:** `tab:zbir-1`–`tab:zbir-4`, DOCX blok 121. **Pre:** razmak u definiciji kolona pripadao je poslednjoj računskoj koloni, pa su crte sabiranja dopirale do objašnjenja. **Posle:** posebna prazna kolona širine 8 mm razdvaja račun od teksta; crte ostaju u računskom delu. **Vrsta:** poboljšanje čitljivosti po zahtevu korisnika. Svi bitovi, prenosi, korekcije i brojevi ostaju isti. Parser je prilagođen praznoj razdelnoj koloni. Lokalna izgradnja, 256.757 provera i strukturna provera prolaze. Konačne fizičke stranice 12 i 13 pregledane su na 130 dpi; ostalih 15 stranica identično je prethodnom PDF-u na 110 dpi.
