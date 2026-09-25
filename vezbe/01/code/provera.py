#!/usr/bin/env python3
"""Checks actual equations, tables, K-map groups, Draw.io nets and compiled VHDL."""
from pathlib import Path
import hashlib,itertools,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'PROVERA'))
from logic import evaluate,uncomment,clean,reviewed_schematic,hazards,kmap_rect
from vhdl_check import check01
s=uncomment((ROOT/'01_kombinacione_hazardi.tex').read_text());count=0

def check(v,msg=''):
 global count
 if not v:raise AssertionError(msg)
 count+=1
rows=list(itertools.product([0,1],repeat=4))
def expect(task,env):
 a,b,c,d=(env[k] for k in 'ABCD')
 return {1:bool((a or c or d) and(not a or c or not d)and(b or not c)),2:'00' in ''.join(map(str,(a,b,c,d))),4:bool((a and not b)or(c and d)or(a and c and not d)),5:bool((not a and not c)or(c and d)or(b and c and not d)),6:bool((not b and not c and not d)or(a and not c and d)or(not a and c and not d))}[task]
# Actual displayed equation chains: every right-hand side, not hard-coded copies.
for m in re.finditer(r'\\begin\{equation\}(.*?)\\end\{equation\}',s,re.S):
 heads=re.findall(r'\\subsection\{Zadatak ([1-6])\}',s[:m.start()])
 if not heads:continue
 task=int(heads[-1]);parts=clean(m.group(1)).split('=');lhs=parts[0].strip()
 for bits in rows:
  env=dict(zip('ABCD',bits))
  if task==3:
   env.update(dict(zip(['A1','A0','B1','B0'],bits)));prod=(2*bits[0]+bits[1])*(2*bits[2]+bits[3]);idx=int(lhs[1]);want=bool(prod>>idx&1)
  else:want=expect(task,env);env.update(Y=want,Z=want)
  for expr in parts[1:]:check(evaluate(expr,env)==want,('equation',task,expr,bits))
# All ten Boolean algebra rules and both forms, read directly from the table.
intro=s[:s.index(r'\section{Zadaci}')]
for expr in re.findall(r'\$([^$]+)\$',intro,re.S):
 if '=' not in expr or expr.startswith('Y'):continue
 for bits in rows:
  env=dict(zip('ABCD',bits));vals=[evaluate(e,env) for e in expr.split('=')];check(len(set(vals))==1,expr)
# Table rows: input/output bits, including every basic-gate truth table.
tables=re.findall(r'\\begin\{tabular\}\{[^\n]+\}(.*?)\\end\{tabular\}',s,re.S)
basic=[lambda a:not a,lambda a:a,lambda a,b:a and b,lambda a,b:a or b,lambda a,b:not(a and b),lambda a,b:not(a or b),lambda a,b:a!=b,lambda a,b:a==b]
bit_tables=[]
for t in tables:
 vals=[]
 for line in t.splitlines():
  if re.match(r'^\s*[01]\s*&',line):vals.append([int(x.strip()) for x in line.split(r'\\')[0].split('&')])
 if vals:bit_tables.append(vals)
check(len(bit_tables)==10,'every numeric truth table accounted for')
for f,t in zip(basic,bit_tables[:8]):
 for row in t:check(f(*row[:-1])==row[-1],row)
