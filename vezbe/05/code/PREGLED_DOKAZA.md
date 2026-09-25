# Stručni pregled vežbe 05 — 25. 9. 2026.

Pročitani su svi teorijski pasusi, šest zadataka sa svim pottačkama i rešenjima, 12 numerisanih jednačina, nenumerisani izrazi, 24 sadržinske tabele (27 tabularnih delova zbog četiri koraka Grejove konstrukcije) i četiri slike. Nema dodatnih zadataka za samostalan rad u telu izvornog DOCX-a. `pregled_izvora.json` vezuje ručno pregledane opšte formule i crteže za SHA-256; `audit_math.py` čita stvarne podatke iz teksta i geometrije.

## Kodne tabele, Grejov kod i zadatak 1

BCD8421: težinski zbir svake reči jednak je njenoj cifri; 10 od 16 reči je dozvoljeno. Za BCD2421 izabran je samokomplementaran skup: za 0–4 isti zapis, za 5–9 binarna vrednost d+6. Težine 2,4,2,1 sabiraju se u 9, pa komplement reči cifre d ima vrednost 9−d. Nije svaki izbor reči sa tim težinama samokomplementaran: izbor konkretne tabele je bitan. Svih pet obojenih parova i crvena osa između 4 i 5 provereni su u izvoru i PDF-u.

„Više 3“ koduje d+3; komplement 15−(d+3) jednak je (9−d)+3. Netеžinskost sada dokazuje protivrečan sistem za prve četiri cifre, čak i ako se dopuste negativne realne težine. Isto važi za oba Grejova koda u dokumentu na bar dva bita: reči 00,01,11,10 traže istovremeno w₀=1, w₁=1 i w₁=3. Jednobitni degenerisani Grejov kod može imati težinu 1; tekst govori o višebitnim kodovima iz zadatka.

Refleksija Gₙ=0Gₙ₋₁,1rev(Gₙ₋₁) čuva unutrašnja jednobitna susedstva, a preko sredine menja samo novi MSB. Prva i poslednja reč takođe se razlikuju samo u MSB-u. Rekurzivna inverzija gᵢ=bᵢ₊₁ XOR bᵢ daje bᵢ=bᵢ₊₁ XOR gᵢ. Dve opšte formule pregledane su algebraički, a svi nizovi širina 1–10 provereni u oba smera. Iz tabele su pročitane sve 2+4+8+16 reči, smerovi strelica, redosled i ose refleksije. Donji biti se reflektuju, ne komplementiraju. Decimalna varijanta ima 1000 za 9 i zatvara ciklus sa 0; to nije reč 1101 standardnog binarnog koda za 9. Grejov kod ne sprečava proizvoljan hazard mreže: važi samo jednobitno susedstvo pod navedenim prelazom.

Svih pet kodovanja i tri dekodovanja provereno je po ćelijama stvarnih tabela, uz nezavisne rezultate u `rezultati.json`. Za nepotpune decimalne četvorke nužna je pretpostavka o izostavljenim spoljnim nulama; dopisivanje nula nije opšte svojstvo svih kodova. Naročito 0000 nije nula koda „više 3“. Za razlomljeni binarni Grejov zapis izričito je usvojeno skaliranje celog niza, a ne odvojeno kodovanje delova. Na primer, 101001.100101 se dekodira kao 110001.000110, odnosno 49+6/64=49.09375; druge tačne vrednosti su 226+89/128 i 13+14/64. Ova konvencija ne proizlazi sama iz naziva Grejov kod. Nedozvoljene četvorke se odbijaju, umesto računanja njihove prividne težinske vrednosti.

## BCD sabiranje i zadatak 2

Za cifre a,b i prenos c, puni zbir t je 0–19. Ako t≤9, cifra je t i prenos 0. Inače t+6=16+(t−10), pa niža četiri bita daju decimalnu cifru t−10 i viši bit prenos 1. Uslov je izlazni binarni prenos ILI niži rezultat >9; sam prenos nastao u drugom sabiranju ne bi bio dovoljan za t≥16. Iscrpno je provereno svih 200 slučajeva. Četiri objavljena sabiranja sada imaju 44 pisana računska reda kroz 11 decimalnih pozicija (05-A15); iz stvarnog teksta čitaju se svi bitovi operanada, prazne pozicije, prenosi, petobitni zbir, korekcija i prepisani niži deo. Rezultati 47,121,1218,961 i njihove BCD reči ponovo se izvode i porede sa prikazanim jednačinama.

