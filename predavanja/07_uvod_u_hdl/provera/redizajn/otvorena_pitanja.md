# Otvorena stručna pitanja — 07 Uvod u HDL

Status: **u_radu**, 2026-10-03. Sledeći predlozi **nisu primenjeni** na slajdove ni izvorne kodove. Početak 07 je odobren; stručne izmene nisu. Potrebno je izričito odobrenje po [PLAN_PREDAVANJA.md](../../../../PLAN_PREDAVANJA.md), odeljak 1.1 i korak 5. Beleške ne sadrže ove predloge ni zahteve za odobrenje.

## 1. s006 — klasifikacija komponenti i EEPROM

Izvorna zagrada „CPLD“ obuhvata i CPLD i FPGA. Predlog: razdvojiti CPLD i FPGA kao dve vrste programabilnih komponenti; ostaviti sve nazive, ostale grupe i postojeći broj slajdova. Intel ih [navodi odvojeno](https://www.intel.com/content/www/us/en/products/details/fpga/max.html).

Naziv „EEPROM — Electrically EPROM“ je skraćen i ne objašnjava sva slova. Predlog: „Electrically Erasable Programmable Read-Only Memory“, prema [Microchip dokumentaciji](https://developerhelp.microchip.com/xwiki/bin/view/products/mcu-mpu/8-bit-avr/structure/memory/). Dugačak naziv rasporediti u dva uredna reda. Slovna greška Fild→Field već je ispravljena kao jezička izmena.

**Odluka:** čeka se odobrenje razdvajanja grupa i punog naziva EEPROM.

## 2. s023 — nedostajuća zagrada u obrascu

U drugom redu PORT piše `SIGNAL]`, dok prvi ima `[SIGNAL]`. Predlog: dodati `[` radi doslednog označavanja opcionog dela. To je sintaksni obrazac sa metaoznakama, ne izvršiv program; ne treba ga „popraviti“ uklanjanjem ostalih metaoznaka.

[Tačan predlog obrasca](predlozi/s023_entity_architecture_obrazac.txt).

**Odluka:** čeka se odobrenje `SIGNAL]`→`[SIGNAL]`.

## 3. s027 — VHDL prioritetni enkoder

ABEL bira dva različita aktivna zahteva počevši od najmanjeg indeksa. Za R(0)=R(7)=1 očekuje se A=0, B=7 uz obe zastavice važenja. VHDL čita stare signalne AVALID/BVALID, pa posle svakog procesa zakazuje nove vrednosti; zastavice u listi osetljivosti ponovo pokreću proces. GHDL stvarno osciluje na 0 ns: A=7/B=0/AVALID=1/BVALID=0, zatim A=0/B=7/AVALID=0/BVALID=1. Simulacija nije stabilan prioritetni enkoder.

Predlog: proces osetljiv samo na R, lokalne promenljive `va` i `vb` sa trenutnom dodelom `:=`, izlazne zastavice dodeliti na kraju. Zadržati interfejs, prioritete i postojeći paket `std_logic_arith`; modernizacija paketa nije deo ovog predloga.

[Predloženi ceo kod](predlozi/s027_prioritet.vhd), [test svih 256 kombinacija](predlozi/s027_test_predloga.vhd), [stvarni izlaz GHDL-a](hdl_dokazi.txt). Predlog prolazi svih 256 kombinacija i zastavica; izvorni kod ostaje u prezentaciji do odluke.

**Odluka:** čeka se odobrenje zamene neispravnog VHDL primera proverenim predlogom.

## 4. s028 — BIT konstanta i smer porta B

U obe varijante stoji `A: in BIT:=1`; BIT zahteva `'1'`. Posle izolovane popravke tog literala GHDL prijavljuje drugi problem: dodelu portu B koji je deklarisan kao `in`.

Predlog za obe varijante: `A: in BIT:='1'` i `B: buffer BIT`, uz nepromenjene tri dodele, njihove redoslede i `after 10 ns`. B tada može da se dodeljuje i čita unutar arhitekture. Početne/konačne vrednosti i ideja nezavisnosti od redosleda ostaju iste; beleške razlikuju delta cikluse i fizičkih 10 ns, bez tvrdnje da se Y i Z menjaju istovremeno.

[Prva varijanta](predlozi/s028_dataflow_a.vhd), [druga varijanta](predlozi/s028_dataflow_b.vhd); obe prolaze GHDL analizu. [Dokaz oba izvorna problema](hdl_dokazi.txt).

**Odluka:** čeka se odobrenje oba literala i oba smera B.

## 5. s030 — značenje „dodela vrednosti na kraju“

Formulacija je preširoka: lokalna promenljiva menja vrednost odmah; signalna dodela zakazuje ažuriranje. Sekvencijalnost se odnosi na naredbe jednog procesa, a odvojeni procesi su konkurentni. Vidi [HDLWorks Process](https://hdlworks.com/hdl_corner/vhdl_ref/VHDLContents/Process.htm) i [SignalAssignment](https://www.hdlworks.com/hdl_corner/vhdl_ref/VHDLContents/SignalAssignment.htm).

Predlog teksta na slajdu: „Behavioral model — sekvencijalne naredbe unutar procesa; signalna dodela zakazuje ažuriranje — PROCESS.“ Obrazac ostaje ceo. Beleške već objašnjavaju promеnljivu/signal i alternative lista osetljivosti/WAIT, kao proverljivu nastavnu dopunu.

**Odluka:** čeka se odobrenje preciznije stručne formulacije na slajdu.

## 6. s031 — BIT literali i treći proces

Drugi i treći zapis imaju `Sel = 1` umesto `Sel = '1'`. U oba predloga dodati apostrofe; prvi zapis ostaje nepromenjen.

Treći zapis dodatno nema dodelu kada Sel nije 1. On zadržava prethodno f i ne bira x1, pa predstavlja latch, ne isti kombinacioni MUX kao prva dva. To potvrđuje [Intel-ova dokumentacija o nedostajućim dodelama](https://www.intel.com.tw/content/www/tw/zh/programmable/quartushelp/19.1/msgs/msgs/wvrfx2_l2_vhdl_id_in_comb_process_holds_value.htm).

**Preporuka:** sačuvati treći proces kao namerni primer nekompletnog opisa, uz kratku oznaku „Zadržava prethodno stanje“ i potpuno nastavno objašnjenje u njegovim beleškama. Sve tri realizacije ostaju na istom slajdu; ne tvrditi da su ekvivalentne.

Alternativa: dodati ELSE sa `f <= x1` i x1 u listu osetljivosti, pa sva tri postaju kombinacioni MUX.

[Drugi zapis sa literalom](predlozi/s031_mux_b.vhd), [treći sa literalom](predlozi/s031_mux_c.vhd), [alternativni potpuni MUX](predlozi/s031_mux_c_potpuni.vhd).

**Odluka:** odobriti apostrofe i izabrati „treći kao latch“ (preporuka) ili „treći kao potpuni MUX“.

## Sledeći korak

Po odluci primeniti samo odobrene predloge, uskladiti beleške pogođenih slajdova, obnoviti računske provere prema dokazanim očekivanjima, kompilirati i pregledati pogođene prikaze. Zatim ponoviti `notes`, `review` i `check LECTURE=07_uvod_u_hdl`. Tek kada sadržinski problemi budu rešeni, status može biti `ceka_odobrenje`. Prelazak na 08 nije odobren.
