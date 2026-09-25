"""Real exercise-02 VHDL, exhaustive domains and timing traces in isolated dirs."""
from pathlib import Path
import re,tempfile,json
from vhdl_check import run,vcd,value

def check02(folder):
 count=0;proof=[]
 def simulate(part,decl,ports,stim,files=None,generic='',transport=False,entity='zadatak'):
  nonlocal count
  src=folder/'code'/('Zadatak_'+part.split('/')[0])/part.split('/')[1]
  with tempfile.TemporaryDirectory(prefix='de1-ghdl02-') as td:
   w=Path(td);names=files or ([p.name for p in sorted(src.glob('*.vhd')) if p.name not in ['zadatak.vhd','tb_zadatak.vhd']]+['zadatak.vhd'])
   for name in names:
    s=(src/name).read_text()
    if transport:s=re.sub(r'<=\s*(?!transport)','<= transport ',s)
    (w/name).write_text(s)
   tb='library ieee;use ieee.std_logic_1164.all;use ieee.numeric_std.all;entity audit_tb is end;architecture test of audit_tb is '+decl+' begin DUT:entity work.'+entity+' '+generic+' port map('+ports+');process begin\n'+'\n'.join(stim)+'\nstd.env.stop;wait;end process;end;'
   (w/'audit_tb.vhd').write_text(tb)
   run(['ghdl','-a','--std=08',*names,'audit_tb.vhd'],w);run(['ghdl','-e','--std=08','audit_tb'],w)
   run(['ghdl','-r','--std=08','audit_tb','--assert-level=error','--vcd=audit.vcd'],w)
   trace=vcd(w/'audit.vcd')
   if entity=='zadatak' and not transport:
    (w/'tb_zadatak.vhd').write_text((src/'tb_zadatak.vhd').read_text())
    run(['ghdl','-a','--std=08','tb_zadatak.vhd'],w);run(['ghdl','-e','--std=08','tb_zadatak'],w);run(['ghdl','-r','--std=08','tb_zadatak','--assert-level=error'],w)
   count+=sum(line.count('assert ') for line in stim)
   proof.append(dict(part=part,entity=entity,mode='transport' if transport else 'inertial/default',assertions=sum(line.count('assert ') for line in stim),result='pass'))
   return trace
 def expect(expr,want):return f'assert {expr} = "{want}" report "{expr} mismatch" severity failure;'
 def bit(i):return "'"+str(int(bool(i)))+"'"
 stim=[]
 for s in range(4):
  for d in range(16):stim.append(f'S<="{s:02b}";D<="{d:04b}";wait for 1 ns;assert Y={bit(d>>s&1)} severity failure;')
 simulate('1/a','signal S:std_logic_vector(1 downto 0);signal D:std_logic_vector(3 downto 0);signal Y:std_logic;','S=>S,D=>D,Y=>Y',stim)
 stim=[]
 for a in range(2):
  for b in range(2):
   for c in range(4):
    y=[(a==b,a!=b),(a!=b,a==b),(not a and not b,not a and b),(a and b,a and not b)][c]
    stim.append(f'A<={bit(a)};B<={bit(b)};C<="{c:02b}";wait for 1 ns;'+expect('Y',''.join(str(int(x)) for x in y)))
 simulate('1/b','signal A,B:std_logic;signal C,Y:std_logic_vector(1 downto 0);','A=>A,B=>B,C=>C,Y=>Y',stim)
 def fun(i):return bool((i&4 and i&2)or(not(i&2)and i&1))
 pairs=[(i,i^(1<<j)) for i in range(8) for j in range(3)]
 for part in ['a','b','d']:
  for transport in [False,True]:
   stim=[]
   for a,b in pairs:
    for i in [a,b]:stim.append(f'X<="{i:03b}";wait for 100 ns;assert Y={bit(fun(i))} severity failure;')
   t=simulate('2/'+part,'signal X:std_logic_vector(2 downto 0);signal Y:std_logic;','A=>X(0),B=>X(1),C=>X(2),Y=>Y',stim,generic='generic map(T=>7 ns)',transport=transport)
   for j,(a,b) in enumerate(pairs):
    start=200*j+100
    if part=='a' and fun(a)!=fun(b):
     assert value(t['y'],start+6.5)==str(int(fun(a))) and value(t['y'],start+7.5)==str(int(fun(b))),('generic T ignored',part,a,b);count+=1
    if part=='b' and (a,b)==(7,5):
     for name,points in {'i1':[(.5,'0'),(7.5,'1')],'i2':[(.5,'0'),(7.5,'1')],'i3':[(7.5,'1'),(14.5,'0')],'y':[(13.5,'1'),(14.5,'0'),(21.5,'1')]}.items():
      for dt,w in points:assert value(t[name],start+dt)==w,(part,transport,name,dt);count+=1
    if part=='b' and (a,b)==(5,7) or part=='d' and fun(a)==fun(b):
     assert all(v==str(int(fun(a))) for ts,v in t['y'] if start<ts<start+100),(part,transport,a,b,'unexpected pulse');count+=1
 for part,width,owidth in [('a',3,8),('b',4,16)]:
  stim=[]
  for i in range(2**width):
   val=1<<i
   if part=='b':val^=(1<<owidth)-1
   stim.append(f'A<="{i:0{width}b}";wait for 1 ns;'+expect('Y',f'{val:0{owidth}b}'))
  stim.append('A<=(others=>\'U\');wait for 1 ns;assert is_x(Y) severity failure;')
  simulate('3/'+part,f'signal A:std_logic_vector({width-1} downto 0);signal Y:std_logic_vector({owidth-1} downto 0);','A=>A,Y=>Y',stim)
 stim=[]
 for i in range(8):
  w=bit(i not in [0,2,7]);stim.append(f'X<="{i:03b}";wait for 1 ns;assert Y_comb={w} and Y_dekoder={w} severity failure;')
 simulate('3/c','signal X:std_logic_vector(2 downto 0);signal Y_comb,Y_dekoder:std_logic;','A=>X(0),B=>X(1),C=>X(2),Y_comb=>Y_comb,Y_dekoder=>Y_dekoder',stim)
 for part in ['b','c']:
  stim=[]
  for en in range(8):
   for i in range(8):
    val=255^(1<<i) if en==4 else 255
    stim.append(f'EN<="{en:03b}";A<="{i:03b}";wait for 1 ns;'+expect('Y',f'{val:08b}'))
  for en,addr,w in [('100','UUU','XXXXXXXX'),('000','UUU','11111111'),('U00','000','XXXXXXXX'),('111','ZZZ','11111111')]:
   stim.append(f'EN<="{en}";A<="{addr}";wait for 1 ns;'+expect('Y',w))
  simulate('3/'+part,'signal EN,A:std_logic_vector(2 downto 0);signal Y:std_logic_vector(7 downto 0);','EN0=>EN(2),EN1_B=>EN(1),EN2_B=>EN(0),A=>A,Y=>Y',stim,files=['decoder.vhd'],entity='decoder')
 out=folder.parent/'PROVERA/_build';out.mkdir(exist_ok=True);(out/'ghdl02.json').write_text(json.dumps(proof,indent=2)+'\n');return count
