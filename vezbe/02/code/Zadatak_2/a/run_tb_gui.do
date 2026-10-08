# run_tb_gui.do

# Create / map the work library
vlib work_sv
vmap work_sv work_sv

# Compile design and testbench
vlog -sv -timescale 1ns/1ps -work work_sv mux4.sv
vlog -sv -timescale 1ns/1ps -work work_sv zadatak.sv
vlog -sv -timescale 1ns/1ps -work work_sv tb_zadatak.sv

# Start simulation of testbench top
vsim -voptargs=+acc work_sv.tb_zadatak

# Add all TB signals to the wave window
add wave -position insertpoint sim:/tb_zadatak/*

# Run for some time so you get some activity
run 400 ns

# Do NOT quit here – leave GUI + waves open
# quit -f
