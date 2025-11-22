library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity zadatak is
    generic (
        T : time := 10 ns   -- globalni delay parametar
    );
    port (
        A, B, C : in  STD_LOGIC;
        Y       : out STD_LOGIC
    );
end entity zadatak;

architecture Structural of zadatak is

  signal I1, I2, I3: STD_LOGIC;

begin

  ----------------------------------------------------------------------------------
  -- I1 = ¬(C · B)
  I1 <= (C nand B) after T;
  ----------------------------------------------------------------------------------
  -- I2 = ¬(B · B)
  I2 <= (B nand B) after T;
  ----------------------------------------------------------------------------------
  -- I3 = ¬(A · I2)
  I3 <= (A nand I2) after T;
  ----------------------------------------------------------------------------------
  -- Y = ¬(I1 · I3)
  Y <= (I1 nand I3) after T;
  
end architecture Structural;
