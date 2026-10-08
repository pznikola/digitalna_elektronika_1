# SystemVerilog je aktivni primer; VHDL izvori i ciljevi su sacuvani.
.DEFAULT_GOAL := run_verilator
PYTHON ?= python3
PROVERA := ../../../../PROVERA
EXAMPLE := 02/code/Zadatak_3/c
TOP ?= tb_zadatak
.PHONY: run_verilator run_iverilog view_wave run_ghdl run_vsim run_vsim_vhdl run_schematic run_schematic_vhdl clean

run_verilator:
	$(PYTHON) $(PROVERA)/simulacija.py $(EXAMPLE) --top $(TOP)

run_iverilog:
	$(PYTHON) $(PROVERA)/simulacija.py $(EXAMPLE) --top $(TOP) --engine iverilog

view_wave:
	gtkwave .build/verilator/$(TOP).vcd

run_ghdl:
	$(PYTHON) $(PROVERA)/simulacija.py $(EXAMPLE) --engine ghdl

run_vsim:
	vsim -do run_tb_gui.do

run_vsim_vhdl:
	vsim -do run_tb_gui_vhdl.do

run_schematic:
	./build_and_open.sh

run_schematic_vhdl:
	./build_and_open_vhdl.sh

clean:
	rm -rf .build/
