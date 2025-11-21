package require ::quartus::project

set proj_name "zadatak"
set rev_name  "zadatak"

if {[project_exists $proj_name]} {
    project_open -revision $rev_name $proj_name
} else {
    project_new  -revision $rev_name $proj_name
}

# Device settings (edit these for your real target)
set_global_assignment -name FAMILY "Cyclone V"
set_global_assignment -name DEVICE "5CSEMA5F31C6"

# Source file and top entity
set_global_assignment -name VHDL_FILE "mux4.vhd"
set_global_assignment -name VHDL_FILE "zadatak.vhd"
set_global_assignment -name TOP_LEVEL_ENTITY "zadatak"

# Put all compilation outputs under tmp/
set_global_assignment -name PROJECT_OUTPUT_DIRECTORY "tmp"

# (optional) Put EDA / simulation outputs under tmp as well
# Optional: put outputs in a dedicated folder
set_global_assignment -name PROJECT_OUTPUT_DIRECTORY output_files

package require ::quartus::flow

project_open -revision $rev_name $proj_name
execute_flow -analysis_and_elaboration

#project_close
