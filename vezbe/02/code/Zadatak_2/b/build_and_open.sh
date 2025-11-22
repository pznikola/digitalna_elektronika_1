#!/usr/bin/env bash
quartus_sh -t make_project.tcl
quartus zadatak.qpf &
# Then in GUI: Tools → Netlist Viewers → RTL Viewer