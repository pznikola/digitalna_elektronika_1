#!/usr/bin/env python3
"""Deliberate faults in disposable copies must be rejected by real checks."""
import json,re,shutil,subprocess,sys,tempfile,xml.etree.ElementTree as ET
from pathlib import Path
from logic import drawio_graph
ROOT=Path(__file__).resolve().parents[1]
proof=[]
with tempfile.TemporaryDirectory(prefix='de1-negative-') as td:
 w=Path(td);shutil.copytree(ROOT/'02',w/'02');(w/'PROVERA').mkdir()
 for name in ['logic.py','vhdl_check.py','vhdl02.py','structure.py']:
  shutil.copy(ROOT/'PROVERA'/name,w/'PROVERA'/name)
 main=next((w/'02').glob('*.tex'));original=main.read_text()
 for kind,old,new,tool,needle in [
  ('formula',r'Y = C B + \bar{B} A',r'Y = C B + B A','02/code/provera.py','eq:zad2-b1'),
  ('table bit','0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 1 & 0','0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 0','02/code/provera.py','tab:bcd-7seg-e'),
  ('reference',r'\ref{fig:zadatak1-a}',r'\ref{fig:nepostojeca}','PROVERA/structure.py','undefined source references')]:
  assert old in original,kind;main.write_text(original.replace(old,new,1))
  cmd=[sys.executable,str(w/tool)]+(['02'] if kind=='reference' else [])
  r=subprocess.run(cmd,capture_output=True,text=True,cwd=w)
  assert r.returncode!=0 and needle in r.stdout+r.stderr,(kind,'fault not detected',r.stdout,r.stderr)
  proof.append(dict(fault=kind,detected=True,evidence=needle));main.write_text(original)
 # Move the real D2 source wire of the two-MUX diagram to another gate output.
 file=w/'02/Images/Zadatak_1/Zadatak_1a.drawio';cells=drawio_graph(file)
 target=next(c for c in cells.values() if c.get('edge')=='1' and c.get('source')=='_W-7RpAwgVxwbJvGlvNT-48')
 target.set('source','_W-7RpAwgVxwbJvGlvNT-44')
 mx=ET.Element('mxfile');d=ET.SubElement(mx,'diagram',name='Mutated copy');g=ET.SubElement(d,'mxGraphModel');r=ET.SubElement(g,'root');r.extend(cells.values());file.write_text(ET.tostring(mx,encoding='unicode'))
 p=subprocess.run([sys.executable,str(w/'02/code/provera.py')],capture_output=True,text=True,cwd=w)
 assert p.returncode!=0 and 'repeat manual diagram review' in p.stderr,('wire fault not detected',p.stderr)
 proof.append(dict(fault='drawn wire source',detected=True,evidence='source SHA differs from manually traced source'))
with tempfile.TemporaryDirectory(prefix='de1-negative-03-') as td:
 w=Path(td);shutil.copytree(ROOT/'03',w/'03')
 main=next((w/'03').glob('03_*.tex'));original=main.read_text()
 for kind,old,new,needle in [
  ('03 arithmetic result','480.1640625','480.1640624','eq:2.1.3 intermediate step'),
  ('03 table digit',r'1 & 0.375$\cdot$ & 2 & 0.75 & 0',r'1 & 0.375$\cdot$ & 2 & 0.75 & 1','table arithmetic')]:
  assert old in original,kind;main.write_text(original.replace(old,new,1))
  r=subprocess.run([sys.executable,str(w/'03/code/provera.py')],capture_output=True,text=True,cwd=w)
  assert r.returncode!=0 and needle in r.stdout+r.stderr,(kind,'fault not detected',r.stdout,r.stderr)
  proof.append(dict(fault=kind,detected=True,evidence=needle));main.write_text(original)

with tempfile.TemporaryDirectory(prefix='de1-negative-04-') as td:
 w=Path(td);shutil.copytree(ROOT/'04',w/'04');(w/'PROVERA').mkdir();shutil.copy(ROOT/'PROVERA/logic.py',w/'PROVERA/logic.py')
 main=next((w/'04').glob('04_*.tex'));original=main.read_text()
 bad=original.replace(r'c:\ 11100\\1111\\+1110',r'c:\ 01100\\1111\\+1110',1)
 assert bad!=original;main.write_text(bad)
 r=subprocess.run([sys.executable,str(w/'04/code/provera.py')],capture_output=True,text=True,cwd=w)
 assert r.returncode!=0 and 'carries' in r.stderr,('04 carry fault missed',r.stderr)
 proof.append(dict(fault='04 carry digit',detected=True,evidence='actual TeX carry vector differs'));main.write_text(original)
 path=w/'04/Images/Zadatak_4/karno.tex';original_map=path.read_text()
 path.write_text(original_map.replace(r'(0.5,3.5){0}',r'(0.5,3.5){1}',1))
 r=subprocess.run([sys.executable,str(w/'04/code/provera.py')],capture_output=True,text=True,cwd=w)
 assert r.returncode!=0 and 'K-map cell' in r.stderr,('04 map fault missed',r.stderr)
 proof.append(dict(fault='04 K-map value',detected=True,evidence='actual cell differs from addition'));path.write_text(original_map)
 path=w/'04/Images/Zadatak_3/maksimum.tex';original_wire=path.read_text();assert '(select.input 2)' in original_wire
 path.write_text(original_wire.replace('(select.input 2)','(select.output)',1))
 r=subprocess.run([sys.executable,str(w/'04/code/provera.py')],capture_output=True,text=True,cwd=w)
 assert r.returncode!=0 and 'repeat manual diagram review' in r.stderr,('04 wire fault missed',r.stderr)
 proof.append(dict(fault='04 selector wire',detected=True,evidence='reviewed source SHA mismatch'))


