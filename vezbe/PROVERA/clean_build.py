#!/usr/bin/env python3
"""Rebuild all seven documents from editable sources in a new temporary tree.

No source PDF, LaTeX sidecar or minted cache is copied. The installed toolchain
is shared. Fresh pages are compared with the reviewed workspace PDFs at 110 dpi;
byte-identical pixels preserve the visual evidence despite PDF metadata changes.
"""
import hashlib,json,os,re,shutil,subprocess,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];HERE=Path(__file__).resolve().parent
DOCS=['01','02','03','04','05','07','08']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(cmd,cwd,log):
 with log.open('w') as f:p=subprocess.run(cmd,cwd=cwd,stdout=f,stderr=subprocess.STDOUT)
 if p.returncode:raise RuntimeError(f'{cmd} failed; see {log}')
 return p

def main():
 target=Path(tempfile.mkdtemp(prefix='de1-clean-audit-'));w=target/'vezbe';w.mkdir();source_hashes={}
 for n in DOCS:
  for p in sorted((ROOT/n).rglob('*')):
   if p.is_file() and (p.suffix in ['.tex','.drawio','.png','.vhd','.py','.json','.md'] or p.name=='Makefile') and '_minted-' not in str(p) and '__pycache__' not in p.parts:
    dst=w/p.relative_to(ROOT);dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dst);source_hashes[str(p.relative_to(ROOT))]=sha(p)
 (w/'PROVERA').mkdir()
 for p in HERE.glob('*.py'):shutil.copy2(p,w/'PROVERA'/p.name);source_hashes[str(p.relative_to(ROOT))]=sha(p)
 shutil.copy2(ROOT/'Makefile',w/'Makefile');source_hashes['Makefile']=sha(ROOT/'Makefile')
 assert not list(w.rglob('*.pdf')) and not list(w.rglob('*.aux')) and not list(w.rglob('_minted-*'))
 print(f'Clean source tree: {w}',flush=True)
 run(['make'],w,target/'build.log');print('Fresh build passed for all seven documents.',flush=True)
 run(['python3','PROVERA/structure.py'],w,target/'structure.log')
 documents={}
 for n in DOCS:
  pdf=next((w/n).glob(n+'_*.pdf'));current=ROOT/n/pdf.name
  a=target/'fresh-pages'/n;b=target/'reviewed-pages'/n;a.mkdir(parents=True);b.mkdir(parents=True)
  for path,out in [(pdf,a),(current,b)]:subprocess.run(['pdftoppm','-r','110','-png',str(path),str(out/'p')],check=True)
  aa={p.name:sha(p) for p in a.glob('*.png')};bb={p.name:sha(p) for p in b.glob('*.png')}
  documents[n]={'fresh_pdf_sha256':sha(pdf),'reviewed_pdf_sha256':sha(current),'page_count':len(aa),'pixels_identical':aa==bb,'different_pages':sorted(k for k in aa.keys()|bb.keys() if aa.get(k)!=bb.get(k))}
  print(n,documents[n],flush=True)
 result={'source_tree':str(w),'sources':source_hashes,'no_generated_inputs':True,'documents':documents,'log':str(target/'build.log')}
 (HERE/'_build').mkdir(exist_ok=True);(HERE/'_build/clean_build.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 if not all(d['pixels_identical'] for d in documents.values()):raise SystemExit('Fresh PDFs differ visually; review listed pages.')
 print('Clean build and all page comparisons passed.',flush=True)
if __name__=='__main__':main()
