# Uočene greške i nedoslednosti originala — MOS, 1. deo

Sve navedeno je **sačuvano u prezentaciji**. Predlozi nisu primenjeni na slajdove.
Broj slajda jednoznačno određuje izvor: PDF strana `(s+1)//2`, neparni gornji,
parni donji isečak. Računski protivprimeri koriste ilustrativne parametre,
a ne naknadno pripisane podatke originalu. Provere su u `../kodovi/provera_logike.py`.

| Slajd / lokacija | Originalni zapis | Razlog sumnje i predlog |
|---|---|---|
| 3, objašnjenje parametara | „redstavlja“, „sors“ | Slovna greška u „predstavlja“; terminologiju sorsa ujednačiti tek u zasebnoj redakciji. |
| 4, modifikovani izraz zasićenja | `VT` bez indeksa n | Okolni izrazi koriste `VTn`; ujednačiti indeks. |
| 12, prva oblast | „i tranzistor ne TD (D – drive) vodi“ | Nepravilan red reči; predlog: „i tranzistor TD … ne vodi“. |
| 13, tekst | „je važi“ | Suvišno „je“. |
| 14, granica zasićenja bez efekta kratkog kanala | `VI=VTn+sqrt(2VDD/(kn RL))` | Izjednačava struju sa VDD/RL, odnosno zanemaruje VO. Tačna granica dugog kanala koristi VO=VI−VTn: za x=VI−VTn važi kn RL x²/2+x−VDD=0. Za VDD=5, kn RL=1, VTn=1, izvor daje VI≈4.162, a granica je ≈3.317. Ako je namerna aproksimacija, navesti uslov i koristiti ≈. |
| 17, tekst | „u režimi“, ponovljeno „treba“ | Predlog „u režimu“ i uklanjanje ponavljanja tek u redakciji. |
| 19, tekst | „diferencirano“ | Predlog „diferenciramo“. |
| 20, pretpostavka | `VO < Ln ECn` | Za zanemarivanje odnosa potreban je znatno manji VO; znak < sam ne opravdava aproksimaciju. |
| 22, tekst | „odgovarajaću“ | Predlog „odgovarajuću“. |
| 27, prvi izraz za IOL | Dodatna zatvorena zagrada posle kvadratnog člana | Ukloniti suvišnu zagradu tek u ispravljenoj verziji. |
| 29, tvrdnja o celom procesu | Uslov zasićenja proverava VO=VOHmin/2 | To proverava interval do polovine izlaznog napona, relevantan za kašnjenje, ne nužno ceo pad do VOL. Precizirati opseg tvrdnje. |
| 31, tekst | „Ekvivalentu otpornost“ | Predlog „Ekvivalentnu otpornost“. |
| 33, decimalni zapisi | `5/6=0.833`, `7/9=0.777` | Konačni decimali su približni; koristiti ≈ (7/9 na tri decimale zaokružuje se na 0.778). Ponavljanje istog integrala ostaje sačuvano. |
| 34, pMOS grafikon i tekst | `VGS` uz pMOS krivu; „kada je nalazi“ | Okolna analiza koristi VSG; proveriti konvenciju. Predlog teksta „kada se nalazi“. |
| 38 i 50, opis kola | „neoptrećeno“ | Predlog „neopterećeno“. |
| 41, slučaj Δ=0 i kn,L=kn,D | Tvrdnja da nema rešenja za jednake parametre | Poslednja jednačina tada postaje identitet, pa tvrdnju treba ograničiti na odgovarajući slučaj Δ≠0. |
| 42, indeks praga | `VTn.L` | Tačka umesto zareza; sačuvana. |
| 43, opis prelaska u triodu | `T1` | Na šemi i u drugim izrazima koristi se TD. |
| 44, treći prikazani izraz | `kn,D(2VO−2VI+2VTn,D)` | Prethodni red daje `kn,D(4VO−2VI+2VTn,D)`. U sledećem VI izrazu koeficijent uz VO treba da bude 2. Greška se prenosi u dalje izvođenje. |
| 44, poslednji imenilac | `kn.D` | Tačka umesto zareza; sačuvana. |
| 45, oba konačna korena | Izrazi sa pozitivnom granom korena | Direktna zamena u početnu ravnotežu struja sa slajda 44 ne daje jednakost (provereno u skriptu). Ponoviti izvođenje sa ispravljenim izvodom i odabrati fizički dopustivu granu. |
| 46–47, drugi oblik VOL | `2VC−VDD−VTn,L` | Iz Δ=VC−VDD−VTn,L sledi `VDD+2Δ=2VC−VDD−2VTn,L`. Nedostaje faktor 2 uz VTn,L. |
| 48, tekst | „koje smo dobilo“ | Predlog „koje smo dobili“. |
| 49, tekst | `T2` | Na šemi tranzistor opterećenja nosi oznaku TL. |
| 51, uslov zasićenja | `VTn,D1` | Suvišna cifra 1 u indeksu. |
| 51, poslednja jednakost uz `????` | Isti koeficijent kn,L na obe strane | Zamenom izraza VI desna strana dobija kn,L²/kn,D. Jednakost nije identitet za proizvoljne parametre. Upitnici su sačuvani kao deo izvornika. |
| 52, tvrdnja da pojačanje nije −1 | `a=−sqrt(kn,D/kn,L)` | Postoji izuzetak kn,D=kn,L. Uslov kn,D>kn,L, naveden na kraju slajda, treba izričito povezati sa uvodnom tvrdnjom. |
| 53, prvi red diferenciranja | `VTn,L` na desnoj strani | Iz diferencirane struje TD sledi VTn,D. |
| 53, sledeći red i VI | `2VO` i zatim `+VO` | Ista izgubljena dvojka kao na slajdu 44: zbir treba 4VO, a VI treba +2VO. |
| 54, konačni koreni | Pozitivna grana korena | Ne zadovoljava polaznu ravnotežu sa slajda 53. Potrebno ponoviti izvođenje; nezavisna zamena u skriptu pokazuje neuspeh. |
| 55, imenilac približnog VOL | `VDD−VTn,D` | Prethodni red koristi VOH−VTn,D, a slajd 50 daje VOH=VDD−VTn,L. U imeniocu nedostaje −VTn,L. |
| 56, završni tekst | „tačku i VIH“, „sors – osnovna“ | Slovne/gramatičke nedoslednosti; predlog „tačku VIH“ i „sors–osnova“. |

Navedene stručne primedbe potiču iz algebre modela koji je već prikazan u
originalu. One ne predstavljaju zamenu modela novijim podacima ili dodatni
nastavni sadržaj. Provera prenosa i provera ispravnosti originala su odvojene.