## Hamingovo rastojanje, parnost i zadaci 3–5

Rastojanje je broj promenjenih koordinata reči iste dužine. Najkraći put po ivicama kocke mora promeniti svaku različitu koordinatu bar jednom; menjajući svaku jednom postiže se ta donja granica. Kod kocki se iz stvarnih ivica proverava ne samo broj 1,4,12 nego i njihov jedinstveni kompletan skup, svih 2,4,8 temena i svako rastojanje najkraćeg puta. Vidljive oznake temena su ručno povezane sa koordinatama. Kanal menja 000 u 001 na bitu 0; obe reči su u punom Grejovom kodu, pa on tu ne detektuje grešku.

Minimalno rastojanje poredi različite dozvoljene reči. Svih 14 navedenih rastojanja BCD reči, uvodni par i tri para zadatka provereni su brojanjem različitih bita. Sve četiri decimalne liste od po osam suseda broja 23 i pet binarnih Grejovih suseda proverene su po stvarnim ćelijama; svaki dozvoljeni sused se dekodira, svaki nedozvoljeni odbija. Sada je izričita širina osam/pet bita, jer bi veća širina dala dodatne susede.

Dokaz granica: detekcija samo članstvom uspeva za manje od d promena. Kugle poluprečnika t oko dozvoljenih reči moraju biti disjunktne, što je ekvivalentno d≥2t+1. Za istovremeno ispravljanje do c i odbijanje grešaka težina c+1 do u, uz u≥c, kugla c oko druge reči ne sme seći kuglu u oko poslate: d≥c+u+1. Nužnost se dobija izborom tačke na najkraćem putu između para na rastojanju d. „Detekcija do u“ u tekstu uključuje i pravilno prepoznate/ispravljene greške do c. Za d=4 režimi su (c,u)=(0,3),(1,2); za d=5 (0,4),(1,3),(2,2). Nema garancije istovremene dodatne detekcije tri greške u poslednjem režimu.

Parnost XOR-uje sve bite; promena k bita menja parnost tačno za neparno k. Zato oba paritetna koda, za fiksnu nepraznu poruku, imaju d=2, otkrivaju sve neparne a nijednu parnu promenu i nemaju opštu korekciju. Svih osam uvodnih i četiri zadate poruke ponovo je provereno iz stvarnih tabela.

## Hamingove konstrukcije i zadatak 6

Broj sindroma 2ʳ mora pokriti n različitih jednobitnih grešaka i odsustvo greške, pa 2ʳ≥n+1=m+r+1. Jednakost daje pun kod, stroga nejednakost skraćeni. Ovo su r kontrolnih bita osnovnog koda, bez dodatne opšte parnosti. Matrica provere ima nenulte, različite binarne kolone sa indeksima pozicija. Kolone 1,2,4,… su jedinični vektori, pa imaju rang r; ima tačno 2ⁿ⁻ʳ poruka. Zato r=5 dopušta 31−5=26 informacionih bita. Nije potrebno nabrajati svih 2²⁶ poruka da bi se dokazao ovaj kapacitet.

Sve pozicije 15–1, binarni indeksi, kontrolne i informacione oznake u četiri prikaza pročitani su iz LaTeX-a. Četiri grupe tačno odgovaraju nenultim bitovima indeksa; kontrolni bit se pri kodovanju bira prema ostalim bitovima grupe, a pri proveri uključuje u XOR. Za konstrukciju (15,11) iscrpno je pregledano svih 2048 poruka i sve pojedinačne i dvobitne greške. Dve različite kolone daju nenulti XOR, ali i indeks treće kolone: sindrom stoga sam ne razlikuje dvostruku od pojedinačne greške. Trojka indeksa 1,2,3 ima nulti XOR, pa d osnovnog punog koda jeste 3, ne više.

Za (7,4) provereno je svih 16 poruka i svih 128 maski greške; za prošireni (8,4) svih 16 poruka i svih 256 maski. Opšta parnost razlikuje pojedinačnu (neparna) i dvobitnu (parna, nenulti stari sindrom) grešku. Nulti stari sindrom sa neparnom opštom parnošću pokazuje grešku baš dodatnog bita. Trostruke greške mogu biti pogrešno ispravljene iako su otkrive u režimu samo detekcije. Minimalna rastojanja 3 i 4 proverena su svim parovima različitih kodnih reči.

