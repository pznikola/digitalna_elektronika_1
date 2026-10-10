# 09_2 — stručna pitanja za odluku

Datum: 2026-10-03. Status svih predloga: **nije odobreno**. Korisnikov nalog odobrava obradu 09_2, ali ne stručne izmene originala. Prezentacija i beleške zadržavaju sporne izvorne zapise, bez vidljivih uredničkih komentara. Donji predlozi nisu nastavne beleške.

Može se odobriti svaki predlog zasebno, ili navesti odobrene oznake P01–P16. Odobrenje ispravki, prihvatanje prezentacije i početak 09_3 tri su odvojene odluke. Originalni PDF se ne menja. Za svaki navedeni sNNN, originalna PDF strana je `(NNN+1)//2`; neparni slajd je gornji, parni donji.

## P01 — s004 i s009: NMOS donji prag i održivost

Na s004 druga jednačina ima odnos `kn,D/kn,L`, ali prethodno diferenciranje daje **kn,L/kn,D**. Izlazni rezultat treba da koristi **1−sqrt(1/(1+kn,L/kn,D))**, umesto grane sa plusom. Ona sa plusom izlazi iz pretpostavljene omske oblasti opterećenja.

Predlog:

- `VI=VTn,D+(kn,L/kn,D)(−VTn,L−(VDD−VO))`.
- `VO(IL)=VDD+VTn,L[1−sqrt(1/(1+kn,L/kn,D))]`.
- Na s009 uslov za β ne predstavljati kao samostalnu garanciju `VO(IL)>VIH`: tu nejednakost proveriti posebno uz izabrano napajanje i važenje oblasti.

Dokaz: za `VDD=5, VTn,D=1, VTn,L=−1, kn,D=4, kn,L=1` fizički koren daje `VIL=1.223607`, `VO(IL)=4.894427`; plus-grana daje `3.105573` i preveliki napon na TL. Poseban kontraprimer zaključka s009: `VDD=2.4, VTn,D=1, VTn,L=−1, kn,D=kn,L=1`. Tada `β=1>1/3`, `VO(IL)=2.107107<VIH=2.154701`; oblasti u obe tačke su ispunjene. Provereno u računskim dokazima.

## P02 — s013, s015 i s044: PMOS konvencija i dva modela brzine

Na s015 pozitivni prag je definisan na s014 kao `VTp>0`. Zato završni linearni izraz treba da sadrži **VSGp−VTp−VSDpsat/2**, a ne `VSGp+VTp+VSDpsat/2`. U drugom punom izrazu modulacija treba da bude `λp VSDp`; u uslovu brzog zasićenja `VSGp−VTp`, a u granici `VSDpsat=Lp ECp`.

Na s013 brzina je najpre `μp ECp/2`, a potom u posebnoj aproksimaciji `μp ECp`; s042 i s044 analogno koriste različite definicije kritičnog polja. Predlog je **izričito razlikovati dva modela**, uz njihove sopstvene parametre: racionalni model sa `vsat=μEC/2` i segmentni linearni model sa `vsat=μEC`. Ne menjati faktor dva na jednom mestu i nastaviti da se isti EC tumači kao identičan parametar oba modela. Linearna aproksimacija mora imati svoj naveden uslov važenja.

Dokaz predznaka: zamena `VGS=−VSG`, `VT,neg=−VT,pos`, `VDSsat,neg=−VSDsat,pos` i `vsat,neg=−vsat,pos` u negativni linearni PMOS izraz daje upravo `W Cox |vsat|(VSG−VT,pos−VSDsat,pos/2)`. Definicije različitih brzinskih modela već su vidljive u izvoru; njihovo razlikovanje nije nova brojčana pretpostavka.

## P03 — dosledne oznake i indeksi

Predlog usklađivanja:

- s009: `VTn1→VTn,D`; s017/s022/s027: `VTn1→VTn`.
- s019: `T1/T2→N/P`, `V0→VO`; s038: `V0→VO`.
- s036: `V0L→VOL`.
- s040/s042: pretpostavka `Coxp=Coxp→Coxp=Coxn`.
- s048: geometrijsko λ razlikovati od **λn i λp**, umesto ponovljenog λn.

Ovo su stručne oznake, pa su izvorne verzije ostale do odluke, iako su očekivane zamene jasne iz priključaka i definicija.

## P04 — s017/s018: pseudo NMOS donji prag

Na s017 iz početne ravnoteže moraju se ukloniti faktori 1/2 sa **obe** strane. Sređeni bilans treba da bude

`kp[2(VO−VDD)(−VDD−VTp)−(VO−VDD)²]=kn(VI−VTn)²`.

