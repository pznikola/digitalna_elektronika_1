#!/usr/bin/env python3
"""Build existing native figures and a standalone exercise; never delete inputs."""
import argparse,os,re,subprocess,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def run(args,cwd):
 p=subprocess.run(args,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 if p.returncode:
  print(p.stdout);raise SystemExit(p.returncode)
 return p.stdout

def build(n,figures_only=False,force=False):
 folder=ROOT/n;main=next(folder.glob('*.tex'));text=main.read_text()
 sources=set((folder/'Images').rglob('*.tex'))
 for name in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',text):
  p=folder/'Images'/name
  d=p.with_suffix('.drawio')
  if d.exists():sources.add(d)
 for src in sorted(sources):
  dst=src.with_suffix('.pdf')
  if not force and dst.exists() and dst.stat().st_mtime>=src.stat().st_mtime:continue
  if src.suffix=='.drawio':
   with tempfile.TemporaryDirectory(prefix='.drawio-export-',dir=src.parent) as td:
    fresh=Path(td)/'figure.pdf'
    output=run(['xvfb-run','-a','drawio','--no-sandbox','--export','--format','pdf','--crop','--output',str(fresh),str(src)],folder)
    if not fresh.is_file() or not fresh.read_bytes().startswith(b'%PDF-'):
     raise RuntimeError('Draw.io did not produce a new PDF: '+output)
    fresh.replace(dst)
  else:run(['latexmk','-pdf','-synctex=1','-interaction=nonstopmode','-halt-on-error','-file-line-error',src.name],src.parent)
  assert dst.is_file(),dst
  print(f'{n}: {src.relative_to(folder)} → PDF',flush=True)
 if figures_only:return
 args=['latexmk','-pdf','-synctex=1','-interaction=nonstopmode','-halt-on-error','-file-line-error']
 if r'\usepackage{minted}' in text:args.append('-shell-escape')
 if force:args.append('-g')
 run(args+[main.name],folder)
 print(f'{n}: {main.with_suffix(".pdf").name}',flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('exercise',choices=['01','02','03','04','05','07','08']);p.add_argument('--figures-only',action='store_true');p.add_argument('--force',action='store_true');a=p.parse_args();build(a.exercise,a.figures_only,a.force)
