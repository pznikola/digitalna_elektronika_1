"""Small strict Boolean LaTeX reader and native Draw.io net reader.
Unsupported syntax raises: it must never be silently counted as verified.
"""
import base64,itertools,re,urllib.parse,xml.etree.ElementTree as ET,zlib

def uncomment(s):return re.sub(r'(?<!\\)%[^\n]*','',s)
def clean(s):
 s=uncomment(s)
 s=re.sub(r'\\(?:label|color)\{[^}]*\}','',s)
 s=re.sub(r'\\textcolor\{[^}]*\}','',s)
 s=re.sub(r'\\(?:begin|end)\{aligned\}','',s)
 s=s.replace(r'\\',' ').replace('&','')
 s=re.sub(r'\\(?:left|right|bigl|bigr|displaystyle)\b','',s)
 s=re.sub(r'\\[,;! ]',' ',s)
 s=s.replace(r'\cdot','*').replace(r'\land','*').replace(r'\lor','+').replace(r'\oplus','^')
 s=re.sub(r'([A-Za-z])_\{([0-9]+)\}',r'\1\2',s)
 s=re.sub(r'([A-Za-z])_([0-9]+)',r'\1\2',s)
 # Ordinary TeX groups control typesetting, not Boolean precedence.
 out=[];stack=[]
 for i,ch in enumerate(s):
  if ch=='{':
   semantic=bool(re.search(r'\\(?:bar|overline)\s*$',s[:i]));stack.append(semantic)
   if semantic:out.append('(')
  elif ch=='}':
   if not stack:raise ValueError(('unbalanced TeX group',s))
   if stack.pop():out.append(')')
  else:out.append(ch)
 if stack:raise ValueError(('unbalanced TeX group',s))
 return ''.join(out)

def evaluate(expr,env):
 s=re.sub(r'\s+','',clean(expr));tok=re.findall(r'\\(?:bar|overline|lnot)|[A-Za-z][0-9]*|[01{}()+*^]',s)
 if ''.join(tok)!=s:raise ValueError(('unsupported Boolean expression',expr,s))
 pos=0
 def atom():
  nonlocal pos
  if pos>=len(tok):raise ValueError(('missing atom',expr))
  t=tok[pos];pos+=1
  if t in [r'\bar',r'\overline',r'\lnot']:return not atom()
  if t in ['{','(']:
   val=disj();end='}' if t=='{' else ')'
   if pos>=len(tok) or tok[pos]!=end:raise ValueError(('unbalanced',expr))
   pos+=1;return val
  if t in ['0','1']:return bool(int(t))
  if t not in env:raise ValueError(('unknown variable',t,expr))
  return bool(env[t])
 def conj():
  nonlocal pos
  v=atom()
  while pos<len(tok) and tok[pos] not in ['+','^','}',')']:
   if tok[pos]=='*':pos+=1
   w=atom();v=v and w
  return v
 def xor():
  nonlocal pos
  v=conj()
  while pos<len(tok) and tok[pos]=='^':pos+=1;v=v!=conj()
  return v
 def disj():
  nonlocal pos
  v=xor()
  while pos<len(tok) and tok[pos]=='+':pos+=1;w=xor();v=v or w
  return v
 result=disj()
 if pos!=len(tok):raise ValueError(('trailing syntax',expr,tok[pos:]))
 return result

def drawio_graph(path):
 root=ET.parse(path).getroot();d=root.find('diagram');g=d.find('mxGraphModel')
 if g is None:g=ET.fromstring(urllib.parse.unquote(zlib.decompress(base64.b64decode(d.text),-15).decode()))
 return {c.get('id'):c for c in g.iter('mxCell')}

def named_schematic(path,inputs):
 cells=drawio_graph(path);state=dict(inputs);pending={k:c for k,c in cells.items() if k.startswith('gate_')}
 while pending:
  progress=False
  for k,c in list(pending.items()):
   ports=[e for e in cells.values() if e.get('edge')=='1' and e.get('target')==k]
   args=[cells[e.get('source')].get('value') for e in ports]
   if not all(a in state for a in args):continue
   style=c.get('style');op='not' if 'inverter_2' in style else re.search(r'operation=([^;]+)',style).group(1)
   bits=[bool(state[a]) for a in args]
   if op!='not':
    assert int(re.search(r'numInputs=(\d+)',style).group(1))==len(ports)
    pin_positions=sorted(float(re.search(r'entryY=([^;]+)',e.get('style')).group(1)) for e in ports)
    assert pin_positions==[(j+.5)/len(ports) for j in range(len(ports))],('wire misses drawn pin',path,k)
   if op=='not':assert len(bits)==1;value=not bits[0]
   elif op=='and':value=all(bits)
   elif op=='or':value=any(bits)
   elif op=='xor':value=bool(sum(bits)%2)
   else:raise ValueError(op)
   if 'negating=1' in style:value=not value
   outs=[e for e in cells.values() if e.get('source')==k and e.get('edge')=='1']
   assert len(outs)==1
   name=cells[outs[0].get('target')].get('value');state[name]=value
   del pending[k];progress=True
  if not progress:raise ValueError(('undriven or cyclic named net',list(pending)))
 return state

def hazards(terms,values):
 return [(i,j) for i in range(len(values)) for j in range(i+1,len(values)) if (i^j).bit_count()==1 and values[i] and values[j] and not any(i in t and j in t for t in terms)]

def reviewed_schematic(path,inputs,review):
 """Evaluate a manually traced legacy drawing, invalidating review on any edit.

 Legacy Draw.io files use free-ended lines and separate inversion circles;
 their connectivity is not inferred from XML source/target attributes alone.
 """
 import hashlib
 if hashlib.sha256(path.read_bytes()).hexdigest()!=review['sha256']:
  raise AssertionError(f'Ponoviti ručni pregled izmenjene šeme: {path}')
 cells=drawio_graph(path);state={k+'_in':v for k,v in inputs.items()}
 expected={g['id'] for g in review['gates']}
 actual={k for k,c in cells.items() if 'logic_gate' in c.get('style','')}
 assert actual==expected,('unreviewed gate',path)
 for g in review['gates']:
  style=cells[g['id']].get('style','');op=g['op'];bits=[bool(state[a]) for a in g['inputs']]
  if op=='not':assert 'inverter_2' in style;value=not bits[0]
  else:
   base={'nand':'and','nor':'or'}.get(op,op)
   assert 'operation='+base+';' in style
   neg=op in ['nand','nor']
   if g['id'] in review.get('separate_inversion_bubbles',{}):
    bubble=cells[review['separate_inversion_bubbles'][g['id']]]
    assert 'ellipse;' in bubble.get('style','') and 'fillColor=#000000' not in bubble.get('style','')
    assert neg
   else:assert ('negating=1' in style)==neg
   value=all(bits) if base=='and' else any(bits) if base=='or' else bool(sum(bits)%2)
   if neg:value=not value
  state[g['output']]=value
 return state

def kmap_rect(a,b):
 gray=[0,1,3,2];ar,ac=gray.index(a//4),gray.index(a%4);br,bc=gray.index(b//4),gray.index(b%4)
 return {4*gray[r]+gray[c] for r in range(min(ar,br),max(ar,br)+1) for c in range(min(ac,bc),max(ac,bc)+1)}
