# Matematički i grafički pregled vežbe 04 — 25. 9. 2026.

Pregledani su svi teorijski pasusi, 12 zadataka i svaka pottačka, 35 numerisanih jednačina, nenumerisani izrazi, 22 sadržinske tabele i svih osam ilustracija (uključujući tri Karnoove karte). Četiri uvodne tabele su simbolički prikazi algoritama, 16 su tabele računskih postupaka, a dve funkcionalne. Naslovna tabela sa kontaktima ne računa se u njih. `pregled_izvora.json` sadrži otiske formula i crteža i zapis stvarno praćenih veza. Izmenjen izvor zahteva novi pregled, a ne automatsko potpisivanje.

## Uvod: sabiranje i oduzimanje

Za jednu cifru, euklidska podela xᵢ+yᵢ+cᵢ sa r daje ostatak sᵢ i prenos cᵢ₊₁. Najveći zbir je 2r−1, pa je prenos samo 0 ili 1, sa granicom ≥r. Za oduzimanje, dᵢ=(xᵢ−yᵢ−bᵢ) mod r i bᵢ₊₁ je 1 tačno kada je argument negativan. Množenjem sa rⁱ i sabiranjem svih kolona unutrašnje pozajmice se poništavaju: X−Y−b₀=Σdᵢrⁱ−bₙ₊₁rⁿ⁺¹. Zato dodatna kolona u opštoj tabeli oduzimanja nije neoznačena cifra dₙ₊₁, već koeficijent −bₙ₊₁. Za razlomke se tačke poravnaju i ceo račun skalira poslednjim mestom. Proverene su sve vrednosti jednocifrenih operacija za osnove 2,7,8,10,16 i oba ulazna prenosa/pozajmice.

ZA se računa nad znakom i apsolutnom vrednošću; kod jednakih apsolutnih vrednosti i suprotnih znakova bira se jedna od dve nule. Prekoračenje postoji ako apsolutna vrednost ne staje u svoje polje. Ne važi opšta tvrdnja |X|<|Y| ⇒ X−Y<0 za proizvoljno označene operande, npr. X=1, Y=−2.

KO zadržava ostatak modulo rᴺ. Za binarno sabiranje prelivanje nastaje samo kada jednaki znakovi daju suprotan znak. Posmatranjem sabiranja poslednje kolone dobija se XOR prenosa u bit znaka i iz njega. Kod oduzimanja kriterijum je (znakX XOR znakY) AND (znakRazlike XOR znakX). To ostaje ispravno i kada negacija najmanjeg KO broja nije predstavljiva. Protivprimer nekritičnom primenjivanju kriterijuma sabiranja posle negacije: 0−(−8)=8 na četiri bita preliva, iako međukod negacije −8 ponovo glasi 1000 i sabiranje 0000+1000 ima različite znakove. Stvarni inline izraz za OF proveren je za svih 256 četvorobitnih parova.

KMV radi modulo rᴺ−1, jer rᴺ≡1 po tom modulu: zato se izlazni prenos vraća na najniže mesto. Za razlomke to mesto ima težinu r⁻ᵏ. Dve nule imaju kodove 0 i rᴺ−1. Proširenje negativnog koda dodaje rᴺ−rⁿ i zato čuva njegovu vrednost; u dva reda sa ulazom 11 sada se čuva i negativni zapis nule, umesto prećutne normalizacije u 0000. Za neparne osnove korišćena je izričita konvencija iz napomene: KO razdvaja kodove na ⌈R/2⌉, KMV izostavlja samokomplementarni srednji kod. Ona je pretpostavka potrebna da izvorni primeri budu jednoznačni.

## Zadaci 2.1–2.4: svi prikazani postupci

`audit_math.py` iz stvarnog LaTeX reda čita oba operanda i osnovu, operaciju, proširene kodne reči, ceo vektor prenosa/pozajmice, niži rezultat, korekciju KMV, konačni rezultat i OF. Sve to mora odgovarati zapisu u `rezultati.json`, koji se zasebno proverava euklidskom podelom svake kolone i tačnim racionalnim dekodiranjem. Time sama prisutnost rezultata u tekstu više nije dovoljna. Obuhvat: 12 neoznačenih i 42 komplementne operacije. U ZA tabeli iz izvornog A,B,C,D računaju se svih osam izraza, pet objavljenih izlaza i svi postupci nad apsolutnim vrednostima; tri nepopunjena reda ostaju za samostalan rad. Njihove vrednosti staju u šest bita (−30,13,21).

