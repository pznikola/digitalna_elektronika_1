#!/usr/bin/env python3
"""Source/reference/asset checks, independent of mathematical and manual reviews."""
from pathlib import Path
from collections import Counter
import re,sys,json
ROOT=Path(__file__).resolve().parents[1]
EXERCISES=['01','02','03','04','05','07','08']

def inspect(n):
 folder=ROOT/n;main=next(folder.glob('*.tex'));raw=main.read_text();s=re.sub(r'(?<!\\)%[^\n]*','',raw)
 labels=re.findall(r'\\label\{([^}]+)\}',s);duplicates=[k for k,v in Counter(labels).items() if v>1]
 assert not duplicates,(n,'duplicate labels',duplicates)
 refs=[x.strip() for m in re.findall(r'\\(?:ref|eqref|autoref|cref|Cref|pageref)\{([^}]+)\}',s) for x in m.split(',')]
 assert set(refs)<=set(labels),(n,'undefined source references',set(refs)-set(labels))
 assert not re.search(r'(?<![A-Za-z\\])oprule\b',s),(n,'literal oprule')
 assert r'\today' in s,(n,'date must be dynamic')
 assets=[]
 for name in re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}',s):
  found=[]
  for base in [folder,folder/'Images']:
   p=base/name
   for f in ([p] if p.suffix else [p.with_suffix('.pdf'),p.with_suffix('.png'),p.with_suffix('.jpg')]):
    if f.exists():found.append(f)
  assert found,(n,'missing image',name)
  p=found[0];native=next((p.with_suffix(ext) for ext in ['.tex','.drawio'] if p.with_suffix(ext).exists()),None)
  assets.append({'export':str(p.relative_to(folder)),'source':str(native.relative_to(folder)) if native else None})
 for file in re.findall(r'\\inputminted(?:\[[^]]*\])?\{[^}]+\}\{([^}]+)\}',s):assert (folder/file).exists(),(n,'missing VHDL include',file)
 for file in re.findall(r'\\(?:input|include)\{([^}]+)\}',s):
  p=folder/file
  assert p.exists() or p.with_suffix('.tex').exists(),(n,'missing include',file)
 log=main.with_suffix('.log')
 if log.exists():
  text=log.read_text(errors='replace')
  bad=re.findall(r'^.*(?:Overfull \\[hv]box|undefined|multiply defined|LaTeX Error|Missing character).*$|^!.*$',text,re.M)
  assert not bad,(n,'LaTeX findings',bad)
 return {'exercise':n,'labels':len(labels),'references':len(refs),'assets':assets,'result':'pass','manual_review':'not implied'}
if __name__=='__main__':
 out=ROOT/'PROVERA/_build';out.mkdir(exist_ok=True)
 result=[inspect(n) for n in (sys.argv[1:] or EXERCISES)]
 (out/'structure.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print('Struktura:',', '.join(r['exercise'] for r in result),'- reference, slike i dostupni logovi ispravni.')
