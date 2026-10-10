#!/usr/bin/env python3
"""Student testbenches and independent VHDL/SV event-trace comparisons in Docker."""
import argparse
from bisect import bisect_right
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile

from hdl_runtime import ROOT, IMAGE, invoke, run
from simulacija import icarus_timescale, simulate


def original_inventory():
    manifest = json.loads((ROOT / 'PROVERA/dokazi/systemverilog_originals.json').read_text())
    actual = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(ROOT.rglob('*.vhd'))}
    assert actual == manifest['vhdl_sha256'], 'Original VHDL sources changed or disappeared'
    for name in actual:
        assert (ROOT / name).with_suffix('.sv').exists(), ('missing SV counterpart', name)
    return len(actual)


def vcd(path):
    """Keep hierarchical names and aliases; normalize time to integer femtoseconds."""
    data = Path(path).read_text()
    scale = re.search(r'\$timescale\s+(\d+)\s*(fs|ps|ns|us|ms|s)\s+\$end', data)
    assert scale, ('missing timescale', path)
    unit = int(scale[1]) * {'fs': 1, 'ps': 1000, 'ns': 10**6, 'us': 10**9, 'ms': 10**12, 's': 10**15}[scale[2]]
    scope, aliases, traces, widths = [], {}, {}, {}
    time = 0
    for line in data.splitlines():
        parts = line.split()
        if not parts:
            continue
        if parts[0] == '$scope':
            scope.append(parts[2].lower())
        elif parts[0] == '$upscope':
            scope.pop()
        elif parts[0] == '$var':
            name = re.sub(r'\[[^]]*\]$', '', parts[4]).lower()
            name = '.'.join([s for s in scope if s != 'top'] + [name])
            aliases.setdefault(parts[3], []).append(name)
            traces[name] = []
            widths[name] = int(parts[2])
        elif line.startswith('#'):
            time = int(line[1:]) * unit
        elif parts[0][0] in 'bB' and len(parts) == 2:
            identifier, value = parts[1], parts[0][1:]
            append_event(traces, widths, aliases.get(identifier, []), time, value)
        elif len(parts) == 1 and line[0] in '01xXzZuU':
            append_event(traces, widths, aliases.get(line[1:], []), time, line[0])
    # Delta cycles have no elapsed physical time. Keep the final value at a timestamp.
    for name, seq in traces.items():
        compressed = []
        for t, value in seq:
            if compressed and compressed[-1][0] == t:
                compressed[-1] = (t, value)
            else:
                compressed.append((t, value))
        traces[name] = [(t, v) for i, (t, v) in enumerate(compressed)
                        if not i or compressed[i-1][1] != v]
    return traces


def append_event(traces, widths, names, time, value):
    value = value.lower().replace('u', 'x')
    for name in names:
        padded = value.rjust(widths[name], value[0] if value[0] in 'xz' else '0')
        traces[name].append((time, padded))


def value_at(seq, time):
    i = bisect_right(seq, (time, '\uffff')) - 1
    assert i >= 0, ('no value', time, seq)
    return seq[i][1]


def compare(golden, actual, instances, start, end):
    compared, events = [], 0
    for instance in instances:
        prefix = 'audit_tb.' + instance.lower() + '.'
        names = [name for name in golden if name.startswith(prefix)]
        assert names, ('no VHDL DUT signals', prefix)
        for name in names:
            assert name in actual, ('untraced SystemVerilog signal', name)
            a, b = golden[name], actual[name]
            times = {start, end}
            times.update(t for t, _ in a if start <= t <= end)
            times.update(t for t, _ in b if start <= t <= end)
            for t in sorted(times):
                assert value_at(a, t) == value_at(b, t), (name, t / 10**6, value_at(a, t), value_at(b, t))
            compared.append(name)
            events += len(times)
    return compared, events


