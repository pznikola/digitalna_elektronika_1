# Izveštaj redizajna — 10: Logička kola sa bipolarnim tranzistorima

Datum: **2026-10-03**. Status: **`u_radu`**. Izgled, beleške, pokrivenost i
pojedinačni pregled obrađeni su; pre konačne predaje potrebne su korisnikove
odluke o [19 grupa stručnih pitanja P01–P19](otvorena_pitanja.md).

## Obuhvat i očuvana struktura

Pročitan je [plan](../../../../PLAN_PREDAVANJA.md), svaki originalni slajd
sa 48 PDF strana, postojeći LaTeX i njegov sačuvani početni prikaz. Pregledani
su svi novi slajdovi i njihove A4 beleške. Obrađeno je samo predavanje 10.

Ostalo je **96 slajdova, u istom redosledu, sa ID-jevima `10-s001`–`10-s096`**.
Svaki okvir daje jednu prezentacionu stranu; nema brisanja, spajanja, deljenja
ili dodatnih overlay strana. Originalni PDF ostao je neizmenjen. Početni prikaz
sa izvorima sačuvan je pre redizajna u [arhivi](pocetni_prikaz.tar.gz).

Korišćena je zamrznuta tema `etf-v1`, stil B, LuaLaTeX i format 16:9. Tamnocrvena
`#A32638` koristi se za nastavna isticanja; nije proglašena zvaničnim ETF
standardom. Tema i zvanični ETF resursi nisu menjani. Sačuvani su autor
prof. dr Lazar Saranovac i izvorna školska godina 2021/22.

## Promene rasporeda i crteža

Uređeni su izvori svih 96 slajdova: jasnije grupe teksta, odvojeni naslovi
ilustracija, čitljivi rezultati i formule, preglednije tabele i razmaci.
Duga objašnjenja i deo međukoraka preneti su u beleške istog slajda;
ključni rezultati, uslovi, šeme, tabele i nastavne ilustracije ostaju vidljivi.

Doterano je **73 vektorska izvora** i **7 izvora tabela**. Analogni simboli
koriste kompaktan izgled po uzoru na Razavija, sa ujednačenim debljinama linija,
kraćim priključnim vodovima i odvojenim oznakama. Obuhvaćeni su modeli dioda i
BJT-a, RTL/DTL/TTL stepeni, totem-pole, testna opterećenja i ECL diferencijalni
par i baferi. Složene TTL/Schottky i ECL šeme zadržavaju proverene izvorne veze;
spojevi su označeni tačkama, a ukrštanja bez spoja ostaju odvojena. Logički
vodovi ne prelaze preko tela simbola. DIP pogledi su raspoređeni sa čitljivim
dimenzijama; ostali izvorni detalji dimenzija nalaze se u beleškama s075.

U završnom prolazu posebno su razdvojene oznake s009, oznake izlaznih bafera
s028, tačke grananja DTL/TTL kola, oznake napajanja i isprekidani okvir
s054/s055, natpisi/opterećenja i vremenski prikazi s079, zaglavlja s080,
napajanje ECL bafera s089 i vrednosti otpornika s093. Precrtavanje nije
iskorišćeno za prećutno menjanje izvornih stručnih tvrdnji ili topologije.

Reprezentativna poređenja (svaka veza prikazuje original, početni, novi slajd
 i beleške):

