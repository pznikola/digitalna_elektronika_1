#!/usr/bin/env python3
"""Traceable audit inventory. Automated runs NEVER sign off human review.
Review attestations bind source and artifact SHA256s, so edits invalidate them.
"""
import argparse,bisect,gzip,hashlib,json,re,subprocess,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];HERE=Path(__file__).resolve().parent
EXERCISES=['01','02','03','04','05','07','08']
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def digest(text):return hashlib.sha256(text.encode()).hexdigest()
def masked(s):return re.sub(r'(?<!\\)%[^\n]*',lambda m:' '*len(m.group()),s)
def brace(s,start):
 depth=0
 for i in range(start,len(s)):
  if s[i]=='{' and (i==0 or s[i-1]!='\\'):depth+=1
  if s[i]=='}' and (i==0 or s[i-1]!='\\'):
   depth-=1
   if not depth:return i+1
 raise ValueError(('unbalanced braces',start))
def inventory(n):
 folder=ROOT/n;main=next(folder.glob('*.tex'));source=main.read_text();s=masked(source);units=[]
 def add(kind,a,b,parent=None):
  txt=source[a:b].strip()
  if not txt:return
  labels=re.findall(r'\\label\{([^}]+)\}',s[a:b])
  units.append({'kind':kind,'source':str(main.relative_to(ROOT)),'line_start':source.count('\n',0,a)+1,'line_end':source.count('\n',0,b)+1,'offset':a,'text':txt,'content_sha256':digest(txt),'label':labels[0] if labels else None,'parent_hint':parent})
 # Whole document partition ensures even unusual environments/macros remain visible.
 for m in re.finditer(r'\S[\s\S]*?(?=\n\s*\n|\Z)',s):
  if m.end()<=s.find(r'\begin{document}'):continue
  add('tekst',m.start(),m.end())
 for m in re.finditer(r'\\(?:section|subsection|subsubsection)\*?\{',s):add('odeljak',m.start(),brace(s,m.end()-1))
 for m in re.finditer(r'\\item(?:\[[^\]]*\])?',s):
  nxt=re.search(r'\\(?:item|end\{(?:enumerate|itemize)\})',s[m.end():]);end=m.end()+nxt.start() if nxt else len(s)
  add('pottačka',m.start(),end)
 # Balanced environment spans preserve nested tables/subfigures.
 stack=[];spans=[]
 for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
  mode,name=m.groups()
  if mode=='begin':stack.append((name,m.start(),m.end()))
  else:
   if not stack or stack[-1][0]!=name:raise ValueError((main,'unbalanced environment',name,m.start()))
   name,a,body=stack.pop();spans.append((name,a,body,m.start(),m.end()))
 kinds={'equation':'jednačina','equation*':'jednačina','align':'jednačina','align*':'jednačina','gather':'jednačina','gather*':'jednačina','figure':'slika','figure*':'slika','subfigure':'podslika','tabular':'tabela','tabularx':'tabela','longtable':'tabela','karnaugh-map':'Karnoova karta','tikzpicture':'TikZ crtež','minted':'kod','tcolorbox':'napomena'}
 for name,a,body,end,b in spans:
  if name in kinds:add(kinds[name],a,b)
  if name in ['tabular','tabularx','longtable']:
   # Row-level coverage includes layout rows; unsupported complex layouts remain full spans.
   for m in re.finditer(r'[^\n]*&[^\n]*(?:\n(?!\s*\n)[^\n]*)*?',s[body:end]):
    add('red tabele',body+m.start(),body+m.end(),a)
 for m in re.finditer(r'(?<!\\)\$(?!\$)(.*?)(?<!\\)\$',s,re.S):add('matematika u tekstu',m.start(),m.end())
 for m in re.finditer(r'\\\((.*?)\\\)|\\\[(.*?)\\\]',s,re.S):add('nenumerisana matematika',m.start(),m.end())
 for m in re.finditer(r'\\(?:includegraphics|inputminted|input|include|lstinputlisting)(?:\[[^\]]*\])?\{',s):
  b=brace(s,m.end()-1)
  if 'inputminted' in m.group() and b<len(s) and s[b]=='{':b=brace(s,b)
  add('uključeni fajl',m.start(),b)

 # Hierarchical context distinguishes e.g. class exercise 1 from homework 1.
 headings=[];levels={};counters=[0,0,0]
 for m in re.finditer(r'\\(section|subsection|subsubsection)(\*)?\{',s):
  depth=['section','subsection','subsubsection'].index(m[1]);end=brace(s,m.end()-1);title=source[m.end():end-1]
  if m[2] and 'Rešenje' in title:continue
  if not m[2]:
   counters[depth]+=1
   for j in range(depth+1,3):counters[j]=0
  levels[depth]=title
  levels={k:v for k,v in levels.items() if k<=depth}
  headings.append((m.start(),end,' > '.join(levels[k] for k in sorted(levels)),'.'.join(map(str,counters[:depth+1]))))
 for u in units:
  eligible=[h for h in headings if h[0]<=u['offset']]
  h=eligible[-1] if eligible else (0,0,'Naslovna strana i sadržaj','0')
  u['context']=h[2];u['section_number']=h[3]
 # Paragraphs are proof units: all claims, qualifiers, examples and inline math in
 # their full text must be reviewed. They are never inferred from a test count.
 for m in re.finditer(r'\\(?:paragraph|subparagraph)\*?\{',s):
  add('naslov pottačke',m.start(),brace(s,m.end()-1))
 # Include native assets and generated exports, with explicit main-file uses.
 for asset in sorted(folder.rglob('*')):
  if not asset.is_file() or asset==main or asset.suffix not in ['.tex','.drawio','.png','.vhd','.pdf']:continue
  if '_minted-' in str(asset) or asset==main.with_suffix('.pdf'):continue
  rel=asset.relative_to(folder).as_posix();stem=asset.with_suffix('').relative_to(folder).as_posix()
  needles=[rel,stem]
  if stem.startswith('Images/'):needles += [stem[len('Images/'):],rel[len('Images/'):]]
  uses=[]
  for u in units:
   if u['kind']=='uključeni fajl' and any(x in u['text'] for x in needles):uses.append(u['line_start'])
  # Alternate PNG is historical; a .tex sibling supplies the current image.
  if asset.suffix=='.png' and asset.with_suffix('.tex').exists():uses=[]
  associated=asset.suffix=='.vhd' and ('/'+rel in source or 'code/' in rel)
  kind='izvor ilustracije' if asset.suffix in ['.drawio','.tex','.png'] else 'izvoz ilustracije' if asset.suffix=='.pdf' else 'VHDL izvor'
  role='uključen' if uses else 'prateći VHDL modul/testbench' if associated else 'nekorišćen materijal'
  raw=asset.read_text() if asset.suffix in ['.tex','.drawio','.vhd'] else ''
  units.append({'kind':kind,'source':str(asset.relative_to(ROOT)),'line_start':1,'line_end':len(raw.splitlines()) if raw else None,'offset':0,'text':raw if asset.suffix in ['.tex','.vhd'] else f'{role}: {rel}','content_sha256':sha(asset),'label':None,'parent_hint':None,'main_uses':uses,'role':role,'context':rel,'section_number':None})
 # Stable IDs are persistent, assigned independently of current line numbers.
 oldpath=HERE/'registar.json';old=[]
 if oldpath.exists():old=[u for u in json.loads(oldpath.read_text())['items'] if u['exercise']==n]
 archived=json.loads(oldpath.read_text()).get('retired_items',[]) if oldpath.exists() else []
 used=set();nextid=max([int(u['id'].split('-')[-1]) for u in old+archived if u.get('exercise')==n]+[0])+1
 for u in sorted(units,key=lambda u:(u['offset'],u['kind'])):
  candidates=[v for v in old if v['id'] not in used and v['kind']==u['kind'] and v['source']==u['source'] and (v['content_sha256']==u['content_sha256'] or u['label'] is not None and v['label']==u['label'])]
  if candidates:oid=min(candidates,key=lambda v:abs(v['line_start']-u['line_start']))['id']
  else:oid=f'{n}-{nextid:05}';nextid+=1
  used.add(oid);u.update(id=oid,exercise=n)
  if 'main_uses' not in u:
   hs=[h for h in headings if h[0]<=u['offset']];h=hs[-1] if hs else (0,0,'Naslovna strana i sadržaj','0')
   u.setdefault('context',h[2]);u.setdefault('section_number',h[3])
   blocks=list(re.finditer(r'% Izvor DOCX: blok (\d+)',source[:u['offset']+1]))
   u['original_location']={'inventory':n+'/INVENTAR.md','section':u['context']}
   if blocks:u['original_location']['docx_block']=int(blocks[-1][1])
   if n in ['07','08']:
    tasks=re.search(r'Zadatak (\d+)',u['context']);task=int(tasks[1]) if tasks else None
    pages={'07':{1:[1,2],2:[3,4],3:[5,6],4:[7,8],5:[9,10]},'08':{1:[1,2,3],2:[4,5],3:[5,6,7,8],4:[8,9],5:[9,10,11],6:[11,12,13],7:[13,14,15],8:[16,17],9:[17,18],10:[18,19,20]}}
    u['original_location']['source_pdf']=n+'_mos.pdf' if n=='08' else '07_staticke_karakteristike.pdf'
    u['original_location']['original_task_pages']=pages[n].get(task,[])
  else:u['original_location']={'inventory':n+'/INVENTAR.md','editable_source_or_export':u['source']}

 return units

