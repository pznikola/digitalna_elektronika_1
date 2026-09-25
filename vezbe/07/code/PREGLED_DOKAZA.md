# Stručni i grafički pregled vežbe 07 — 25. 9. 2026.

Svih deset stranica originalnog PDF-a ponovo je pročitano i vizuelno poređeno sa LaTeX-om. Obuhvat: svih pet zadataka, sve pottačke i postojeća rešenja, 20 numerisanih jednačina, svi izrazi u tekstu, jedna sadržinska tabela i 14 ilustracija. `audit_math.py` sada proverava stvarne segmente, ćelije i nacrtane koordinate; `pregled_izvora.json` vezuje opšte formule i ručno praćene veze za otisak izvora. Naslovna tabela kontakata je pregledana kao element izgleda.

## Zadatak 1 — grafički odgovor i ograničenje izvornika

Rekurzija vₖ=f(vₖ₋₁) neposredno prati rednu vezu bez opterećenja koje bi menjalo karakteristiku. Za strogo opadajuću funkciju parna kompozicija f∘f je rastuća. Dvociklus zadovoljava f(VL)=VH i f(VH)=VL; fiksna tačka zadovoljava f(VS)=VS. Lokalni multiplikator parne iteracije je f′(VL)f′(VH), po pravilu izvoda kompozicije. Modul <1 daje privlačenje, >1 odbijanje; jednakost nije presuda o stabilnosti. Sam presek krive i odraza stoga nije dovoljan dokaz stabilnosti. Kod prikazanog S oblika spoljašnji preseci privlače, a srednji odbija. Pošto je 1.75 V ispod srednjeg preseka, parni izlazi teže niskom nivou, neparni visokom.

Original ne daje analitičku funkciju ni tačne koordinate potrebne za numerički VL. Kao u prethodnoj konverziji, odgovor ostaje nekoliko desetih volta uz grafičku preciznost. Numerički parametri Bézier crteža služe samo ponovljivom nacrtavanju. Nisu izmereni tehnološki parametri, niti dokaz tačnog numeričkog rezultata iz originala. Ova stavka je ograničena nedostajućim podacima; grafički zaključak je potvrđen.

Četiri crteža koriste iste četiri kontrolne tačke. Monotonost parametarske x komponente vidi se i analitički: za postojeće tačke x′(t)=0.375+55.5(t−0.5)²>0, pa je kriva jednoznačna. Numerička inverzija x(t) proverava svaku crvenu projekciju u četiri iteracije do prikazane preciznosti koordinata. Rotacije 0°,90°,180°,270° daju put (v₀,0),(v₀,v₁),(−v₂,v₁),(−v₂,−v₃),(v₄,−v₃),(v₄,0). Odraz u dijagonali zamenjuje x/y svake kontrolne tačke, a horizontalno-vertikalni put alternira između krive i odraza. Na poslednjoj slici zadržana su dva razlučiva koraka; tri kasnije strelice su imale iste početne/krajnje koordinate do pet decimala i samo su zaklanjale presek.

## Zadatak 2 — uslovi šuma

SSNM pretpostavlja da je prethodni deo lanca bez šuma već dostigao stabilan par. Jedan statički poremećaj ne sme prebaciti ulaz preko granice basena VS: VH−VN>VS za visok i VL+VN<VS za nizak nivo. Odatle granične amplitude VS−VL i VH−VS. Tačna jednakost može ostaviti tačku na nestabilnom pragu, pa za siguran oporavak važe stroge nejednakosti. Model ne daje toleranciju na trajanje impulsa niti dinamički odziv.

Za izabrane dozvoljene ulazne intervale monotono opadanje daje najviši niski izlaz f(VIH) i najniži visoki izlaz f(VIL). Uključivanje najnepovoljnijih znakova šuma daje f(VIH)+VN<VIL i f(VIL)−VN>VIH. To su dovoljni uslovi invarijantnosti intervala; svaki sledeći stepen ostaje u validnom intervalu indukcijom. Jedna nejednakost |f′|<1 opisuje samo lokalno slabljenje male perturbacije. Ne predstavlja sama po sebi univerzalni nužni i dovoljni uslov tolerancije konačnog šuma proizvoljne kaskade. Granice nagiba −1 su konvencionalne za S karakteristiku; kod loma nema izvoda u samoj tački, koriste se krajevi susednih segmenata.

