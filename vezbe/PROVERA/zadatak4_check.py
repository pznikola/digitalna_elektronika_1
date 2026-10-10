#!/usr/bin/env python3
"""Check task 02/4 scope, combinational dependencies and meaningful RTL faults."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile

from hdl_runtime import ROOT, invoke
from simulacija import simulate


def original_source_sha(name):
    """Permit only the three recorded comment deletions requested by the user."""
    data = (ROOT / name).read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    cleanup = json.loads((ROOT / 'PROVERA/dokazi/student_text_cleanup.json').read_text())
    change = cleanup['comment_only_sv'].get(name)
    if change:
        assert actual == change['after_sha256'], ('unreviewed comment cleanup change', name)
        before = change['before_source'].encode()
        assert hashlib.sha256(before).hexdigest() == change['before_sha256']
        removed = b'    ' + (change['removed_comment'] + '\n').encode()
        assert before.count(removed) == 1, ('recorded comment not unique', name)
        expected = before.replace(removed, b'', 1)
        assert data == expected, ('change beyond the recorded comment deletion', name)
        return change['before_sha256']
    return actual


def references(expression):
    expression = re.sub(r"\b\d+'[sS]?[bBoOdDhH][0-9a-fA-FxXzZ_]+", '', expression)
    return set(re.findall(r'\b[A-Za-z_]\w*(?:\[\d+\])?', expression))


def assignments(source):
    source = re.sub(r'//[^\n]*', '', source)
    return {name: references(expr) for name, expr in
            re.findall(r'assign\s+(\w+)\s*=\s*(.*?);', source, re.S)}


def leaves(graph, signal, visiting=()):
    assert signal not in visiting, ('combinational feedback', visiting, signal)
    if signal not in graph:
        return {signal}
    return set().union(*(leaves(graph, other, (*visiting, signal)) for other in graph[signal]))


def inventory():
    frozen = json.loads((ROOT / 'PROVERA/dokazi/zadatak4_originals.json').read_text())
    for group in ['previous_sv_sha256', 'vhdl_sha256']:
        for name, expected in frozen[group].items():
            assert original_source_sha(name) == expected, ('changed original', name)
    base = ROOT / '02/code/Zadatak_4'
    for name in ['a', 'b', 'c']:
        folder = base / name
        for file in ['zadatak.sv', 'tb_zadatak.sv', 'Makefile']:
            assert (folder / file).is_file(), ('missing task 4 example', name, file)
        make = (folder / 'Makefile').read_text()
        relative = re.search(r'^PROVERA := (.*)$', make, re.M)[1]
        assert (folder / relative).resolve() == ROOT / 'PROVERA'
        for target in ['run_verilator', 'run_iverilog', 'view_wave', 'clean']:
            assert '\n' + target + ':' in make, ('missing Make target', name, target)
        for rtl in folder.glob('*.sv'):
            if not rtl.name.startswith('tb_'):
                source = rtl.read_text()
                assert not re.search(r'\b(timeunit|timeprecision|parameter|always|always_comb|always_ff)\b|`timescale|#', source), ('unnecessary RTL constructs', rtl)

    nor = (base / 'a/zadatak.sv').read_text()
    expressions = re.findall(r'assign\s+\w+\s*=\s*(.*?);', nor, re.S)
    assert len(expressions) == 26, ('NILI network inventory', len(expressions))
    for expr in expressions:
        assert re.fullmatch(r'\s*~\([\w\s|]+\)\s*', expr), ('not a NILI gate', expr)
    for bit in 'DCBA':
        assert f'assign {bit}_n = ~({bit} | {bit});' in nor, ('tied-input inverter', bit)

    helper = assignments((base / 'c/bcd_cifra.sv').read_text())
    helper_dependencies = {port: leaves(helper, port) for port in [*'abcdefg', 'ERROR', 'LZ_OUT']}
    assert helper_dependencies['ERROR'] == {'D', 'C', 'B'}, 'ERROR depends on display control'
    assert helper_dependencies['LZ_OUT'] == {'LZ_IN', 'D', 'C', 'B', 'A'}
    main = (base / 'c/zadatak.sv').read_text()
    graph = assignments(main)
    instances = re.findall(r'bcd_cifra\s+(\w+)\s*\((.*?)\);', main, re.S)
    assert {name for name, _ in instances} == {'CIFRA3', 'CIFRA2', 'CIFRA1', 'CIFRA0'}
    for name, body in instances:
        ports = dict(re.findall(r'\.(\w+)\(([^()]*)\)', body))
        if name == 'CIFRA0':
            assert ports['ERROR'] == '' and ports['LZ_OUT'] == '', 'unit control outputs must be unused'
            assert ports['OFF'] == "1'b0" and ports['LZ_IN'] == "1'b0"
        for port, deps in helper_dependencies.items():
            output = ports[port]
            if output:
                assert output not in graph, ('multiple signal drivers', output)
                graph[output] = set().union(*(references(ports[dep]) for dep in deps))
    expanded = {signal: sorted(leaves(graph, signal)) for signal in graph}
    assert set(expanded['G']) == {f'BCD{i}[{bit}]' for i in range(4) for bit in [3, 2, 1]}, 'global error is not from original BCD inputs'
    return dict(original_vhdl=len(frozen['vhdl_sha256']), previous_sv=len(frozen['previous_sv_sha256']),
                rtl=4, testbenches=4, nor_gates=26, hierarchical_graph_acyclic=True,
                helper_dependencies={k: sorted(v) for k, v in helper_dependencies.items()},
                expanded_main_dependencies=expanded)


def negative(output):
    cases = [
        ('a', 'zadatak.sv', 'tb_zadatak', [('a = ~(a1 | a2)', 'a = (a1 | a2)')], 'segment polarity'),
        ('c', 'zadatak.sv', 'tb_zadatak', [('BCD0[2] | BCD0[1]', 'BCD0[2]')], 'raw unit error'),
        ('c', 'zadatak.sv', 'tb_zadatak', [(".OFF(1'b0)", '.OFF(G)')], 'unit display blanked on error'),
        ('c', 'zadatak.sv', 'tb_zadatak', [('.a(SEG0[6])', '.a(SEG0[0])'), ('.g(SEG0[0])', '.g(SEG0[6])')], 'segment bit order'),
        ('c', 'bcd_cifra.sv', 'tb_bcd_cifra', [('ERROR = D & (C | B)', 'ERROR = ~OFF & D & (C | B)')], 'ERROR masked by OFF'),
    ]
    results = []
    with tempfile.TemporaryDirectory(prefix='de1-task4-negative-') as td:
        for index, (name, source, top, edits, label) in enumerate(cases):
            folder = Path(td) / str(index)
            shutil.copytree(ROOT / '02/code/Zadatak_4' / name, folder,
                            ignore=shutil.ignore_patterns('.build'))
            path = folder / source
            text = path.read_text()
            for old, new in edits:
                assert text.count(old) == 1, (label, 'mutation no longer matches', old)
                text = text.replace(old, new)
            path.write_text(text)
            try:
                simulate(folder, top, folder / 'simulation', 'iverilog', True)
            except RuntimeError as exc:
                assert 'FATAL:' in str(exc), (label, 'failure was not a testbench assertion', str(exc))
            else:
                raise AssertionError((label, 'testbench accepted the wrong design'))
            results.append(dict(fault=label, detected=True))
    Path(output).write_text(json.dumps(results, indent=2) + '\n')
    print(f'Task 02/4 negative: {len(results)} wrong designs rejected.', flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inside', action='store_true')
    args = parser.parse_args()
    record = inventory()
    if args.inside:
        negative('/out/zadatak4_negative.json')
    else:
        output = ROOT / 'PROVERA/_build'
        output.mkdir(exist_ok=True)
        (output / 'zadatak4_structure.json').write_text(json.dumps(record, indent=2) + '\n')
        invoke(__file__, ['--inside'], output)
        print('Task 02/4: 4 RTL modules, 4 testbenches, acyclic hierarchical graph; '
              f'{record["original_vhdl"]} VHDL unchanged; {record["previous_sv"]} prior SV programs '
              'preserved, with three recorded comment deletions.')


if __name__ == '__main__':
    main()
