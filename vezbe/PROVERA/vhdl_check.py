"""Compile the real VHDL in isolated temporary workdirs and check its event traces."""
from pathlib import Path
import itertools,subprocess,tempfile,re,json

def run(args,cwd):
 p=subprocess.run(args,cwd=cwd,capture_output=True,text=True)
 if p.returncode:raise AssertionError(' '.join(args)+'\n'+p.stdout+p.stderr)
 return p.stdout

def vcd(path):
 names={};traces={};time=0;scale=1
 for line in path.read_text().splitlines():
  x=line.split()
  if len(x)>4 and x[0]=='$var':names[x[3]]=x[4].lower();traces[x[4].lower()]=[]
  elif line.startswith('#'):time=int(line[1:])
  elif x and x[0][0] in '01xXuUzZ' and len(x)==1:
   if x[0][1:] in names:traces[names[x[0][1:]]].append((time,x[0][0].lower()))
  elif x and x[0].startswith('b') and len(x)==2 and x[1] in names:traces[names[x[1]]].append((time,x[0][1:].lower()))
 # GHDL emits 1 fs; fail explicitly if the tool changes its time unit.
 assert re.search(r'\$timescale\s+1\s+fs\s+\$end',path.read_text())
 return {n:[(t/1e6,v) for t,v in seq] for n,seq in traces.items()} # ns

def value(seq,t):
 vals=[v for ts,v in seq if ts<=t];assert vals,(seq,t);return vals[-1]

def check01(folder):
 count=0;proof=[]
 def expected(task,i):
  a,b,c,d=[bool(i>>(3-j)&1) for j in range(4)]
  if task==1:return int((a or c or d)and(not a or c or not d)and(b or not c))
  if task==2:return int('00' in f'{i:04b}')
  if task==3:return (i//4)*(i%4)
  if task==4:return int(a and not b or c and d or a and c and not d)
  if task==5:return int(not a and not c or c and d or b and c and not d)
  return int(not b and not c and not d or a and not c and d or not a and c and not d)
 for task in range(1,7):
  outputs=['C'] if task==3 else ['Y_ZP','Y_PZ'] if task<3 else ['Y'] if task==4 else ['Y_min','Y_no_hazard']
  pairs=[(i,i^(1<<j)) for i in range(16) for j in range(4)] if task>=4 else [(i,i) for i in range(16)]
  for mode in (['inertial','transport'] if task>=4 else ['zero-delay']):
   with tempfile.TemporaryDirectory(prefix=f'de1-ghdl01-{task}-') as td:
    work=Path(td);src=(folder/'code'/f'Zadatak_{task}'/'zadatak.vhd').read_text()
    if mode=='transport':src=re.sub(r'<=\s*(?!transport)', '<= transport ',src)
    (work/'dut.vhd').write_text(src)
    outdecl='signal C: std_logic_vector(3 downto 0);' if task==3 else 'signal '+','.join(outputs)+': std_logic;'
    ports='A=>X(3 downto 2),B=>X(1 downto 0),C=>C' if task==3 else 'A=>X(3),B=>X(2),C=>X(1),D=>X(0),'+','.join(o+'=>'+o for o in outputs)
    stim=[]
    for a,b in pairs:
     stim += [f'X <= "{a:04b}"; wait for 20 ns;',f'X <= "{b:04b}"; wait for 20 ns;']
    tb='library ieee; use ieee.std_logic_1164.all; entity audit_tb is end; architecture test of audit_tb is signal X: std_logic_vector(3 downto 0); '+outdecl+' begin U: entity work.zadatak '+('generic map (T=>2 ns) ' if task>=4 else '')+'port map ('+ports+'); process begin '+'\n'.join(stim)+' std.env.stop; wait; end process; end;'
    (work/'tb.vhd').write_text(tb)
    run(['ghdl','-a','--std=08','dut.vhd','tb.vhd'],work);run(['ghdl','-e','--std=08','audit_tb'],work);run(['ghdl','-r','--std=08','audit_tb','--vcd=audit.vcd','--assert-level=error'],work)
    traces=vcd(work/'audit.vcd')
    for j,(a,b) in enumerate(pairs):
     for word,t in [(a,40*j+19),(b,40*j+39)]:
      for output in outputs:
       name='c[3:0]' if task==3 else output.lower();got=value(traces[name],t)
       assert int(got,2)==expected(task,word),(task,mode,word,output,got);count+=1
     if task>=5 and expected(task,a)==expected(task,b):
      constant=str(expected(task,a));start=j*40+20;end=j*40+39
      assert value(traces['y_no_hazard'],start)==constant
      assert all(v==constant for t,v in traces['y_no_hazard'] if start<t<=end),(task,mode,a,b,'hazard-free output pulse');count+=1
     if task==4 and (a,b)==(15,14):
      t=40*j+20
      for name,points in {'i1':[(.5,'0'),(2.5,'1')],'i2':[(.5,'0'),(7,'0')],'i3':[(.5,'1'),(2.5,'0')],'i4':[(2.5,'0'),(4.5,'1')],'y':[(2.5,'1'),(4.5,'0'),(6.5,'1')]}.items():
       for dt,want in points:assert value(traces[name],t+dt)==want,(mode,name,dt,traces[name]);count+=1
     if task==4 and (a,b)==(14,15):
      t=40*j+20;assert all(v=='1' for ts,v in traces['y'] if t<ts<=t+19);count+=1
    proof.append({'task':task,'mode':mode,'states_or_transitions':len(pairs),'result':'pass'})
 out=folder.parent/'PROVERA'/'_build';out.mkdir(exist_ok=True)
 (out/'ghdl01.json').write_text(json.dumps(proof,indent=2)+'\n')
 return count