Pri `VO′=−1` levi izvod je `2kp(VO+VTp)`, a ne njegova negativna vrednost. Zato druga jednačina glasi

`VI=VTn+(kp/kn)(VO+VTp)`.

Na s018 u **svim ponovljenim oblicima VIL** treba `sqrt(kn/(kp+kn))`, odnosno `sqrt(1/(1+kp/kn))`, umesto korena sa kp u brojiocu. Izraz za VO(IL) ostaje.

Dokaz: `VDD=5, VTn=1, VTp=−1, kn=4, kp=1` daje `VO(IL)=4.577709`, ispravno `VIL=1.894427` i obe struje 1.6 u istim normalizovanim jedinicama. Izvorni VIL je `1.447214`: N struja je 0.4, dok P ostaje 1.6.

## P05 — s024: imenilac P struje zasićenja

U prvom delu izraza u beleškama nedostaje `−VTp`: imenilac treba `1+(VGS,P−VTp)/(ECp Lp)`. Drugi deo iste jednakosti već sadrži odgovarajući član. Predlog: dopuniti prenapon u prvom imenitelju, bez drugih promena modela.

## P06 — s032/s033/s035: CMOS oblast i gornji prag

- s032: oznaku „N tranzistor u zasićenju“ promeniti u **„N tranzistor u omskoj oblasti“**. Isti slajd već koristi omski izraz i uslov `VO≤VI−VTn`.
- s033: `VIL→VIH`; mala veličina za N je **VO(IH)/(Ln ECn)**, bez `−VDD`. Poslednji normalizovani koeficijent uz VTn je **kn/kp**, ne kp/kn. Nenormalizovan oblik je već saglasan sa diferenciranjem.
- s035: `VDS,N=VI=0→VDS,N=VO=0`. Visok ulaz je upravo ono što uključuje N; nult je izlaz.

Dokaz normalizacije: deljenje celog brojioca i imenitelja sa kp. Za `kn=4, kp=1, VO=.2, VDD=5, VTn=1, VTp=−1` nenormalizovan zapis daje 1.92, a pogrešan normalizovan 1.17. Ispravljen normalizovan daje 1.92.

## P07 — s043/s045: odnos širina i domen aproksimacije

Na s043 u srednjem članu niza jednakosti zadržati apsolutnu vrednost: **Lp·2|vsatp|/μp**. Inače je taj član negativan, dok su početni i završni odnosi pozitivni.

Na s045 završni odnos `VDSnsat/|VDSpsat|` za jednake dužine i apsolutne brzine jednak je **μp/μn**, ne μn/μp. Međutim, važnije je da se linearni model izrazitog zasićenja ne može nastaviti u navedeni uslov dugačkog kanala. Predlog: sačuvati logičku celinu poređenja, navesti granicu važenja, a za dugačak kanal koristiti zasebno prethodno izvođenje `Wp/Wn=μn/μp`. Ne tvrditi da ono sledi iz tog nepravilnog prelaza.

Dokaz: `μn=2μp` i jednake apsolutne brzine daju `VDSnsat/|VDSpsat|=1/2`, dok izvorna desna strana daje 2.

## P08 — s047: naziv tehnološkog čvora i fizičke dimenzije

Predlog: predstaviti jednaku minimalnu širinu i dužinu kao **pretpostavku nastavnog primera normalizacije**, umesto opšte tvrdnje da naziv čvora garantuje oba fizička minimuma. Istorijska lista i sve izvorne veze ostaju.