Ponovo potvrđeni raniji nalazi uključuju 436₈−627₈=−171₈, uz trocifreni ostatak 607₈ i izlaznu pozajmicu 1, kao i različite KO/KMV izlaze 86FA/86F9 za 8135₁₆−FA3B₁₆. Kod razlomaka proveravaju se i tačka i širina, ne samo ceo niz cifara. Četvorocifreni OF u svakoj tabeli poredi se sa tačnim opsegom zadate predstave.

## Zadaci 2.5–2.6: množenje i deljenje

Distributivnost XY=ΣXyⱼ2ʲ opravdava i paralelno sabiranje svih parcijalnih proizvoda i uzastopno sabiranje sa međuzbirom. Za binarni KO najviši bit ima težinu −2ᴺ⁻¹, pa poslednji parcijalni proizvod ulazi sa suprotnim znakom. Pre pomeranja potrebno je proširenje znaka; 2N bita sigurno obuhvata proizvod dva N-bitna KO operanda. Za razlomke se konačna vrednost deli sa 2ᵏˣ⁺ᵏʸ. U svih šest tabela provereni su svaki yⱼ, težina, desetobitni parcijalni proizvod, međuzbir modulo 1024, širina konačnog izlaza i položaj tačke. Nema novog tumačenja označenih operanada kao neoznačenih.

Za deljenje, posle dopisivanja sledećeg bita deljenika privremeni ostatak je 2R+b; bit količnika je 1 ako je on ≥Y. Zatim se po potrebi oduzima Y, čime ponovo važi 0≤R<Y. Invarijanta obrađenog prefiksa jeste prefiks=YQ+R. Sva 26 prikazana koraka pročitana su iz tri tabele; provereni su i konačni identiteti, uključujući ostatke. Delilac je nenulti u sva tri primera.

## Zadaci 3.1–3.2, 3.5–3.6: privatna provera

Rešenja nisu dopisana u studentski tekst. Za 3.1 dobijaju se A=37, B=−572, C=1, dakle A>C>B; dodat je potreban dogovor da rezultat ima dovoljnu širinu (A ne staje u prvobitnih šest KMV bita). U 3.2a X je FF2.B0 u petocifrenom heksadecimalnom KO, a 520₉ u trocifrenom KO znači −306; šestocifreni ternarni KMV kod je neoznačeni broj 422 u osnovi 3. Nije srednji, izostavljeni kod.

Iskazi koje student treba da proceni ostali su namerno netačni. U 3.2b leva vrednost je −12, tačna desna −18 preliva petobitni ZA, a pri izričito dodatom dogovoru o zadržavanju znaka i četiri niža bita magnitude daje −2. Iskaz je netačan i pre tog odsecanja. Dogovor određuje ponašanje posle OF; takav rezultat nije tačna razlika. U 3.2c porede se −98 i 96, odnosno −54 i −21. Automatska provera čita njihove operande iz dokumenta.

Svih 42 dodatnih operacija na pet cifara ponovo se izvodi iz postavki 3.5/3.6. Originalne širine određuju vrednost ulaza; proširenje se radi pre negiranja i sabiranja. Provereni su kodovi, tačne racionalne vrednosti i OF; mašinski rezultati su u `../PROVERA/_build/homework04.json`. Nijedno novo studentsko rešenje nije dodato.

## Zadaci 3.3–3.4: povezivanje slika, tabela i formula

Komparator: viša polovina odlučuje osim pri jednakosti, zato G=G_H OR E_H G_L, E=E_H E_L, L=NOT(G OR E). Praćeni su priključci oba bloka i sva četiri logička kola na crtežu; njihov ručni model vezan za SHA proverava svih 256 ulaza. Prikazani NILI po zadatoj biblioteci ima realizaciju ILI+NI sa spojenim ulazima.

Maksimum: M=max(A,⌊C/2⌋) staje u četiri bita. Z=2B treba pet bita. Ako Z₄=1, sigurno je Z>M; inače odlučuje četvorobitni komparator Z₃:₀>M. ILI kolo za tu disjunkciju i oba podatkovna ulaza prvog MUX-a sada su stvarno nacrtani. Praćena mreža prolazi svih 4096 kombinacija A,B,C.