U zadatku 6 stvarne XOR grupe daju s₁=1,s₂=0,s₄=1, indeks 5. 1011100 XOR 0010000 = 1001100; nova provera daje nulu. Kodna reč ima tri jedinice, zato je dopunski bit 1: 10011001. U obe Venove slike numerički je provereno da oznaka pozicije p leži tačno u krugovima kontrola čiji bit indeks p sadrži. Crveni krug obuhvata samo d₅; d₇ eliminiše ispravna kontrola c₂. Sam opšti bit ne renumeriše stare pozicije.

## Primarni izvor i granice pregleda

[R. W. Hamming, Error Detecting and Error Correcting Codes (1950)](https://ineffectivetheory.com/edu/papers/hamming-codes-1950.pdf): odeljak 3, štampane str. 150–153, konstrukcija i kontrolne pozicije; odeljak 4, str. 153–154, dodavanje opšte parnosti; odeljak 5, str. 154–156, geometrijska interpretacija i razmena korekcije za detekciju. Ponovo pročitan izvorni rad. Konkretni rezultati i dokazi iznad izvedeni su nezavisno; važe za zamene bita u reči fiksne dužine, ne za umetanje ili gubitak bita.

## Naknadno vraćeni detalji — 05-A08 do 05-A13

`tab:distances`: svih 14 parova ima obeležene tačno različite pozicije u obe reči. `tab:parity3`: obeležen je samo poslednji bit svake od 16 kodnih reči. `tab:raspored-provera` i `tab:grupe`: strelice pokazuju po sedam informacionih pozicija svake kontrole; zajedno sa polaznom kontrolom daju baš skup {i: i AND p ≠ 0}. Oznake d₃ u `fig:venn` podignute su bez promene pripadnosti krugovima.

`tab:kodiranje`: postavka i prvi red usklađeni su na 43 po zahtevu korisnika (izvorna postavka i tabela su se razlikovale). Običan zapis 101011₂ i njegov pomeraj 010101 daju XOR 111110; decimalni Grej BCD iz reči za cifre 4 i 3 daje 0110 0010. Preostali početni binarni zapisi su 000000, 001111, 110001, 111110, za 0, 15, 49, 62. Skripta parsira oba koraka svih pet redova i poredi ih sa postavkom i pravilom Grejove transformacije. Razlozi i precizna mesta pre/posle navedeni su u lokalnom izveštaju; ranija odluka 05-30 više ne opisuje aktuelni prvi red.

## Vraćeni pisani međukoraci — 05-A15/A16

U `tab:zbir-1`–`tab:zbir-4` svaki red računa čita se iz matematičkog niza, sa stvarnim pozicijama cifara. Za poziciju i nezavisno se računa t=aᵢ+bᵢ+cᵢ i k=6 ako t>9, inače 0. Sirovi zapis mora odgovarati t·16ⁱ+L, a korigovani (t+k)·16ⁱ+L, gde L sadrži već završene niže BCD cifre. Posebno se proveravaju pomerena 0110 korekcija, nenulti ulazni prenos na mestu 2⁴ⁱ, širine i konačni decimalni zbir. Time se proveravaju i poravnanje i svaki međurezultat, umesto samo konačnog odgovora.

U `tab:susedi-*` svaka reč poredi se sa stvarnim početnim kodom broja 23. Obojen i numerisan mora biti upravo promenjeni bit. Dozvoljene decimalne četvorke dekoduju se nezavisno prema odgovarajućoj kodnoj tabeli; za nedozvoljene se proverava navedeni konkretni razlog. Kod Grejovih suseda svaki običan binarni međuzapis proverava se kumulativnim XOR-om s leva nadesno, pa se tek onda proverava decimalna vrednost. Sva tri para rastojanja u 2.3a proveravaju se zajedno sa označenim pozicijama. Četiri negativne probe potvrđuju da provere zaista otkrivaju pogrešan međuzbir, pogrešnu korekciju, pogrešan binarni međuzapis i izgubljeno isticanje.