def cases(n):
    result = []
    if n == '01':
        for task in range(1, 7):
            outputs = {'C': 4} if task == 3 else {'Y_ZP': 1, 'Y_PZ': 1} if task < 3 else {'Y': 1} if task == 4 else {'Y_min': 1, 'Y_no_hazard': 1}
            ports = {'A': (3, 2), 'B': (1, 0)} if task == 3 else {k: 3-i for i, k in enumerate('ABCD')}
            result.append(dict(path=f'01/code/Zadatak_{task}', entity='zadatak', width=4, ports=ports, outputs=outputs, delay=1 if task >= 4 else None))
    else:
        result = [
            dict(path='02/code/Zadatak_1/a', entity='zadatak', width=6, ports={'S': (5, 4), 'D': (3, 0)}, outputs={'Y': 1}, delay=None),
            dict(path='02/code/Zadatak_1/b', entity='zadatak', width=4, ports={'A': 3, 'B': 2, 'C': (1, 0)}, outputs={'Y': 2}, delay=None),
        ]
        for part, delay in [('a', 20), ('b', 10), ('d', 10)]:
            result.append(dict(path=f'02/code/Zadatak_2/{part}', entity='zadatak', width=3, ports={'A': 0, 'B': 1, 'C': 2}, outputs={'Y': 1}, delay=delay))
        for part, width, outputs in [('a', 3, {'Y': 8}), ('b', 4, {'Y': 16}), ('c', 3, {'Y_comb': 1, 'Y_dekoder': 1})]:
            ports = {'A': (width-1, 0)} if part != 'c' else {'A': 0, 'B': 1, 'C': 2}
            result.append(dict(path=f'02/code/Zadatak_3/{part}', entity='zadatak', width=width, ports=ports, outputs=outputs, delay=None))
        for part, delay in [('Zadatak_1/b', None), ('Zadatak_2/a', 20)]:
            result.append(dict(path='02/code/'+part, entity='mux4', width=6, ports={'S': (5, 4), 'D': (3, 0)}, outputs={'Y': 1}, delay=delay))
        for part in ['b', 'c']:
            result.append(dict(path=f'02/code/Zadatak_3/{part}', entity='decoder', width=6,
                               ports={'EN0': 5, 'EN1_B': 4, 'EN2_B': 3, 'A': (2, 0)}, outputs={'Y': 8}, delay=None))
    return result


def schedule(case):
    width = case['width']
    delays = [case['delay'], 7] if case['delay'] else []
    hold = (max(delays or [1]) * 10 + 10) * 1000  # picoseconds
    steps = [(0, hold)]
    steps += [(i, hold) for i in range(2**width)]
    pairs = [(a, a ^ (1 << bit)) for a in range(2**width) for bit in range(width)]
    for a, b in pairs:
        steps += [(a, hold), (b, hold)]
    if delays:
        for delay in sorted(set(delays)):
            for a in [0, 2**width-1]:
                for bit in range(width):
                    for pulse in [delay*1000-1, delay*1000, delay*1000+1, 2*delay*1000]:
                        steps += [(a, hold), (a ^ (1 << bit), pulse), (a, hold)]
    return steps, pairs, hold


def four_state_schedule(case):
    width = case['width']
    hold = 10000
    steps = [(0, hold)]
    for initial in ['0' * width, '1' * width]:
        for bit in range(width):
            for unknown in 'xz':
                word = initial[:bit] + unknown + initial[bit+1:]
                steps += [(int(initial, 2), hold), (word, hold)]
    steps += [('x' * width, hold), ('z' * width, hold)]
    if case['entity'] == 'decoder':
        # Known enable, unknown address; known disable dominates unknown inputs.
        steps += [('100xxx', hold), ('100zzz', hold), ('000xxx', hold),
                  ('x00000', hold), ('z00000', hold), ('111zzz', hold),
                  ('0xxzzz', hold), ('x10xxx', hold)]
    return steps, [], hold


