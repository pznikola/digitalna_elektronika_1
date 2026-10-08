#!/usr/bin/env bash
quartus_sh -t make_project.tcl
quartus zadatak_sv.qpf &
# Then in GUI: Tools → Netlist Viewers → RTL Viewer