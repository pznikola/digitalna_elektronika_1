# Uočene greške originala — 07

- Slajd 23, PDF strana 12, gornji: u drugom redu PORT obrasca piše `SIGNAL]`, bez otvarajuće `[` kao u prvom redu. Verovatno treba `[SIGNAL]`. Izvorni zapis je sačuvan; primer je sintaksni obrazac, ne kompletan program.

- Slajd 2: „Jedačinama“, „jedna vid“, „sa njia“, „orjentisano“, „konkuretno“. Predlozi: „Jednačinama“, „jedan vid“, „sa njima“, „orijentisano“, „konkurentno“. Svi izvorni oblici ostaju.
- Slajd 6: „Fild Programmable Gate Array“; predlog „Field“. Zagrada označena CPLD obuhvata i FPGA, što meša različite vrste programabilnih komponenti. Zagrada i njena oznaka su sačuvane.
- Slajd 9: „doveli su to toga“; predlog „do toga“.
- Slajdovi 14 i 28: „Konkuretno“ / „Konkuretni“; predlog „Konkurentno“ / „Konkurentni“.
- Slajd 19: „Gatevai Design Automation“; sumnjiv izvorni zapis imena; nije prepravljan. Istorijske tvrdnje iz ovog pasusa prenete su kao sadržaj originala, bez ažuriranja današnjim stanjem.
- Slajd 27: VHDL prevod nije ekvivalentan ABEL prioritetnom koderu. Signalne dodele zastavicama postaju vidljive tek posle procesa, a zastavice su i u sensitivity listi. Za R="10000001" stvarna GHDL simulacija na 0 ns ponavlja A=111, B=000, AVALID=1, BVALID=0 i A=000, B=111, AVALID=0, BVALID=1. ABEL bira A=0, B=7. Predlog za ispravljeno izdanje: lokalne promenljive za trenutno pretraživanje i signalne dodele izlazima na kraju procesa, uz proveru prioriteta. Originalni kod nije promenjen sem razmaka i preloma. Reprodukcija nalaza: `kodovi/s027_test_izvorne_greske.vhd`.
- Slajd 28: port A tipa BIT inicijalizovan je brojem `1` umesto literalom `'1'`; port B je deklarisan `in`, a arhitektura mu dodeljuje vrednost. Primer je verno prenet u obe varijante, pa nije označen kao izvršiv ispravan VHDL program.
- Slajd 31: druga i treća varijanta koriste `Sel = 1`, a prva `Sel = '0'`. Ako je Sel bit/logički tip kao u prvoj varijanti, treba `'1'`. Treći proces nema dodelu u svim granama i zadržava prethodno f kada uslov nije ispunjen; moguće da je namera da se pokaže razlika u odnosu na kombinacioni multiplekser. Nisu dodate dopunske dodele ili objašnjenja u slajd.

## Provera ponašanja izvornog primera sa slajda 27

Lokalno korišćen GHDL 6.0.0-dev (5.1.1.r569.g9f219f49f.dirty), LLVM 14.0.0.
Za analizu potrebna je opcija `--std=08 --ieee=synopsys`, zbog izvornog paketa
`std_logic_arith`. Simulacija je zaustavljena sa `--stop-delta=12`.
Test je pomoćni dokaz izvorne greške; GHDL nije obavezna zavisnost izgradnje slajdova.