def audit_sources(case, steps):
    width, outputs = case['width'], case['outputs']
    sv_decl = [f'    logic [{width-1}:0] X;']
    vh_decl = [f'signal X: std_logic_vector({width-1} downto 0);']
    sv_inst, vh_inst = [], []
    variants = [('dut_default', None)] + ([('dut_changed', 7)] if case['delay'] else [])
    for inst, delay in variants:
        sv_ports, vh_ports = [], []
        for name, bit in case['ports'].items():
            if isinstance(bit, tuple):
                sv, vh = f'X[{bit[0]}:{bit[1]}]', f'X({bit[0]} downto {bit[1]})'
            else:
                sv, vh = f'X[{bit}]', f'X({bit})'
            sv_ports.append(f'.{name}({sv})'); vh_ports.append(f'{name}=>{vh}')
        for name, bits in outputs.items():
            signal = inst + '_' + name
            sv_decl.append(f'    logic ' + (f'[{bits-1}:0] ' if bits > 1 else '') + signal + ';')
            vh_decl.append(f'signal {signal}: ' + (f'std_logic_vector({bits-1} downto 0)' if bits > 1 else 'std_logic') + ';')
            sv_ports.append(f'.{name}({signal})'); vh_ports.append(f'{name}=>{signal}')
        sv_inst.append(f'    {case["entity"]} ' + (f'#(.T({delay}ns)) ' if delay else '') + inst + ' (' + ', '.join(sv_ports) + ');')
        vh_inst.append(inst + ': entity work.' + case['entity'] + (f' generic map(T=>{delay} ns)' if delay else '') + ' port map(' + ','.join(vh_ports) + ');')
    words = [(word if isinstance(word, str) else f'{word:0{width}b}', ps) for word, ps in steps]
    sv_steps = '\n'.join(f"        X = {width}'b{word}; #{ps}ps;" for word, ps in words)
    vh_steps = '\n'.join(f'X <= "{word.upper().replace("X", "U")}"; wait for {ps} ps;' for word, ps in words)
    sv = 'module audit_tb;\n    timeunit 1ns; timeprecision 1ps;\n' + '\n'.join(sv_decl + sv_inst) + '\n    initial begin\n        $dumpfile("audit.vcd"); $dumpvars(0, audit_tb);\n' + sv_steps + '\n        $finish;\n    end\nendmodule\n'
    vh = 'library ieee; use ieee.std_logic_1164.all; entity audit_tb is end; architecture test of audit_tb is\n' + '\n'.join(vh_decl) + '\nbegin\n' + '\n'.join(vh_inst) + '\nprocess begin\n' + vh_steps + '\nstd.env.stop; wait; end process; end;\n'
    return sv, vh, [i for i, _ in variants]


def equivalent(case, work, engine='verilator', four_state=False):
    folder = ROOT / case['path']
    work.mkdir()
    steps, pairs, hold = four_state_schedule(case) if four_state else schedule(case)
    sv, vh, instances = audit_sources(case, steps)
    (work / 'audit_tb.sv').write_text(sv)
    (work / 'audit_tb.vhd').write_text(vh)
    vhdl = [p for p in sorted(folder.glob('*.vhd')) if p.name not in ['zadatak.vhd', 'tb_zadatak.vhd']]
    if case['entity'] == 'zadatak':
        vhdl += [folder / 'zadatak.vhd']
    else:
        vhdl = [folder / (case['entity'] + '.vhd')]
    run(['ghdl', '-a', '--std=08', *map(str, vhdl), 'audit_tb.vhd'], work)
    run(['ghdl', '-e', '--std=08', 'audit_tb'], work)
    run(['ghdl', '-r', '--std=08', 'audit_tb', '--assert-level=error', '--vcd=golden.vcd'], work)
    sv_designs = [p for p in sorted(folder.glob('*.sv')) if not p.name.startswith('tb_')]
    if case['entity'] != 'zadatak':
        sv_designs = [folder / (case['entity'] + '.sv')]
    if engine == 'verilator':
        run(['verilator', '--binary', '--timing', '--trace', '--assert', '--top-module', 'audit_tb',
             '--timescale', '1ns/1ps',
             '--Mdir', str(work / 'obj_dir'), '-j', '2', *map(str, sv_designs), 'audit_tb.sv'], work)
        run([str(work / 'obj_dir/Vaudit_tb')], work)
    else:
        run(['iverilog', '-g2012', '-s', 'audit_tb', '-o', 'audit', '-c', icarus_timescale(work),
             *map(str, sv_designs), 'audit_tb.sv'], work)
        run(['vvp', 'audit'], work)
    signals, events = compare(vcd(work / 'golden.vcd'), vcd(work / 'audit.vcd'), instances,
                             hold * 1000, sum(ps for _, ps in steps) * 1000)
    return dict(path=case['path'], entity=case['entity'], result='pass', engine=engine,
                four_state=four_state, binary_states=0 if four_state else 2**case['width'], single_input_transitions=len(pairs),
                delay_ns=[case['delay'], 7] if case['delay'] else [],
                short_pulse_tests=bool(case['delay']), signals=signals, compared_timepoints=events)