Pretpostavlja se ulaz unutar domena zadate krive. Šum suprotnog znaka od najnepovoljnijeg mogao bi gurnuti idealnu šinu izvan opsega 0–5 V; ponašanje tamo nije zadato i nije neprimetno produženo pravom. Izlazni nivoi u odsustvu šuma nisu isto što i garantovane granice. Aproksimacije f(VIH)≈VL i f(VIL)≈VH opravdane su samo pri dovoljno ravnim krajnjim delovima.

Na ilustrativnoj slici nivoa proverene su koordinate (2,4),(3,1), obe projekcije, VS=2.5 i krajevi 0/5. Obe šeme imaju četiri invertora. Prati se svaki stvarni `.output`/`.input` priključak i svaki ulaz sabiračkog simbola Σ: jedan izvor −VN između prvog i drugog kola, odnosno −VN,+VN,−VN na sve tri međuveze. Nema premošćene sabiračke tačke ni obrnutog znaka šuma.

## Zadatak 3 — sve invertorske karakteristike

Nagibi izvedeni iz grafičkih krajeva: f₁ ima −2,−1/3,−2; f₂ ima −1; f₃ ima −1/2,−3,−1/2. Svaki segment, njegova dva kraja i kontinuitet porede se sa stvarno odštampanim izrazima. U oblasti [1,4] za f₁ važi f₁(x)−2.5=−(x−2.5)/3; [2,3] je invarijantan podinterval, pa x₀=2.7 zauvek ostaje na srednjem segmentu. Tačna rekurzija daje (−1/3)ᵏ(x₀−2.5), bez potenciranja napona. Izvan sredine, par koraka množi mali otklon od šine sa 4, dok ne uđe u srednji segment. Idealne šine 0↔5 su nestabilni izuzetak. Za f₂ parna kompozicija je identitet: 2.7,2.3,2.7,…, bez regeneracije.

Za f₃ odstupanje od sredine raste faktorom −3 do ulaska u spoljašnji segment. Zatim se udaljenost od odgovarajuće šine prepolovljava svakim stepenom. Od 2.7: v₁=1.9,v₂=4.05,v₃=0.475,…; parni podniz teži 5. Svi f₁/f₃ dvociklusi izvedeni su kompozicijom segmenata: koreni parne fiksne tačke su 0,2.5,5, sa multiplikatorima 4,1/9,4 za f₁ i 1/4,9,1/4 za f₃. Time se proverava i stabilnost, ne samo mnogo iteracija.

Za f₃, prag 2.5 i ulazne granice 2/3 daju VOL=1,VOH=4, obe garantovane margine 1 V i SSNM 2.5 V. Aproksimacija pomoću stabilnih šina daje 2 V i precenjuje marginu za 1 V. U odrazu su sve koordinate tačno zamenjene. U tri postavke vraćene su originalne pomoćne projekcije unutrašnjih preloma; krive nisu promenjene.

## Zadatak 4 — opšti afini segment i baferi

Indukcija rekurzije yₙ=kyₙ₋₁+C daje kⁿx₀+CΣⱼ₌₀ⁿ⁻¹kʲ. Geometrijski zbir za k≠1 daje C(kⁿ−1)/(k−1), odnosno y*+kⁿ(x₀−y*) za y*=C/(1−k). Konvergencija pri |k|<1 zahteva da se iteracija i dalje nalazi na tom segmentu. Ako je |k|>1 i x₀≠y*, otklon raste; za k<−1 i menja znak. Za k=−1 postoji dvociklus, za k=1 aritmetički niz x₀+nC, konstantan samo ako C=0. Fiksna početna tačka ostaje takva za svaki k, uključujući nestabilnu. Stvarni ograničeni segment napušta se pre matematičkog beskonačnog napona.

