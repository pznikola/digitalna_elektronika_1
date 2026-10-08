# run_tb_gui.do

# Create / map the work library
vlib work
vmap work work

# Compile design and testbench
vcom zadatak.vhd
vcom tb_zadatak.vhd

# Start simulation of testbench top
vsim -voptargs=+acc tb_zadatak

# Set ABCD to binary radix
radix signal sim:/tb_zadatak/ABCD -binary

# Add all TB signals to the wave window
add wave -position insertpoint sim:/tb_zadatak/*

# Run for some time so you get some activity
run 700 ns

# Do NOT quit here – leave GUI + waves open
# quit -f
