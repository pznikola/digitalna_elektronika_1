"""Veza stvarnih formula/crteža sa nezavisnim racionalnim proračunom."""
from fractions import Fraction as Q
from pathlib import Path
from itertools import product
import ast,re,json,hashlib

def arithmetic(s,x=Q(0)):
 s=s.strip().rstrip(';.,').replace('\\le','<=').replace('^','**')
 s=re.sub(r'(\d|\))x',r'\1*x',s)
 s=re.sub(r'(\d|\))\(',r'\1*(',s)
 def ev(n):
  if isinstance(n,ast.Expression):return ev(n.body)
  if isinstance(n,ast.Constant) and isinstance(n.value,int):return Q(n.value)
  if isinstance(n,ast.Name) and n.id=='x':return x
  if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub):return -ev(n.operand)
  if isinstance(n,ast.BinOp):
   a,b=ev(n.left),ev(n.right)
   if isinstance(n.op,ast.Add):return a+b
   if isinstance(n.op,ast.Sub):return a-b
   if isinstance(n.op,ast.Mult):return a*b
   if isinstance(n.op,ast.Div):return a/b
  raise ValueError(('unsupported math',s,ast.dump(n)))
 return ev(ast.parse(s,mode='eval'))

def run(root,check,F,B,H,val):
 tex=(root/'07_staticke_karakteristike.tex').read_text()
 equations={re.search(r'\\label\{([^}]+)\}',s)[1]:s for s in re.findall(r'\\begin\{equation\}(.*?)\\end\{equation\}',tex,re.S)}
 def parse_cases(label):
  curves=[]
  for body in re.findall(r'\\begin\{cases\}(.*?)\\end\{cases\}',equations[label],re.S):
   segs=[]
   for line in body.split(r'\\'):
    expr,domain=line.split('&')
    m=re.fullmatch(r'(.+?)\\le x\\le(.+?)[;,.]?',domain.strip());assert m,(domain,label)
    lo,hi=arithmetic(m[1]),arithmetic(m[2]);v0=arithmetic(expr,0);slope=arithmetic(expr,1)-v0
    for i in [Q(-2),Q(2),Q(3,7)]:check(arithmetic(expr,i)==v0+slope*i,f'{label}: affine expression')
    segs.append((lo,hi,slope,v0))
   curves.append(segs)
  return curves
 f1,f3=parse_cases('eq:3.1');b1,b3=parse_cases('eq:4.2');h,=parse_cases('eq:5.1')
 check([f1,f3]==[F[0],F[2]],'actual inverter segments');check([b1,b3]==[B[0],B[2]],'actual buffer segments');check(h==H,'actual cascade segments')
 for label,symbol,target in [('eq:3.1','f_2',F[1]),('eq:4.2','b_2',B[1])]:
  expr=re.search(re.escape(symbol)+r'\(x\)&=([^;]+);',equations[label])[1]
  for x in [Q(0),Q(1),Q(5)]:check(arithmetic(expr,x)==val(target,x),'actual middle characteristic')
 # Derive a composition by splitting at preimages of all later breakpoints.
 def compose(f,g):
  knots={s[0] for s in f}|{f[-1][1]};gknots={s[0] for s in g}|{g[-1][1]}
  for a,b,k,c in f:
   if k:
    for y in gknots:
     x=(y-c)/k
     if a<x<b:knots.add(x)
  knots=sorted(knots);segs=[]
  for a,b in zip(knots,knots[1:]):
   u,v=val(g,val(f,a)),val(g,val(f,b));slope=(v-u)/(b-a);segs.append((a,b,slope,u-slope*a))
  return segs
 check(compose(f3,b3)==h,'derived exact composition knots/slopes')
 # General fixed-point and two-cycle stability from all actual segments.
 for f,roots,slopes in [(f1,{Q(0),Q(5,2),Q(5)},{Q(4),Q(1,9)}),(f3,{Q(0),Q(5,2),Q(5)},{Q(1,4),Q(9)}),(h,{Q(0),Q(5,2),Q(5)},{Q(1,16),Q(81)})]:
  ff=compose(f,f);found={}
  for a,b,k,c in ff:
   check(k!=1,'isolated two-step fixed points')
   x=c/(1-k)
   if a<=x<=b:found[x]=k
  check(set(found)==roots and set(found.values())==slopes,'actual two-cycle stability')
 for b in [b1,b3]:
  found={}
  for a,z,k,c in b:
   x=c/(1-k)
   if a<=x<=z:found[x]=k
  check(set(found)=={Q(0),Q(5,2),Q(5)},'buffer fixed points')
  check(found[Q(5,2)]==(Q(1,3) if b==b1 else Q(3)),'buffer middle stability')
 # All source composition table rows; exact rational arithmetic.
 tab=re.search(r'\\label\{tab:prelomi\}(.*?)\\end\{tabular\}',tex,re.S)[1]
 rows=re.findall(r'^([^\n]+?) & ([^&]+) & ([^&]+) & ([^\n]+?)\\\\',tab,re.M);rows=rows[1:]
 check(len(rows)==6,'six composition rows')
 xx=[]
 for name,x,z,y in rows:
  x,z,y=[arithmetic(v.replace('$','').strip()) for v in [x,z,y]]
  check(val(f3,x)==z and val(b3,z)==y==val(h,x),'actual composition table')
  xx.append(x)
 check(xx==[Q(0),Q(2),Q(7,3),Q(8,3),Q(3),Q(5)],'all composition knots')
 # Numbers in final bounds must agree with the actual functions, including units.
 for label,fun,inputs in [('eq:3.5',f3,(3,2)),('eq:4.3',b3,(2,3)),('eq:5.2',h,(3,2))]:
  s=equations[label];nums=re.findall(r'=([\d.]+)\\,\\mathrm V',s)
  check(len(nums)==3,'output bound syntax')
  lo,hi,margin=map(Q,nums);check((lo,hi)==tuple(val(fun,Q(x)) for x in inputs),'actual output bounds')
  check(margin==2-lo==hi-3,'actual noise margins')
  # Interval invariance with adverse signs: extrema suffice for affine monotone pieces.
  check(lo+margin==2 and hi-margin==3,'boundary margins')
  check(lo+margin+Q(1,100)>2 and hi-margin-Q(1,100)<3,'above guaranteed margin')
 for curve in [f3,b3,h]:
  for low in [Q(0),Q(1,100),Q(1),Q(249,100)]:
   for v in [low,5-low]:
    x=v
    for i in range(100):x=val(curve,x)
    check(abs(x-(0 if v<Q(5,2) else 5))<Q(1,10**20),'single-source basin/rail convergence')
  check(val(curve,Q(5,2))==Q(5,2),'exact threshold remains fixed')
 # Every plotted piecewise curve is read from actual paths, compared with formulas.
 def paths(stem,style='Primary,thick'):
  s=(root/f'Images/{stem}.tex').read_text()
  return [[(Q(a),Q(b)) for a,b in re.findall(r'\(([-\d.]+),([-\d.]+)\)',path)] for path in re.findall(r'\\draw\['+re.escape(style)+r'\]\s*([^;]+);',s)]
 def plot_matches(pts,curve,msg):
  check(len(pts)==len(curve)+1,msg+' count')
  for (x,y),knot in zip(pts,[s[0] for s in curve]+[curve[-1][1]]):
   check(abs(x-knot)<Q(1,10**12) and abs(y-val(curve,knot))<Q(1,10**12),msg+' coordinate')
 for stem,curves in [('Zadatak_3/karakteristike',F),('Zadatak_4/karakteristike',B),('Zadatak_5/karakteristike',[f3,b3]),('Zadatak_5/rezultat',[h]),('Zadatak_3/preslikavanje',[f3]),('Zadatak_2/nivoi',[f3])]:
  drawn=paths(stem);check(len(drawn)==len(curves),'plot count')
  for pts,curve in zip(drawn,curves):plot_matches(pts,curve,stem)
 refl=paths('Zadatak_3/preslikavanje','orange,dashed,thick')[0]
 check(refl==[(y,x) for x,y in paths('Zadatak_3/preslikavanje')[0]],'actual reflected graph')
 rot=paths('Zadatak_5/rotacija','orange,thick')[0]
 check(rot==[(-y,x) for x,y in paths('Zadatak_5/karakteristike')[1]],'actual rotated buffer')
 s=(root/'Images/Zadatak_5/rotacija.tex').read_text()
 coords=re.search(r'\\foreach\\x/\\z/\\y in\{([^}]+)\}',s)[1]
 for row in coords.split(','):
  x,z,y=map(Q,row.split('/'));check(abs(val(f3,x)-z)<Q(1,10**5) and val(b3,z)==y,'rotated composition guides')
 # Qualitative Bézier drawing: consistency only, not a numerical solution of the original problem.
 def bezier(t,pts):return tuple((1-t)**3*pts[0][j]+3*(1-t)**2*t*pts[1][j]+3*(1-t)*t*t*pts[2][j]+t**3*pts[3][j] for j in [0,1])
 raw=(root/'Images/Zadatak_1/karakteristika.tex').read_text();patt=r'\\draw\[Primary,thick\] ([^;]+);'
 path=re.search(patt,raw)[1];points=[tuple(map(float,m)) for m in re.findall(r'\(([-\d.]+),([-\d.]+)\)',path)]
 check(len(points)==4,'four Bezier control points')
 def bezval(x):
  lo,hi=0.,1.
  for _ in range(65):
   t=(lo+hi)/2
   if bezier(t,points)[0]<x:lo=t
   else:hi=t
  return bezier((lo+hi)/2,points)[1]
 for t in [i/100 for i in range(101)]:
  dx=3*((1-t)**2*(points[1][0]-points[0][0])+2*(1-t)*t*(points[2][0]-points[1][0])+t*t*(points[3][0]-points[2][0]))
  check(dx>0,'Bezier is single-valued')
 seq=[1.75]
 for i in range(12):seq.append(bezval(seq[-1]))
 for stem in ['iteracije','rotacija','preslikavanje']:
  src=(root/f'Images/Zadatak_1/{stem}.tex').read_text();curves=re.findall(patt,src)
  check(all(c==path for c in curves),'same illustrative curve in every view')
  if stem=='iteracije':
   pairs=re.findall(r'\\draw\[dashed,red\] \(([-\d.]+),0\)\|-\(0,([-\d.]+)\)',src)
   check(len(pairs)==4,'four graphical iteration steps')
   for i,(x,y) in enumerate(pairs):check(abs(float(x)-seq[i])<5.1e-6 and abs(float(y)-seq[i+1])<5.1e-6,'actual graphical iteration point')
  elif stem=='rotacija':
   path2=re.search(r'\\draw\[red,dashed,->\] ([^;]+);',src)[1];coords=[tuple(map(float,m)) for m in re.findall(r'\(([-\d.]+),([-\d.]+)\)',path2)]
   expected=[(seq[0],0),(seq[0],seq[1]),(-seq[2],seq[1]),(-seq[2],-seq[3]),(seq[4],-seq[3]),(seq[4],0)]
   check(len(coords)==len(expected) and all(abs(a-c)<1e-12 and abs(b-d)<1e-12 for (a,b),(c,d) in zip(coords,expected)),'actual rotated iteration')
  else:
   reflected=re.search(r'\\draw\[orange,thick,dashed\] ([^;]+);',src)[1];pts=[tuple(map(float,m)) for m in re.findall(r'\(([-\d.]+),([-\d.]+)\)',reflected)]
   check(pts==[(y,x) for x,y in points],'actual reflected Bezier')
   for i,line in enumerate(re.findall(r'\\draw\[red,->\] ([^;]+);',src)):
    drawn=[tuple(map(float,m)) for m in re.findall(r'\(([-\d.]+),([-\d.]+)\)',line)];k=2*i
    wanted=[(seq[k],seq[k+1]),(seq[k+2],seq[k+1]),(seq[k+2],seq[k+3])]
    check(len(drawn)==3 and all(abs(a-c)<5.1e-6 and abs(b-d)<5.1e-6 for (a,b),(c,d) in zip(drawn,wanted)),'actual reflected iteration')
 # Hash-bound manual proof of all general formulas and following of all circuit connections.
 reviewed=json.loads((root/'code/pregled_izvora.json').read_text())
 check(set(equations)==set(reviewed['equations']),'equation inventory')
 for label,s in equations.items():check(hashlib.sha256(s.encode()).hexdigest()==reviewed['equations'][label]['sha256'],label+': repeat proof review')
 for name,r in reviewed['figures'].items():check(hashlib.sha256((root/name).read_bytes()).hexdigest()==r['sha256'],name+': repeat manual diagram review')
