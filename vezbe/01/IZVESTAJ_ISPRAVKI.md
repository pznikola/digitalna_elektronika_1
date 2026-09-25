# Provera i ispravke — vežba 01

Polazno stanje sačuvano je u arhivi navedenoj u `../PROVERA/pocetno_stanje.json`.
Izvorni PDF `01_Kombinacione_Hazardi.pdf` nije menjan. Novi nalazi odnose se na polazni LaTeX, njegove crteže i kod. PDF stranice pre i posle izmene ne moraju imati iste brojeve; merodavne su navedene LaTeX oznake.

## 01-S01 — Uvod: priroda i uklanjanje statičkog hazarda

- **Pre:** hazard je „karakterističan za sekvencijalne mreže“, a praktično se „rešava korišćenjem metoda simulacije“.
- **Posle:** objašnjeni su hazard 1/0 u kombinacionoj mreži, različita kašnjenja rekonvergentnih putanja i razlika između detekcije simulacijom i uklanjanja promenom realizacije.
- **Zašto:** izabrana simulacija ne ispituje sve moguće odnose kašnjenja. Dvonivojski kriterijum zajedničkog pokrivanja susednih jedinica/nula važi uz promenu jednog ulaza. Ne daje garanciju za proizvoljne promene više ulaza.
- **Dokaz:** [MIT 6.004, 4.1, Glitches](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c4/c4s1/), [UMBC, Lab 7, Introduction i Discussion](https://userpages.cs.umbc.edu/phatak/212/labs-s21/Lab7-hazards/index.html). U kodu se iscrpno proveravaju susedni mintermi i oba smera svih promena jednog ulaza.
- **Uticaj:** objašnjenja zadataka 4–6 usklađena su sa uslovima navedene garancije.

## 01-S02 — Zadatak 1a, `eq:zad21_min_zp` i `eq:zad21_min_pz`: minimalnost i broj kola

- **Pre:** Karnoova karta navodno garantuje najmanji broj kola i njihovih ulaza; za ZP se navode „3 I i 2 ILI“ kola.
- **Posle:** razdvojeni su minimalno dvonivojsko pokrivanje i optimizacija proizvoljnog sklopa. ZP ima tri I i jedno ILI kolo, PZ tri ILI i jedno I kolo; oba traže još tri negacije ako nisu već dostupne.
- **Zašto:** tačno brojanje daje 4 glavna + 3 invertora = 7 kola. Faktorizacija, biblioteka kola i deljenje međurezultata menjaju optimizacioni problem. Prikazane NAND2/NOR2 transformacije ne predstavljaju dokaz globalnog minimuma.
- **Uticaj (konačna verzija):** sačuvan je izvorni razvod horizontalnih signala i njihovih komplemenata, sa vertikalnim vodovima ka kolima. Dva invertovanja po ulazu ostaju deo prikaza izvornog razvoda. Tekst sada jasno razdvaja minimalnu realizaciju (7 kola) od prikazane šeme ZP sa kompletnim razvodom (12 kola).
- **Provera:** sve jednakosti čitaju se iz LaTeX-a i proveravaju za 16 ulaza. Veze izvornih Draw.io šema ručno su praćene na uvećanim izvozima, a pregled je vezan za SHA-256 tačnog XML izvora u `code/pregled_sema.json`. Provera izvršava tu listu veza za svih 16 ulaza i odbija svaki promenjeni crtež bez novog pregleda.

## 01-S03 — Zadatak 1d, `fig:zadatak1-2-nili`: pogrešne veze

- **Pre:** srednje prvostepeno NILI kolo povezano je na B umesto negacije A; desno je povezano na C umesto negacije C. Crtež daje `(C+(A+D)(B+¬D))(B+C)`.
- **Posle:** srednje kolo prima negacije A i D, a desno B i negaciju C, saglasno `eq:zad21_pz_tran_5`.
- **Zašto:** za ABCD=0001 zadatak zahteva Y=1, a stari crtež daje Y=0. To je greška realizacije, dok je nameravana algebarska funkcija ispravna.
- **Uticaj:** popravljen je Draw.io izvor i regenerisan vektorski PDF; prolazi svih 16 kombinacija.

## 01-S04 — Zadatak 2, `fig:zadatak2-impl`: negacije i oznaka izlaza

- **Pre:** desno I kolo na crtežu prima A i B umesto njihovih negacija; izlaz i pojedine formule označeni su Y iako je zadat Z.
- **Posle:** treći proizvod je `¬A·¬B`, izlaz je Z, kao i oznake minimalnih formi.
- **Zašto:** na ulazu 1101 ne postoje susedne nule, ali stari proizvod AB daje jedinicu. Za 0011 stare veze daju nulu iako dve susedne nule postoje.
- **Uticaj:** tabela i već ispravni VHDL ostaju funkcionalno isti; crtež je usklađen sa njima. Zadržan je izvorni razvod, uz objašnjenje da njegovih osam invertora nije neophodno za minimalnu realizaciju sa četiri invertora.
- **Provera:** svih 16 reči provereno je prema uslovu da string ABCD sadrži `00`, uz odvojeno računanje nacrtane mreže.

## 01-S05 — Zadatak 3, `fig:zadatak3`: ulazni razvod

Izvorna šema sa horizontalnim parovima signala i vertikalnim vezama je vraćena. Osam ulaznih invertora služi potpunom prikazu razvoda i može se izostaviti kada se traži minimalna realizacija, jer ostatak kola koristi samo direktne ulaze. To je objašnjeno u tekstu; raspored, funkcije i oznake izlaza su sačuvani. Posebno, C3=(A0·B1)(A1·B0), C2=¬(A0·B0)(A1·B1), C1=(A0·B1) XOR (A1·B0), C0=A0·B0. Sve reči proverene su i preko VHDL-a.

## 01-S06 — Zadatak 1d: neuparene zagrade

U `eq:zad21_pz_tran_4` i `eq:zad21_pz_tran_5` izvorni zapis sadrži višak zatvorenih zagrada i nejasne granice komplementiranja. Prepisan je sa pravilno uparenim zagradama i istim nameravanim negacijama. Svaki korak proverava se za svih 16 ulaza. Za precizan tekst pre/posle videti `../PROVERA/nalazi_01.json`.

## 01-S07 — Zadaci 4–6: kriterijum hazarda i originalne strelice

- **Stručna dopuna:** kriterijum je odsustvo zajedničkog pokrivanja susednog para istom konturom. U ZP se ispituju susedne jedinice, a u PZ susedne nule, pri promeni jednog ulaza.
- **Grafički prikaz:** četiri slike (`fig:kmap-zad4`, `fig:kmap-5`, `fig:kmap-zad5`, `fig:kmap-zad6-marked`) vraćene su tačno na izvorni TikZ kod, uključujući boje, smerove i položaje strelica. Prvobitne strelice nisu bile stručna greška; njihova zamena tokom pregleda bila je nepotrebna i pogoršala je prikaz.
- **Provereni parovi:** zadatak 4: (14,15); zadatak 5 izvorna forma: (1,3),(4,6),(5,7),(6,7),(14,15); minimalna forma: (1,3),(4,6),(5,7). Konačne realizacije zadataka 4/5 pokrivaju sve susedne jedinice. Zadatak 6 PZ: (3,11),(4,5),(7,15),(12,14).
- **Dokaz:** nezavisno enumerisanje susednih ulaza sa Hamingovim rastojanjem 1. Oba smera i rubna susednost potvrđeni su na originalnom crtežu. Otisci četiri originalna bloka čuvaju se u `code/pregled_sema.json`, tako da se slučajna promena položaja strelica prijavljuje proverom.

## 01-D01 — Dopuna: VHDL kašnjenje

`after T` koristi podrazumevano inertno kašnjenje. To nije isto što i transportno kašnjenje: kraći impulsi mogu biti filtrirani. Kod nije neprimetno prebačen na drugi model. Provera u privremenoj kopiji zasebno izvršava oba modela.

U zadatku 4 pri 1111→1110, I1 raste i I3 opada nakon T, I4 raste nakon 2T, a Y ima lažnu nulu od 2T do 3T. Za obrnuti prelaz pri jednakim zadatim kašnjenjima nema impulsa. To ne znači odsustvo strukturnog hazarda za druge odnose kašnjenja. Proveren je i rubni slučaj impulsa trajanja tačno T.

Referenca: [HARDI Electronics, VHDL Handbook, štampana strana 37, Signal assignment](https://www.csee.umbc.edu/portal/help/VHDL/VHDL-Handbook.pdf).

## Jezičke i grafičke ispravke

Ispravljeni su slaganje reči, „formazbira“, „minimizaiciju“, „brinarni“, „Da bi smo“, ponovljeno „slike slike“, neujednačena oznaka Z i slične greške. Ručni brojevi slika 11,13,14,21 zamenjeni su LaTeX referencama. Uklonjena je dupla linija zaglavlja tabele množenja. Precizne stare/nove formulacije i polazne lokacije nalaze se u `nalazi_01.json`.

## Provera i ograničenja

`python3 code/provera.py` proverava stvarne formule, istinitosne tabele, svaku Karnoovu kartu i nacrtane grupe, šest izvornih Draw.io šema sa ispravljenim vezama i svih šest postojećih VHDL realizacija. Simulacije se izvršavaju u privremenim direktorijumima. GHDL odzivi sadrže unutrašnje signale; automatski se proveravaju konačne vrednosti, relevantni impulsi i izlaz bez hazarda.

Samostalni zadaci ostaju bez objavljenih rešenja; provereni su opseg i potrebna širina rezultata. Potvrda završnog vizuelnog pregleda i otisci izvora nalaze se u zajedničkom registru, a ne proizlaze iz samog prolaska testova.

## 01-F01 — Prelom kodnih blokova

Uklonjeni su dekorativni redovi komentara sa nizovima crtica u šest VHDL izvora; funkcionalni kod i objašnjavajući komentari ostali su sačuvani. Kod, njegov uvod i link ka testbenču drže se u jednom bloku; prethodne slike ispisuju se pre njega, pa više ne prekidaju kod između dve stranice. Završni samostalni zadaci počinju na novoj stranici, da se prvi zadatak ne prelomi neposredno pred kraj. Ponovljene duge napomene o istom modelu zamenjene su referencom. Time se sprečavaju usamljeni početni/završni redovi koda i stranica sa samo linkom. Komentar u zadatku 6 ispravljen je sa `I1 I2 I3 I4 I4 I6` na `I1 I2 I3 I4 I5 I6`; sama naredba je već bila tačna.

## 01-F02 — Povratak na izvorni način crtanja po zahtevu korisnika

Odbačena je nova realizacija pomoću odvojenih kola sa imenovanim mrežama. Vraćeno je svih šest izvornih šema rešenja zadataka 1–3, uključujući izvorne veličine u dokumentu. U četiri šeme Draw.io izvor je identičan polaznom; u dve su promenjeni samo pogrešni priključci, oznaka Z i uklonjeni sitni ostaci linija. Šeme u postavkama nisu menjane. Izvozi su regenerisani, a sve šeme ponovo pregledane uvećano. Ova dopuna zamenjuje ranije navode o novom rasporedu kola i prevezivanju strelica.

## Čista izgradnja — provera izvozâ

Izgradnja iz prazne kopije izvora našla je razliku samo na PDF stranici 16: dva stara Draw.io izvoza zadatka 4 imala su nešto drugačiju granicu obrezivanja. Izvorna šema postavke i izvorni vremenski dijagram nisu menjani, uključujući sve veze i strelice. PDF izvozi su obnovljeni iz istih `.drawio` fajlova, a stranica ponovo pregledana. Razlika je u obrezivanju izvoza, ne u načinu crtanja ili sadržaju postavke. Karnoove karte i njihovi originalni TikZ blokovi ostaju identični originalu.
