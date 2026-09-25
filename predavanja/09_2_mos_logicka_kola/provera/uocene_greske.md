# Uočene greške i nedoslednosti originala

Svi navedeni zapisi ostaju verno preneti u prezentaciji. Predlozi ispod nisu uneti u nastavne slajdove. Brojevi označavaju izvorne slajdove; PDF strana je `(slajd+1)//2`, neparni su gore, parni dole. Tačne granice i identifikatori nalaze se u `mapa.json`.

| Slajd | Izvorni zapis / lokacija | Razlog sumnje i predlog |
|---|---|---|
| 4 | Jednačina 2, odnos `kn,D/kn,L` | Iz prethodne diferencirane jednačine sledi recipročan odnos `kn,L/kn,D`. |
| 4 | Završni `VO(IL)`, grana `1+sqrt(...)` | Ova grana izlazi iz pretpostavljene omske oblasti tranzistora TL i nema nagib −1. Fizičko rešenje prethodnog sistema ima `1−sqrt(...)`. Nezavisna provera potvrđuje kontraprimer. |
| 9, 17, 22, 27 | Indeks `VTn1` | Na tim mestima očekuje se prag N tranzistora (`VTn,D` u prvom kolu, odnosno `VTn`). Indeks 1 je zadržan. |
| 11 | „polarizacija osnova“ | Moguća jezička omaška; proveriti da li je nameravano „polarizacija osnove“. |
| 15 | Pozitivna konvencija PMOS: `VDS` u λ članu, `VGS` u uslovu, `VDSpsat`; završno `VSG+VTp+VSDsat/2` | Konvencije VDS/VSD i VGS/VSG nisu dosledne. Pri pozitivnom VSD i VSG linearni izraz ima `VSG+VTp−VSDsat/2`. Potrebna je zajednička revizija predznaka i oznaka, ne samo jedne promenljive. |
| 16 | „neoptrećeno“ | Predlog „neopterećeno“. |
| 17 | Prva zamenjena jednačina ima `kp`, a desna strana `kn/2`; diferenciranje | Faktor 1/2 nije dosledno prenet. Diferenciranje P struje po VI uz VO′=−1 daje pozitivan doprinos; prikazani predznaci zahtevaju reviziju. |
| 18 | `VIL=VTn+(VDD+VTp)(kp/kn)sqrt(kp/(kp+kn))` | Uz prikazani VO(IL), ravnoteža struja i nagib −1 zahtevaju `sqrt(kn/(kp+kn))`. Kontraprimeri za tri odnosa kp/kn su provereni. Ista greška ponovljena je u istaknutim izrazima. |
| 19 | Oznake T1/T2 i V0 | Nedosledno sa prethodnim P/N i VO. Zadržane su oznake originala. |
| 24 | Prvi imenilac modela zasićenja P tranzistora | Nedostaje član −VTp u izrazu prenapona, u odnosu na isti model u ostatku predavanja. |
| 26, 30, 32 | „Iz uslov“ | Predlog „Iz uslova“. |
| 32 | U tekstu N „u zasićenju“, a u istom koraku omski izraz i odgovarajući uslov ≤ | Predlog „u omskoj oblasti“ za taj korak. |
| 33 | VIL; mali član `(VO(IH)−VDD)/(Ln ECn)`; završni normalizovani član s VTn | Izvodi se VIH. N tranzistor ima VDS=VO(IH), bez oduzimanja VDD. Posle deljenja sa kp koeficijent uz VTn treba proveriti kao kn/kp, umesto kp/kn. |
| 35 | „neeopterećeno“; `VDS,N=VI=0` | Predlog „neopterećeno“ i `VDS,N=VO=0` u stanju visokog ulaza. |
| 36 | V0L | Cifra 0 je zadržana; očekivana oznaka je VOL. |
| 40, 42 | `Coxp=Coxp` | Tautologija u pretpostavci iste tehnologije; nameravano je `Coxp=Coxn`. |
| 43 | `abs(Lp ECp)` zamenjeno sa `Lp 2 vsatp/μp` bez apsolutne vrednosti | Prethodna konvencija daje negativan vsatp. Potrebna je apsolutna vrednost u srednjem članu jednakosti. Završni pozitivan odnos μn/μp odgovara apsolutnim vrednostima. |
| 44 | `EC=vsat/μ` u uslovima, dok slajd 42 daje `EC=2 vsat/μ` | Različita definicija kritičnog polja/faktor 2 između dva modela. Razlikovati parametre aproksimacija ili ujednačiti definiciju; izvor je prenet bez izmene. |
| 45 | Poslednji red `VDSnsat/abs(VDSpsat)=μn/μp` i tvrdnja o dugom kanalu | Za jednake dužine i jednake apsolutne brzine zasićenja leva strana daje **μp/μn**. Uslov dugog kanala izlazi iz pretpostavke prethodnog linearnog modela brzog zasićenja, pa se njime ne može opravdati prikazani prelaz. Nezavisni kontraprimer potvrđen. |
| 46 | „potreba“ | U navedenoj rečenici očekuje se „potrebna“. |
| 48 | „uveden je normirana“, „svi ostale“; oba λ indeksa n | Jezičke omaške i moguća ponovljena oznaka umesto λn/λp. Zaokruživanje 2.376×10 na 24 je provereno i nije greška. |
| 51 | „Uključenje tranzistor“; napon na RS1 obezbeđuje provođenje TN | Predlog „tranzistora“. U nacrtanom ekvivalentnom kolu napon baze TN prema emiteru nalazi se na RS2, dok je RS1 iznad tog čvora. Oznaku otpornika u objašnjenju treba proveriti. |
| 52 | „spojni svet“, „napona napon“ | Predlog „spoljni svet“ i uklanjanje ponovljene reči. |
| 53 | „jako malo“; `Istat ~ 10^-9 = 1 nA` | Predlog „jako mala“ i jedinica A uz 10^-9. Primer 10^9 tranzistora, ukupno 1 A i baterija 1 Ah za 1 h računski je ispravan u navedenoj idealizaciji. |
| 54 | „neidalnosti“ | Predlog „neidealnosti“. |
| 55 | Integrand `CL uCL(t)/dt` | Nedostaje diferencijal d u brojniku, tj. treba `CL duCL(t)/dt`. Završni energetski rezultati su računski ispravni. |
| 56 | TP definisano kao trajanje logičke jedinice na ulazu dok P radi | P tranzistor puni izlaz pri logičkoj nuli na ulazu. Predlog „trajanje logičke nule“ za TP. |
| 57 | Disipacija raste „sa trećim stepenom“ napajanja | To zahteva dodatnu aproksimaciju f∝VDD i stalno CL; nije opšta posledica samo izraza Pdyn=CL VDD² f. Izvorna tvrdnja je zadržana. |
| 58 | `VTn=VTp=VT` | Uz korišćeni negativni prag P tranzistora očekuje se `VTn=abs(VTp)=VT`, kao u sledećem koraku. |
| 59 | Prvi izraz za tSC, nezatvorena spoljašnja zagrada | Jedna zatvorena zagrada nedostaje u originalu; ista nepotpunost sačuvana je u novoj prezentaciji. Računski izraz sa pravilno zatvorenom zagradom daje prikazani rezultat. |
| 62 | λp bez apsolutne vrednosti i prelaz na tp∝VDD/(VDD−VTe) | Na slajdu 57 koristi se abs(λp). Pri poslednjem prelazu dodatno se zanemaruje korekcija modulacije dužine kanala. Minimum 3VTe/2 potvrđen je za tu pojednostavljenu funkciju. |

Istorijske tvrdnje i izvorne veze o tehnološkim procesima na slajdovima 46–48 prenete su kao deo originalnog materijala; nisu ažurirane niti predstavljaju proveru današnjih tehnoloških specifikacija.

`kodovi/provera_logike.py` sadrži 179 nezavisnih numeričkih provera: bilanse struja i nagib, naponske pragove, dimenzionisanje, energiju punjenja/pražnjenja, kratkospojne impulse, PDP/EDP i minimum EDP. Kontraprimeri grešaka originala su izričito odvojeni od provera ispravnih formula.
