#!/usr/bin/env python3
"""Check displayed mathematics, tables/maps, reviewed drawings and real VHDL.
Manual drawing traces are bound to their exact source hashes, never inferred
from the mere presence of numbers in TeX.
"""
from pathlib import Path
import hashlib,itertools,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'PROVERA'))
from logic import evaluate,clean,uncomment,kmap_rect,hazards
from vhdl02 import check02
s=uncomment(next(ROOT.glob('*.tex')).read_text());count=0;proof=[]
def check(value,msg=''):
 global count
 if not value:raise AssertionError(msg)
 count+=1
segs=['1111110','0110000','1101101','1111001','0110011','1011011','1011111','1110000','1111111','1111011']+['1001111']*6
blocks={re.search(r'\\label\{([^}]+)\}',m.group(1)).group(1):m.group(1) for m in re.finditer(r'\\begin\{equation\}(.*?)\\end\{equation\}',s,re.S) if r'\label{' in m.group(1)}
def task2(i):return bool(i&4 and i&2 or not(i&2) and i&1)
def task3(i):return i not in [0,2,7]
# Every form of each Boolean equation is evaluated from the actual TeX.
for label,b in blocks.items():
 if label.startswith('eq:zad4-'):
  for i in range(10 if label.startswith('eq:zad4-b') else 16):
   env=dict(zip('DCBA',map(int,f'{i:04b}')));target=None
   for line in re.split(r'\\\\(?:\[[^]]*\])?',b):
    e=clean(line).strip()
    if not e:continue
    chunks=e.split('=');lhs=chunks[0].strip()
    if lhs:target=lhs;want=int(segs[i]['abcdefg'.index(target)]);env[target]=want
    for exp in chunks[1:]:check(evaluate(exp,env)==want,(label,i,exp,want))
 elif label in ['eq:zad2','eq:zad2-a1','eq:zad2-b1','eq:zad2-b2','eq:zad2-d1','eq:zad3','eq:zad3-c1','eq:zad3-c2']:
  for i in range(8):
   env=dict(zip('CBA',map(int,f'{i:03b}')));want=task2(i) if label.startswith('eq:zad2') else task3(i)
   env.update(Y=want,Y0=i==0,Y2=i==2,Y7=i==7)
   for exp in clean(b).split('=')[1:]:check(evaluate(exp,env)==want,(label,i,exp))
 elif label=='eq:zad2-a2':
  for a,b,c in itertools.product(range(2),repeat=3):
   rhs=re.search(r'Y\('+str(a)+','+str(b)+r',C\)\s*&=\s*([^\\\n]+)',blocks[label]).group(1)
   check(evaluate(rhs,{'C':c})==task2(4*c+2*b+a),label)
 elif label=='eq:zad3-a1':
  for exp in clean(b).splitlines():
   if '=' not in exp:continue
   lhs,rhs=exp.split('=');index=int(lhs.strip()[1:])
   for i in range(8):check(evaluate(rhs,dict(zip(['A2','A1','A0'],map(int,f'{i:03b}'))))==(index==i),label)
 elif label=='eq:zad1_b':
  for i in range(64):
   bits=list(map(int,f'{i:06b}'));env=dict(zip(['S1','S0','D3','D2','D1','D0'],bits))
   check(evaluate(clean(b).split('=')[1],env)==env['D'+str(2*bits[0]+bits[1])],label)
 elif label in ['eq:zad1_1','eq:zad1_2']:
  for a,b in itertools.product(range(2),repeat=2):
   vals=[evaluate(e,{'A':a,'B':b}) for e in clean(blocks[label]).split('=')];check(len(set(vals))==1,label)
 elif label in ['eq:error','eq:lzout']:
  expr=blocks[label].split('=')[1].replace('LZ_{IN}','L');expr=re.sub(r'\\end\{[^}]+\}','',expr)
  for i,l in itertools.product(range(16),range(2)):
   env=dict(zip('DCBA',map(int,f'{i:04b}')));env['L']=l
   check(evaluate(expr,env)==(i>9 if label=='eq:error' else l and i==0),label)
 elif label=='eq:feedback':
  check('F=I(R+F).' in b,label)
  for raw,I,F in itertools.product(range(2),repeat=3):
   check(evaluate('I(R+F)',{'I':I,'R':raw,'F':F})==bool(I and(raw or F)),label)
 elif label=='eq:zad3-d':
  check('Y_{8i+j}=H_iL_j' in b,label)
  for word in range(64):
   actual=[int(i==word//8 and j==word%8) for i in range(8) for j in range(8)]
   check(sum(actual)==1 and actual[word]==1,label)
 else:raise AssertionError(('Unreviewed displayed equation',label))
# All rows of all five functional tables, read directly, with expected domains.
tables={re.search(r'\\label\{([^}]+)\}',m.group()).group(1):m.group() for m in re.finditer(r'\\begin\{table\}.*?\\end\{table\}',s,re.S)}
for name in ['tab:bcd-7seg-e','tab:bcd-7seg-b','tab:decoder3to8','tab:zad1']:
 rows=[]
 for line in tables[name].splitlines():
  if re.match(r'^\s*[01]+\s*&',line):rows.append([x.strip().strip('$') for x in line.split(r'\\')[0].split('&')])
 check(len(rows)==(16 if '7seg' in name else 8 if 'decoder' in name else 4),name)
 for n,row in enumerate(rows):
  if '7seg' in name:
   check(''.join(row[:4])==f'{n:04b}',name)
   check(''.join(row[4:])==(segs[n] if n<10 or name.endswith('-e') else 'bbbbbbb'),(name,n))
  elif 'decoder' in name:check(row[0]==f'{n:03b}' and int(''.join(row[1:]),2)==1<<n,(name,n))
  else:
   check(row[0]==f'{n:02b}',name)
   for a,b in itertools.product(range(2),repeat=2):
    want=[(a==b,a!=b),(a!=b,a==b),(not a and not b,not a and b),(a and b,a and not b)][n]
    check(tuple(evaluate(expr,dict(A=a,B=b)) for expr in row[1:])==tuple(map(bool,want)),(name,n,a,b))
# All eighteen K-maps: domains, groups, wrap-around, cube property and coverage.
kmaps=list(re.finditer(r'\\begin\{karnaugh-map\}.*?\\end\{karnaugh-map\}',s,re.S))
check(len(kmaps)==18,'K-map inventory changed')
for m in kmaps:
 b=m.group();task=int(re.findall(r'\\subsection\{Zadatak ([1-4])\}',s[:m.start()])[-1]);one=set(map(int,re.search(r'\\minterms\{([^}]+)\}',b).group(1).split(',')));zero=set(map(int,re.search(r'\\maxterms\{([^}]+)\}',b).group(1).split(',')))
 dc=set(map(int,re.search(r'\\terms\{([^}]+)\}',b).group(1).split(','))) if r'\terms{' in b else set()
 domain=set(range(16 if task==4 else 8));check(one|zero|dc==domain and not(one&zero or dc&one or dc&zero),'map domain')
 groups=[kmap_rect(int(a),int(z)) for a,z in re.findall(r'\\implicant\{(\d+)\}\{(\d+)\}',b)]
 groups += [kmap_rect(int(a),int(z))|kmap_rect(int(c),int(d)) for a,z,c,d in re.findall(r'\\implicantedge\{(\d+)\}\{(\d+)\}\{(\d+)\}\{(\d+)\}',b)]
 if r'\implicantcorner' in b:groups.append({0,2,8,10})
 for g in groups:
  check(g<=one|dc or g<=zero|dc,('mixed group',task,g));check(len(g)==2**(max(g)^min(g)).bit_count(),('noncube',g))
 if task==4:
  seg=re.search(r'\\caption\{Segment \$([a-g])',s[m.end():]).group(1);want={i for i in domain if segs[i]['abcdefg'.index(seg)]=='1'}
 else:want={i for i in domain if (task2(i) if task==2 else task3(i))}
 check(one==want-dc,('Kmap values',task))
 check(set.union(*groups)|dc >= (one if groups[0]<=one|dc else zero),('uncovered',task))
 if task==2:check(hazards(groups,[task2(i) for i in range(8)])==([] if len(groups)==3 else [(5,7)]),'hazard adjacency')
# Prove 4 NAND2 gates minimal in an acyclic library, even allowing constants.
initial=tuple(sorted(tuple(sum(((i>>j)&1)<<i for i in range(8)) for j in range(3))+(0,255)))
target=sum(task2(i)<<i for i in range(8));states={initial}
for depth in range(1,4):
 nxt=set()
 for state in states:
  for a,b in itertools.combinations_with_replacement(state,2):
   z=255^(a&b);check(z!=target,('smaller NAND network',depth))
   if z not in state:nxt.add(tuple(sorted(state+(z,))))
 states=nxt
# Every four-digit input; evaluate the drawn feedback after the stated reset.
def cascade(digits):
 raw=any(d>9 for d in digits);F=False # INIT low clears the feedback
 F=raw or F # INIT high with stable data
 effective=digits[:-1]+[digits[-1]|(12 if F else 0)]
 out=[];lz=True
 for k,d in enumerate(effective):
  incoming=lz if k<3 else False
  lz=incoming and d==0;off=(F if k<3 else False)or lz
  out.append('' if off else str(d) if d<10 else 'E')
 return ''.join(out)
for digits in itertools.product(range(16),repeat=4):
 expected='E' if any(d>9 for d in digits) else str(sum(d*10**(3-j) for j,d in enumerate(digits)))
 check(cascade(list(digits))==expected,('cascade',digits))
# Both feedback histories: removing an error alone need not clear it.
for prior,raw,init in itertools.product(range(2),repeat=3):
 F=bool(init and(raw or prior));check(not init and not F or init and F==bool(raw or prior))
for text,want in re.findall(r'^\s*([0-9A-F]{4})\s*&\s*([0-9E]+)',tables['tab:bcd-konvertor'],re.M):check(cascade([int(x,16) for x in text])==want,'display example')
# Homework: check feasibility and all selector choices privately, without adding solutions.
# A 13-input decoder is feasible in four AND2 levels (inverters excluded).
# Truth masks independently represent all 8192 input words; each balanced tree
# must select exactly its own word, not merely count input or output bits.
fullmask=(1<<8192)-1
variables=[sum(((i>>j)&1)<<i for i in range(8192)) for j in range(13)]
for word in range(8192):
 terms=[(mask if word>>j&1 else fullmask^mask,0) for j,mask in enumerate(variables)]
 while len(terms)>1:
  terms=[(terms[k][0]&terms[k+1][0],1+max(terms[k][1],terms[k+1][1])) if k+1<len(terms) else terms[k] for k in range(0,len(terms),2)]
 check(terms[0]==(1<<word,4),'balanced 13-input decoder')
check((13-1).bit_length()==4,'13-input balanced AND depth')
goals={}
for pair in ['DC','BA','DB','CA']:
 expr=re.findall(r'\\begin\{equation\}(.*?)\\end\{equation\}',s[s.index(r'\section{Zadaci za samostalni rad}'):],re.S)[0].split('=')[1]
 envs=[dict(zip('DCBA',map(int,f'{i:04b}'))) for i in range(16)]
 cofactors={sel:{tuple(e[k] for k in 'DCBA' if k not in pair):evaluate(expr,e) for e in envs if tuple(e[k] for k in pair)==sel} for sel in itertools.product(range(2),repeat=2)}
 for e in envs:check(cofactors[tuple(e[k] for k in pair)][tuple(e[k] for k in 'DCBA' if k not in pair)]==bool(not e['D'] and e['C'] and not e['A'] or not e['B'] and e['A'] or not e['C'] and e['A']),('homework cofactor',pair,e))
 goals[pair]={sum(v<<i for i,v in enumerate(cf.values())) for cf in cofactors.values()}
 proof.append(dict(homework_select=pair,cofactors={''.join(map(str,k)):list(v.values()) for k,v in cofactors.items()}))
# Exact minimum for each homework selector, under the explicitly chosen
# NOT/AND/OR library, arbitrary fan-in, shared subexpressions and free constants.
states={frozenset([0,15,12,10])};minima={}
for depth in range(6):
 for pair,goal in goals.items():
  if pair not in minima and any(goal<=state for state in states):minima[pair]=depth
 if len(minima)==4:break
 nxt=set()
 for state in states:
  candidates={15^x for x in state}
  for width in range(2,len(state)+1):
   for args in itertools.combinations(state,width):
    a,o=15,0
    for x in args:a&=x;o|=x
    candidates.update([a,o])
  for out in candidates-state:nxt.add(state|{out})
 states=nxt
check(minima=={'CA':2,'DC':3,'BA':3,'DB':5},('homework minimal library costs',minima))
proof.append(dict(homework_minima=minima,library='NOT, arbitrary-fan-in AND/OR; constants and wires free'))
# Drawings use free-ended lines: manual evidence must match the exact editable source.
review=json.loads((ROOT/'code/pregled_sema.json').read_text())
for name,record in review['figures'].items():
 check(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==record['sha256'],('repeat manual diagram review',name))
 for env,wants in record.get('cases',[]):
  actual={key:evaluate(expr,env) for key,expr in record['outputs'].items()}
  check(actual==wants,('drawn net vs specification',name,env,actual,wants))
raw=next(ROOT.glob('*.tex')).read_text()
for label,digest in review['original_arrow_figures'].items():
 block=next(m.group() for m in re.finditer(r'\\begin\{figure\}.*?\\end\{figure\}',raw,re.S) if r'\label{'+label+'}' in m.group())
 check(hashlib.sha256(block.encode()).hexdigest()==digest,('original arrows changed',label))
count+=check02(ROOT)
out=ROOT.parent/'PROVERA/_build';out.mkdir(exist_ok=True);(out/'math02.json').write_text(json.dumps(dict(checks=count,proof=proof),indent=2)+'\n')
print(f'02: {count} uspešnih provera formula, tabela, karata, mreža i VHDL-a.')
