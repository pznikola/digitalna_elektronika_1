.DEFAULT_GOAL := run_verilator
PYTHON ?= python3
LECTURE := 02_sinteza_kombinacionih_mreza
SLIDE := 02-s021
TOP ?= tb_mreza_zp
HDL_LOCAL ?= 0
RUNNER := ../../../../_alati/simulacija_sv.py
WAVES := ../../../build/redizajn/systemverilog/$(SLIDE)
.PHONY: run_verilator run_iverilog run_student view_wave
run_verilator:
	$(PYTHON) $(RUNNER) --lecture "$(LECTURE)" --slide "$(SLIDE)" --engine verilator --top "$(TOP)" $(if $(filter 1,$(HDL_LOCAL)),--local,)
run_iverilog:
	$(PYTHON) $(RUNNER) --lecture "$(LECTURE)" --slide "$(SLIDE)" --engine iverilog --top "$(TOP)" $(if $(filter 1,$(HDL_LOCAL)),--local,)
run_student: TOP := tb_mreza_zp_bez_provere
run_student: run_verilator
view_wave:
	gtkwave "$(WAVES)/verilator/$(TOP)/$(TOP).vcd"