def negative_checks(output):
    """Real gate, pin, parameter and delay faults must fail event comparison."""
    global ROOT
    original_root = ROOT
    faults = [
        ('01', 2, 'zadatak.sv', '~(A[0] & B[0])', '(A[0] & B[0])', 'multiplier negation'),
        ('02', 1, 'zadatak.sv', '.D(D_Y1)', '.D(D_Y0)', 'MUX pin connection'),
        ('02', 2, 'zadatak.sv', '#(.T(T))', '#(.T(20ns))', 'delay parameter propagation'),
        ('01', 3, 'zadatak.sv', 'assign #(T) I1', 'assign I1', 'inverter delay'),
    ]
    proof = []
    try:
        with tempfile.TemporaryDirectory(prefix='de1-sv-negative-') as td:
            ROOT = Path(td) / 'sources'
            for n in ['01', '02']:
                shutil.copytree(original_root / n / 'code', ROOT / n / 'code',
                                ignore=shutil.ignore_patterns('.build', '__pycache__'))
            for index, (n, case_index, filename, old, new, description) in enumerate(faults):
                case = cases(n)[case_index]
                source = ROOT / case['path'] / filename
                original = source.read_text()
                assert old in original, (description, old)
                source.write_text(original.replace(old, new, 1))
                try:
                    equivalent(case, Path(td) / f'fault-{index}', 'iverilog')
                except AssertionError as error:
                    proof.append(dict(fault=description, detected=True, evidence=str(error)))
                else:
                    raise AssertionError(('HDL fault was not detected', description))
                finally:
                    source.write_text(original)
    finally:
        ROOT = original_root
    Path(output).write_text(json.dumps(proof, indent=2) + '\n')
    print('SystemVerilog negative checks:', len(proof), 'detected faults', flush=True)


def check(n, output, students=True, equivalence=True, four_state=True):
    original_inventory()
    proof = dict(exercise=n, image=IMAGE, versions={}, student_testbenches=[], equivalence=[])
    for tool in ['verilator', 'ghdl', 'iverilog']:
        proof['versions'][tool] = run([tool, '--version' if tool != 'iverilog' else '-V'], ROOT).splitlines()[0]
    with tempfile.TemporaryDirectory(prefix='de1-sv-'+n+'-') as td:
        work = Path(td)
        if students:
            for index, tb in enumerate(sorted((ROOT / n / 'code').rglob('tb_*.sv'))):
                for engine in ['verilator', 'iverilog']:
                    simulate(tb.parent, tb.stem, work / f'student-{index}-{engine}', engine, engine == 'iverilog')
                    proof['student_testbenches'].append(dict(path=str(tb.relative_to(ROOT)), engine=engine, result='pass'))
                print(n, str(tb.relative_to(ROOT)), 'Verilator + Icarus: pass', flush=True)
        if equivalence and n in ['01', '02']:
            for i, case in enumerate(cases(n)):
                result = equivalent(case, work / f'equivalence-{i}')
                proof['equivalence'].append(result)
                print(n, case['path'], case['entity'], 'VHDL/SV:', result['compared_timepoints'], 'timepoints: pass', flush=True)
        if n == '02' and four_state:
            for i, case in enumerate(cases(n)):
                if '/Zadatak_3/' in case['path']:
                    result = equivalent(case, work / f'four-state-{i}', 'iverilog', True)
                    proof['equivalence'].append(result)
                    print(n, case['path'], case['entity'], 'VHDL/Icarus X/Z: pass', flush=True)
    Path(output).write_text(json.dumps(proof, ensure_ascii=False, indent=2) + '\n')
    return proof


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('exercise', choices=['01', '02', '04', '05', 'negative'])
    p.add_argument('--inside', action='store_true')
    p.add_argument('--output')
    p.add_argument('--only', choices=['students', 'equivalence', 'four-state'])
    a = p.parse_args()
    if not a.inside:
        args = [a.exercise, '--inside', '--output', '/out/systemverilog'+a.exercise+('.'+a.only if a.only else '')+'.json']
        if a.only:
            args += ['--only', a.only]
        invoke(__file__, args, ROOT / 'PROVERA/_build')
    else:
        if a.exercise == 'negative':
            negative_checks(a.output)
        else:
            check(a.exercise, a.output, a.only not in ['equivalence','four-state'],
                  a.only not in ['students','four-state'], a.only != 'students')


if __name__ == '__main__':
    main()
