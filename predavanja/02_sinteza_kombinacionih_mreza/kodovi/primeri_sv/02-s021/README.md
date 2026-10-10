# 02-s021 — RTL: mreža I–ILI

Primer prati [slajd](../../../slajdovi/s021_rasterecenje_ulaza.tex) i [prikaz RTL koda](../../../slajdovi/s021_rtl01.tex).

- [mreza_zp.sv](mreza_zp.sv): mreža sa istim gejtovima i ulaznim invertorima kao na šemi.
- [tb_mreza_zp.sv](tb_mreza_zp.sv): automatske provere, svih osam binarnih kombinacija.
- [tb_mreza_zp_bez_provere.sv](tb_mreza_zp_bez_provere.sv): jednostavan niz pobuda i čekanja; menjajte ga za svoje eksperimente. Nema provera ni očekivanih rezultata.

Iz ovog direktorijuma:

```sh
make                           # automatski TB, Verilator
make run_iverilog               # automatski TB, Icarus
make run_student               # studentska pobuda, Verilator
make run_iverilog TOP=tb_mreza_zp_bez_provere
make view_wave TOP=tb_mreza_zp_bez_provere   # opcioni GTKWave
```

Prvenstveno se koristi lokalni Docker image `hdlview-tools:2025.12`. Kada Docker nije dostupan, runner koristi instalirane simulatore; `HDL_LOCAL=1` ih bira izričito. Nije potreban pristup mreži. Rezultati oba testbench-a i oba simulatora imaju zasebne direktorijume u `../../../build/redizajn/systemverilog/02-s021/`. Svaki VCD sadrži i međusignale.

Ulazi se čitaju redom CBA. Funkcija daje F=1 za 011, 101 i 110. Sufiksi _n i _p predstavljaju komplementni i pravi izlaz para invertora. Kašnjenja gejtova nisu modelovana.

