library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity zadatak is
    generic ( T : time := 10 ns ); -- delay parametar
    port    ( A, B, C : in  STD_LOGIC;
              Y       : out STD_LOGIC );
end entity zadatak;
architecture Structural of zadatak is
  signal I1, I2, I3: STD_LOGIC;
begin
  I1 <= (C and B) after T;        -- I1 = C · B
  I2 <= (not B and A) after T;    -- I2 = ¬B · A
  I3 <= (C and A) after T;        -- I3 = C · A
  Y  <= (I1 or I2 or I3) after T; -- Y = I1 + I2 + I3
end architecture Structural;