def dependencies(n):
 folder=ROOT/n
 return {str(p.relative_to(ROOT)):sha(p) for p in sorted(folder.rglob('*')) if p.is_file() and '_minted-' not in str(p) and '__pycache__' not in p.parts and (p.suffix in ['.tex','.drawio','.png','.vhd','.py','.json'] or p.name=='Makefile')}

def evidence_dependencies(n):
 """Separate from historical local-source attestations; changes invalidate review."""
 paths=list((ROOT/n).rglob('*.md'))+list((ROOT/n/'Images').rglob('*.pdf'))
 main=next((ROOT/n).glob('*.tex'))
 paths += [p for p in (ROOT/n).glob('*.pdf') if p!=main.with_suffix('.pdf')]
 paths += [p for p in ROOT.glob(n+'_*') if p.suffix in ['.docx','.pdf']]
 helpers=['audit.py','build.py','logic.py','structure.py','negative_checks.py','registry_check.py','clean_build.py']+(['vhdl_check.py'] if n=='01' else ['vhdl02.py'] if n=='02' else [])
 paths += [HERE/k for k in helpers]
 paths += [ROOT/'Makefile']
 # Historical findings and portable execution records are evidence too.
 paths += list(HERE.glob('nalazi_'+n+'*'))
 paths += list((HERE/'dokazi').glob('*.json'))
 return {str(p.relative_to(ROOT)):sha(p) for p in sorted(set(paths))}