Proizvođač razlikuje naziv procesa i fizičku dužinu gejta: [Intel, objava iz 2002](https://www.intel.com/pressroom/archive/releases/2002/20020813tech.htm) navodi proces 90 nm sa gejtom od 50 nm. To je protivprimer i pre datuma ovog predavanja; ne radi se samo o ažuriranju današnjih naziva.

## P09 — s049: naponski opseg zaštitnih dioda

Predlog: zadržati šemu, ali razjasniti da diode ograničavaju napon **uz svoj propusni pad**, a ne tačno na 0 i VDD. Granice i dozvoljena injektovana struja zavise od konkretnog kola; ne dodavati univerzalnu brojčanu garanciju.

[TI, Understanding and Interpreting Standard-Logic Data Sheets](https://www.ti.com/lit/an/szza036c/szza036c.pdf), odeljak o apsolutnim maksimumima, opisuje ulazne clamp diode i granicu VCC+0.5 V. [TI objašnjenje ESD zaštite](https://www.ti.com/document-viewer/lit/html/SSZTCN0/GUID-540DB5B6-45A1-40EF-A3C7-A07EB772C47F) opisuje provođenje prema VCC u propusnom smeru. To ne podržava tvrdnju o savršenom ograničavanju na naponske šine.

## P10 — s051: otpornik u baznoj povratnoj sprezi

Izvorni opis kaže da napon na RS1 održava provođenje TN. U obe izvorne šeme **RS2** je između baze TN i njegovog emitera/mase. Predlog: RS1 u tom delu nastavnog objašnjenja zameniti RS2, na slajdu i u potpunom opisu u beleškama. RS1 ostaje u topologiji; ne preimenovati otpornike da bi se tekst učinio tačnim.

## P11 — s053: jedinica struje

Predlog: `Istat≈10⁻⁹=1 nA→Istat≈10⁻⁹ A=1 nA`. Broj tranzistora, ukupno 1 A i baterijski primer ostaju. Iznos 1 nA po tranzistoru označiti kao pretpostavku primera; tvrdnju da su stvarne struje u svim savremenim sistemima znatno manje ne predstavljati bez konkretnih uslova tehnologije, temperature i radne tačke.

## P12 — s055: diferencijal u energetskom integralu

U beleškama je sačuvan izvorni `CL uCL(t)/dt`. Predlog: **CL duCL(t)/dt**. Veza `i=C du/dt` daje prikazanu promenu integracione promenljive. Konačni EVDD, ECL, EP i EN su tačni i ostaju.

## P13 — s056: trajanje rada P tranzistora

Predlog: TP je trajanje **logičke nule na ulazu**, kada P puni izlaz. TN je trajanje ulazne jedinice, kada N prazni izlaz. Energija ciklusa, učestanost i snaga ostaju.

## P14 — s056 (beleške), s057/s060: uslovi energetskih aproksimacija

Predlog:

- `Req∼1/VDD` označiti kao dodatnu aproksimaciju odgovarajućeg režima, ne kao sigurnu opštu relaciju iz prikazanog modela.
- Rast `Pdyn∼VDD³` vezati za pretpostavke **f∼VDD i stalno CL**; pri stalnoj učestanosti prikazani izraz daje kvadratni rast.
- U objašnjenjima s056/s057 izbeći opštu garanciju overklokovanja i apsolutnu tvrdnju da povećanje učestanosti nikad ne može uspeti bez većeg napajanja; zadržati temu i objasniti zavisnost od vremenske rezerve i konkretnih uslova rada.
- Na s060 dominaciju Pdyn vezati za aktivno prebacivanje i model u kojem se druga dva doprinosa zanemaruju pri PDP analizi. Na primer, pri f=0 je Pdyn=0, dok struja curenja može ostati nenulta.

Provere slede neposredno iz formula snage i otpornosti ovog predavanja; ne menjaju energetske rezultate PDP.

## P15 — s058/s059: pragovi i zatvaranje izraza

Predlog na s058: **VTn=|VTp|=VT**, uz negativnu P konvenciju ostatka izvođenja. Na s059 zatvoriti spoljašnju zagradu posle `VDD−(VTn+|VTp|)`. Rezultati tSC, ESC i PSC ostaju; faktor 0.8 saglasan je sa linearnom ivicom i definicijom 10–90%.

## P16 — s062: modulacija i optimum EDP

Predlog: u polaznoj otpornosti koristiti **|λp|**, kao na s057. Izričito navesti da se pri prelasku na `tp≈α CL VDD/(VDD−VTe)` zanemaruje faktor modulacije ili uzima konstantnim u izabranoj aproksimaciji; α je tada konstantan za optimizaciju.

Minimum `3VTe/2` je tačan za pojednostavljenu funkciju u domenu `VDD>VTe>0`. Treba dodatno proveriti da tako izabran napon zadovoljava pretpostavku brzog zasićenja i radne uslove kola; matematički minimum sam ne garantuje važenje polaznog modela. Predlog: dodati taj uslov uz rezultat, bez predstavljanja izračunatog napona kao univerzalnog optimuma stvarnog procesa.

## Dokazi i nastavak

Računski dokazi: [postojeća provera](../../kodovi/provera_logike.py) i [dopunska provera](../../kodovi/provera_redizajna.py). Pregledane su i formule koje nisu u tabeli: rezultati s005–s008, s020–s021, simetrični CMOS pragovi i margine, oba modela dimenzionisanja u njihovim domenima, baterijski račun, energije, kratkospojni impulsi i minimum pojednostavljene EDP funkcije.

Posle stvarne korisnikove odluke primeniti odobrene predloge na slajd i beleške istog ID-ja, ažurirati mapu pokrivenosti, pregledati sve pogođene prikaze i obnoviti potvrde. Ne prepisivati obrazloženja ovog dokumenta u nastavne beleške.
