#!/usr/bin/env python3
"""Nezavisne provere prepisanih kodnih tabela i računskih primera."""
import json
import math
import re
import struct
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def bcd(value):
    digits=[]
    while value:
        digit=value&15
        assert digit<10
        digits.append(digit);value>>=4
    return sum(d*10**i for i,d in enumerate(digits))


def table_bits(n):
    text=(ROOT/f'tabele/s{n:03d}_bcd_aritmetika.tex').read_text()
    rows={}
    for x,y,bit in re.findall(r'\\node\[text=[^\]]+\] at \(([\d.]+),(-[\d.]+)\) \{([01])\};',text):
        row=round(-float(y)/.43-.5)
        rows.setdefault(row,[]).append((float(x),bit))
    return {r:int(''.join(bit for x,bit in sorted(v)),2) for r,v in rows.items()}


def main():
    columns=json.loads((ROOT/'podaci/s003_ascii.json').read_text())['columns']
    assert len(columns)==8 and all(len(c)==16 for c in columns)
    for c in range(2,8):
        for r,text in enumerate(columns[c]):
            code=16*c+r
            if code==32:assert text=='SP'
            elif code==127:assert text=='DEL'
            else:assert ord(text)==code,(r,c,text)
    assert ord('1')-0x30==1 and ord('P')+0x20==ord('p')
    codes=json.loads((ROOT/'podaci/s004_bcd.json').read_text())
    for d,row in enumerate(codes):
        assert int(row[0],2)==d and int(row[1],2)-3==d
        for text,weights in [(row[2],[2,4,2,1]),(row[3],[8,4,-2,-1])]:
            assert sum(int(bit)*weight for bit,weight in zip(text,weights))==d
        for c in [1,2,3]:assert int(row[c],2)^15==int(codes[9-d][c],2)
    t=table_bits(5);assert t[0]+t[1]==t[2] and t[2]+t[3]==t[5];assert bcd(t[5])==72
    t=table_bits(6);assert t[0]+t[1]==t[2] and t[2]+(t[3]<<4)==t[4];assert bcd(t[4])%100==24
    t=table_bits(7);assert t[0]+t[1]==t[2]+16*t[3] and t[2]+16*t[3]+t[4]==t[5];assert bcd(t[5])-100==-24
    assert 19-53!=-24  # izvorni prvi red s7 protivreči ostatku slajda
    value=0
    for digit in '11110011':value=2*value+int(digit)
    assert value==243
    for n in [9,10]:
        data=json.loads((ROOT/f'podaci/s{n:03d}_koraci.json').read_text())
        final=''.join(c for c in data['rows'][-1][1:] if c in ['0','1'])
        assert bcd(int(final,2))==243
    rows=json.loads((ROOT/'podaci/s011_shift_add_3.json').read_text())
    decimal=0;binary='11110011';observed=[]
    for i in range(8):
        decimal=(decimal<<1)|int(binary[0]);binary=binary[1:]
        observed.append((decimal,binary))
        if i<7:
            for shift in [0,4,8]:
                if (decimal>>shift)&15>4:decimal+=3<<shift
    display_shift=[]
    for label,h,t,o,rest in rows:
        if label=='<<':display_shift.append((int((h or '0')+(t.zfill(4))+(o.zfill(4)),2),rest))
    assert display_shift==observed,(display_shift,observed)
    assert bcd(decimal)==243
    encoded=struct.unpack('>I',struct.pack('>f',13.25))[0]
    bits=f'{encoded:032b}'
    assert bits=='0'+'10000010'+'10101000000000000000000'
    decoded=struct.unpack('>f',int('1'+'10000110'+'01001000000000000000000',2).to_bytes(4,'big'))[0]
    assert decoded==-164 and int('101001',2)!=164
    for exponent in [1,254]:
        x=struct.unpack('>f',(exponent<<23).to_bytes(4,'big'))[0]
        assert math.isfinite(x) and x>0
    extra_checks()
    print('Kodovi 1–30: 128 ASCII ćelija (96 štampajućih/specijalnih pozicija računski), 40 BCD kodova i komplementi, tri BCD računa, koraci konverzije 243, FPF primeri i rubni normalni eksponenti. Grejov ciklus, parnost, CRC sa svim međukoracima i Hemingov (13,9) kod provereni. Izvorne greške sačuvane.')



