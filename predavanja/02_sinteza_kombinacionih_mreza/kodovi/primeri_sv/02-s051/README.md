# 02-s051 — Simulacioni model statičkog hazarda

Primer prati [slajd](../../../slajdovi/s051_vremenski_dijagram_hazarda.tex) i [prikaz RTL koda](../../../slajdovi/s051_rtl01.tex).

- [mreza_sa_hazardom.sv](mreza_sa_hazardom.sv): simulacioni model sa kašnjenjem samo invertora.
- [tb_mreza_sa_hazardom.sv](tb_mreza_sa_hazardom.sv): automatske provere, uključujući lažnu nulu za T=5 ns i T=7 ns.
- [tb_mreza_sa_hazardom_bez_provere.sv](tb_mreza_sa_hazardom_bez_provere.sv): jednostavan niz pobuda i čekanja; menjajte ga za svoje eksperimente. Nema provera ni očekivanih rezultata.

Iz ovog direktorijuma:

```sh
make                           # automatski TB, Verilator
make run_iverilog               # automatski TB, Icarus
make run_student               # studentska pobuda, Verilator
make run_iverilog TOP=tb_mreza_sa_hazardom_bez_provere
make view_wave TOP=tb_mreza_sa_hazardom_bez_provere   # opcioni GTKWave
```

Prvenstveno se koristi lokalni Docker image `hdlview-tools:2025.12`. Kada Docker nije dostupan, runner koristi instalirane simulatore; `HDL_LOCAL=1` ih bira izričito. Nije potreban pristup mreži. Rezultati oba testbench-a i oba simulatora imaju zasebne direktorijume u `../../../build/redizajn/systemverilog/02-s051/`. Svaki VCD sadrži i međusignale.

U studentskom TB-u `T=5ns`: početno CBA=111, u 20 ns B pada na 0, a F ima lažnu nulu od 20 do 25 ns. Promenite T ili pobude i ponovite simulaciju. Naredba `assign #(T)` služi samo ovom simulacionom primeru; u realnom RTL projektovanju ne zadajemo kašnjenje gejta na ovaj način. Ostali gejtovi u modelu su idealno brzi, kao na originalnom slajdu.

