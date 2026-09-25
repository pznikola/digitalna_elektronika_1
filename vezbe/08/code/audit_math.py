"""Source-bound MOS, switch graph, timing and table audit.

Only the documented, orthogonal Circuitikz subset is interpreted. Unsupported
geometry is rejected. MOS pin stubs are abstracted outside the device body;
manual SHA-bound review covers symbols, body contacts, all formulas and theory.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
from math import sqrt
import hashlib,json,re,sys
import sympy as sp
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'PROVERA'))
from logic import evaluate

NUM=r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[-+]?\d+)?'
PAIR=rf'({NUM}),({NUM})'

def switch_graph(src):
 nodes={m[2]:(m[1],float(m[3]),float(m[4])) for m in re.finditer(r'\\node\[(nmos|pmos)\]\((m\d+)\)at\('+PAIR+r'\)',src)}
 assert nodes, 'no MOS nodes'
 pins={}
 for name,(kind,x,y) in nodes.items():
  for pin,direction in [('D',1 if kind=='nmos' else -1),('S',-1 if kind=='nmos' else 1)]:pins[name+'.'+pin]=(x,y+direction*.35)
 # Inverter symbol is only used as a load; its independent truth function is checked later.
 for m in re.finditer(r'\\node\[not gate US,draw\]\s*\((\w+)\)at\('+PAIR+r'\)',src):
  pins[m[1]+'.input']=(float(m[2])-.4,float(m[3]));pins[m[1]+'.output']=(float(m[2])+.4,float(m[3]))
 gates={m[1]:m[2].strip() for m in re.finditer(r'\\draw\((m\d+)\.G\)[^;]+?node\[left(?:,[^\]]*)?\]\{\$(.*?)\$\};',src)}
 assert set(gates)==set(nodes),'missing drawn gate labels'
 edges=[];points=set()
 def point(p):return tuple(round(v,8) for v in p)
 for path in re.findall(r'\\draw([^;]+);',src):
  if re.match(r'\(m\d+\.G\)',path):continue
  if 'ellipse' in path:continue
  previous=None;end=0
  for m in re.finditer(r'(\+\+)?\(([^()]+)\)',path):
   raw=m[2];relative=bool(m[1])
   if raw in pins:p=pins[raw]
   else:
    match=re.fullmatch(PAIR,raw)
    assert match,('unparsed coordinate',raw)
    p=tuple(map(float,match.groups()))
   if relative:
    assert previous is not None
    p=(previous[0]+p[0],previous[1]+p[1])
   p=point(p);points.add(p)
   between=path[end:m.start()]
   if previous is not None and '--' in between:
    assert not any(x in between for x in ['to[','|-','-|']),('unsupported path',path)
    assert previous[0]==p[0] or previous[1]==p[1],('nonorthogonal wire',previous,p)
    edges.append((previous,p))
   previous=p;end=m.end()
 for p in pins.values():points.add(point(p))
 parent={p:p for p in points}
 def find(p):
  p=point(p)
  while parent[p]!=p:parent[p]=parent[parent[p]];p=parent[p]
  return p
 def union(a,b):parent[find(a)]=find(b)
 # T junctions are endpoints on a wire. Interior crossings alone do not join.
 for a,b in edges:
  for p in points:
   if a[0]==b[0]==p[0] and min(a[1],b[1])<=p[1]<=max(a[1],b[1]) or a[1]==b[1]==p[1] and min(a[0],b[0])<=p[0]<=max(a[0],b[0]):union(a,p)
 mos=[(name,kind,gates[name],find(pins[name+'.D']),find(pins[name+'.S'])) for name,(kind,x,y) in nodes.items()]
 root=find((0,0));ground=find(min((p for p in points if p[0]==0),key=lambda p:p[1]));power=find(max((p for p in points if p[0]==0),key=lambda p:p[1]))
 return dict(mos=mos,root=root,ground=ground,power=power,pins={k:find(v) for k,v in pins.items()},wires=edges)

def conductive(graph,values,which):
 target=graph['ground' if which=='nmos' else 'power'];reached={graph['root']}
 for _ in graph['mos']:
  for name,kind,label,a,b in graph['mos']:
   bit=values['CLK'] if label=='CLK' else evaluate(label,values)
   if kind==which and bool(bit)==(kind=='nmos') and (a in reached or b in reached):reached.update([a,b])
 return target in reached

def run(base,check):
 tex=(base/'08_mos.tex').read_text()
 def eq(label):return re.search(r'\\begin\{equation\}\\label\{'+re.escape(label)+r'\}(.*?)\\end\{equation\}',tex,re.S)[1].strip()
 def number(pattern,source=tex):
  m=re.search(pattern,source);assert m,pattern;return float(m[1].rstrip('.'))
 def near(a,b,tol=5.1e-7,msg='actual numerical value'):
  check(abs(float(a)-float(b))<tol,(msg,a,b,tol))
 def bisect(f,a,b):
  check(f(a)*f(b)<0,'root bracket')
  for _ in range(80):
   x=(a+b)/2
   if f(a)*f(x)<=0:b=x
   else:a=x
  return (a+b)/2
 sec={i:re.search(r'\\section\{Zadatak '+str(i)+r':.*?(?=\\section\{Zadatak|\\end\{document\})',tex,re.S)[0] for i in range(1,11)}
 # Read the given parameters, not only occurrences of expected answer strings.
 src=sec[1].split(r'\end{enumerate}')[0]
 B0=number(r'\\mu_n C_\{ox\}=(\d+)',src)*1e-6;T=number(r'V_T=([\d.]+)',src);ratio=number(r'W/L=(\d+)',src);D=number(r'V_\{DD\}=([\d.]+)',src);R=number(r'R_L=(\d+)',src)*1000;B=B0*ratio;alpha=1/(B*R)
 low=bisect(lambda y:(D-y)/R-B*((D-T)*y-y*y/2),0,D-T);linlow=D/(1+B*R*(D-T));large=2*(alpha+D-T)-low
 check(0<low<T<D-T and large>D,'physical low root; other root rejected')
 vil=T+alpha;vih=T-alpha+sqrt(8*alpha*D/3);oh=D-alpha/2;ol=sqrt(2*alpha*D/3)
 check(oh>=vil-T and ol<vih-T,'threshold operating regions')
 # Implicit slopes are obtained by differentiating the original current balance.
 x,y,b,r,d,t=sp.symbols('x y b r d t',positive=True)
 Fs=(d-y)/r-b*(x-t)**2/2;Fl=(d-y)/r-b*((x-t)*y-y*y/2)
 for expr,xx,yy in [(Fs,vil,oh),(Fl,vih,ol)]:
  vals={x:xx,y:yy,b:B,r:R,d:D,t:T}
  near(expr.subs(vals),0,1e-13,'balance at slope -1');near((-sp.diff(expr,x)/sp.diff(expr,y)).subs(vals),-1,1e-10,'implicit derivative')
 table=re.search(r'\\label\{tab:1.nivoi\}(.*?)\\bottomrule',tex,re.S)[1]
 rows=re.findall(r'^([^&\n]+)&\s*\$([\d.]+)\\,\\mathrm V\$',table,re.M)
 check(len(rows)==5,'all five actual voltage rows')
 for row,value in zip(rows,[D,linlow,low,vil,vih]):near(float(row[1]),value)
 nums=re.findall(r'=([\d.]+)\\,\\mathrm V',eq('eq:1.11'))
 check(len(nums)==4,'four guaranteed levels and margins')
 for actual,want in zip(nums,[oh,ol,vil-ol,oh-vih]):near(float(actual),want)
 for name,val in [('NM_0',vil-linlow),('NM_1',D-vih)]:near(number(re.escape(name)+r'\\approx([\d.]+)',sec[1]),val)
 vs=bisect(lambda x:(D-x)/R-B*(x-T)**2/2,T,D);near(number(r'V_S=([\d.]+)',sec[1]),vs)
 near(number(r'B_n=(\d+)',sec[1])*1e-6,B,1e-14);near(number(r'\\alpha=(\d+\.\d+)',sec[1]),alpha,5.1e-8)
 # Body effect, unit conversions, KR interpretations and all printed intermediate results.
 src=sec[2].split(r'\end{enumerate}')[0]
 phi=number(r'2\|\\phi_F\|=([\d.]+)',src);t0=number(r'V_\{T0\}=([\d.]+)',src);D=number(r'V_\{DD\}=([\d.]+)',src);gamma=number(r'\\gamma=([\d.]+)',src)
 mu=number(r'\\mu_n=(\d+)',src);cox=number(r'C_\{ox\}=([\d.]+)',src)*1e-6;vel=number(r'v_\{\\mathrm\{sat\}\}=([\d.]+)',src)*1e6
 E=number(r'E_CL=([\d.]+)',src);low=number(r'V_L=([\d.]+)',src);L=number(r'L_1=L_2=(\d+)',src)*1e-7
 vt=lambda y:t0+gamma*(sqrt(y+phi)-sqrt(phi));vh=bisect(lambda y:y+vt(y)-D,0,D)
 near(number(r'V_H=([\d.]+)\\,\\mathrm V',sec[2]),vh);near(number(r'V_H=([\d.]+)-0.2',sec[2]),D-t0+gamma*sqrt(phi),5.1e-8)
 near(number(r'V_\{T2\}\(0.1\\,\\mathrm V\)=([\d.]+)',sec[2]),vt(low))
 u=D-low-vt(low);current1=mu*cox*((vh-t0)*low-low*low/2)/(1+low/E);current2=L*vel*cox*u*u/(u+E);kr=current2/current1
 near(number(r'\\approx([\d.]+)',eq('eq:2.5')),kr,5.1e-6)
 near(number(r'K_R=([\d.]+)',sec[2][sec[2].index('nametne tačna'):]),kr*(mu*E/(2*vel*L)),5.1e-6)
 near(number(r'2v_\{\\mathrm\{sat\}\}L/\\mu_n=([\d.]+)',sec[2]),2*vel*L/mu)
 near(number(r'V_\{T2\}\(V_\{DD\}\)=([\d.]+)',sec[2]),vt(D));near(number(r'V_\{GG\}>([\d.]+)',sec[2]),D+vt(D))
 check(low<vh-t0 and D-low>=u>0,'actual task 2 regions');check(abs(current1*1.7-current2)>current2*.5,'original KR violates current balance')
 # Model: continuity is distinct from smoothness/physical validity.
 U,V,E0,B0=sp.symbols('U V E B',positive=True);lin=B0*(U*V-V**2/2)/(1+V/E0);sat=B0*U**2/(2*(1+U/E0))
 check(sp.simplify(lin.subs(V,U)-sat)==0,'piecewise current continuity')
 check(sp.simplify(sp.diff(lin,V).subs(V,U)+B0*U**2/(2*E0*(1+U/E0)**2))==0,'negative boundary slope limitation')
 maxd=E0*(sp.sqrt(1+2*U/E0)-1);check(sp.simplify(sp.diff(lin,V).subs(V,maxd))==0,'lin current maximum precedes chosen boundary')
 # Depletion model identities and branch checks are independently algebraic, no invented device values.
 K,q,z=sp.symbols('K q z',positive=True);u0=z/sp.sqrt(K*(K+1));d0=z*(1-sp.sqrt(K/(K+1)))
 check(sp.simplify(K*u0*u0-2*z*d0+d0*d0)==0,'depletion VIL satisfies original approximate balance')
 check(sp.simplify(K*u0+d0-z)==0,'depletion slope condition')
 ol=sp.sqrt(q/(3*K));check(sp.simplify(K*(2*(2*ol)*ol-ol**2)-q)==0,'depletion VIH balance')
 root=U-sp.sqrt(U**2-q/K);check(sp.simplify(K*(2*U*root-root*root)-q)==0,'depletion physical root identity')
 # Actual CMOS input dimensions/table values; bisection never selects spurious algebraic roots.
 src=sec[4].split(r'\end{enumerate}')[0]
 D=number(r'V_\{DD\}=([\d.]+)',src);T=number(r'V_\{TN\}=\|V_\{TP\}\|=([\d.]+)',src);Ln=number(r'L_n=L_p=(\d+)',src)*1e-3
 ep=number(r'E_\{CP\}=(\d+)',src);en=ep/number(r'=([\d.]+)E_\{CN\}',src);wn=number(r'W_n=(\d+)',src)
 expected_widths=[number(r'W_\{p1\}=(\d+)',src),number(r'W_\{p2\}=(\d+)',src)]
 table=re.search(r'\\label\{tab:4.prag\}(.*?)\\bottomrule',tex,re.S)[1];rows=re.findall(r'^(\d+) & (\d+) & ([\d.]+)',table,re.M)
 check(len(rows)==2,'two CMOS widths');vsvalues=[]
 for (wp,ratio,answer),expected in zip(rows,expected_widths):
  wp,ratio,answer=map(float,[wp,ratio,answer]);check(wp==expected and ratio==wp/wn,'geometry ratios')
  f=lambda x:(x-T)**2/(x-T+en*Ln)-ratio*(D-x-T)**2/(D-x-T+ep*Ln)
  value=bisect(f,T,D-T);near(answer,value);check(T<value<D-T,'CMOS physical root');near(f(answer),0,5e-7,'rounded result current balance');vsvalues.append(value)
 check(vsvalues[0]>vsvalues[1],'stronger PMOS moves threshold upward')
 # Interpret the actually drawn switch connections (gate types, labels, wires).
 cases=[('Zadatak_5/pdn',lambda a,b,c,d:not((a or b)and(c or d)),False),('Zadatak_5/cmos',lambda a,b,c,d:not((a or b)and(c or d)),True),('Zadatak_5/bez_negacija',lambda a,b,c,d:(a or b)and(c or d),True)]
 cases += [(stem,lambda a,b,c,d:a or b and(c or d),stem.endswith(('cmos','dimenzije'))) for stem in ['Zadatak_6/pdn','Zadatak_6/cmos','Zadatak_7/cmos','Zadatak_7/dimenzije']]
 graphs={}
 for stem,fn,both in cases:
  g=switch_graph((base/f'Images/{stem}.tex').read_text());graphs[stem]=g
  for bits in product([0,1],repeat=4):
   v=dict(zip('ABCD',bits));pd=conductive(g,v,'nmos');check(pd==bool(fn(*bits)),stem+' actual PDN wires')
   if both:check(conductive(g,v,'pmos')!=pd,stem+' actual PUN duality')
  if stem.endswith('bez_negacija'):check(g['pins']['inv.input']==g['root'],'drawn inverter input must be connected to Y1')
 # Actual normalized dimensions: all simple conducting paths, including simultaneous branches.
 src=(base/'Images/Zadatak_7/dimenzije.tex').read_text();widths={}
 for m in re.finditer(r'\\draw\((m\d+)\.G\)[^;]+;\\node\[right(?:,[^\]]*)?\][^;]+?\{\$\s*(\d+)\s*\$\}',src):widths[m[1]]=Q(m[2])
 g=graphs['Zadatak_7/dimenzije'];check(len(widths)==8,'eight actual width labels')
 for which,target,maxR in [('nmos','ground',Q(1)),('pmos','power',Q(1,2))]:
  maxpath=Q(0)
  for bits in product([0,1],repeat=4):
   v=dict(zip('ABCD',bits));edges=[(a,b,Q(1)/widths[name]) for name,kind,label,a,b in g['mos'] if kind==which and bool(evaluate(label,v))==(which=='nmos')]
   def paths(node,seen,res):
    if node==g[target]:return [res]
    ans=[]
    for a,b,r in edges:
     nxt=b if a==node else a if b==node else None
     if nxt is not None and nxt not in seen:ans+=paths(nxt,seen|{nxt},res+r)
    return ans
   rr=paths(g['root'],{g['root']},Q(0))
   if rr:check(all(r<=maxR for r in rr),'dimensioned conducting paths');maxpath=max(maxpath,max(rr))
  check(maxpath==maxR,'worst series resistance attained')
 # Dynamic/footer/precharge connections, no conducting rail short for any binary state.
 dynamic=[]
 for stem,fn in [('Zadatak_8/dinamicko',lambda a,b,c,d:a and b or c and d),('Zadatak_9/kolo',lambda a,b,c,d:c and(a or b))]:
  g=switch_graph((base/f'Images/{stem}.tex').read_text());dynamic.append(g)
  for bits in product([0,1],repeat=5):
   v=dict(zip(['A','B','C','D','CLK'],bits));check(conductive(g,v,'nmos')==bool(v['CLK']and fn(*bits[:4])),stem+' PDN/foot');check(conductive(g,v,'pmos')==(not v['CLK']),stem+' precharge')
 # Domino scopes are separately wired gates connected by explicitly named P/Q nets.
 scopes=re.findall(r'\\begin\{scope\}.*?(?=\\end\{scope\})',(base/'Images/Zadatak_8/domino.tex').read_text(),re.S)
 check(len(scopes)==3,'three domino stages');dom=[]
 for src in scopes:
  g=switch_graph(src);check(g['pins']['inv.input']==g['root'],'domino inverter connected');dom.append(g)
 for bits in product([0,1],repeat=4):
  v=dict(zip('ABCD',bits),CLK=1);v['P']=int(conductive(dom[0],v,'nmos'));v['Q']=int(conductive(dom[1],v,'nmos'))
  check(v['P']==(v['A']and v['B']) and v['Q']==(v['C']and v['D']),'domino AND stages')
  check(conductive(dom[2],v,'nmos')==bool(v['P']or v['Q']),'domino OR stage')
 # Actual timing polylines, exact event locations and levels in both input/output figures.
 def traces(stem):
  s=(base/f'Images/Zadatak_9/{stem}.tex').read_text();paths=re.findall(r'\\draw\[Primary\] ([^;]+);',s)
  return [[tuple(map(float,p)) for p in re.findall(r'\('+PAIR+r'\)',path)] for path in paths]
 inp=traces('ulazi');out=traces('izlaz');check(len(inp)==4 and len(out)==5,'actual timing traces');check(inp==out[:4],'input diagrams match')
 def level(path,t):
  y=path[0][1]
  for x,z in path:
   if x<=t:y=z
  return round(y-min(z for x,z in path))
 # Constant A low requires its documented baseline, not normalization against a nonexistent high.
 events=sorted({x for path in out for x,y in path});state=1
 for a,b in zip(events,events[1:]):
  t=(a+b)/2;clk,c,bb,aa=[level(path,t) for path in inp];v=dict(CLK=clk,A=aa,B=bb,C=c,D=0)
  if conductive(dynamic[1],v,'pmos'):state=1
  elif conductive(dynamic[1],v,'nmos'):state=0
  check(level(out[-1],t)==state,('actual dynamic trace',a,b,state))
 # Boolean formulas in the main source, parsed rather than matched by number occurrence.
 for label in ['eq:5.1','eq:6.1','eq:8.1','eq:8.2','eq:10.1','eq:10.2','eq:10.3']:
  parts=eq(label).replace('\\qquad',',').replace('\\,','').strip().rstrip('.').split(',')
  for chain in parts:
   rhs=chain.split('=')[1:]
   for bits in product([0,1],repeat=4):
    v=dict(zip('ABCD',bits));v['P']=int(not v['C'] or (not v['A'] and not v['D']) or v['C']and(v['A']or v['D']));v['Y']=int(not(v['A']and v['B']or v['C']and v['D']))
    vals=[evaluate(e.replace('[','(').replace(']',')'),v) for e in rhs];check(all(x==vals[0] for x in vals),label+' actual Boolean chain')
 src8=re.search(r'\\\[Y=(.*?)\\\]',sec[8],re.S)[1]
 for bits in product([0,1],repeat=4):
  v=dict(zip('ABCD',bits));check(evaluate(src8.rstrip('.'),v)==(not(v['A']and v['B']or v['C']and v['D'])),'actual task 8 statement simplifies')
 # TG schematic input/control labels are read from the drawn ports, including Z propagation.
 def tg_groups(stem):
  src=(base/f'Images/Zadatak_10/{stem}.tex').read_text()
  ctrl=[v.strip() for v in re.findall(r'\\node\[above\]at\([^)]*\)\{\$(.*?)\$\}',src)]
  inv=[v.strip() for v in re.findall(r'\\node\[below\]at\([^)]*\)\{\$(.*?)\$\}',src)]
  data=[v.strip() for v in re.findall(r'\\draw\([^)]*\)node\[left(?:,[^\]]*)?\]\{\$(.*?)\$\}',src)]
  check(len(ctrl)==len(inv)==len(data),'TG ports count')
  return list(zip(ctrl,inv,data))
 groups=tg_groups('kolo');check(len(groups)==6,'six actual TGs')
 def tgpair(pair,v):
  selected=[]
  for ctrl,bar,data in pair:
   bit=evaluate(ctrl,v);check(evaluate(bar,v)!=bit,'complementary TG controls')
   if bit:selected.append(v[data] if data in v else int(data))
  check(len(selected)==1,'exactly one conducting TG in each mux');return selected[0]
 table=re.search(r'\\label\{tab:10.1\}(.*?)\\bottomrule',tex,re.S)[1]
 rows=re.findall(r'\\texttt\{([01]{4})\} & ([01])',table);check(len(rows)==16,'all binary TG rows')
 for word,y in rows:
  v=dict(zip('ABCD',map(int,word)));v['P']=tgpair(groups[:2],v);v['Q']=tgpair(groups[2:4],v);actual=tgpair(groups[4:],v);check(actual==int(y),'actual TG truth table');check(actual==evaluate(eq('eq:10.1').split('=')[-1].rstrip('.'),v),'drawn TG vs formula')
 table=re.search(r'\\label\{tab:10.2\}(.*?)\\bottomrule',tex,re.S)[1];rows=re.findall(r'^([01]{3}) & ([^\n]+?)\\\\',table,re.M);check(len(rows)==8,'all three-state TG rows')
 for word,y in rows:
  for d in [0,1,'Z']:
   v=dict(zip('ABC',map(int,word)),D=d);v['P']=tgpair(groups[:2],v);v['Q']=tgpair(groups[2:4],v);actual=tgpair(groups[4:],v);check(actual==(d if y=='$D$' else int(y)),'actual Z table')
 groups=tg_groups('sinteza');check(len(groups)==4,'four synthesis TGs')
 for bits in product([0,1],repeat=3):
  v=dict(zip('ABC',bits));v['Q']=tgpair(groups[:2],v);check(tgpair(groups[2:],v)==bool((v['A']or v['B'])and v['C']),'actual TG synthesis')
 # Manual algebra/theory/connectivity proofs bind to every displayed equation and figure.
 review=json.loads((base/'code/pregled_izvora.json').read_text())
 for label,digest in review['equations'].items():check(hashlib.sha256(eq(label).encode()).hexdigest()==digest,('repeat manual equation review',label))
 for rel,digest in review['figures'].items():check(hashlib.sha256((base/rel).read_bytes()).hexdigest()==digest,('repeat manual diagram review',rel))