def extra_checks():
    from itertools import combinations
    from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_UP, ROUND_DOWN, ROUND_CEILING, ROUND_FLOOR
    # Nezavisno izracunati svi prikazani rezultati zaokruzivanja.
    text=(ROOT/'tabele/s015_zaokruzivanje.tex').read_text()
    numeric=re.findall(r'([+-]\d+\.\d+)',text)
    values=[Decimal(x) for x in numeric]
    assert values[:4]==[Decimal(x) for x in ['11.5','12.5','-11.5','-12.5']]
    expected=[v.quantize(Decimal('1'),rounding=mode) for mode in [ROUND_HALF_EVEN,ROUND_HALF_UP,ROUND_DOWN,ROUND_CEILING,ROUND_FLOOR] for v in values[:4]]
    assert values[4:]==expected
    table=(ROOT/'tabele/s016_specijalni_kodovi.tex').read_text()
    for line in table.splitlines():
        cells=[re.sub(r'\s','',c) for c in line.split('&')]
        if len(cells)!=4 or not cells[0].isdigit():continue
        i=int(cells[0]);words=[re.sub(r'[^01]','',c) for c in cells[1:]]
        assert [int(v,2) for v in words]==[i,2**i-1,2**i]
    codes=json.loads((ROOT/'podaci/s017_grejov_kod.json').read_text())
    g=[int(v,2) for v in codes['gray']]
    assert g==[i^(i>>1) for i in range(16)]
    for seq in [g,[int(v,2) for v in codes['bcd'] if v]]:
        assert all((a^b).bit_count()==1 for a,b in zip(seq,seq[1:]+seq[:1]))
    # Izvorna povratna formula koristi samo susedna g; pravi inverz je kumulativni XOR.
    assert (g[8]^(g[8]>>1))!=8
    for value,gray in enumerate(g):
        decoded=0
        while gray:decoded^=gray;gray>>=1
        assert decoded==value
    parity=[]
    for line in (ROOT/'tabele/s022_bit_parnosti.tex').read_text().splitlines():
        cells=[re.sub(r'[^0-9]','',c) for c in line.split('&')]
        if len(cells)==4 and cells[0].isdigit() and len(cells[1])==3:
            d,b,p,c=cells;assert int(b,2)==int(d) and c==b+p and c.count('1')%2==0
            parity.append(int(c,2))
    assert len(parity)==8
    assert min((a^b).bit_count() for a,b in combinations(parity,2))==2
    assert all(((word^mask).bit_count()%2==1)==(mask.bit_count()%2==1) for word in parity for mask in range(16))
    def divmod_poly(num,den):
        q=0
        while num.bit_length()>=den.bit_length():
            shift=num.bit_length()-den.bit_length();q^=1<<shift;num^=den<<shift
        return q,num
    message=int('11100110',2);generator=int('11001',2)
    q,r=divmod_poly(message<<4,generator)
    assert q==sum(1<<i for i in [7,5,4,2,1]) and r==int('0110',2)
    assert divmod_poly((message<<4)|r,generator)[1]==0
    # Svaki prepisani petobitni ostatak i operacija, ne samo krajnji CRC.
    rows=json.loads((ROOT/'podaci/s025_crc_deljenje.json').read_text())
    def first(v):return v[0] if v else ''
    window=int(''.join(first(v) for v in rows[0][1:6]),2)
    for k in range(7):
        c=k+1;oprow=1+3*k;resultrow=oprow+1
        divisor=int(''.join(first(v) for v in rows[oprow][c:c+5]),2)
        assert divisor==(generator if window&16 else 0)
        window^=divisor
        assert int(''.join(first(v) for v in rows[resultrow][c:c+5]),2)==window
        nxt=first(rows[0][c+5]);window=(window<<1)|int(nxt)
    assert window==r
    assert int(''.join(first(v) for v in rows[-1] if v),2)==r
    tx=json.loads((ROOT/'podaci/s028_heming.json').read_text())
    rx=json.loads((ROOT/'podaci/s029_heming.json').read_text())
    for bit in range(4):
        for position in range(1,14):
            col=14-position
            assert (rx['rows'][bit+3][col]=='x')==bool(position&(1<<bit) or (bit==1 and position==13))
            assert (tx['rows'][bit+3][col]=='x')==bool((position&(1<<bit) and position!=1<<bit) or (bit==1 and position==13))
            assert ([bit+3,col] in tx['red'])==(position==1<<bit)
    # Svih 512 poruka skraćenog (13,9) koda; svih 13 jednobitnih kvarova.
    positions=[i for i in range(1,14) if i not in (1,2,4,8)]
    def syndrome(word):
        result=0
        for pos in range(1,14):
            if word>>(pos-1)&1:result^=pos
        return result
    words=[]
    for message in range(512):
        word=sum(((message>>i)&1)<<(pos-1) for i,pos in enumerate(positions))
        check=syndrome(word)
        for bit in range(4):word|=((check>>bit)&1)<<((1<<bit)-1)
        assert syndrome(word)==0;words.append(word)
        for pos in range(1,14):assert syndrome(word^(1<<(pos-1)))==pos
    assert min(w.bit_count() for w in words if w)==3
    assert (int('10011',2)^int('10110',2)).bit_count()==2
    assert min((a^b).bit_count() for a,b in combinations([2**i for i in range(8)],2))==2
    assert min((a^b).bit_count() for a,b in combinations([2**i-1 for i in range(8)],2))==1

if __name__=='__main__':main()