def synctex_lines(main):
 path=main.with_suffix('.synctex.gz');mapping={}
 if not path.exists():return mapping
 data=gzip.open(path,'rt').read();tags={int(i) for i,p in re.findall(r'^Input:(\d+):(.+)$',data,re.M) if Path(p).name==main.name};page=None
 for row in data.splitlines():
  m=re.match(r'^\{(\d+)$',row)
  if m:page=int(m[1]);continue
  if row=='}':page=None;continue
  m=re.match(r'^[\[\(hvkxgr$](\d+),(\d+)(?:,\d+)?:',row)
  if m and page and int(m[1]) in tags:mapping.setdefault(int(m[2]),set()).add(page)
 return mapping

def assign_pages(units,main,count):
 mapping=synctex_lines(main);keys=sorted(mapping)
 def span(lo,hi):
  result=set().union(*(mapping[k] for k in keys if lo<=k<=hi)) if keys else set()
  # Macro headings and includes may not have an exact node: use the next
  # nearby node, never fabricate a page unrelated to the source location.
  if not result and keys:
   nearby=min(keys,key=lambda k:(abs(k-lo),k<lo))
   if abs(nearby-lo)<=12:result=mapping[nearby]
  return sorted(x for x in result if 1<=x<=count)
 for u in units:
  if 'main_uses' in u:
   u['pdf_pages']=sorted({p for line in u['main_uses'] for p in span(line,line+1)})
   u['page_mapping']='mesto uključivanja u glavnom izvoru' if u['main_uses'] else 'prilog bez samostalne PDF stranice'
  else:
   u['pdf_pages']=span(u['line_start'],u['line_end']);u['page_mapping']='SyncTeX zapisi u rasponu izvora ili najbliži susedni čvor (do 12 linija)'
 # A subpart or display macro may have no direct nodes. Its enclosing reviewed
 # paragraph/figure supplies an explicit parent relationship, not guessed data.
 for u in units:
  if u['pdf_pages'] or 'main_uses' in u:continue
  parents=[v for v in units if v['source']==u['source'] and v['id']!=u['id'] and v['line_start']<=u['line_start'] and (v['line_end'] or 0)>=u['line_end'] and v['pdf_pages']]
  if parents:
   parent=min(parents,key=lambda v:v['line_end']-v['line_start']);u['pdf_pages']=parent['pdf_pages'];u['page_parent']=parent['id'];u['page_mapping']='stranice obuhvatne celine '+parent['id']

