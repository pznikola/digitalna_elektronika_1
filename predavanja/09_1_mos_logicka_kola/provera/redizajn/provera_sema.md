# Pregled šema i topologije — 09_1

Datum: 2026-10-03. Pregledani originalni isečci, početni prikazi, uređivi izvori i novi prikazi. Linije su tamne, spojevi imaju pune tačke, prelazi bez spoja ostaju odvojeni. Debljina vodova je dosledna; oznake se ne smanjuju zajedno sa crtežom. Nastavna isticanja koriste lokalnu tamnocrvenu, uz tekst ili simbol.

| ID / izvori | Proverene veze i značenje |
|---|---|
| s002, šesnaest simbola | Sačuvane sve četiri konvencije i n/p, indukovani/ugrađeni kanal, D/G/S/B. Ovaj slajd podučava simbolima, pa različite konvencije nisu zamenjene jednim simbolom. |
| s003 | I_G prema gejtu, I_D od drejna, I_S prema sorsu; smerovi naponskih oznaka i plus oznake upoređeni sa originalom. |
| s009–s011 | PUN iznad izlaza, PDN ispod; sve tri simboličke realizacije po rednoj/paralelnoj mreži sačuvane. Zajednički gornji/donji čvorovi paralelnih grana imaju tačke. Gejtovi A/B ostaju nezavisni. De Morganove funkcije nisu promenjene. |
| s012 | R_L: VDD–VO; TD.D: VO; TD.S: masa; TD.G: VI. Izlazni krak sa tačkom na drejnu. Kratki vodovi, uredivi Razavi simbol. |
| s028 | Punjenje: RL između VDD i VO, CL između VO i mase. Pražnjenje: dodatni strujni izvor između VO i mase, usmeren naniže; prikazani iRC/iC i polaritet vo. Model i pravci poređeni sa originalom. |
| s030/s031 | TD.D i CL.gornji priključak na VO, oba donja priključka na masu, TD.G na VI. Radne tačke 1/2 i smer pražnjenja sačuvani. |
| s034 | pMOS.S: VDD, D: VO, G: VI; CL: VO–masa. Osa VSD i smer punjenja sačuvani. Izvorna sporna oznaka VGS uz krive ostaje za odluku P06. |
| s036–s039 | TL.D: VDD, TL.S i TD.D: VO, TD.S: masa; TL.G: VC, TD.G: VI. Izlaz ima čvornu tačku. Dva gejta se ne spajaju. Strelica nije vod kola. |
| s049–s051 | Ista redna grana kao prethodno, ali TL.G povezan sa TL.D i VDD. Veza gejta do napajanja obilazi simbol i ima tačku na napajanju. TD.G ostaje VI. |
| s056 levo | Sačuvan nastavni primer pogrešne pretpostavke nezavisnih osnova: svaki B vezan za sopstveni S, ukršten tamnocrveno kao u originalu. Ovo nije nova preporučena topologija. |
| s056 desno | Zajednička B oba tranzistora na masi; S opterećenja ostaje VO. Preskok preko izlaznog voda označava ukrštanje bez spoja; pune tačke označavaju stvarne B/B i izlazne spojeve. |

Ostale karakteristike s005/s008/s012/s015/s023/s030/s031/s034/s048/s055 su kvalitativni vektorski crteži: nisu proglašene merenjima. Ose, granične tačke, oblasti, smerovi i svi izvorni natpisi pregledani su. Strelice s015 i s023 pozicionirane su izvan teksta i pokazuju odgovarajuće tačke; s034 ima samo otvoreno pitanje o oznaci napona. Izvori ostaju u `slike/tikz/`, bez rasterizacije nastavnih šema.
