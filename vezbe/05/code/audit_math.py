"""Provere podataka pročitanih iz dokumenta i stvarnih TikZ dijagrama."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from collections import deque
import re,json,hashlib

def run(root,check,data):
 tex=(root/'05_kodovi.tex').read_text()
 blocks={int(n):s for n,s in re.findall(r'% Izvor DOCX: blok (\d+)\n(.*?)(?=% Izvor DOCX: blok |\\end\{document\})',tex,re.S)}
 def tables(block):
  return re.findall(r'\\begin\{tabular\}\{[^}]+\}(.*?)\\end\{tabular\}',blocks[block],re.S)
 def rows(table):
  return [line.strip().removesuffix(r'\\').strip() for line in table.splitlines() if '&' in line and line.rstrip().endswith(r'\\')]
 def plain(cell):
  for cmd in ['mathtt','texttt']:
   cell=re.sub(r'\\'+cmd+r'\{([^{}]*)\}',r'\1',cell)
  return cell.replace('$','').strip()
 def gd(bits):
  b=0;out=''
  for v in bits:b^=int(v);out+=str(b)
  return out
 def dist(a,b):
  assert len(a)==len(b)
  return sum(x!=y for x,y in zip(a,b))
 def marked_bits(word):
  tokens=re.findall(r'\\istaknutbit\{[01]\}|[01]',word)
  check(''.join(tokens)==word,'complete highlighted bit string')
  return ''.join(t[-2] if t.startswith('\\') else t for t in tokens),{i for i,t in enumerate(tokens) if t.startswith('\\')}
 actual={}
 for block,key in [(30,'BCD'),(35,'BCD2421'),(42,'Više 3'),(61,'Grej BCD')]:
  entries=re.findall(r'(\d) & \$\\mathtt\{([01]{4})\}',tables(block)[0]);check(len(entries)==10,'code table row count')
  actual[key]=[v for _,v in entries];check([int(i) for i,_ in entries]==list(range(10)),'digit order')
  check(actual[key]==data['codes'][key],f'actual code table {key}')
  for d,word in entries:
   d=int(d)
   if key=='BCD':check(int(word,2)==d,'BCD weight')
   elif key=='BCD2421':check(sum(w*int(b) for w,b in zip((2,4,2,1),word))==d,'2421 weight')
   elif key=='Više 3':check(int(word,2)==d+3,'excess weight')
   if key in ('BCD2421','Više 3'):check(int(word,2)^int(actual[key][9-d],2)==15,'complement pair')
  if key=='Grej BCD':
   for i in range(10):check(dist(actual[key][i],actual[key][(i+1)%10])==1,'decimal Gray cycle')
 # Construction table: actual columns, all four stages; symmetry vs complement.
 tabs=tables(50);check(len(tabs)==4,'four Gray stages')
 for n,table in enumerate(tabs,1):
  entries=[]
  for row in rows(table):
   if not re.match(r'^\d+ &',row):continue
   cols=row.split('&');i=int(cols[0]);word=''.join(re.findall(r'\\texttt\{([01]+)\}',row))
   check(word==format(i^(i>>1),f'0{n}b'),f'Gray construction n={n}, row={i}')
   if n>1:check(('downarrow' if i<2**(n-1) else 'uparrow') in cols[3],'reflection arrows')
   entries.append(word)
  check(len(entries)==2**n,'Gray count')
  for a,b in zip(entries,entries[1:]+entries[:1]):check(dist(a,b)==1,'Gray adjacency including wrap')
  if n>1:check([w[1:] for w in entries[:2**(n-1)]]==[w[1:] for w in reversed(entries[2**(n-1):])],'lower-bit reflection')
 # Generic conversion recurrences, checked for all words through width 10.
 for n in range(1,11):
  for x in range(2**n):
   b=format(x,f'0{n}b');g=b[0]+''.join(str(int(a)^int(c)) for a,c in zip(b,b[1:]))
   check(int(g,2)==x^(x>>1) and gd(g)==b,'Gray inverse')
 # All 14 explicitly listed distances plus the introductory example.
 distances=re.findall(r'd\(([^,]+),([^()]+)\)=(\d+)',blocks[73]);check(len(distances)==14,'distance table count')
 for left,right,d in distances:
  a,ma=marked_bits(left);b,mb=marked_bits(right)
  check(len(a)==len(b)==4 and dist(a,b)==int(d),'actual distance table')
  check(ma==mb=={i for i,(x,y) in enumerate(zip(a,b)) if x!=y},'highlight exactly differing bits in both words')
 check(dist('0110110','0110010')==1,'intro distance')
 for block,a,b,d in [(128,'100','101',1),(129,'110','011',2),(130,'011','100',3)]:
  left,right,result=re.fullmatch(r'(.+?) : (.+?) \\ensuremath\{\\to\} H\\textsubscript\{d\} = (\d+)\s*',blocks[block]).groups()
  x,mx=marked_bits(left);y,my=marked_bits(right)
  check((x,y,int(result))==(a,b,d) and dist(x,y)==d,'actual task distance')
  check(mx==my=={i for i,(u,v) in enumerate(zip(x,y)) if u!=v},'task distance emphasis')
 # Tables of parity, no fixture substring matching.
 for block,size in [(81,8),(147,4)]:
  table=tables(block)[0]
  if block==81:
   marked_rows=[row.split('&') for row in rows(table) if re.match(r'^[01]+ &',row)]
   for cells in marked_rows:
    words=[marked_bits(cell.strip()) for cell in cells]
    check(words[0][1]==set() and words[1][1]==words[2][1]=={3},'only appended parity bits highlighted')
   table=re.sub(r'\\istaknutbit\{([01])\}',r'\1',table)
  entries=re.findall(r'^([01]+) & ([01]+) & ([01]+)',table,re.M);check(len(entries)==size,'parity rows')
  for b,e,o in entries:check(e==b+str(b.count('1')%2) and o==b+str(1-b.count('1')%2),'actual parity row')
 # Positions/roles and all parity-check groups in the four construction layouts.
 for block in (93,95,97,99):
  tab=tables(block)[0];rs=rows(tab);pos=[int(v.strip()) for v in rs[0].split('&')]
  check(pos==list(range(15,0,-1)),'Hamming position order')
  vals=rs[1].split('&');check([v.strip() for v in vals]==[format(i,'04b') for i in pos],'Hamming position binary')
  if block!=93:
   roles=[v.strip() for v in rs[2].split('&')];j=10
   for p,v in zip(pos,roles):
    if block==99:
     mark=re.fullmatch(r'(?:\\cellcolor\{[^{}]+\})?\\tikzmarknode\[inner sep=0pt\]\{hamming-(\d+)\}\{\\strut ([CD]\\textsubscript\{\d+\})\}',v)
     check(mark is not None and int(mark[1])==p,'arrow anchor matches position');v=mark[2]
    if p&(p-1)==0:want=f'C\\textsubscript{{{p}}}'
    elif block==95:want=''
    else:want=f'D\\textsubscript{{{j}}}';j-=1
    check(v==want,'Hamming data/check placement')
 groups={int(p):[int(v.strip()) for v in vals.split(',')] for p,vals in re.findall(r'\$c_(\d)\$ & ([\d, ]+)',tables(99)[1])}
 check(set(groups)=={1,2,4,8},'four parity groups')
 for p,positions in groups.items():check(positions==[i for i in range(1,16) if i&p],'actual parity-check membership')
 arrows={int(p):list(map(int,targets.split(','))) for p,targets in re.findall(r'^\s*([1248])/[-\d.]+/[-\d.]+/[^/]+/\{([\d,]+)\}',blocks[99],re.M)}
 check(set(arrows)==set(groups),'all four control groups have arrows')
 for p,targets in arrows.items():check(targets==[i for i in groups[p] if i!=p],'arrow targets match the parity group')
 # Exact table cells for encoded/decode outputs; independent fixtures checked by provera.py too.
 enc=[line for line in rows(tables(112)[0]) if re.match(r'^\d+ &',line)]
 check(len(enc)==5,'encoding count')
 assigned=list(map(int,re.findall(r'\d+',blocks[106])))
 check(assigned==[rec['number'] for rec in data['encodings']],'encoding operands agree with the task')
 for line,record in zip(enc,data['encodings']):
  cells=[plain(v) for v in line.split('&')];check(int(cells[0])==record['number'],'source decimal operand')
  check(cells[1:5]==record['values'],'actual decimal code row')
  steps=re.fullmatch(r'([01]{6})_2\\;\\to\\;([01]{6})_\{\\mathrm\{G\}\}',cells[5])
  check(steps is not None,'binary-to-Gray conversion has both steps')
  binary,gray=steps.groups();number=int(binary,2)
  check(number==record['number'] and gray==record['gray'] and int(gray,2)==number^(number>>1),'actual binary-to-Gray conversion')
  for key,word in zip(actual,cells[1:5]):check(''.join(actual[key][int(d)] for d in str(record['number']))==word.replace(' ',''),'encoding digits')
 dec=[line for line in rows(tables(114)[0]) if re.match(r'^[01]+\.',line)]
 check(len(dec)==3,'decode count')
 for line,rec in zip(dec,data['decodings']):
  cells=[plain(v) for v in line.split('&')];check(cells[0]==rec['bits'],'source encoded operand')
  check(cells[1:5]==[v if v is not None else '--' for v in rec['values']],'actual decoding table')
  values=re.fullmatch(r'([01]+\.[01]+)_2=([\d.]+)_\{10\}',cells[5]);check(values is not None,'decoded fixed point syntax')
  a,b=cells[0].split('.');decoded=gd(a+b)
  check(values[1].replace('.','')==decoded and len(values[1].split('.')[1])==len(b),'Gray binary fixed point')
  check(F(values[2])==F(int(decoded,2),2**len(b)),'Gray exact decimal')
 # Written BCD additions: parse every digit, blank, operator and carried suffix.
 arrays=re.findall(r'\\begin\{array\}\{r\*\{(\d+)\}\{c\}@\{\}c@\{\}l\}(.*?)\\end\{array\}',blocks[121],re.S)
 check(len(arrays)==len(data['additions'])==4,'all four written additions')
 assigned=[tuple(map(int,pair)) for pair in re.findall(r'(\d+)\s*\+\s*(\d+)',blocks[118])]
 check(assigned==[(v['a'],v['b']) for v in data['additions']],'addition task operands')
 def packed_decimal(x,n):
  return sum((x//10**i%10)*16**i for i in range(n))
 for idx,((width,body),rec) in enumerate(zip(arrays,data['additions']),1):
  width=int(width);n=max(len(str(rec['a'])),len(str(rec['b'])));check(width==4*n+1,'written digit width')
  stages=re.findall(r'% BCD korak (\d+)\n(.*?)(?=% BCD korak |\Z)',body,re.S)
  check([int(i) for i,_ in stages]==list(range(n)),'all decimal positions shown')
  carry=0;lower=0;out=0
  for i,(_,stage) in enumerate(stages):
   shown=[]
   for line in rows(stage):
    cols=[v.strip() for v in line.split('&')];check(len(cols)==width+3 and cols[-2]=='','aligned digit columns and empty spacer')
    digits=cols[1:-2];clean=[re.sub(r'\\istaknutbit\{([01])\}',r'\1',v) for v in digits]
    check(all(v in ('','0','1') for v in clean),'literal written bits')
    value=int(''.join(v or '0' for v in clean),2);occupied={j for j,v in enumerate(clean) if v}
    marked={j for j,v in enumerate(digits) if v.startswith(r'\istaknutbit')}
    shown.append((cols[0],value,occupied,cols[-1],marked))
   a=rec['a']//10**i%10;b=rec['b']//10**i%10;t=a+b+carry;corr=6 if t>9 else 0;co,digit=divmod(t+corr,16)
   check(len(shown)==3+bool(carry)+2*bool(corr),'all operand, carry, sum and correction rows')
   nibble=set(range(width-4*(i+1),width-4*i));suffix=set(range(width-(5+4*i),width))
   for k,operand in enumerate((rec['a'],rec['b'])):
    op,value,occupied,note,marked=shown[k]
    expected=packed_decimal(operand,n) if i==0 else (operand//10**i%10)*16**i
    check(op==('' if k==0 else '+') and value==expected,'actual aligned operand')
    check(occupied==(set(range(1,width)) if i==0 else nibble) and not marked,'operand width and position')
   check(shown[0][3]==f'i={i}:'+r'\ \text{prvi sabirak}','decimal position annotation')
   q=2
   if carry:
    op,value,occupied,note,marked=shown[q];q+=1
    check(op=='+' and value==16**i and occupied==marked=={width-4*i-1},'explicit input carry position')
    check(note==r'\text{Ulazni prenos }c_'+str(i)+'=1','input carry annotation')
   op,value,occupied,note,marked=shown[q]
   check(op=='' and value==t*16**i+lower and occupied==suffix and not marked,'actual uncorrected sum with completed low digits')
   check(note==(r'\text{Binarni zbir; potrebna korekcija}' if corr else r'\text{Nema korekcije; }c_'+str(i+1)+'=0'),'correction decision annotation')
   check(len(re.findall(r'\\cline\{\d+-\d+\}',stage))==1+bool(corr),'written addition rules')
   if corr:
    op,value,occupied,note,marked=shown[q+1]
    check(op=='+' and value==6*16**i and occupied==marked==nibble,'actual aligned 0110 correction')
    op,value,occupied,note,marked=shown[q+2]
    check(op=='' and value==(t+6)*16**i+lower and occupied==suffix and not marked,'actual corrected sum with carry')
    check(note==r'\text{Korigovana cifra; }c_'+str(i+1)+'=1','output carry annotation')
   out+=digit*10**i;lower+=digit*16**i;carry=co
  out+=carry*10**n;check(out==rec['a']+rec['b'],'BCD reconstructed result')
  eq=re.search(r'\\label\{eq:bcd-zbir-'+str(idx)+r'\}(.*?)\\end\{equation\}',blocks[121],re.S)[1]
  a,b,c=map(int,re.match(r'\s*(\d+)\+(\d+)=(\d+)',eq).groups());word=re.search(r'\\mathtt\{(.*?)\}',eq)[1].replace(r'\,','')
  check((a,b,c)==(rec['a'],rec['b'],out) and word==''.join(actual['BCD'][int(d)] for d in str(out)),'BCD final equation')
 # Every neighbour: changed bit, code membership and the displayed decoding steps.
 tabs=tables(132);check(len(tabs)==len(data['neighbors'])==5,'all five neighbour tables')
 starts=re.findall(r'\\textbf\{([^}]+)\}: (.*?)\.\\par',blocks[132]);check(len(starts)==5,'all starting words')
 for table,(key,rec),(title,initial) in zip(tabs,data['neighbors'].items(),starts):
  check(title==key,'neighbour code title')
  if key=='Grej binarni':
   check(initial==r'$23_{10}=10111_2\to\mathtt{11100}_{\mathrm{G}}$' and gd(rec['start'])=='10111','Gray encoding of 23')
  else:
   initial_bits=re.search(r'\\mathtt\{([^}]+)\}',initial)[1].replace(r'\,','')
   check(initial_bits==rec['start']==actual[key][2]+actual[key][3],'actual decimal code of 23')
  entries=[r for r in rows(table) if re.match(r'^\d+ &',r)];check(len(entries)==len(rec['start']),'neighbour row count')
  seen=set()
  for row in entries:
   bit,word,step=[v.strip() for v in row.split('&')];bit=int(bit)
   marked=re.fullmatch(r'\$\\mathtt\{(.*?)\}(?:_\{\\mathrm\{G\}\})?\$',word)[1]
   w,marks=marked_bits(marked.replace(r'\,',''));seen.add(w)
   check(dist(w,rec['start'])==1 and marks=={len(w)-1-bit}=={i for i,(x,y) in enumerate(zip(w,rec['start'])) if x!=y},'actual flipped bit and emphasis')
   if key=='Grej binarni':
    binary,decimal=re.fullmatch(r'\$\\to([01]{5})_2=(\d+)_\{10\}\$',step).groups()
    check(binary==gd(w) and int(decimal)==int(binary,2),'Gray to binary to decimal steps')
   else:
    valid=all(part in actual[key] for part in (w[:4],w[4:]))
    if valid:
     a,da,b,db,value=re.fullmatch(r'\$\\mathtt\{([01]{4})\}\\to(\d),\\;\\mathtt\{([01]{4})\}\\to(\d)\\;\\Rightarrow (\d{2})\$',step).groups()
     check(a+b==w and actual[key][int(da)]==a and actual[key][int(db)]==b and value==da+db,'both decimal digit decoding steps')
    else:
     invalid=re.fullmatch(r'Nedozvoljena reč: \$\\mathtt\{([01]{4})\}\$ nije kod cifre',step)[1]
     check(invalid in (w[:4],w[4:]) and invalid not in actual[key],'specific forbidden nibble')
  check(len(seen)==len(rec['start']),'each neighbour unique')
 # Syndromes: parse the actual symbol groups, received bits and each shown XOR.
 word=re.search(r'=([01]{7})',blocks[150])[1];bits={p:int(v) for p,v in enumerate(reversed(word),1)}
 for p,terms,values,out in re.findall(r's_(\d)&=(.*?)=([01](?:\\oplus[01])*)=([01])',blocks[153]):
  p=int(p);positions=[int(v) for v in re.findall(r'[cd]_(\d)',terms)];check(set(positions)==set(groups[p])&set(range(1,8)),'syndrome symbolic group')
  shown=list(map(int,values.split(r'\oplus')));check(shown==[bits[v] for v in positions] and sum(shown)%2==int(out),'actual syndrome XOR')
 syndrome=0
 for p,b in bits.items():syndrome^=p*b
 position=int(re.search(r'poziciji (\d+)',blocks[154])[1]);fixed=re.search(r'ispravljena reč \$([01]+)\$',blocks[154])[1]
 check(position==syndrome==5 and int(fixed,2)==int(word,2)^(1<<(position-1)),'actual correction')
 check(fixed+str(fixed.count('1')%2)==re.sub(r'\\textbf\{([01])\}',r'\1',blocks[159]).strip().splitlines()[0],'extended example')
 # Exhaustive error masks verify guarantees and failures beyond them, all messages (7,4),(8,4).
 def enc(msg,r):
  n=2**r-1;v=[0]*(n+1);positions=[i for i in range(1,n+1) if i&(i-1)]
  for p,b in zip(positions,msg):v[p]=b
  for k in range(r):p=2**k;v[p]=sum(v[j] for j in range(1,n+1) if j&p)%2
  return sum(v[p]<<(p-1) for p in range(1,n+1))
 def syn(w):
  s=0
  for p in range(1,w.bit_length()+1):
   if w>>(p-1)&1:s^=p
  return s
 for msg in product(range(2),repeat=4):
  w=enc(msg,3);ext=(w<<1)|(w.bit_count()%2)
  for mask in range(128):
   damaged=w^mask;s=syn(damaged);weight=mask.bit_count()
   check((s==0)==(syn(mask)==0),'H7 linear syndrome')
   if weight<=1:check((damaged^(1<<(s-1)) if s else damaged)==w,'H7 correct single')
   if weight in (1,2):check(s!=0,'H7 detect only up to two')
  for mask in range(256):
   received=ext^mask;weight=mask.bit_count();s=syn(received>>1);p=received.bit_count()%2
   if weight==0:check(s==0 and p==0,'SECDED no error')
   elif weight==1:check(p==1 and received^(1<<s if s else 1)==ext,'SECDED correct single')
   elif weight==2:check(p==0 and s!=0,'SECDED reject double')
   elif weight==3:check(p==1 and (received^(1<<s if s else 1))!=ext,'SECDED triples can miscorrect')
 # Fifteen-position construction shown in theory: all 2048 messages and all single/double errors.
 for msg in product(range(2),repeat=11):
  w=enc(msg,4);check(syn(w)==0,'H15 codeword')
  for p in range(1,16):check(syn(w^(1<<(p-1)))==p,'H15 single error')
  for p,q in combinations(range(1,16),2):check(syn(w^(1<<(p-1))^(1<<(q-1)))==p^q!=0,'H15 double error detection')
 # Cube completeness AND shortest-path metric, from actual coordinates/edges/labels.
 cube=(root/'Images/Uvod/kocke.tex').read_text()
 for prefix,n in [('a',1),('b',2),('c',3)]:
  vertices=re.findall(r'\\coordinate \('+prefix+r'([01]+)\)',cube);edges=re.findall(r'\('+prefix+r'([01]+)\)--\('+prefix+r'([01]+)\)',cube)
  check(set(vertices)=={format(i,f'0{n}b') for i in range(2**n)} and len(vertices)==2**n,'actual cube vertices')
  want={frozenset((a,b)) for a,b in combinations(vertices,2) if dist(a,b)==1}
  check({frozenset(e) for e in edges}==want and len(edges)==len(want),'cube edge set')
  graph={v:set() for v in vertices}
  for a,b in edges:graph[a].add(b);graph[b].add(a)
  for start in vertices:
   ds={start:0};queue=deque([start])
   while queue:
    for v in graph[queue.popleft()]:
     if v not in ds:ds[v]=min(ds[u]+1 for u in graph[v] if u in ds);queue.append(v)
   for v in vertices:check(ds[v]==dist(start,v),'cube shortest path')
 # Numeric geometry of actual Venn circles: each label must be in exactly its check groups.
 for name in ['Uvod/ven','Zadatak_6/ven']:
  s=(root/f'Images/{name}.tex').read_text()
  circles=[tuple(map(F,m)) for m in re.findall(r'\\draw\[(?:blue!70!black|teal!80!black|orange!80!black)\]\(([-\d.]+),([-\d.]+)\)circle\(([-\d.]+)\)',s)]
  nodes=re.findall(r'\\node at\(([-\d.]+),([-\d.]+)\)\{\$[cd]_(\d)\$\}',s);check(len(circles)==3 and len(nodes)==7,'Venn content')
  for x,y,p in nodes:
   x,y,p=F(x),F(y),int(p)
   for group,(cx,cy,r) in zip([1,2,4],circles):check(((x-cx)**2+(y-cy)**2<r*r)==bool(p&group),'Venn membership')
  if name.startswith('Zadatak'):
   cx,cy,r=map(F,re.search(r'\\draw\[red,very thick\]\(([-\d.]+),([-\d.]+)\)circle\(([-\d.]+)\)',s).groups())
   check([int(p) for x,y,p in nodes if (F(x)-cx)**2+(F(y)-cy)**2<r*r]==[5],'Venn highlighted error')
 # Manual review hashes bind unparsed general formulas and the communication diagram.
 reviewed=json.loads((root/'code/pregled_izvora.json').read_text())
 for name,rec in reviewed['figures'].items():check(hashlib.sha256((root/name).read_bytes()).hexdigest()==rec['sha256'],f'{name}: repeat manual diagram review')
 eqs=re.findall(r'\\begin\{equation\}(.*?)\\end\{equation\}',tex,re.S);check(len(eqs)==len(reviewed['equations']),'equation inventory')
 for eq in eqs:
  label=re.search(r'\\label\{([^}]+)\}',eq)[1];check(hashlib.sha256(eq.encode()).hexdigest()==reviewed['equations'][label]['sha256'],f'{label}: repeat proof review')
