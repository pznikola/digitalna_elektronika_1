library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
entity test_predloga is end;
architecture tb of test_predloga is
 signal r:std_logic_vector(0 to 7):=(others=>'0');
 signal a,b:std_logic_vector(2 downto 0);
 signal av,bv:std_logic;
begin
 dut:entity work.Vprior2 port map(r,a,b,av,bv);
 process
 variable ea,eb,n:integer;
 begin
 for mask in 0 to 255 loop
 ea:=0;eb:=0;n:=0;
 for i in 0 to 7 loop
  if (mask/(2**i)) mod 2=1 then
   r(i)<='1';
   if n=0 then ea:=i; elsif n=1 then eb:=i; end if;
   n:=n+1;
  else r(i)<='0'; end if;
 end loop;
 wait for 1 ns;
 assert to_integer(unsigned(a))=ea and to_integer(unsigned(b))=eb
  report "Pogresan prioritet, mask="&integer'image(mask) severity failure;
 if n>0 then assert av='1' severity failure; else assert av='0' severity failure;end if;
 if n>1 then assert bv='1' severity failure; else assert bv='0' severity failure;end if;
 end loop;
 report "PROVERENO: svih 256 kombinacija prioriteta i zastavica";
 wait;
 end process;
end;