METHODS={
 'tekst':'Ručni pregled svih tvrdnji i njihovih pretpostavki u pasusu; dokazni prilog i provere povezanih formula.',
 'jednačina':'Nezavisno izvođenje / racionalna ili simbolička provera; izvor vezan za dokumentovano izvođenje.',
 'matematika u tekstu':'Provera u kontekstu pasusa i zadatka, uključujući domen, oznake, jedinice i preciznost.',
 'nenumerisana matematika':'Nezavisni račun ili dokaz u kontekstu; bez dodavanja studentskih rešenja nerešenim zadacima.',
 'tabela':'Svaki podatak/pravilo i pripadnost redova provereni; numeracija, linije i izgled pregledani.',
 'red tabele':'Poređenje stvarnih ćelija sa nezavisnim računom ili pravilom; zaglavlja i napomene ručno.',
 'slika':'Poređenje oznaka i stvarnih veza/koordinata sa tekstom; pregled konačnog PDF-a.',
 'izvor ilustracije':'Praćenje izmenjivih veza/koordinata i oznaka; algoritamska provera gde je parsirana, inače ručni dokaz vezan SHA256 otiskom.',
 'izvoz ilustracije':'Regenerisanje iz izmenjivog izvora i vizuelno poređenje u dokumentu; čista izgradnja.',
 'VHDL izvor':'GHDL u izolovanom direktorijumu; automatska očekivanja i vremenski događaji, uz pregled izvora.',
 'Karnoova karta':'Sve ćelije, implicirane grupe i rubna susednost; originalne strelice sačuvane i proverene.',
}

LIMITS={
 '02':[('Zadatak 4','02-S09','Trajanje inicijalizacije/povratne sprege zavisi od nezadatih kašnjenja; logika potvrđena uz opisani reset protokol.')],
 '07':[('Zadatak 1','07-L01','Izvorni graf nema analitički model za tačnu numeričku granicu.')],
 '08':[(f'Zadatak {task}:',f'08-L{i}',desc) for task,i,desc in [(1,'01','Nije zadat EC L; brojni odgovor je aproksimativan.'),(2,'02','Dati parametri blago neusaglašeni; dva označena tumačenja.'),(3,'03','Nedostaju napajanje, geometrije i tehnološki parametri.'),(4,'04','Odnos brzina zasićenja/oksida nije zadat; korišćena eksplicitna pretpostavka izvora.'),(7,'05','Dimenzije su normalizovane uz izabranu referencu; apsolutne nisu određene.')]],
}

def findings(n):
 path=ROOT/n/'IZVESTAJ_ISPRAVKI.md';src=path.read_text();found=[]
 for m in re.finditer(r'(?m)^#{2,3} .*?\b('+n+r'-(?:[A-Z])?\d+)\b[^\n]*|^\| ('+n+r'-[A-Z]\d+) \|[^\n]*',src):
  ident=m[1] or m[2];end=src.find('\n##',m.end());end=len(src) if end<0 else end
  if m[2]:end=src.find('\n',m.end())
  text=src[m.start():end];found.append({'id':ident,'report':str(path.relative_to(ROOT)),'report_line':src[:m.start()].count('\n')+1,'title':m[0],'labels':sorted(set(re.findall(r'\b(?:eq|fig|tab|sec):[\w.\-]+',text))),'text':text})
 return found

