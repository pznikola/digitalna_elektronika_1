#!/usr/bin/env bash

DESIGN = zadatak

# Clean old stuff
clean:
	rm -rf *.o *.cf *.vcd tb_${DESIGN} transcript *.qpf *.qsf *.wlf *.qws modelsim.ini ./db/ ./incremental_db/ ./output_files/ ./work/

# Run the simulation using GHDL
run_ghdl:
# Clean all
	make clean
# Analyze (compile) VHDL files
	ghdl -a --std=08 ${DESIGN}.vhd
	ghdl -a --std=08 tb_${DESIGN}.vhd
# Elaborate the testbench
	ghdl -e --std=08 tb_${DESIGN}
# Run the simulation, dump VCD waveform
	ghdl -r --std=08 tb_${DESIGN} \
		--vcd=${DESIGN}.vcd \
		--stop-time=100ns
# Show waveform
	gtkwave ${DESIGN}.vcd &

# Run the simulation using Quartus
run_vsim:
# Clean all
	make clean
# Run simulation
	vsim -do run_tb_gui.do


# Create Quartus project, elaborate it and open the project in order to inspect RTL schematic
run_schematic:
# Clean all
	make clean
# Build project
	./build_and_open.sh &
