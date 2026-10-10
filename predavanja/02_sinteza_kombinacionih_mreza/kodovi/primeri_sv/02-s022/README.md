# 02-s022 — RTL: mreža ILI–I

Primer prati [slajd](../../../slajdovi/s022_mreza_ili_i.tex) i [prikaz RTL koda](../../../slajdovi/s022_rtl01.tex).

- [mreza_pz.sv](mreza_pz.sv): mreža sa istim gejtovima i ulaznim invertorima kao na šemi.
- [tb_mreza_pz.sv](tb_mreza_pz.sv): automatske provere, svih osam binarnih kombinacija.
- [tb_mreza_pz_bez_provere.sv](tb_mreza_pz_bez_provere.sv): jednostavan niz pobuda i čekanja; menjajte ga za svoje eksperimente. Nema provera ni očekivanih rezultata.

Iz ovog direktorijuma:

```sh
make                           # automatski TB, Verilator
make run_iverilog               # automatski TB, Icarus
make run_student               # studentska pobuda, Verilator
make run_iverilog TOP=tb_mreza_pz_bez_provere
make view_wave TOP=tb_mreza_pz_bez_provere   # opcioni GTKWave
```

Prvenstveno se koristi lokalni Docker image `hdlview-tools:2025.12`. Kada Docker nije dostupan, runner koristi instalirane simulatore; `HDL_LOCAL=1` ih bira izričito. Nije potreban pristup mreži. Rezultati oba testbench-a i oba simulatora imaju zasebne direktorijume u `../../../build/redizajn/systemverilog/02-s022/`. Svaki VCD sadrži i međusignale.

Ulazi se čitaju redom CBA. Funkcija daje F=1 za 011, 101 i 110. Sufiksi _n i _p predstavljaju komplementni i pravi izlaz para invertora. Kašnjenja gejtova nisu modelovana.
