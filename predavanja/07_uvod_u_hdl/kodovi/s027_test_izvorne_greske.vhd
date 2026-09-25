library ieee;
use ieee.std_logic_1164.all;
entity provera_vprior is end;
architecture test of provera_vprior is
signal r: std_logic_vector(0 to 7):="10000001";
signal a,b: std_logic_vector(2 downto 0);
signal av,bv: std_logic;
begin
u: entity work.Vprior2 port map(r,a,b,av,bv);
process
begin
for delta in 1 to 8 loop
wait for 0 ns;
report "delta=" & integer'image(delta) & " A=" & to_string(a) & " B=" & to_string(b) & " av=" & std_logic'image(av) & " bv=" & std_logic'image(bv);
end loop;
wait;
end process;
end;
