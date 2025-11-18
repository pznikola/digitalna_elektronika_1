#!/usr/bin/env bash

# Analyze (compile) all VHDL files
compile:
	ghdl -a --std=08 zadatak_4.vhd
	ghdl -a --std=08 tb_zadatak_4.vhd

# Elaborate the testbench
elaborate:
	ghdl -e --std=08 tb_zadatak_4

# Run the simulation, dump VCD waveform
run:
	ghdl -r --std=08 tb_zadatak_4 \
		--vcd=zadatak_4.vcd \
		--stop-time=100ns

# Show waveform
show:
	gtkwave zadatak_4.vcd

# Clean old stuff
clean:
	rm -f *.o *.cf tb_zadatak_4 wave.vcd

# Run the simulation, dump VCD waveform
run_all:
	make clean
	make compile
	make elaborate
	make run
	make show