Svaka rastuća karakteristika bᵢ=5−fᵢ ima odgovarajuće pozitivne nagibe. Fiksne tačke b₁ i b₃ su 0,2.5,5; b₁ ima spoljašnje nagibe 2 i srednji 1/3, a b₃ spoljašnje 1/2 i srednji 3. b₂ je identitet. Zato za zadati x₀=2.7 granice glase 2.5,2.7,5. Dodato je da b₁ ostavlja tačne šine 0/5 na nestabilnim fiksnim tačkama; bez toga ranija rečenica „privlači tačke sredini“ bila je preširoka.

Za rastući b₃ izlazne granice računaju se na istim ulaznim krajevima: VOL=b₃(2)=1,VOH=b₃(3)=4. Garantovane margine su 1 V, SSNM 2.5 V, procena šinama 2 V. U šemi četiri ista bloka povezani su redno; y₁,y₂,y₃ označavaju međuveze, y₄ izlaz četvrtog bloka, a tri tačke nastavak lanca. Raniji natpis y₄,…,yₙ na jednoj vezi zamenjen je y₄ uz odvojenu oznaku nastavka.

## Zadatak 5 — kompozicija i domen margina

Kaskada je b₃(f₃(x)); redosled je bitan. Prelomi potiču od x=2,3 prvog kola i inverznih slika prelomnih ulaza 3,2 drugog kola: 10−3x=3,2, tj. x=7/3,8/3. Uz krajeve 0,5 dobija se šest tačaka tabele. Kompozicija izvedena nezavisnim deljenjem intervala daje nagibe −1/4,−3/2,−9,−3/2,−1/4 i konstante 5,15/2,25,5,5/4. Svi krajevi su neprekidni; T₄ je (3,1/2), ne (4,1/2). Uslov |nagib| prelazi 1 na 2 i pada ispod 1 na 3. Sve koordinatne putanje rotiranog drugog kola daju iste tačke kao tabela i konačna kriva.

Parna kompozicija h∘h ima fiksne tačke 0,2.5,5, multiplikatore 1/16,81,1/16. Dakle šine su stabilne i prag nestabilan. VOL=h(3)=1/2,VOH=h(2)=9/2 daju garantovane margine 3/2 V; SSNM je 5/2 V. Svi numerički izlazni nivoi/margine u jednačinama 3.5,4.3,5.2 čitaju se iz LaTeX-a i proveravaju zamenom u stvarne funkcije. Pri granici margine intervali se dodiruju; uz malo veću amplitudu izlazi izlaze iz garantovanih intervala.

Ove margine pripadaju celom novodobijenom kolu: unutrašnja veza f₃→b₃ je idealna, a izvori šuma su između kopija tog kola. Ako se šum doda i unutra, npr. b₃(f₃(x)+e₁)+e₂, izračunata margina 1.5 V nije automatska garancija za oba izvora. Pretpostavka je sada izričita; proizvoljno ponašanje internih šumova nije dodato postavci. Obnovljene pomoćne projekcije na konačnom grafiku služe očitavanju; bele podloge oznaka T₁–T₄ sprečavaju prolaz isprekidanih linija kroz tekst.

## Reference, izgled i ograničenja

Ponovo provereno u primarnom nastavnom izvoru [MIT 6.012, Lecture 11, slajdovi 4–7](https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-spring-2009/b96efcfa398f43f970ae4f36ac43456b_MIT6_012S09_lec11.pdf): konvencionalni pragovi nagiba −1, garantovani izlazi, margine i pojednostavljenje krajnjim naponima. Ostali dokazi iznad izvedeni su direktno iz zadatih funkcija. Modeli su statički; ne tvrde se kašnjenja niti stabilnost fizičkog povratno spregnutog kola iz same prostorne iteracije kaskade.

Svih 14 konačnih stranica pregledano je pojedinačno na 110 dpi, uključujući četiri strane sa većim samostalnim grafikonima. Tabele imaju diskretne razdelnike bez duplih linija uz istaknute granice. Jedina sadržinska tabela sada ima broj i oznaku. U zadatku 1 tačna numerička granica ostaje izričito ograničena nedostatkom analitičkih podataka; grafički postupak i kvalitativna granica su provereni.
