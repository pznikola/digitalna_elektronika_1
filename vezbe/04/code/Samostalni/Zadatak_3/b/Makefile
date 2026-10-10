# Svaki primer ima zasebnu simulaciju i biblioteku.
.DEFAULT_GOAL := run_verilator
PYTHON ?= python3
PROVERA := ../../../../../PROVERA
EXAMPLE := 04/code/Samostalni/Zadatak_3/b
TOP ?= tb_zadatak
.PHONY: run_verilator run_iverilog view_wave clean
run_verilator:
	$(PYTHON) $(PROVERA)/simulacija.py $(EXAMPLE) --top $(TOP)
run_iverilog:
	$(PYTHON) $(PROVERA)/simulacija.py $(EXAMPLE) --top $(TOP) --engine iverilog
view_wave:
	gtkwave .build/verilator/$(TOP).vcd
clean:
	rm -rf .build/
