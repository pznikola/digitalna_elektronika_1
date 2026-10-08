"""Run HDL tools in the pinned local Docker image; no GUI or network required."""
import os
from pathlib import Path
import shlex
import subprocess

IMAGE = os.environ.get('HDL_IMAGE', 'hdlview-tools:2025.12')
ROOT = Path(__file__).resolve().parents[1]


def docker_command(args, mounts, cwd='/work'):
    cmd = ['docker', 'run', '--rm', '--network', 'none',
           '--user', f'{os.getuid()}:{os.getgid()}',
           '-e', 'DE1_IN_CONTAINER=1', '-e', 'PYTHONDONTWRITEBYTECODE=1']
    for source, target, readonly in mounts:
        cmd += ['--mount', f'type=bind,src={Path(source).resolve()},dst={target}' + (',readonly' if readonly else '')]
    return cmd + ['-w', cwd, '--entrypoint', '/bin/bash', IMAGE, '-lc', shlex.join(map(str, args))]


def run(args, cwd, timeout=300):
    """Existing GHDL checks also use Docker when called on the host."""
    cmd = list(map(str, args)) if os.environ.get('DE1_IN_CONTAINER') else docker_command(args, [(cwd, '/work', False)])
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    if p.returncode:
        raise RuntimeError(shlex.join(cmd) + '\n' + p.stdout + p.stderr)
    return '\n'.join(line for line in p.stdout.splitlines() if not line.startswith('[INFO] Final '))


def invoke(script, args, output):
    """Expose sources read-only and only the selected artifact directory writable."""
    output = Path(output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    relative = Path(script).resolve().relative_to(ROOT)
    cmd = docker_command(['python3', '/src/' + relative.as_posix(), *args],
                         [(ROOT, '/src', True), (output, '/out', False)], '/src')
    p = subprocess.run(cmd)
    if p.returncode:
        raise SystemExit(p.returncode)