Sabirač: svih 16 redova tabele proverava S=A+B. Provereno je svih 48 stvarnih ćelija karata i 11 implicanata, uključujući spajanje isto obojenih rubnih oblasti s₀. Iscrpnim nabrajanjem svih 3⁴ kubova i pokrivanja jedinica potvrđena je minimalnost svake sume proizvoda: s₂ ima 3 proizvoda/8 literala, s₁ 6/20, s₀ 2/4. To nije tvrdnja o globalnoj minimalnosti višestrukog izlaznog kola. Svi izrazi SOP i XOR čitaju se iz formula; praćena šema sa tri XOR, tri I i jednim ILI daje isti zbir. Prenos sa najnižeg bita označen je c₁ da se ne pomeša sa ulaznim c₀.

Proizvod i konačna funkcija: dvobitni sabirač sa ulazom 01 daje S=A+1. Za B=0,1,2,3 treba birati S,2S,3S,4S. Četiri reda D₂ i svih pet njegovih bitnih formula daju 3(A+1); dodati invertori proizvode komplementarne bite pre njihove upotrebe na magistrali. S≤4, X≤16, pa treba pet bita. Šestobitni MUX bira 0X/X0, a maska NOT(E) isključuje svih šest izlaza pri A=B. Invertor E je sada nacrtan. Svih 16 ulaza praćene mreže daje zadatu komadnu funkciju, najviše 24; zato je krajnji najviši bit uvek nula. Širina šest unutrašnjih bita je dovoljna, bez tvrdnje da je minimalna.

## Izgled i opseg dokaza

Sačuvani su osnovni rasporedi osam crteža i potpuno neizmenjen izvor Karnoovih karata. Promenjene veze/oznake opisane su u izveštaju. Svi izvozi provereni su na konačnim stranicama; gušće šeme pregledane su i zasebno uvećane. Diskretne horizontalne linije razdvajaju redove; nema dodatnih tankih linija uz granice zaglavlja/završetka. Šesnaest računskih tabela dobilo je postojeće LaTeX brojeve kao vidljive naslove, oznake i naslov nastavka, umesto da prvi vidljivi naziv bude tek „Tabela 17“. Nazivi množenja više nisu odvojeni od postupaka. Konačni dokument ima 27 stranica; svih 27 pregledano je posle poslednjih izmena.


## Dopunski pregled pisanih postupaka i veza

Dopuna 04-A13–A16 zamenjuje prethodni tabelarni pregled množenja/deljenja izvornim pisanim računom. Vrednosti ostaju iste. `audit_math.py` direktno parsira svih dvanaest postupaka množenja (I/II za šest primera), poravnanje deset bitnih pozicija, pet parcijalnih proizvoda, početni zbir i svih pet međuzbirova. Svaki parcijalni proizvod nezavisno se računa iz X, stvarnog bita yⱼ i težine ±2ʲ. Bojeni biti EZ ponavljaju znak; crveni DK red ima negativnu težinu. Desetobitni međuzbirovi računaju se modulo 1024; 35 numerisanih formula nisu promenjene.

Za deljenje, umesto prethodnih 26 pojedinačnih dopisivanja od praznog početnog prefiksa, početna grupa ima širinu delioca, kao u originalnom DOCX-u. To daje 5+8+5=18 prikazanih oduzimanja, 18 ostataka i 4+7+4=15 dopisivanja sledećeg bita. Nijedna operacija sa grupisanim početnim ciframa nije izostavljena. Svaki umanjilac, međuostatak i dopisani bit provereni su iz stvarnih ćelija i njihovih težinskih kolona. Važi obrađeni prefiks = delilac × dosadašnji količnik + ostatak, 0≤ostatak<delilac. Devet konačnih jednačina ima iste rezultate i oznake.

U Sl. 5 stvarno nacrtani prenos sa levog I kola ulazi u gornje priključke desnih XOR/I kola, a izlaz levog XOR kola u oba donja. Most razlikuje ukrštanje od spoja; dve tačke označavaju grananja. Uslovi s₀=a₀ XOR b₀, s₁=(a₁ XOR b₁) XOR a₀b₀ i s₂=a₁b₁+(a₁ XOR b₁)a₀b₀ i dalje daju A+B za svih 16 ulaza. Karnoove karte zadržavaju iste ćelije i grupe, sa dodatom ispunom iza crnih oznaka.

Slika 7, dopuna 04-A17: D₁ se odvaja u (3,1.5) sa iste vertikale S, pa nema promene logičkog grafa. D₀=S, D₁=2S, D₂=3(A+1), D₃=4S i dalje iscrpno daju X=(A+1)(B+1). Svi segmenti spojnih vodova provereni su u izvoru i uvećanom izvozu kao horizontalni/vertikalni.
