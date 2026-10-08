#!/usr/bin/env python3
"""One exercise directory per build: repeated module names never share a library."""
import argparse
from pathlib import Path

from hdl_runtime import ROOT, invoke, run


def sources(folder, top):
    designs = [p for p in sorted(folder.glob('*.sv')) if not p.name.startswith('tb_')]
    tb = folder / (top + '.sv')
    if not tb.exists():
        raise FileNotFoundError(tb)
    return [*designs, tb]


def icarus_timescale(output):
    # Compilation-unit defaults belong to simulation setup, outside student RTL.
    config = Path(output) / 'simulation_timescale.sv'
    config.write_text('`timescale 1ns/1ps\n')
    return str(config)


def simulate(folder, top, output, engine='verilator', four_state=False):
    folder, output = Path(folder).resolve(), Path(output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    files = list(map(str, sources(folder, top)))
    if engine == 'verilator':
        run(['verilator', '--binary', '--timing', '--trace', '--assert',
             '--timescale', '1ns/1ps',
             '--top-module', top, '--Mdir', str(output / 'obj_dir'),
             '-j', '2', *files], output)
        text = run([str(output / 'obj_dir' / ('V' + top))], output)
    elif engine == 'iverilog':
        run(['iverilog', '-g2012', '-s', top, *(['-DFOUR_STATE'] if four_state else []),
             '-o', str(output / 'testbench'), icarus_timescale(output), *files], output)
        text = run(['vvp', str(output / 'testbench')], output)
    else:
        raise ValueError(engine)
    if 'PASS:' not in text:
        raise AssertionError((folder, top, 'testbench did not report completion', text))
    return text


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('example', help='Example path relative to vezbe, e.g. 01/code/Zadatak_4')
    p.add_argument('--top', default='tb_zadatak')
    p.add_argument('--engine', choices=['verilator', 'iverilog', 'ghdl'], default='verilator')
    p.add_argument('--inside', action='store_true')
    p.add_argument('--output')
    a = p.parse_args()
    folder = (ROOT / a.example).resolve()
    folder.relative_to(ROOT)
    if not a.inside:
        invoke(__file__, [a.example, '--top', a.top, '--engine', a.engine,
                         '--inside', '--output', '/out'], folder / '.build' / a.engine)
        return
    output = Path(a.output)
    if a.engine == 'ghdl':
        # Original stimuli end with an indefinite wait; allow all sequences to finish.
        files = [p for p in sorted(folder.glob('*.vhd')) if p.name not in ['zadatak.vhd', 'tb_zadatak.vhd']]
        files += [folder / 'zadatak.vhd', folder / 'tb_zadatak.vhd']
        run(['ghdl', '-a', '--std=08', *map(str, files)], output)
        run(['ghdl', '-e', '--std=08', 'tb_zadatak'], output)
        print(run(['ghdl', '-r', '--std=08', 'tb_zadatak', '--assert-level=error',
                   '--vcd=tb_zadatak.vcd', '--stop-time=1us'], output))
    else:
        print(simulate(folder, a.top, output, a.engine, a.engine == 'iverilog'))
    print(f'VCD: {a.example}/.build/{a.engine}/{a.top}.vcd', flush=True)


if __name__ == '__main__':
    main()
