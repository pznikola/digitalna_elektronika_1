# Konverzija i provera vežbi 03, 04, 05, 07 i 08

Pripremljeno je pet samostalnih LaTeX dokumenata, sa PDF izdanjima, inventarima prenosa i pojedinačnim izveštajima. Obuhvaćena su sva 42 zadatka: 9 + 12 + 6 + 5 + 10. Preneta su postojeća rešenja; nerešenim zadacima za samostalni rad nisu dodata nova rešenja.

| Vežba | Dokument | Zadaci | Vektorski crteži | Provere | Izveštaj i inventar |
|---|---|---:|---:|---:|---|
| 03 — Brojni sistemi | [PDF](03/03_brojni_sistemi_i_predstave_binarnih_brojeva.pdf), [LaTeX](03/03_brojni_sistemi_i_predstave_binarnih_brojeva.tex) | 9 | 0 | 195 | [Ispravke](03/IZVESTAJ_ISPRAVKI.md), [inventar](03/INVENTAR.md) |
| 04 — Aritmetika | [PDF](04/04_aritmeticke_operacije.pdf), [LaTeX](04/04_aritmeticke_operacije.tex) | 12 | 8 | 6.992 | [Ispravke](04/IZVESTAJ_ISPRAVKI.md), [inventar](04/INVENTAR.md) |
| 05 — Kodovi | [PDF](05/05_kodovi.pdf), [LaTeX](05/05_kodovi.tex) | 6 | 4 | 1.854 | [Ispravke](05/IZVESTAJ_ISPRAVKI.md), [inventar](05/INVENTAR.md) |
| 07 — Statičke karakteristike | [PDF](07/07_staticke_karakteristike.pdf), [LaTeX](07/07_staticke_karakteristike.tex) | 5 | 14 | 1.879 | [Ispravke](07/IZVESTAJ_ISPRAVKI.md), [inventar](07/INVENTAR.md) |
| 08 — MOS kola | [PDF](08/08_mos.pdf), [LaTeX](08/08_mos.tex) | 10 | 20 | 275 | [Ispravke](08/IZVESTAJ_ISPRAVKI.md), [inventar](08/INVENTAR.md) |

Ukupno: 46 izmenjivih TikZ/Circuitikz crteža i njihovih vektorskih PDF izvoza, kao i 11.195 uspešnih računskih, simboličkih i logičkih provera. Broj provera predstavlja broj izvršenih kontrolnih tvrdnji, uključujući iscrpno nabrajanje ulaza i granične slučajeve; nije broj pronađenih grešaka.

## Prenos i izgled

DOCX sadržaj izdvojen je Pandoc-om i upoređen sa Word XML strukturom. Za PDF izvore pregledani su izdvojeni tekst i svaka izvorna stranica. Izgubljeni znaci pri ekstrakciji razlikovani su od stvarnih grešaka izvornika. U DOCX konverzijama svi sadržinski blokovi imaju komentar porekla; inventari povezuju odeljke, zadatke, formule, tabele i slike sa novim oznakama.

Izgled prati vežbe 01 i 02: A4, 11 pt, margine 2,5 cm, srpska latinica, Latin Modern, boje, naslovna strana sa dogovorenim autorima i kontaktima, automatski sadržaj i zaglavlje. Datum je `\today`. Jednačine i postojeće imenovane tabele/slike koriste LaTeX numeraciju i reference. Nenazvane računske tabele ostaju u okviru odgovarajućih rešenja. Word tabele koje su služile samo poravnanju formula zamenjene su matematičkim okruženjima.

Redovi podataka razdvojeni su diskretnim sivim linijama. Uz istaknute linije zaglavlja i završetka nema dodatne tanke linije. Artefakt „oprule“ uklonjen je: poticao je od pogrešno obrađene komande `\toprule`, čiji početak `\t` je pri konverziji protumačen kao tabulator. Komanda booktabs treba da iscrta gornju ivicu, a ne da se pojavi u tekstu.

## Dopune vežbe 05 prema naknadnim primedbama

