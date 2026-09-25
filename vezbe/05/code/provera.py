#!/usr/bin/env python3
"""Iscrpne provere kodova, parnosti, BCD sabiranja i Hamingovih kodova."""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as F
import json,re
root=Path(__file__).resolve().parents[1];data=json.loads((root/'code/rezultati.json').read_text());codes=data['codes'];tex=(root/'05_kodovi.tex').read_text();checks=0
def check(ok,msg=''):
    global checks
    assert ok,msg
    checks+=1
def hdist(a,b):return sum(x!=y for x,y in zip(a,b))
def gray_decode(bits):
    prev=0;out=''
    for ch in bits:prev^=int(ch);out+=str(prev)
    return out
for key,table in codes.items():
    check(len(table)==10 and len(set(table))==10)
    for i,word in enumerate(table):
        check(len(word)==4 and set(word)<=set('01'))
        if key=='BCD':check(sum(int(x)*w for x,w in zip(word,[8,4,2,1]))==i)
        if key=='BCD2421':check(sum(int(x)*w for x,w in zip(word,[2,4,2,1]))==i)
        if key=='Više 3':check(int(word,2)-3==i)
        if key in ['BCD2421','Više 3']:check(int(word,2)^int(table[9-i],2)==15)
        if key=='Grej BCD':check(hdist(word,table[(i+1)%10])==1)
for rec in data['encodings']:
    for key,code in zip(codes,rec['values']):
        decoded=''.join(str(codes[key].index(w)) for w in code.split());check(int(decoded)==rec['number'])
        check(code in tex)
    check(int(gray_decode(rec['gray']),2)==rec['number'])
for rec in data['decodings']:
    before,after=rec['bits'].split('.')
    a=before.zfill((len(before)+3)//4*4);b=after.ljust((len(after)+3)//4*4,'0')
    for key,value in zip(codes,rec['values']):
        groups=[a[i:i+4] for i in range(0,len(a),4)]+[b[i:i+4] for i in range(0,len(b),4)]
        valid=all(w in codes[key] for w in groups)
        check(valid==(value is not None))
        if valid:check(value==''.join(str(codes[key].index(a[i:i+4])) for i in range(0,len(a),4))+'.'+''.join(str(codes[key].index(b[i:i+4])) for i in range(0,len(b),4)))
    result=gray_decode(before+after);check(result==rec['gray_binary'].replace('.',''));check(F(int(result,2),2**len(after))==F(rec['gray_decimal']))
for key,rec in data['neighbors'].items():
    start=rec['start'];items=rec['items'];check(len(items)==len(start))
    check(len({x['word'] for x in items})==len(start))
    for item in items:
        word=item['word'];check(hdist(start,word)==1)
        if key=='Grej binarni':check(int(item['value'])==int(gray_decode(word),2))
        else:
            valid=word[:4] in codes[key] and word[4:] in codes[key];check(valid==(item['value'] is not None))
            if valid:check(int(item['value'])==10*codes[key].index(word[:4])+codes[key].index(word[4:]))
for a,b,c in product(range(10),range(10),range(2)):
    total=a+b+c;low=total&15;binary_carry=total>>4;need=bool(binary_carry or low>9);corrected=total+6*need
    check((corrected>>4,corrected&15)==divmod(total,10))
for rec in data['additions']:
    result=0
    for i,(a,b,cin,total,corr,digit,cout) in enumerate(rec['steps']):
        check(a+b+cin==total);check(corr==(6 if total>9 else 0));check((total+corr)==16*cout+digit);result+=digit*10**i
    result+=cout*10**len(rec['steps']);check(result==rec['result']==rec['a']+rec['b'])
for bits in ['100101','10101011','1101011','110100101']:
    even=bits+str(sum(map(int,bits))%2);odd=bits+str(1-sum(map(int,bits))%2)
    check(sum(map(int,even))%2==0 and sum(map(int,odd))%2==1);check(even in tex and odd in tex)
# Hamming: use parity-check columns indexed 1..7; message bits placed at 3,5,6,7.
def syndrome(w):
    s=0
    for pos,bit in enumerate(reversed(w),1):
        if bit=='1':s^=pos
    return s
def encode(message):
    w=[0]*8
    for pos,bit in zip([3,5,6,7],message):w[pos]=bit
    for p in [1,2,4]:w[p]=sum(w[i] for i in range(1,8) if i&p)%2
    return ''.join(str(w[i]) for i in range(7,0,-1))
def flip(w,*positions):
    a=list(w)
    for i in positions:a[i]=str(1-int(a[i]))
    return ''.join(a)
words=[encode(msg) for msg in product(range(2),repeat=4)]
check(min(hdist(a,b) for a,b in combinations(words,2))==3)
for w in words:
    check(syndrome(w)==0)
    for i in range(7):
        damaged=flip(w,i);s=syndrome(damaged);check(s==7-i);check(flip(damaged,7-s)==w)
    for i,j in combinations(range(7),2):check(syndrome(flip(w,i,j))!=0)
extended=[w+str(sum(map(int,w))%2) for w in words]
check(min(hdist(a,b) for a,b in combinations(extended,2))==4)
for w in extended:
    for i in range(8):
        damaged=flip(w,i);s=syndrome(damaged[:7]);p=sum(map(int,damaged))%2
        check(p==1);corrected=flip(damaged,7-s if s else 7);check(corrected==w)
    for i,j in combinations(range(8),2):
        damaged=flip(w,i,j);check(sum(map(int,damaged))%2==0 and syndrome(damaged[:7])!=0)
check(syndrome('1011100')==5);check(syndrome('1001100')==0);check('10011001' in extended);check(2**5-5-1==26)
for d,t,u in [(4,0,3),(4,1,2),(5,0,4),(5,1,3),(5,2,2)]:check(d>=t+u+1 and u>=t)
labels=re.findall(r'\\label\{([^}]+)\}',tex);check(len(labels)==len(set(labels)))
for ref in re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',tex):check(ref in labels,ref)
check('\toprule' not in tex)
# Reflected Gray construction and every actual drawn hypercube edge.
for n in range(2,5):
    prev=[format(i^(i>>1),f'0{n-1}b') for i in range(2**(n-1))]
    reflected=['0'+w for w in prev]+['1'+w for w in reversed(prev)]
    check(reflected==[format(i^(i>>1),f'0{n}b') for i in range(2**n)])
cube=(root/'Images/Uvod/kocke.tex').read_text()
for prefix,n in [('a',1),('b',2),('c',3)]:
    edges=re.findall(r'\('+prefix+r'([01]+)\)--\('+prefix+r'([01]+)\)',cube)
    check(len(edges)==n*2**(n-1))
    for a,b in edges:check(hdist(a,b)==1)
from audit_math import run
run(root,check,data)

print(f'Vežbe 05: {checks} provera uspešno završeno.')
