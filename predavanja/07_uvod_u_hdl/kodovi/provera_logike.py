#!/usr/bin/env python3
"""Nezavisne provere prikazanih kodova; sintaksni obrasci nisu kompletni programi."""
import itertools
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def compact(name):
    return re.sub(r'\s+','',(ROOT/name).read_text())


def main():
    fuse_lines=(ROOT/'s008_jedec_osiguraci.jed').read_text().splitlines()
    zeros=[[2,30],[0,30],[4,30],[9,21,30],[9,16,30],[9,12,30],
           [1,3,5,8,31],[1,3,5,13,17,20,31],[3,30],[0,30],[4,30]]
    for i,line in enumerate(fuse_lines):
        address,bits=line.split()
        assert address==f'*L{32*i:05d}' and len(bits)==32
        assert [j for j,b in enumerate(bits) if b=='0']==zeros[i]
    assert len(fuse_lines)==11
    and_code=compact('s010_and1.abl')
    tests=re.findall(r'\[([01]),([01])\]->\[([01])\];',and_code)
    assert len(tests)==4
    for a,b,out in tests:assert int(out)==int(a)&int(b)
    priority=compact('s010_prioritet.abl')
    primary=[tuple(map(int,p)) for p in re.findall(r'WHENR(\d)==1THENA=(\d);',priority)]
    secondary=[tuple(map(int,p)) for p in re.findall(r'WHEN\(R(\d)==1\)&\(A!=(\d)\)THENB=(\d);',priority)]
    assert primary==[(i,i) for i in range(8)]
    assert secondary==[(i,i,i) for i in range(8)]
    for mask in range(256):
        active=[i for i in range(8) if mask>>i&1]
        a=next((out for bit,out in primary if mask>>bit&1),None)
        b=next((out for bit,exclude,out in secondary if mask>>bit&1 and a!=exclude),None)
        assert a==(active[0] if active else None)
        assert b==(active[1] if len(active)>1 else None)
    mux=compact('s011_multiplekser.abl')
    vectors=re.findall(r'\[([0-3]),([\dHLX]+),([\dHLX]+),([\dHLX]+)\]->(\d+);',mux)
    assert len(vectors)==12
    def value(v):return {'H':15,'L':0,'X':None}.get(v,int(v) if v.isdigit() else None)
    for sel,a,b,c,out in vectors:
        chosen=[a,b,c,c][int(sel)];assert value(chosen)==int(out)
    fulladd=(ROOT/'s024_potpuni_sabirac.vhd').read_text()
    equations=dict(re.findall(r'(s|Cout)\s*<=\s*(.*?);',fulladd))
    for x,y,carry in itertools.product([0,1],repeat=3):
        observed=[]
        for signal in ['s','Cout']:
            expr=equations[signal]
            assert set(re.findall(r'[A-Za-z]+',expr))<=set(['x','y','Cin','AND','OR','XOR'])
            expr=expr.replace('XOR','^').replace('AND','&').replace('OR','|')
            observed.append(eval(expr,{'__builtins__':{}},{'x':x,'y':y,'Cin':carry}))
        assert observed[0]+2*observed[1]==x+y+carry
    for x1,x2,x3 in itertools.product([0,1],repeat=3):
        diagram=(x1&x2)|((1-x2)&x3)
        assert diagram==(x1 if x2 else x3)
    a=compact('s028_dataflow_a.vhd');b=compact('s028_dataflow_b.vhd')
    def assignments(s):return sorted(re.findall(r'[BYZ]<=.*?;',s))
    assert assignments(a)==assignments(b)
    # Primer ostaje sintaksno neispravan: BIT:=1 i dodela portu B deklarisanom IN.
    assert 'BIT:=1' in a and 'B:inBIT' in a and 'B<=AandA;' in a
    q,nq=1,0
    states=[]
    for r in [1,1,1,0]:
        states.append((r,q,nq));q,nq=int(not(r or nq)),int(not q)
    assert states==[(1,1,0),(1,0,0),(1,0,1),(0,0,1)]
    # Izvorni VHDL prioritet ima delta oscilaciju. Zastavice se menjaju tek nakon procesa.
    av,bv=0,0;trace=[]
    for _ in range(6):
        na,nb=0,0;va,vb=0,0
        for i in [0,7]:
            if av==0:na=i;va=1
            elif bv==0:nb=i;vb=1
        av,bv=va,vb;trace.append((na,nb,av,bv))
    assert trace==[(7,0,1,0),(0,7,0,1)]*3
    print('Provereno: 352 JEDEC bita prema ručnom inventaru, 4 AND vektora, 256 ABEL prioriteta, 12 MUX vektora, 8 punih sabiranja, 8 kombinacija logičke šeme, isti dataflow izrazi i 4 SR koraka. Izvorne HDL greške nisu ispravljene.')


if __name__=='__main__':main()
