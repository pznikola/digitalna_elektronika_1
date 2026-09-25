"""Bind the displayed rows to independently checked arithmetic; audit actual maps.
Manual circuit traces and non-Boolean mathematics are invalidated by source edits.
"""
from pathlib import Path
from fractions import Fraction as F
import ast,hashlib,itertools,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'PROVERA'))
from logic import evaluate,clean

def run(records):
 s=next(ROOT.glob('04_*.tex')).read_text();checks=0
 def check(ok,msg):
  nonlocal checks
  assert ok,msg;checks+=1
 def block(n):return re.search(r'% Izvor DOCX: blok '+str(n)+r'\n(.*?)(?=% Izvor DOCX:|\\end\{document\})',s,re.S)[1]
 def word(p,r):return int(p.replace('.',''),r)
 def signed(w,r,kind):
  N=len(w.replace('.',''));k=len(w.partition('.')[2]);u=word(w,r);R=r**N
  check(kind!='KMV' or R%2==0 or u!=(R-1)//2,'unused odd-radix KMV word')
  return F(u-(R-(kind=='KMV') if 2*u>=R else 0),r**k)
 def scalar(p):return p.replace('$','').strip()
 seen=[]
 for n,kind,rep,sub in [(70,'unsigned',None,False),(72,'unsigned',None,True),(87,'signed','KO',False),(89,'signed','KO',True),(97,'signed','KMV',False),(99,'signed','KMV',True)]:
  rows=[line for line in block(n).splitlines() if line.startswith('$(')]
  selected=[r for r in records if r['kind']==kind and r.get('rep')==rep and r['sub']==sub]
  check(len(rows)==len(selected),f'block {n} row count')
  for row in rows:
   expr,calc,result=row.split(' & ');terms=re.findall(r'\(([0-9A-F.]+)\)_\{(\d+)\}',expr)
   check(len(terms)==2 and terms[0][1]==terms[1][1],f'block {n} operands')
   a,r=terms[0];b,_=terms[1];r=int(r)
   rec=next(x for x in selected if x['a']==a and x['b']==b and x['base']==r);seen.append(rec)
   context=f'{rep or kind} {a}{"-" if sub else "+"}{b}'
   check(('}-(' in expr)==sub,context+' operation sign')
   lines=re.search(r'\\begin\{array\}\{r\}(.*?)\\end\{array\}',calc)[1].split(r'\\')
   carry=re.search(r'([01]+)$',lines[0])[1]
   check([int(x) for x in reversed(carry)]==rec['carry'],context+' carries')
   u=lines[1];v=lines[2][1:];low=lines[3].replace(r'\hline','').strip()
   check(low==rec['low'],context+' low result')
   check(lines[2][0]==('-' if kind=='unsigned' and sub else '+'),context+' arithmetic operator')
   if kind=='signed':
    check(u==rec['u'] and v==rec['v'],context+' extended/negated words')
    # The original sign, including KMV negative zero, drives extension.
    oldN=len(a.replace('.',''));R=r**oldN;U=word(a,r)
    ext=U+(r**rec['n']-R if 2*U>=R else 0)
    check(word(u,r)==ext,context+' actual sign extension')
    actual=re.match(r'\$([0-9A-F.]+)\$\\newline OF = ([01])',result)
    check(actual is not None and actual[1]==rec['result'] and int(actual[2])==rec['of'],context+' displayed result/OF')
    if rep=='KMV':
     correction=lines[4][1:];final=lines[5].replace(r'\hline','').strip()
     check(word(correction,r)==rec['carry'][-1],context+' circular carry')
     check(word(final,r)==word(low,r)+word(correction,r) and final==rec['result'],context+' after circular carry')
    else:check(len(lines)==4,context+' complete calculation')
   else:
    k=rec['k'];check(F(word(u,r),r**len(u.partition('.')[2]))==F(word(a,r),r**len(a.partition('.')[2])),context+' operand alignment')
    check(F(word(v,r),r**len(v.partition('.')[2]))==F(word(b,r),r**len(b.partition('.')[2])),context+' operand alignment')
    actual=re.search(r'(?:\$|\{r\})(-?[0-9A-F.]+)',result)[1]
    check(actual==rec['result'],context+' displayed result')
    if sub:check(int(re.search(r'b_\{N\}=([01])',result)[1])==rec['carry'][-1],context+' output borrow')
    check((expr.endswith(('-1$' if sub else '+1$')))==bool(rec['cin']),context+' input carry/borrow')
 check(len(seen)==54,'all unsigned/signed examples bound')
 # All ZA operations, with private verification of the three unsolved entries.
 vals={name:(-1 if w[0]=='1' else 1)*int(w[1:],2) for name,w in re.findall(r'([ABCD]) = ([01]{6})',block(76))}
 check(len(vals)==4,'ZA input inventory')
 def calc_expr(t):
  t=re.sub(r'(\d)([ABCD])',r'\1*\2',t)
  def rec(n):
   if isinstance(n,ast.Expression):return rec(n.body)
   if isinstance(n,ast.Name):return vals[n.id]
   if isinstance(n,ast.Constant):return n.value
   if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub):return -rec(n.operand)
   if isinstance(n,ast.BinOp):
    a,b=rec(n.left),rec(n.right)
    return a+b if isinstance(n.op,ast.Add) else a-b if isinstance(n.op,ast.Sub) else a*b if isinstance(n.op,ast.Mult) else None
   raise ValueError(ast.dump(n))
  return rec(ast.parse(t,mode='eval'))
 rows=[l for l in block(79).splitlines() if l.startswith('$')];check(len(rows)==8,'ZA row count')
 for row in rows:
  expr=scalar(row.split(' & ')[0]);v=calc_expr(expr)
  if 'Za samostalni rad' in row:check(-31<=v<=31,'unsolved ZA fits six bits');continue
  rec=next(x for x in records if x['kind']=='sm' and x['expr']==expr)
  w=re.search(r'\$([01]{6})_',row)[1];check(w==rec['result'] and v==rec['value'],'ZA displayed result '+expr)
  arithmetic=re.search(r'\|R\|=([01]+)([+-])([01]+)',row)
  left,right=int(arithmetic[1],2),int(arithmetic[3],2)
  check((left+right if arithmetic[2]=='+' else left-right)==abs(v),'ZA absolute arithmetic '+expr)
  check(('Znak $-$' in row)==(v<0),'ZA displayed sign '+expr)
 # Read the actual written algorithms, including alignment, signs and annotations.
 def written_arrays(table):
  result=[]
  for body in re.findall(r'\\begin\{array\}\[t\][^\n]*\n(.*?)\\end\{array\}',table,re.S):
   rows=[]
   for line in body.splitlines():
    if '&' not in line:continue
    cells=[t.strip() for t in line.split(r'\\')[0].split('&')]
    check(len(cells)==12,'written arithmetic: operator, ten bit places and annotation')
    bits=[re.sub(r'\\cellcolor\{[^}]+\}','',c) for c in cells[1:11]]
    check(all(t in ('','0','1') for t in bits),'written arithmetic bit alphabet')
    rows.append((cells[0],bits,cells[-1],cells[1:11]))
   result.append((rows,body.count(r'\cline{1-11}')))
  return result
 def numeric(bits):return int(''.join(b or '0' for b in bits),2)
 def fullword(row,expected):
  check(row[0]=='' and all(row[1]) and numeric(row[1])==expected%1024,'ten-bit intermediate sum')
 def tables(n):
  return re.findall(r'\\caption\{([^\n]+)\}\\label\{tab:postupak-\d+\}(.*?)\\begin\{equation\}.*?\n(.*?)\\end\{equation\}',block(n),re.S)
 multiply=[r for r in records if r['kind']=='multiply'];idx=0
 for n,is_signed in [(108,False),(110,True)]:
  chunks=tables(n);check(len(chunks)==3,'multiplication inventory')
  for title,table,equation in chunks:
   rec=multiply[idx];idx+=1
   terms=re.findall(r'\(([01.]+)\)',title);check(terms==[rec['a'],rec['b']],'multiplication operands')
   arrays=written_arrays(table);check(len(arrays)==2,'both written multiplication methods')
   (parallel,lines1),(serial,lines2)=arrays
   check(len(parallel)==6 and len(serial)==11 and lines1==1 and lines2==5,'five partial products, all five additions and ruling')
   x=word(rec['a'],2)-(32 if is_signed and rec['a'][0]=='1' else 0);y=word(rec['b'],2);total=0
   fullword(serial[0],0)
   for j in range(5):
    bit=(y>>j)&1;v=x*bit*(-1 if is_signed and j==4 else 1);expected=v*2**j;total+=expected
    for row,op in [(parallel[j],'+' if j==4 else ''),(serial[1+2*j],'+')]:
     sign,bits,note,styled=row
     check(sign==op and numeric(bits)==expected%1024,'actual shifted partial product and addition sign')
     start=0 if is_signed else 5-j
     check(all(bits[i] for i in range(start,10-j)) and not any(bits[:start]) and not any(bits[10-j:]),'partial product position and blank low places')
     args=re.search(r'\(([01]+)\)_2\\times ([01])',note)
     check(args and args[1]==rec['a'].replace('.','') and int(args[2])==bit and f'(j={j})' in note,'partial product annotation')
     check((r'\mathrm{DK}' in note)==(is_signed and j==4) and (r'\mathrm{EZ}' in note)==is_signed,'DK/EZ annotations')
     if is_signed:
      if j==4:check(all('red!13' in c for c in styled[:6]),'negative-weight product highlighted')
      else:
       check(all('Primary!15' in c for c in styled[:5-j]),'sign-extension bits highlighted')
       check(all(c==bits[5-j] for c in bits[:5-j]),'actual repeated sign bits')
    fullword(serial[2+2*j],total)
    check(f'S_{j}' in serial[2+2*j][2],'intermediate sum index')
   fullword(parallel[-1],total)
   check(re.findall(r'\(([01.]+)\)',equation)==[rec['a'],rec['b'],rec['result']],'mult final equation and point')
 # Long division follows the original left-to-right pencil-and-paper layout.
 chunks=tables(116);check(len(chunks)==3,'division inventory')
 for title,table,equation in chunks:
  a,b=re.search(r'\$([01]+):([01]+)\$',title).groups();n=len(a);m=len(b);divisor=int(b,2)
  arrays=written_arrays(table);check(len(arrays)==1 and divisor>0,'division domain')
  rows,lines=arrays[0];steps=n-m+1
  check(len(rows)==3*steps and lines==steps,'every subtraction, remainder and brought-down bit')
  check(rows[0][1][:n]==list(a) and not any(rows[0][1][n:]),'written dividend')
  rhs=re.findall(r'\(([01]+)\)',rows[0][2]);check(rhs[0]==b and int(rhs[1],2)==int(a,2)//divisor,'divisor and full quotient')
  # The first m dividend bits are grouped, just as in the original table.
  rem=int(a[:m],2);pos=1;quotient=''
  for end in range(m,n+1):
   q=int(rem>=divisor);quotient+=str(q);sub=divisor*q
   op,bits,note,_=rows[pos];pos+=1
   check(op=='-' and bits[end-m:end]==list(f'{sub:0{m}b}') and not any(bits[:end-m]+bits[end:]),'aligned subtrahend, including zero')
   check(note==f'({b})_2'+r'\times '+str(q),'quotient bit in subtraction annotation')
   rem-=sub;op,bits,note,_=rows[pos];pos+=1
   check(op=='' and numeric(bits)==rem*2**(10-end) and not any(bits[end:]) and 0<=rem<divisor,'aligned subtraction remainder')
   if end<n:
    op,bits,note,styled=rows[pos];pos+=1;digit=int(a[end]);rem=2*rem+digit
    check(op=='' and numeric(bits)==rem*2**(9-end) and not any(bits[end+1:]),'brought-down bit and new partial dividend')
    check(note==r'\text{dopisuje se }'+str(digit) and 'Primary!15' in styled[end] and bits[end]==str(digit),'highlighted actual next dividend bit')
  check(pos==len(rows) and int(quotient,2)==int(rhs[1],2),'all long-division rows consumed')
  words=re.findall(r'\(([01]+)\)',equation)
  check(list(map(lambda w:int(w,2),words))==[int(a,2),divisor,int(quotient,2),rem],'division final equation')
 # Actual Boolean equations and two actual functional tables.
 equations=dict(re.findall(r'\\begin\{equation\}\\label\{([^}]+)\}(.*?)\\end\{equation\}',s,re.S))
 for A,B in itertools.product(range(4),repeat=2):
  env={'a1':A>>1,'a0':A&1,'b1':B>>1,'b0':B&1,'p1':(A>>1)^(B>>1)}
  for label,bit in [('eq:3.4.2',0),('eq:3.4.3',1),('eq:3.4.4',2),('eq:3.4.5',0),('eq:3.4.6',1),('eq:3.4.7',2)]:
   for rhs in clean(equations[label]).strip().rstrip('.').split('=')[1:]:check(evaluate(rhs,env)==bool((A+B)>>bit&1),label)
  D2=0
  for num,bit in [(14,4),(15,3),(16,2),(17,1),(18,0)]:
   D2|=int(evaluate(equations[f'eq:3.4.{num}'].split('=')[1].strip(),env))<<bit
  check(D2==3*(A+1),'D2 actual expressions')
 for n,width,expected in [(148,4,lambda i:(i>>2)+(i&3)),(168,2,lambda i:3*(i+1))]:
  rows=[]
  for line in block(n).splitlines():
   if re.match(r'^\s*[01]\s*&',line):rows.append([int(x.strip()) for x in line.split(r'\\')[0].split('&')])
  check(len(rows)==2**width,'functional table domain')
  for i,row in enumerate(rows):
   check(int(''.join(map(str,row[:width])),2)==i and int(''.join(map(str,row[width:])),2)==expected(i),f'functional table {n} row {i}')
 # All 48 K-map cells and 11 distinct implicants, including joined edge groups.
 maps=(ROOT/'Images/Zadatak_4/karno.tex').read_text();gray=[0,1,3,2]
 scopes=re.findall(r'\\begin\{scope\}.*?\\end\{scope\}',maps,re.S);check(len(scopes)==3,'K-map count')
 for bit,scope in zip([2,1,0],scopes):
  cells=re.findall(r'\\node at \(([0-3]\.5),([0-3]\.5)\)\{([01])\};',scope);check(len(cells)==16,'K-map cells')
  ones=set();groups={}
  for x,y,v in cells:
   A=gray[3-int(float(y))];B=gray[int(float(x))];index=4*A+B
   check(int(v)==((A+B)>>bit)&1,'K-map cell')
   if v=='1':ones.add(index)
  for color,x0,y0,x1,y1 in re.findall(r'\\draw\[([^,]+),rounded[^]]+\] \(([^,]+),([^,]+)\) rectangle \(([^,]+),([^,]+)\);',scope):
   pts={4*gray[3-int(float(y))]+gray[int(float(x))] for x,y,v in cells if float(x0)<float(x)<float(x1) and float(y0)<float(y)<float(y1)}
   groups.setdefault(color,set()).update(pts)
  covered=set();literals=0
  for pts in groups.values():
   check(bool(pts) and pts<=ones,'K-map group contains only ones')
   mask=0
   for i in pts:mask|=i^min(pts)
   check(len(pts)==2**mask.bit_count(),'K-map group is a cube')
   literals+=4-mask.bit_count();covered|=pts
  check(covered==ones,'K-map coverage')
  # Exhaustive implicant cover proves minimal number of products and literals.
  cubes=[]
  for pat in itertools.product([-1,0,1],repeat=4):
   pts={i for i in range(16) if all(p==-1 or ((i>>(3-j))&1)==p for j,p in enumerate(pat))}
   if pts<=ones:cubes.append((sum(1<<i for i in pts),sum(p!=-1 for p in pat)))
  target=sum(1<<i for i in ones);best={0:(0,0)}
  for state in range(1<<16):
   if state not in best:continue
   for cube,nlit in cubes:
    nxt=state|cube;cost=(best[state][0]+1,best[state][1]+nlit)
    if cost<best.get(nxt,(100,1000)):best[nxt]=cost
  check(best[target]==(len(groups),literals),'minimum SOP cover')
 # The new subtraction overflow criterion is checked on every binary 4-bit pair.
 for u,v in itertools.product(range(16),repeat=2):
  x=u if u<8 else u-16;y=v if v<8 else v-16;z=(u-v)%16
  actual=bool(((u>>3)^(v>>3))&((z>>3)^(u>>3)))
  check(actual==(not -8<=x-y<=7),'subtraction OF including negation boundary')
 # Read and solve the remaining unsolved arithmetic privately, retaining their statements.
 homework=[]
 def fixed(w,r,kind,N):
  u=word(w,r);old=r**len(w.replace('.',''))
  return u+(r**N-old if 2*u>=old else 0)
 for n,kind,sub in [(178,'KO',False),(180,'KO',True),(183,'KMV',False),(185,'KMV',True)]:
  pairs=re.findall(r'([0-9A-F.]+)\\textsubscript\{(\d+)\}\s*([+-])\s*([0-9A-F.]+)\\textsubscript\{(\d+)\}',block(n))
  check(len(pairs)==(11 if sub else 10),'five-digit task input coverage')
  for a,r,op,b,r2 in pairs:
   r=int(r);check(r==int(r2) and (op=='-')==sub,'five-digit input operation')
   k=len(a.partition('.')[2]);check(k==len(b.partition('.')[2]),'five-digit point alignment')
   x=signed(a,r,kind);y=signed(b,r,kind);exact=x-y if sub else x+y
   N=5;R=r**N;u=fixed(a,r,kind,N);v=fixed(b,r,kind,N)
   if sub:v=(-v)%R if kind=='KO' else R-1-v
   raw=u+v;z=raw%R
   if kind=='KMV':z+=raw//R
   hi=(R-1)//2 if kind=='KO' else (R-2)//2;lo=-(R//2) if kind=='KO' else -hi
   overflow=not lo<=exact*r**k<=hi
   decoded=F(z-(R-(kind=='KMV') if 2*z>=R else 0),r**k)
   check(overflow or decoded==exact,'five-digit task result')
   homework.append({'block':n,'a':a,'b':b,'base':r,'representation':kind,'exact':str(exact),'code_integer':z,'overflow':overflow})
 # Self-study 1: original widths determine values; result width is sufficient.
 Awords=re.findall(r'([01]+)\\textsubscript\{KMV\}',block(120));Bwords=re.findall(r'([01]+)\\textsubscript\{KO\}',block(121));Cwords=re.findall(r'([0-3]+)\\textsubscript\{4KO\}',block(122))
 A=signed(Awords[0],2,'KMV')-signed(Awords[1],2,'KMV');B=signed(Bwords[0],2,'KO')*signed(Bwords[1],2,'KO');C=signed(Cwords[0],4,'KO')-signed(Cwords[1],4,'KO')
 check((A,B,C)==(37,-572,1) and A>C>B,'self-study 1 exact values and order')
 # Self-study 2a: extract decimal value, base-9 code, width set in the statement.
 v=F(re.search(r'=(-?[0-9.]+)_\{?10',block(125))[1]);scaled=v*16**2
 check(scaled.denominator==1 and -16**5//2<=scaled<16**5//2,'hex fixed-point representability')
 U=int(scaled)%16**5;check(F(U-16**5,16**2)==v and format(U,'05X')=='FF2B0','hex fixed-point private answer')
 w=re.search(r'=\(([0-8]+)\)_\{9,',block(125))[1];v=signed(w,9,'KO');U=int(v)+3**6-1
 check(U!=(3**6-1)//2 and F(U-(3**6-1))==v and v==-306,'ternary KMV private answer')
 # Self-study 2b: false statement must stay false, with the declared ZA overflow policy.
 ws=re.findall(r'\(([01]+)\)',block(127));check(len(ws)==4,'self-study 2b operands')
 left=signed(ws[0],2,'KMV')+signed(ws[1],2,'KMV')
 sm=lambda w:(-1 if w[0]=='1' else 1)*int(w[1:],2)
 right=sm(ws[2])-sm(ws[3]);wrapped=(-1 if right<0 else 1)*(abs(right)%16)
 check(left==-12 and right==-18 and abs(right)>15 and wrapped==-2 and left!=wrapped,'self-study 2b false with OF')
 # Both intentionally false comparisons in 2c, independently decoded.
 ts=re.findall(r'\(([0-9A-F]+)\)',block(130));check(len(ts)==8,'self-study 2c operands')
 a,b,c,d,e,f,g,h=ts
 check(signed(a,5,'KO')+signed(b,5,'KO')==-98 and signed(c,2,'KO')*signed(d,2,'KO')==96,'self-study 2c inequality is false')
 check(signed(e,16,'KMV')-signed(f,16,'KMV')==-54 and sm(g)-sm(h)==-21,'self-study 2c equality is false')
 out=ROOT.parent/'PROVERA/_build';out.mkdir(parents=True,exist_ok=True)
 (out/'homework04.json').write_text(json.dumps(homework,ensure_ascii=False,indent=2)+'\n')
 # Actual inline subtraction criterion, rather than a second independent literal.
 of=re.search(r'\\mathrm\{OF\}=(\(x_n.*?), gde',s)[1].strip('$')
 of=of.replace('x_n','x').replace('y_n','y').replace('s_n','s')
 for u,v in itertools.product(range(16),repeat=2):
  x=u if u<8 else u-16;y=v if v<8 else v-16
  check(evaluate(of,dict(x=u>>3,y=v>>3,s=((u-v)%16)>>3))==(not -8<=x-y<=7),'actual subtraction OF criterion')
 # Manual source traces: changed gates/wires/formulas force a fresh review.
 proof=json.loads((ROOT/'code/pregled_izvora.json').read_text())
 for name,entry in proof['figures'].items():check(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==entry['sha256'],'repeat manual diagram review '+name)
 for label,body in equations.items():check(hashlib.sha256(body.strip().encode()).hexdigest()==proof['equations'][label]['sha256'],'repeat manual formula review '+label)

 # Evaluate the manually traced networks, not just the equations next to them.
 def network(name,inputs):
  spec=next(v for k,v in proof['figures'].items() if Path(k).stem==name);state=dict(inputs)
  for out,expr in spec.get('boolean',[]):state[out]=int(evaluate(expr,state))
  for out,op,*args in spec.get('steps',[]):
   a=[x if isinstance(x,int) else state[x] for x in args]
   if op=='copy':v=a[0]
   elif op=='shr':v=a[0]>>a[1]
   elif op=='shl':v=a[0]<<a[1]
   elif op=='and':v=a[0]&a[1]
   elif op=='or':v=a[0]|a[1]
   elif op=='not':v=1-a[0]
   elif op=='gt':v=int(a[0]>a[1])
   elif op=='eq':v=int(a[0]==a[1])
   elif op=='add':v=a[0]+a[1]
   elif op=='mul':v=a[0]*a[1]
   elif op=='mux':v=a[1] if a[0] else a[2]
   elif op=='mux4':v=a[1+a[0]]
   elif op=='concat':
    v=0
    for bit in a:check(bit in [0,1],'bus concatenation bit');v=2*v+bit
   else:raise ValueError(op)
   state[out]=v
  return state
 for A,B in itertools.product(range(4),repeat=2):
  v=network('sabirac',dict(a1=A>>1,a0=A&1,b1=B>>1,b0=B&1))
  check(4*v['s2']+2*v['s1']+v['s0']==A+B,'drawn adder')
  v=network('proizvod',dict(A=A,B=B));check(v['X']==(A+1)*(B+1),'drawn product')
  w=network('kompletna',dict(A=A,B=B,X=v['X']))
  check(w['Y']==((A+1)*(B+1)*(2 if A>B else 1) if A!=B else 0) and w['Y']<32,'drawn final network')
 for A,B in itertools.product(range(16),repeat=2):
  v=network('komparator4',dict(H=A//4>B//4,E=A//4==B//4,L=A%4>B%4,F=A%4==B%4))
  check((v['G'],v['J'],v['Q'])==(A>B,A==B,A<B),'drawn comparator')
 for A,B,C in itertools.product(range(16),repeat=3):
  v=network('maksimum',dict(A=A,B=B,C=C))
  check(v['RES']==max(A,2*B,C//2),'drawn maximum')
 return checks