with tempfile.TemporaryDirectory(prefix='de1-negative-05-') as td:
 w=Path(td);shutil.copytree(ROOT/'05',w/'05')
 main=w/'05/05_kodovi.tex';original=main.read_text()
 old=r'8 & $\mathtt{1110}$ & $1$';new=r'8 & $\mathtt{1111}$ & $1$'
 assert old in original;main.write_text(original.replace(old,new,1))
 r=subprocess.run([sys.executable,str(w/'05/code/provera.py')],capture_output=True,text=True,cwd=w)
 assert r.returncode!=0 and 'actual code table BCD2421' in r.stderr,('05 code bit fault missed',r.stderr)
 proof.append(dict(fault='05 BCD2421 code bit',detected=True,evidence='actual table differs from verified code'));main.write_text(original)
 path=w/'05/Images/Uvod/kocke.tex';original_cube=path.read_text()
 # Duplicate an edge: total count and each edge distance remain correct, completeness fails.
 path.write_text(original_cube.replace('(c000)--(c100)','(c001)--(c101)',1))
 r=subprocess.run([sys.executable,str(w/'05/code/provera.py')],capture_output=True,text=True,cwd=w)
 assert r.returncode!=0 and 'cube edge set' in r.stderr,('05 missing cube edge fault missed',r.stderr)
 proof.append(dict(fault='05 missing cube edge replaced by duplicate',detected=True,evidence='actual unique cube edge set differs'))


with tempfile.TemporaryDirectory(prefix='de1-negative-07-') as td:
 w=Path(td);shutil.copytree(ROOT/'07',w/'07')
 main=w/'07/07_staticke_karakteristike.tex';original=main.read_text()
 old='5-x/4,';new='5+x/4,';assert old in original;main.write_text(original.replace(old,new,1))
 r=subprocess.run([sys.executable,str(w/'07/code/provera.py')],capture_output=True,text=True,cwd=w)
 assert r.returncode!=0 and 'actual cascade segments' in r.stderr,('07 slope fault missed',r.stderr)
 proof.append(dict(fault='07 slope sign',detected=True,evidence='actual cascade segment differs'));main.write_text(original)
 path=w/'07/Images/Zadatak_3/karakteristike.tex';original_curve=path.read_text()
 assert '(0,5)--(1,3)--(4,2)' in original_curve
 path.write_text(original_curve.replace('(0,5)--(1,3)--(4,2)','(0,5)--(1,3.1)--(4,2)',1))
 r=subprocess.run([sys.executable,str(w/'07/code/provera.py')],capture_output=True,text=True,cwd=w)
 assert r.returncode!=0 and 'Zadatak_3/karakteristike coordinate' in r.stderr,('07 plot fault missed',r.stderr)
 proof.append(dict(fault='07 graph ordinate',detected=True,evidence='drawn curve coordinate differs from formula'))


with tempfile.TemporaryDirectory(prefix='de1-negative-08-') as td:
 w=Path(td);shutil.copytree(ROOT/'08',w/'08');(w/'PROVERA').mkdir();shutil.copy(ROOT/'PROVERA/logic.py',w/'PROVERA/logic.py')
 main=w/'08/08_mos.tex';original=main.read_text()
 for kind,old,new,needle in [
  ('08 CMOS threshold', '400 & 4 & 0.611288', '400 & 4 & 0.612288', 'actual numerical value'),
  ('08 TG row 0101', r'\texttt{0101} & 1', r'\texttt{0101} & 0', 'actual TG truth table')]:
  assert old in original;main.write_text(original.replace(old,new,1))
  r=subprocess.run([sys.executable,str(w/'08/code/provera.py')],capture_output=True,text=True,cwd=w)
  assert r.returncode!=0 and needle in r.stderr,(kind,'fault missed',r.stderr)
  proof.append(dict(fault=kind,detected=True,evidence=needle));main.write_text(original)
 path=w/'08/Images/Zadatak_5/bez_negacija.tex';orig=path.read_text();assert r'\draw(2.8,0)--(inv.input)' in orig
 path.write_text(orig.replace(r'\draw(2.8,0)--(inv.input)',r'\draw(3.4,0)--(inv.input)',1))
 r=subprocess.run([sys.executable,str(w/'08/code/provera.py')],capture_output=True,text=True,cwd=w)
 assert r.returncode!=0 and 'drawn inverter input' in r.stderr,('08 wire break missed',r.stderr)
 proof.append(dict(fault='08 disconnected inverter input',detected=True,evidence='graph has distinct electrical nodes'))

(ROOT/'PROVERA/_build').mkdir(exist_ok=True)
(ROOT/'PROVERA/_build/negative.json').write_text(json.dumps(proof,indent=2)+'\n')
print(f'Negativne probe: {len(proof)} namernih grešaka u formulama, tabelama, vezama i referencama uspešno odbijeno.')
