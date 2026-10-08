#!/usr/bin/env bash
quartus_sh -t make_project_vhdl.tcl
quartus zadatak.qpf &
# Then in GUI: Tools → Netlist Viewers → RTL Viewer