def report(render=False):
 oldpath=HERE/'registar.json';previous=json.loads(oldpath.read_text()) if oldpath.exists() else {};retired=previous.get('retired_items',[])
 items=[];docs={};allfind=[];att=HERE/'rucni_pregled.json';review=json.loads(att.read_text()) if att.exists() else {}
 for n in EXERCISES:
  main=next((ROOT/n).glob('*.tex'));pdf=main.with_suffix('.pdf');deps=dependencies(n);edeps=evidence_dependencies(n);current=review.get(n,{})
  verified=current.get('sources')==deps and current.get('evidence_sources')==edeps
  pdfhash=sha(pdf) if pdf.exists() else None
  info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True).stdout if pdf.exists() else '';count=int(re.search(r'Pages:\s*(\d+)',info).group(1)) if 'Pages:' in info else 0
  page_review=current.get('pdf_sha256')==pdfhash and sorted(current.get('pages',[]))==list(range(1,count+1)) and count>0
  docs[n]={'sources':deps,'evidence_sources':edeps,'pdf_sha256':pdfhash,'pages':count,'content_review_current':verified,'visual_review_current':page_review,'evidence':current.get('evidence',[]),'limitations':current.get('limitations',[])}
  units=inventory(n);assign_pages(units,main,count);fs=findings(n);allfind+=fs
  for u in units:
   u['status']='potvrđeno' if verified and page_review else 'neprovereno'
   u['method']=METHODS.get(u['kind'],'Ručni pregled u kontekstu zadatka, strukturna provera, dokazni prilog i pregled konačnih stranica.')
   u['evidence']=current.get('evidence',[]) if verified else [];u['findings']=[f['id'] for f in fs if u.get('label') and u['label'] in f['labels']]
   u['proof_locations']=[]
   for evidence in u['evidence']:
    ep=ROOT/evidence
    if ep.is_file() and ep.suffix in ['.py','.md']:
     for ln,textline in enumerate(ep.read_text().splitlines(),1):
      if u.get('label') and u['label'] in textline:u['proof_locations'].append({'path':evidence,'line':ln,'matches_label':u['label']})
   if not u['proof_locations']:
    proof=f'{n}/code/PREGLED_DOKAZA.md' if (ROOT/n/'code/PREGLED_DOKAZA.md').exists() else f'{n}/IZVESTAJ_ISPRAVKI.md'
    u['proof_locations'].append({'path':proof,'context':u.get('context'),'method':'dokazni odeljak odgovarajuće celine; tačna izvorna lokacija i SHA u ovoj stavci'})
   u['source_evidence']=dict(source_sha256=deps.get(u['source'],edeps.get(u['source'])),pdf_sha256=pdfhash,scope='konzervativno poništavanje potvrde za ceo dokument i zavisne rezultate')
   if u['status']=='potvrđeno' and u['findings']:u['status']='ispravljeno i ponovo provereno'
   for selector,ident,desc in LIMITS.get(n,[]):
    if selector in u.get('context',''):
     u.setdefault('limitations',[]).append({'id':ident,'description':desc})
     if u['status']!='neprovereno':u['status']='ograničeno nedostajućim podacima'
   if u.get('role')=='nekorišćen materijal':u['method']='Evidentiran istorijski prilog; ne učestvuje u konačnom PDF-u. Poređenje sa zamenom je opisano u izveštaju.'
   items.append(u)
  if render and pdf.exists():
   out=HERE/'_build'/'pages'/n;out.mkdir(parents=True,exist_ok=True)
   for old in out.glob('p-*.png'):old.unlink()
   subprocess.run(['pdftoppm','-r','150','-png',str(pdf),str(out/'p')],check=True)
  print(f'{n}: {len(units)} stavki, {count} stranica, sadržaj={verified}, izgled={page_review}',flush=True)
 ids={u['id'] for u in items};retired_ids={u['id'] for u in retired}
 for old in previous.get('items',[]):
  if old['id'] not in ids and old['id'] not in retired_ids:retired.append({**old,'archived_reason':'Izmenjena/uklonjena inventarska celina; važeći naslednik locira se po izvoru, oznaci i kontekstu. Istorija se ne briše.'})
 record={'schema_version':2,'documents':docs,'items':items,'findings':allfind,'retired_items':retired}
 oldpath.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
 # A portable, compact evidence record complements the ignored detailed build logs.
 lines=['# Zajednički izveštaj provere','', 'Automatski cilj ne potvrđuje ručni pregled. Potvrde su vezane za pregledane izvore, dokaze, izvoze ilustracija i tačan PDF. Promena bilo kog od njih poništava odgovarajuću potvrdu.','', '| Vežba | Stavke | Stranice | Sadržaj | Svaka stranica | Izveštaj |','|---|---:|---:|---|---|---|']
 for n,d in docs.items():lines.append(f'| {n} | {sum(u["exercise"]==n for u in items)} | {d["pages"]} | {"pregledan" if d["content_review_current"] else "NEPOTVRĐEN"} | {"pregledana" if d["visual_review_current"] else "NEPOTVRĐENA"} | [ispravke](../{n}/IZVESTAJ_ISPRAVKI.md) |')
 lines+=['','## Pokrivenost po dokumentima i kategorijama','','Brojevi predstavljaju inventarske celine koje se namerno preklapaju (npr. tabela i njeni redovi), a ne broj nezavisnih dokaza ili testova. Pasus obuhvata sve tvrdnje i pretpostavke u njemu.','', '| Vežba | Kategorija | Sve | Potvrđene | Ispravljene | Ograničene | Neproverene |','|---|---|---:|---:|---:|---:|---:|']
 for n in EXERCISES:
  for kind in sorted({u['kind'] for u in items if u['exercise']==n}):
   us=[u for u in items if u['exercise']==n and u['kind']==kind];c=Counter(u['status'] for u in us)
   lines.append(f'| {n} | {kind} | {len(us)} | {c["potvrđeno"]} | {c["ispravljeno i ponovo provereno"]} | {c["ograničeno nedostajućim podacima"]} | {c["neprovereno"]} |')
 lines+=['','## Ograničenja izvornika','']
 for n,d in docs.items():
  for lim in d['limitations']:lines.append(f'- **{n}:** {lim if isinstance(lim,str) else lim["id"]+": "+lim["description"]}')
 lines+=['','## Sledljivost i završne provere','', 'Registar [`registar.json`](registar.json) sadrži stabilne ID-jeve, izvorni tekst, lokaciju, oznaku, kontekst, PDF stranice, metod, dokaz, status i vezu sa nalazima. Arhivirane celine čuvaju prethodnu istoriju. Stranice su fizičke PDF stranice, uključujući naslovnu. SyncTeX obuhvata raspon izvora; prilozi bez direktnog prikaza imaju eksplicitnu oznaku te uloge.','', 'Dokumentovani nalazi su u lokalnim izveštajima; [`REZULTATI.md`](REZULTATI.md) sadrži završne komande, čistu izgradnju, sažetak ispravki i granice dokaza. Izvorni prikaz šema rešenja i strelica Karnoovih karata u 01 vraćen je i regresiono zaštićen.','']
 (HERE/'IZVESTAJ.md').write_text('\n'.join(lines))
 count=Counter(u['status'] for u in items);print('Inventar:',len(items),dict(count))
 missing_pages=[u['id'] for u in items if not u['pdf_pages'] and 'main_uses' not in u]
 if missing_pages:print('Nedostaju PDF lokacije:',missing_pages)
 return all(d['content_review_current'] and d['visual_review_current'] for d in docs.values()) and not count['neprovereno'] and not missing_pages

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--render',action='store_true');p.add_argument('--require-complete',action='store_true');a=p.parse_args();complete=report(a.render)
 if a.require_complete and not complete:sys.exit('Audit nije završen: ručni pregled nedostaje ili je promenom izvora/PDF-a poništen.')
