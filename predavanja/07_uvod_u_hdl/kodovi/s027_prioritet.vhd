library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.std_logic_arith.all;
entity Vprior2 is port (
R:in STD_LOGIC_VECTOR (0 to 7);
A,B:out STD_LOGIC_VECTOR (2 downto 0);
AVALID,BVALID:buffer STD_LOGIC); end Vprior2;
architecture Vprior2_arch of Vprior2 is
begin process(R,AVALID,BVALID) begin
AVALID<='0'; BVALID<='0';
A<="000"; B<="000";
for i in 0 to 7 loop
if R(i)='1' and AVALID='0' then
A<=CONV_STD_LOGIC_VECTOR(i,3); AVALID<='1';
elsif R(i)='1' and BVALID='0' then
B<=CONV_STD_LOGIC_VECTOR(i,3);
BVALID<='1'; end if; end loop;
end process; end Vprior2_arch;