for row in bit_tables[8]:check(expect(2,dict(zip('ABCD',row[:4])))==row[-1],row)
for row in bit_tables[9]:check((2*row[0]+row[1])*(2*row[2]+row[3])==sum(v*2**(3-i) for i,v in enumerate(row[4:])),row)
# Every K-map, its min/maxterms and its drawn implicants.
kmaps=list(re.finditer(r'\\begin\{karnaugh-map\}.*?\\end\{karnaugh-map\}',s,re.S))
for m in kmaps:
 body=m.group();task=int(re.findall(r'\\subsection\{Zadatak ([1-6])\}',s[:m.start()])[-1])
 one=set(map(int,re.search(r'\\minterms\{([^}]+)\}',body).group(1).split(',')));zero=set(map(int,re.search(r'\\maxterms\{([^}]+)\}',body).group(1).split(',')))
 check(one|zero==set(range(16)) and not(one&zero))
 if task!=3:check(one=={i for i,b in enumerate(rows) if expect(task,dict(zip('ABCD',b)))})
 else:
  # Figure caption immediately following the map identifies C3..C0.
  idx=int(re.search(r'\\caption\{Karnoova mapa za \$C_([0-3])',s[m.end():]).group(1));check(one=={i for i,b in enumerate(rows) if (((2*b[0]+b[1])*(2*b[2]+b[3]))>>idx)&1})
 groups=[kmap_rect(int(a),int(b)) for a,b in re.findall(r'\\implicant\{(\d+)\}\{(\d+)\}',body)]
 groups += [kmap_rect(int(a),int(b))|kmap_rect(int(c),int(d)) for a,b,c,d in re.findall(r'\\implicantedge\{(\d+)\}\{(\d+)\}\{(\d+)\}\{(\d+)\}',body)]
 for group in groups:
  check(len(group) in [1,2,4,8,16] and (group<=one or group<=zero),('Kmap group',task,group))
  # A valid implicant is a Boolean cube, including wrap-around groups.
  varying=(max(group)^min(group)).bit_count();check(len(group)==2**varying,group)
 if groups:
  target=one if groups[0]<=one else zero
  check(set.union(*groups)==target,('uncovered map cells',task))
# Legacy drawings have free-ended wires: a manual trace is bound to the exact XML hash.
review=json.loads((ROOT/'code/pregled_sema.json').read_text())
check(len(review['schematics'])==6,'all six solution schematics must be reviewed')
for name,record in review['schematics'].items():
 file=ROOT/name
 task=int(file.parent.name.split('_')[-1])
 for bits in rows:
  env=dict(zip(['A1','A0','B1','B0'] if task==3 else 'ABCD',bits));actual=reviewed_schematic(file,env,record)
  if task==3:check(sum(actual[f'C{i}']*2**i for i in range(4))==(2*bits[0]+bits[1])*(2*bits[2]+bits[3]),file)
  else:check(actual['Z' if task==2 else 'Y']==expect(task,env),(file,bits))
# Preserve the user's original arrow positions and two differently colored directions.
raw=(ROOT/'01_kombinacione_hazardi.tex').read_text()
for label,digest in review['original_arrow_figures'].items():
 block=next(m.group() for m in re.finditer(r'\\begin\{figure\}.*?\\end\{figure\}',raw,re.S) if r'\label{'+label+'}' in m.group())
 check(hashlib.sha256(block.encode()).hexdigest()==digest,('original arrow layout changed',label))
# Hazard criteria independently derived from terms; enumerate every single-input edge.
for task,label,want in [(4,'eq:zad4',[(14,15)]),(5,'eq:zad5',[(1,3),(4,6),(5,7),(6,7),(14,15)]),(5,'eq:zad5-min',[(1,3),(4,6),(5,7)]),(5,'eq:zad5-fin',[]),(4,'eq:zad4_2',[])]:
 block=next(m.group(1) for m in re.finditer(r'\\begin\{equation\}(.*?)\\end\{equation\}',s,re.S) if r'\label{'+label+'}' in m.group(1));expr=clean(block).split('=')[-1]
 terms=[{i for i,b in enumerate(rows) if evaluate(term,dict(zip('ABCD',b)))} for term in expr.split('+')]
 check(hazards(terms,[expect(task,dict(zip('ABCD',b))) for b in rows])==want,label)
# Homework feasibility only; no new student-facing solutions.
check(max(a*a+b*b for a in range(4) for b in range(4)).bit_length()==5)
check(max(i.bit_count() for i in range(16)).bit_length()==3)
count+=check01(ROOT)
print(f'01: {count} uspešnih provera stvarnih formula, tabela, karata, Draw.io veza i VHDL-a.')