| ID | Rezultat |
|---|---|
| [s009](../../build/redizajn/pregled/index.html#10-s009) | Kompaktni kompenzovani razdelnik; odvojene oznake paralelnih elemenata |
| [s022](../../build/redizajn/pregled/index.html#10-s022) | Dva suprotna zahteva jasno poređena; potpuno obrazloženje u beleškama |
| [s043](../../build/redizajn/pregled/index.html#10-s043) | Pregledna DTL ulazna mreža i nedvosmisleni spojevi |
| [s055](../../build/redizajn/pregled/index.html#10-s055) | Poređenje otvorenog kolektora i totem-pole stepena |
| [s075](../../build/redizajn/pregled/index.html#10-s075) | Razdvojeni pogledi DIP14 kućišta; detaljne dimenzije u beleškama |
| [s079](../../build/redizajn/pregled/index.html#10-s079) | Tri odvojena testna kola; natpisi i vremenska merenja bez preklapanja |
| [s093](../../build/redizajn/pregled/index.html#10-s093) | Čitljiviji vodovi i vrednosti ECL otpornika; izvorni dupli T3 čeka odluku |

## Beleške i pokrivenost

Napisani su izvori `beleske/s001.tex`–`s096.tex` i A4 prateći PDF od **96 strana**,
sa prikazom slajda, njegovim ID-jem i naslovom. Naslovni s001 ima samo vezu sa
ID-jem, bez veštačkog popunjavanja. Ostale beleške sadrže smislen nastavni tekst:
fizički tok prelaza, potpune premeštene međukorake, definicije oznaka,
konture, tumačenja merenja, dimenzije kućišta i potrebna proverljiva objašnjenja.
U beleškama nema istorije redizajna, kontrolnih suma, odobrenja ili predloga ispravki.

[Inventar](inventar.json) ima **348 elemenata: 318 izvornih grupa i 30 dopuna**.
Svaki ima provereno odredište u [mapi pokrivenosti](pokrivenost.md); 105 grupa
povezano je sa beleškama. Poreklo prenetog objašnjenja i razlika od dopune
vode se u [evidenciji beležaka](evidencija_beleski.md), bez druge kopije nastavnog
teksta. Na s016 su posebno evidentirani znak pojačanja, definicija izvoda i
uslov velikog apsolutnog nagiba; sva tri ostaju vidljiva.

Potvrda odredišta znači da izvorni detalj nije izgubljen. **Ne potvrđuje stručnu
tačnost spornog izvornog zapisa**: odgovarajuće stručne kategorije ostale su
`problem` do korisnikove odluke.

## Jezičke ispravke i stručna pitanja

Jezička obrada čuva značenje. Na s002 izraz „spoljnih elementa“ prenet je u
beleške sa pravilnim „spoljnih elemenata“, a „diode vodi“ oblikovan je kao
„dioda vodi“ / „vodi“. Na s022 ispravljeno je „prethodno kola“ u „prethodnog
kola“ i gramatički sređeno obrazloženje kompromisa. Interpunkcija, razmaci,
sastavljanje rečenica i tipografski zapis uređeni su kroz predavanje.

Tokom rada ispravljene su sopstvene greške prenosa, uključujući vraćanje
izvornog minusa u `V_IH` na s059; to nije promena originalne formule.
Brojevima 10 i 100 u AC tabeli s096 nije pripisana neproverena jedinica.

Predlozi P01–P19 obuhvataju pogrešne nazive/indekse, znak pada na diodi,
nesklad logičke funkcije i simbola, uslove modela pri izlasku iz zasićenja,
trostatičku tabelu i ECL izraze za struje, smetnje i punjenje. Konkretan izvorni
zapis, problem i predloženi zahvat dati su u [otvorenim pitanjima](otvorena_pitanja.md).
**Nijedan stručni predlog nije odobren ni primenjen.** Radni nastavni PDF-ovi
zato još sadrže te izvorne nedoslednosti. Odluke se vode [odvojeno](odluke.md).

## Provere i pregledani otisci

`all`, `notes` i `review` uspešno grade aktuelne izlaze. Kompilacijski logovi
nemaju greške ili upozorenja o prelivanju. Postojeći model daje **1018 uspešnih
nezavisnih računskih provera**. Pojedinačni vizuelni pregled obuhvata svaki
originalni, početni i novi slajd, svaku šemu/formulu i A4 beleške.

`check` ostaje **`NEZAVRŠENO` u 26 stručnih kategorija na 20 ID-jeva**, zbog
P01–P19. Nema strukturnih grešaka, zastarelih potvrda, izgubljenih odredišta
ili nedostajućih resursa. [Rezultati provera](rezultati_provera.md) daju komande
 i potpuni spisak nalaza. Računski model nije dokaz tačnosti svake doslovno
prenete formule i ne uklanja potrebu za stručnim odlukama.

Pojedinačni otisci originala, početnog i novog prikaza, izvora slajda i beležaka
vezani su za stvarno korišćenu temu u [pregled.json](pregled.json).
[Izgradnja](izgradnja.json) beleži stvarne zavisnosti; promena izvora ili beležaka
poništava samo pogođene potvrde.

| Pregledani objekat | SHA-256 |
|---|---|
| Originalni PDF | `7740f5a6f67475059f7512c14d35e31ee4733bfa3bab3f74a7241cea832e14d7` |
| Manifest redizajna | `a5cd9bf34886fb905a4424e20b3a58d5974dad4c062565a41a61768214643194` |
| Arhiva početnog prikaza | `7f04f863d92b8ad9ee14c4f8cace8b074336a1c2403532fdb3dedef1b125643f` |
| Prezentacija | `3b0f07023bfa1870eff68e34c063e94552b347c24b0d75e362122e49339015fb` |
| A4 beleške | `bf8d9e4f3a3d6e714df65e14fb0834e003a0e037ca1d491bbf01bbbe95168785` |
| Manifest teme | `87c94849f57da28ea52dcacdc7badf90bdd16d3d6cf5d9925d195b24b4fddc41` |

## Isporuka i precizan nastavak

- [Prezentacioni PDF](../../build/10_logicka_kola_sa_bipolarnim_tranzistorima.pdf)
- [PDF beležaka](../../build/10_logicka_kola_sa_bipolarnim_tranzistorima_beleske.pdf)
- [Uporedni pregled](../../build/redizajn/pregled/index.html)
- [Predlozi za odluku P01–P19](otvorena_pitanja.md)

Naredni korak je korisnikova odluka o konkretnim stručnim predlozima.
Po odobrenju primeniti samo odobrene promene, pregledati pogođene slajdove i
beleške, obnoviti njihovu pokrivenost i potvrde i izvršiti `notes`, `review` i
`check` za 10. Tek kada su stručna pitanja razrešena i provere prolaze, predati
konačno izdanje i postaviti `ceka_odobrenje`. Agent ne daje odobrenje rezultata.
Ovo je poslednje predavanje u katalogu; ne započinjati samoinicijativno druga.

Ne ponavljati već pregledanu analizu nepogođenih ID-jeva ako su otisci isti.
Za pogođene formule, tabele, crteže i beleške nastaviti od konkretnog Pxx,
uz [centralnu evidenciju](../../../../STATUS_PREDAVANJA.md).

## Spisak doteranih vektorskih izvora i tabela

Broj 73 označava izmenjene vektorske fajlove: obuhvata potpuno precrtane modele
 i lokalne dorade vodova, oznaka, spojeva, strelica i tehničkih pogleda.

- [s004_dioda_impulsno_kolo.tex](../../slike/tikz/s004_dioda_impulsno_kolo.tex)
- [s004_oporavak_diode.tex](../../slike/tikz/s004_oporavak_diode.tex)
- [s005_naponi_npn.tex](../../slike/tikz/s005_naponi_npn.tex)
- [s008_impulsno_kolo.tex](../../slike/tikz/s008_impulsno_kolo.tex)
- [s008_prelazni_proces.tex](../../slike/tikz/s008_prelazni_proces.tex)
- [s009_kompenzovani_razdelnik.tex](../../slike/tikz/s009_kompenzovani_razdelnik.tex)
- [s010_nacin_crtanja.tex](../../slike/tikz/s010_nacin_crtanja.tex)
- [s010_pojacavac_sa_zajednickim_emitorom.tex](../../slike/tikz/s010_pojacavac_sa_zajednickim_emitorom.tex)
- [s011_karakteristika_prenosa_kolo.tex](../../slike/tikz/s011_karakteristika_prenosa_kolo.tex)
- [s016_nagib_i_zaobljenje.tex](../../slike/tikz/s016_nagib_i_zaobljenje.tex)
- [s021_strujni_kapacitet_kolo.tex](../../slike/tikz/s021_strujni_kapacitet_kolo.tex)
- [s028_rasterecenje_izlaza.tex](../../slike/tikz/s028_rasterecenje_izlaza.tex)
- [s028_rasterecenje_ulaza.tex](../../slike/tikz/s028_rasterecenje_ulaza.tex)
- [s033_integrisano_rtl_kolo.tex](../../slike/tikz/s033_integrisano_rtl_kolo.tex)
- [s034_dva_kolektorska_otpornika.tex](../../slike/tikz/s034_dva_kolektorska_otpornika.tex)
- [s034_spojeni_izlazi_invertora.tex](../../slike/tikz/s034_spojeni_izlazi_invertora.tex)
- [s034_viseulazno_rtl_kolo.tex](../../slike/tikz/s034_viseulazno_rtl_kolo.tex)
- [s034_zajednicki_kolektorski_otpornik.tex](../../slike/tikz/s034_zajednicki_kolektorski_otpornik.tex)
- [s035_dva_otvorena_kolektora.tex](../../slike/tikz/s035_dva_otvorena_kolektora.tex)
- [s035_otvoren_kolektor.tex](../../slike/tikz/s035_otvoren_kolektor.tex)
- [s035_slozena_funkcija_otvoreni_kolektori.tex](../../slike/tikz/s035_slozena_funkcija_otvoreni_kolektori.tex)
- [s037_oc_nacin_crtanja.tex](../../slike/tikz/s037_oc_nacin_crtanja.tex)
- [s039_diodna_ili_funkcija.tex](../../slike/tikz/s039_diodna_ili_funkcija.tex)
- [s043_dtl_sa_negativnim_napajanjem.tex](../../slike/tikz/s043_dtl_sa_negativnim_napajanjem.tex)
- [s044_neispravno_uklanjanje_negativnog_napajanja.tex](../../slike/tikz/s044_neispravno_uklanjanje_negativnog_napajanja.tex)
- [s045_dtl_invertor_sa_diodama.tex](../../slike/tikz/s045_dtl_invertor_sa_diodama.tex)
- [s045_dtl_viseulazno_sa_diodama.tex](../../slike/tikz/s045_dtl_viseulazno_sa_diodama.tex)
- [s046_dtl_invertor.tex](../../slike/tikz/s046_dtl_invertor.tex)
- [s046_karakteristika_dtl_i_granice.tex](../../slike/tikz/s046_karakteristika_dtl_i_granice.tex)
- [s049_dtl_ekvivalent_praznjenja.tex](../../slike/tikz/s049_dtl_ekvivalent_praznjenja.tex)
- [s049_dtl_sa_izlaznom_kapacitivnoscu.tex](../../slike/tikz/s049_dtl_sa_izlaznom_kapacitivnoscu.tex)
- [s049_dtl_ulazni_i_izlazni_odziv.tex](../../slike/tikz/s049_dtl_ulazni_i_izlazni_odziv.tex)
- [s049_ulazni_prelazi.tex](../../slike/tikz/s049_ulazni_prelazi.tex)
- [s050_ttl_bez_diode.tex](../../slike/tikz/s050_ttl_bez_diode.tex)
- [s050_ttl_sa_diodom.tex](../../slike/tikz/s050_ttl_sa_diodom.tex)
- [s050_zamena_dioda_tranzistorom.tex](../../slike/tikz/s050_zamena_dioda_tranzistorom.tex)
- [s053_dva_ulazna_tranzistora.tex](../../slike/tikz/s053_dva_ulazna_tranzistora.tex)
- [s053_tranzistor_sa_vise_emitera.tex](../../slike/tikz/s053_tranzistor_sa_vise_emitera.tex)
- [s054_standardno_ttl_otvoreni_kolektor.tex](../../slike/tikz/s054_standardno_ttl_otvoreni_kolektor.tex)
- [s055_standardno_ttl_otvoreni_kolektor.tex](../../slike/tikz/s055_standardno_ttl_otvoreni_kolektor.tex)
- [s055_standardno_ttl_totem_pole.tex](../../slike/tikz/s055_standardno_ttl_totem_pole.tex)
- [s056_standardno_ttl_kolo.tex](../../slike/tikz/s056_standardno_ttl_kolo.tex)
- [s057_standardno_ttl_karakteristika.tex](../../slike/tikz/s057_standardno_ttl_karakteristika.tex)
- [s063_aktivni_ekvivalent_punjenja.tex](../../slike/tikz/s063_aktivni_ekvivalent_punjenja.tex)
- [s064_zasiceni_ekvivalent_punjenja.tex](../../slike/tikz/s064_zasiceni_ekvivalent_punjenja.tex)
- [s066_ttl_sa_izlaznom_kapacitivnoscu.tex](../../slike/tikz/s066_ttl_sa_izlaznom_kapacitivnoscu.tex)
- [s066_ttl_vremenski_odziv_rezimi.tex](../../slike/tikz/s066_ttl_vremenski_odziv_rezimi.tex)
- [s067_low_power_ttl.tex](../../slike/tikz/s067_low_power_ttl.tex)
- [s068_high_power_ttl_darlington.tex](../../slike/tikz/s068_high_power_ttl_darlington.tex)
- [s069_high_power_ttl.tex](../../slike/tikz/s069_high_power_ttl.tex)
- [s069_schottky_ttl.tex](../../slike/tikz/s069_schottky_ttl.tex)
- [s070_schottky_spoj.tex](../../slike/tikz/s070_schottky_spoj.tex)
- [s070_schottky_tranzistor_struje.tex](../../slike/tikz/s070_schottky_tranzistor_struje.tex)
- [s071_schottky_ttl_sa_aktivnim_praznjenjem.tex](../../slike/tikz/s071_schottky_ttl_sa_aktivnim_praznjenjem.tex)
- [s072_low_power_schottky_ttl.tex](../../slike/tikz/s072_low_power_schottky_ttl.tex)
- [s075_dip14_pogledi.tex](../../slike/tikz/s075_dip14_pogledi.tex)
- [s076_dva_spojena_totem_pole_izlaza.tex](../../slike/tikz/s076_dva_spojena_totem_pole_izlaza.tex)
- [s077_centralna_kontrola.tex](../../slike/tikz/s077_centralna_kontrola.tex)
- [s077_dozvola_rada.tex](../../slike/tikz/s077_dozvola_rada.tex)
- [s077_otvoreni_kolektori.tex](../../slike/tikz/s077_otvoreni_kolektori.tex)
- [s077_zajednicki_prijemnik.tex](../../slike/tikz/s077_zajednicki_prijemnik.tex)
- [s078_nor_sa_dozvolom.tex](../../slike/tikz/s078_nor_sa_dozvolom.tex)
- [s078_s_ttl_trostaticki_izlaz.tex](../../slike/tikz/s078_s_ttl_trostaticki_izlaz.tex)
- [s078_simboli_trostatickih_kola.tex](../../slike/tikz/s078_simboli_trostatickih_kola.tex)
- [s079_testno_kolo_otvoreni_kolektor.tex](../../slike/tikz/s079_testno_kolo_otvoreni_kolektor.tex)
- [s079_testno_kolo_totem_pole.tex](../../slike/tikz/s079_testno_kolo_totem_pole.tex)
- [s079_testno_kolo_trostaticko.tex](../../slike/tikz/s079_testno_kolo_trostaticko.tex)
- [s080_ls126a_unutrasnja_sema.tex](../../slike/tikz/s080_ls126a_unutrasnja_sema.tex)
- [s082_ecl_diferencijalni_par.tex](../../slike/tikz/s082_ecl_diferencijalni_par.tex)
- [s089_ecl_bez_bafera.tex](../../slike/tikz/s089_ecl_bez_bafera.tex)
- [s089_ecl_izlazni_baferi.tex](../../slike/tikz/s089_ecl_izlazni_baferi.tex)
- [s090_ecl_odvojena_napajanja.tex](../../slike/tikz/s090_ecl_odvojena_napajanja.tex)
- [s093_standardno_dvoulazno_ecl_kolo.tex](../../slike/tikz/s093_standardno_dvoulazno_ecl_kolo.tex)

Izmenjene tabele:

- [s073_dozvoljeni_opsezi.tex](../../tabele/s073_dozvoljeni_opsezi.tex)
- [s074_dc_ac_karakteristike.tex](../../tabele/s074_dc_ac_karakteristike.tex)
- [s076_spajanje_izlaza.tex](../../tabele/s076_spajanje_izlaza.tex)
- [s080_kasnjenja_ls125a_ls126a.tex](../../tabele/s080_kasnjenja_ls125a_ls126a.tex)
- [s094_pecl_dc_karakteristike.tex](../../tabele/s094_pecl_dc_karakteristike.tex)
- [s095_necl_dc_karakteristike.tex](../../tabele/s095_necl_dc_karakteristike.tex)
- [s096_ac_karakteristike.tex](../../tabele/s096_ac_karakteristike.tex)