- BCD2421 tabela ima crvenu horizontalnu osu između cifara 4 i 5 i jednako obojene komplementarne parove. Objašnjeno je pravilo `c(9−d) = komplement(c(d))`.
- Konstrukcija Grejovog koda prikazuje sva četiri koraka n=1,2,3,4. Odvojeni su novi MSB, donji biti, reflektovana polovina i smer čitanja. Donji biti se ponavljaju obrnutim redom; njihove vrednosti se ne komplementiraju. Novi MSB prelazi iz 0 u 1.
- Slika 2, geometrijska interpretacija Hamingovog rastojanja, ima sve ivice: 1, 4 i 12 za dimenzije 1, 2 i 3. Oznake temena i dimenzija razmaknute su od crteža.

Ovo su popravke vizuelnog prenosa. Ne predstavljaju greške izvorne teorije.

## Najvažnije stručne ispravke i granice podataka

- **03:** `13.375₁₀ = 1101.011₂`; ispravljene su i druge konverzije, periodični zapisi, komplementi, širine, opsezi i proširenja znaka. Racionalna aritmetika razdvaja tačan rezultat od odsecanja ili zaokruživanja.
- **04:** ispravljeni su uslovi prenosa i pozajmice, međukoraci i širine aritmetičkih zapisa, kao i veze u realizacijama funkcija. Za neparne osnove i nepotpuno zadatu širinu navedena je korišćena konvencija. Zadati iskazi koje student treba da oceni nisu neprimetno pretvoreni u tačne tvrdnje.
- **05:** proverene su kodne tabele, refleksija, rastojanja, parnost, sindromi i mogućnosti detekcije/korekcije. Hamingov (7,4) kod razlikovan je od proširenog (8,4) SECDED koda. Proverene su sve pojedinačne greške i relevantne dvobitne greške.
- **07:** ispravljeni su rekurentni izrazi, uslovi konvergencije, prelomne tačke kompozicije i zamene ulaznih pragova. Garantovane margine šuma razlikovane su od procena preko krajnjih napona. Za prvi, isključivo grafički zadatak nije izmišljen precizan fizički model ili tačan broj.
- **08:** provereni su znakovi i oblasti MOS modela, izbor fizički prihvatljivih korena, jedinice, odnosi geometrija, PDN/PUN, dimenzionisanje, domino i TG logika. Red `0101` u izvornoj tabeli 10.1 daje `Y=1`. Nedostajući `EC·L` u zadatku 1 i nezadati parametri zadatka 3 jasno su navedeni; rezultati zavise od označenih aproksimacija. Razlika između zadatog `EC·L` i vrednosti izvedene iz ostalih parametara u zadatku 2 obrađena je kroz oba tumačenja. Visoka impedansa se modeluje kao odsustvo aktivnog pogona, a ne kao Bulova vrednost.

Pojedinačni izveštaji daju izvorni zapis, ispravku, odgovarajuće novo mesto, obrazloženje i uticaj. Stručna pitanja o Hamingovim kodovima, marginama šuma i MOS/dinamičkim kolima proverena su u primarnim izvorima navedenim u tim izveštajima.

## Izgradnja i završna provera

```sh
make -C vezbe
make -C vezbe check
```

Izgradnja je proverena i u odvojenoj kopiji koja je na početku sadržala samo `.tex`, `.py`, `.json` i Makefile fajlove, bez pomoćnih fajlova i PDF-ova. Svih pet dokumenata i sve ilustracije uspešno se grade pomoću latexmk-a i pdfLaTeX-a. Konačni logovi nemaju greške, nedefinisane reference, duplirane oznake ili prekoračenja širine sadržaja. Pregledane su sve stranice novih PDF-ova; dodatno su pregledane šeme, tabele i crteži na kojima su menjani raspored ili oznake.

Izvorni DOCX/PDF dokumenti i postojeći rad u vežbama 01 i 02 sačuvani su. Zavisnosti i način pojedinačne izgradnje opisani su u [uputstvu](README_KONVERZIJA.md) i lokalnim README fajlovima.

## Predlozi za naredne izmene

Pri promenama brojnih primera ažurirati i odgovarajuće podatke za proveru, pa pokrenuti `make check`. Za buduću tehnološki konkretnu verziju MOS zadataka prvo dopuniti nedostajuće parametre; tek tada ima smisla dodati poređenje sa odgovarajućim SPICE modelom. Za grafički zadatak 07.1 može se zadati analitička karakteristika ili tabela tačaka ako se želi jednoznačan numerički odgovor.
