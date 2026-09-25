"""Read actual displayed arithmetic and table cells; exact rational evaluation.
General symbolic formulas have a separate hash-bound deductive review record.
"""
import ast, hashlib, json, re
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DIGITS='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def value(s,base):
 a,_,b=s.partition('.')
 assert all(DIGITS.index(c)<base for c in a+b),(s,base)
 return sum((F(DIGITS.index(c))*base**i for i,c in enumerate(reversed(a))),F())+sum((F(DIGITS.index(c),base**i) for i,c in enumerate(b,1)),F())
def run():
 s=next(ROOT.glob('03_*.tex')).read_text();count=0
 def check(test,where):
  nonlocal count
  assert test,where
  count+=1
 eq=dict(re.findall(r'\\begin\{equation\}\\label\{([^}]+)\}\s*(.*?)\\end\{equation\}',s,re.S))
 def arithmetic(text,base=10):
  t=text
  # Explicit base literals are converted before ordinary numeric tokens.
  vals={}
  def save(v):
   key='q'+chr(97+len(vals));vals[key]=v;return key
  t=re.sub(r'\(([0-9A-F.]+)\)_\{?(2|7|8|10|16)\}?',lambda m:save(value(m[1],int(m[2]))),t)
  t=re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}',r'(\1)/(\2)',t)
  t=re.sub(r'\\frac([0-9])\{([^{}]+)\}',r'(\1)/(\2)',t)
  t=re.sub(r'\\frac([0-9])([0-9])',r'(\1)/(\2)',t)
  t=t.replace(r'\cdot','*').replace('^','**').replace('{','(').replace('}',')')
  t=re.sub(r'(?<![a-z0-9])([0-9A-F]+(?:\.[0-9A-F]+)?)(?![a-z0-9])',lambda m:save(value(m[1],base)),t)
  tree=ast.parse(t.strip(),mode='eval')
  def calc(n):
   if isinstance(n,ast.Expression):return calc(n.body)
   if isinstance(n,ast.Name):return vals[n.id]
   if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub):return -calc(n.operand)
   if isinstance(n,ast.BinOp):
    a,b=calc(n.left),calc(n.right)
    if isinstance(n.op,ast.Add):return a+b
    if isinstance(n.op,ast.Sub):return a-b
    if isinstance(n.op,ast.Mult):return a*b
    if isinstance(n.op,ast.Div):return a/b
    if isinstance(n.op,ast.Pow):assert b.denominator==1;return a**int(b)
   raise ValueError(ast.dump(n))
  return calc(tree)
 # All positional-expansion intermediate sums and displayed approximations.
 for label in ['eq:2.1.1','eq:2.1.2','eq:2.1.3','eq:2.1.4','eq:13-375']:
  text=eq[label].strip();parts=re.split(r'=|\\approx',text)
  expected=arithmetic(parts[0])
  for i,p in enumerate(parts[1:]):
   actual=arithmetic(p)
   if r'\approx' in text and i==len(parts)-2:
    digits=len(re.search(r'\.(\d+)',p)[1]);check(abs(actual-expected)<=F(1,2*10**digits),label+' rounding')
   else:check(actual==expected,label+' intermediate step '+str(i))
 # Both conversion tables, every row and continuity from row to row.
 tables=re.findall(r'\\begin\{tabular\}\{ccccc\}(.*?)\\end\{tabular\}',s,re.S)
 check(len(tables)==2,'two conversion tables')
 for ti,t in enumerate(tables):
  rows=re.findall(r'^([1234])\s*&\s*(.*?)\s*&\s*(\d+)\s*&\s*([\d.]+)\s*&\s*(\d+)\s*\\\\',t,re.M)
  previous=F(13) if ti==0 else F('0.375')
  check(len(rows)==(4 if ti==0 else 3),'all conversion rows')
  for idx,(step,input_,base,rest,digit) in enumerate(rows,1):
   v=F(re.match(r'[\d.]+',input_)[0]);r=int(base);out=F(rest);d=int(digit)
   check(int(step)==idx and previous==v,'table continuity')
   check(v==r*out+d if ti==0 else r*v==d+out,'table arithmetic')
   check(0<=d<r and (out.denominator==1 if ti==0 else 0<=out<1),'table digit/remainder')
   previous=out
  check(previous==0,'table termination')
 # Octal/hex groups: use source code words rather than expected literal constants.
 text=eq['eq:2.1.5'];a,b=text.split('=')
 first=re.search(r'\{([\d.]+)\}_\{8\}',a)[1];bits=re.sub(r'\\\s|\s','',b).strip()
 check(value(first,8)==value(bits,2),'eq:2.1.5')
 text=eq['eq:2.1.6'].replace(r'\,','');a,b=text.split('=')
 check(arithmetic(a)==arithmetic(b),'eq:2.1.6')
 text=eq['eq:2.1.7'];period=re.search(r'\\overline\{([01]+)\}',text)[1]
 check(arithmetic(text.split('=')[0])==arithmetic(text.split('=')[1]),'eq:2.1.7 rational')
 check(arithmetic(text.split('=')[0])==int('10001001',2)+F(int(period,2),2**len(period)-1),'eq:2.1.7 periodic')
 # Prove that this is the shortest period by following exact remainder states.
 rem=43;seen={};seq=''
 while rem not in seen:
  seen[rem]=len(seq);d,rem=divmod(2*rem,49);seq+=str(d)
 check(seen[rem]==0 and seq==period,'shortest period from division')
 # Every sign-magnitude output is decoded independently.
 for k in range(3,9):
  text=eq[f'eq:2.3.{k}'];a,b=text.split(r'\longmapsto');word=re.search(r'\(([01]+)\)',b)[1]
  check(len(word)==7 and int(a.replace('\\','').strip())==(-1 if word[0]=='1' else 1)*int(word[1:],2),f'eq:2.3.{k}')
 for k in range(10,15):
  parts=eq[f'eq:2.3.{k}'].split('=');v=int(parts[-1].strip())
  for part in parts[:-1]:
   word=re.search(r'\(([01]+)\)',part)[1]
   check(v==(-1 if word[0]=='1' else 1)*int(word[1:],2),f'eq:2.3.{k}')
 # All valid integer complementary encodings and their arithmetic intermediates.
 for task,kind in [(4,'KMV'),(5,'KO')]:
  for base,indices in [(10,[3,4,5,6,7]),(16,[12,13,14,15]),(8,[21,22,23]),(2,[28,29,30,31])]:
   for k in indices:
    label=f'eq:2.{task}.{k}';t=eq[label]
    # Remove base/kind annotations and grouping but retain arithmetic operations.
    t=re.sub(r'_\{(?:2|8|10|16),\\mathrm\{(?:KO|KMV)\}\}', '',t)
    t=re.sub(r'_\{?\\mathrm\{(?:KO|KMV)\}\}?','',t)
    t=re.sub(r'_\{?(?:KO|KMV|2|8|10|16)\}?','',t)
    t=t.replace(r'\ ','').replace('{','').replace('}','').strip()
    left,right=t.split(r'\longmapsto');D=-arithmetic(left,base)
    check(D>=0 and D<=(base**4//2-(kind=='KMV')),label+' range')
    expected=(base**4-(kind=='KMV')-D)%base**4
    if r'\bmod' in right:
     # Zero modulo special case: final encoded word is still read from TeX.
     check(D==0 and arithmetic(right.split('=')[-1],base)==expected,label+' zero')
    else:
     for step in right.split('='):
      check(arithmetic(step,base)==expected,label+' intermediate arithmetic')
 # Fractional KMV/KO step is one last-position unit, not the integer 1.
 for label,adjust in [('eq:2.4.19',F(0)),('eq:2.5.19',F(1,64))]:
  word=re.search(r'=\(([0-7.]+)\)',eq[label])[1]
  check(value(word,8)==64-F(1,64)-value('24.70',8)+adjust,label)
 # Input source statements drive private solutions, never added to student PDF.
 for block,base in [(253,8),(255,16)]:
  part=re.search(r'% Izvor DOCX: blok '+str(block)+r'\n(.*?)(?=% Izvor DOCX:)',s,re.S)[1]
  for text,srcbase in re.findall(r'([0-9A-F.]+)\\textsubscript\{(\d+)',part):
   v=value(text,int(srcbase));whole=v.numerator//v.denominator;fraction=v-whole;digits=[];states=set()
   while fraction:
    check(fraction not in states,'homework terminates');states.add(fraction)
    f=fraction*base;d=f.numerator//f.denominator;digits.append(d);fraction=f-d
   check(v==whole+sum((F(d,base**i) for i,d in enumerate(digits,1)),F()),f'homework block {block} {text}')
 # Exhaustive representations, carry propagation, sign extension, zero and bias.
 for base in [2,8,10,16]:
  for n in range(1,4):
   R=base**n;M=R-1
   for u in range(R):
    ds=[];x=u
    for _ in range(n):x,d=divmod(x,base);ds.append(d)
    c=1;out=0
    for i,d in enumerate(ds):e=(base-1-d+c)%base;c=(base-1-d+c)//base;out+=e*base**i
    check(out==(-u)%R,'KO digit carry recurrence')
    if u<R//2:v=u
    else:v=u-R
    extended=u if v>=0 else (base**(n+1)-R)+u
    decoded=extended if extended<base**(n+1)//2 else extended-base**(n+1)
    check(decoded==v,'KO extension')
    v=u if u<R//2 else u-M
    extended=u if u<R//2 else (base**(n+1)-R)+u
    decoded=extended if extended<base**(n+1)//2 else extended-(base**(n+1)-1)
    check(decoded==v,'KMV extension including both zeros')
 for n in range(1,9):
  for B in [0,1,2**(n-1),2**n-1]:
   represented=[u-B for u in range(2**n)]
   check(min(represented)==-B and max(represented)==2**n-1-B,'offset endpoints')
 # This is a manual proof certificate, not automatic sign-off: any edit invalidates it.
 proof=json.loads((ROOT/'code/pregled_formula.json').read_text())
 for label,body in eq.items():
  check(label in proof,'missing manual proof '+label)
  check(proof[label]['sha256']==hashlib.sha256(body.strip().encode()).hexdigest(),'repeat formula review '+label)
 return count
if __name__=='__main__':print(run())
