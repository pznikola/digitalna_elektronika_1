library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity zadatak is
    port (
        A, B, C, D : in  STD_LOGIC;
        Y_ZP, Y_PZ : out STD_LOGIC
    );
end zadatak;

architecture Behavioral of zadatak is
    -- interni signali
    signal A_n, C_n, D_n : STD_LOGIC;
begin
    --------------------------------------------------------------------
    -- Invertovane vrednost signala
    --------------------------------------------------------------------
    A_n <= not A;
    C_n <= not C;
    D_n <= not D;
    --------------------------------------------------------------------
    -- Y_ZP = A_n C_n D + A C_n D_n + BC
    --------------------------------------------------------------------
    Y_ZP <= (A_n and C_n and D) or (A and C_n and D_n) or (B and C);
    --------------------------------------------------------------------
    -- Y_PZ = (A + C + D)(A_n + C + D_n)(B + C_n)
    --------------------------------------------------------------------
    Y_PZ <= (A or C or D) and (A_n or C or D_n) and (B or C_n);
end Behavioral;