# Dokazi za vežbu 03 — pregled 25. 9. 2026.

Ovo je zapis ručnog pregleda svih jednačina i teorijskog teksta. Otisci u `pregled_formula.json` vezuju zapis za konkretne formule. Skripta ne potvrđuje izmenjenu formulu automatski. Stare probe u `provera.py` ostaju regresioni primeri; `audit_math.py` dodatno čita računske izraze i redove tabela iz samog dokumenta.

<a id="p1"></a>

## P1 — Pozicioni zapis i konverzije (uvod 1.1)

Za r≥2 i 0≤dᵢ<r, definicija vrednosti je suma dᵢrⁱ. Izdvajanjem d₀ i faktora r dobija se Hornerov oblik za ceo deo. Celobrojno deljenje daje jedinstvene količnik i ostatak, pa ponavljanjem dobijamo cifre od najmanje ka najvećoj težini. Za razlomak, rF=d₋₁+ostatak daje cifre suprotnim redosledom. Za racionalni broj postoji konačno mnogo mogućih ostataka, pa postupak ili staje ili ulazi u period. Greška odsecanja posle K cifara manja je od r⁻ᴷ; jednakost konačnih suma zato zahteva konačne zapise u obe osnove. Grupisanje binarnih cifara sledi iz (2ᵏ)ⁱ=2ᵏⁱ. Dopunske nule smeju samo ispred celog i iza razlomljenog dela. Pročitani su i svi koraci oba algoritma.

<a id="p2"></a>

## P2 — Znak, komplementi i ofset (uvod 1.2)

ZA: za bit znaka s i preostalu neoznačenu vrednost a važi D=(−1)ˢa; 0≤a≤2ⁿ⁻¹−1. Dve nule slede iz a=0, s=0/1. KMV: M=rⁿ−1, pa M−D nema pozajmice i svaka cifra je r−1−dᵢ. Za parno r, polovina kodnih reči ima svaki znak: krajevi su ±(rⁿ/2−1), a 0 i M kodiraju dve nule. KO: kod je D mod rⁿ, dekodiranje U za U<rⁿ/2, inače U−rⁿ; krajevi −rⁿ/2 i rⁿ/2−1. Komplement cifara i jedinica daju (−D) mod rⁿ, uključujući nulu i najnegativniji broj. Na toj granici KMV nema istu predstavljivu vrednost: izmenjena formula više ne tvrdi da ima. Rekurencija prenosa je obična euklidska podela zbira r−1−dᵢ+cᵢ sa r. Za k razlomljenih mesta sve vrednosti i opsezi množe se r⁻ᵏ, uključujući korak dodavanja. Ofset: translacija U−B pomera oba kraja za B. Tvrdnje o opsezima izričito zahtevaju parnu osnovu; neparna osnova upućuje na konvenciju u vežbi 04 i ovde joj nije pripisan isti celobrojni opseg.

<a id="p3"></a>

## P3 — Konverzije zadatka 2.1

Svaki član proširenih suma i sve cifre pročitanih izlaza ponovo se računaju racionalnom aritmetikom. Oba postupka u tabelama proveravaju svaki međukorak i vezu sa narednim redom. Za 43/49, deljenje daje najkraći period od 21 bita 111000001010011100101: njihov celobrojni broj p zadovoljava p/(2²¹−1)=43/49. Sedam bita daje 137.875, a razlika je 1/392; za šest prikazanih decimala aproksimacije korišćena je tolerancija pola poslednjeg decimalnog mesta. Sve osnove i dozvoljene cifre su proverene.

<a id="p4"></a>

## P4 — Nepoznata osnova zadatka 2.2

Zapisi 51ᵣ, 144ᵣ, 12ᵣ znače 5r+1, r²+4r+4, r+2. Zamenom u 3x²−51ᵣx+144ᵣ dobija se 3(r+2)²−(5r+1)(r+2)+(r+2)²=−r²+5r+14=(7−r)(r+2). Jedina celobrojna osnova veća od cifre 5 je 7. Za nju je poznati koren x=9: 243−324+81=0. U LaTeX-u `{3x}^{2}` se vizuelno čita 3x²; koeficijent nije unutar napisanih zagrada, pa nije (3x)².

<a id="p5"></a>

## P5 — Predstave u zadacima 2.3–2.5

ZA na 7 bita ima opseg [−63,63]. Za svaku kodnu reč provereni su znak, broj bita i apsolutna vrednost; oba šestobitna ulaza u tački c proširuju se nulom unutar polja apsolutne vrednosti. Reč 1000000 je negativna nula, a 74 ne staje. Svaki opseg KMV/KO za r=10,16,8,2 dobijen je iz P2 sa n=4: KMV ±4999/32767/2047/7, KO donja granica za jedan manja. B2A4₁₆=45732, 7377₈=3839 i 1011₂=11 izlaze iz odgovarajućih opsega. Svaki prikazani celobrojni rezultat i svaki međukorak oduzimanja proverava skripta iz TeX-a. Kod nule KMV daje M, a KO 0. Za oktalni 24.70 sa dve razlomljene cifre korak je 1/64: M=63+63/64, KMV=53.07₈, KO=53.10₈. Skupovi i cifre graničnih zapisa posebno su upoređeni sa formulama P2.

<a id="p6"></a>

## P6 — Proširenje i negiranje, zadaci 2.6–2.7

Pravilo dopunjavanja sledi iz razlike kapaciteta rⁿ⁺ᵐ−rⁿ: negativnom kodu doda se ta razlika, pa se dekodirana vrednost ne menja ni za KO ni za KMV. Za pozitivan kod dopisuju se nule. To važi i za obe nule KMV. Ako se negira kodna reč, prvo se proširi. Izvorni zadatak 2.6 i njegovo rešenje koriste kodirane ulaze; to je sada izričito navedeno i pre rešenja. U KMV je 54₁₀ vrednost −45, pa je njen negativ +45, a ne −54. Provereni su svi ulazi: KO −45→9955, 14₈→0014, 1010₂ ostaje, 01₂→0001, 10₂→1110 (−2); KMV −54→0045, 36₈→0036, 1010₂ ostaje, 01₂→0001, 10₂→1110 (−1). Za osam bita opseg KO je [−128,127]; kodovi svih šest predstavljivih zadatih vrednosti odgovaraju ostatku modulo 256. +128 ne staje. Za svaki trobitni ulaz u zadatku 2.7b šestobitni izlaz dekodira se u suprotnu vrednost, uključujući dodatno proverenu granicu 100 (−4). Taj dodatni slučaj služi objašnjenju redosleda, bez dopisivanja rešenja nerešenih zadataka.

<a id="p7"></a>

## P7 — Samostalni zadaci (privatna provera, bez novih studentskih rešenja)

Za svih šest konverzija proverene su cifre, tačna racionalna vrednost, konačnost ciljnih zapisa i povratna konverzija. 202ₓ=20₅₀ znači 2x²+2=100: x=7, jer osnova mora biti pozitivna i veća od 2. Za poznati koren 3 u x²−12ᵣx+21ᵣ=0 sledi 9−3(r+2)+(2r+1)=4−r=0, dakle r=4, što dozvoljava sve upotrebljene cifre. Jednačina je (x−3)²=0: drugo rešenje jednako je prvom (dvostruki koren), pa zahtev nije kontradiktoran. Poslednji zbir je 2+7+14+23=46=114₆. Originalne namere zadataka i svi podzahtevi sačuvani su.
