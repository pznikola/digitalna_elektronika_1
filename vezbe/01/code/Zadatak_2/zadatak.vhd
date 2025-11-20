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
    signal A_n, B_n, C_n, D_n : STD_LOGIC;
begin
    --------------------------------------------------------------------
    -- Invertovane vrednost signala
    --------------------------------------------------------------------
    A_n <= not A;
    B_n <= not B;
    C_n <= not C;
    D_n <= not D;
    --------------------------------------------------------------------
    -- Y_ZP = C_n D_n + A_n B_n + B_n C_n
    --------------------------------------------------------------------
    Y_ZP <= (C_n and D_n) or (A_n and B_n) or (B_n and C_n);
    --------------------------------------------------------------------
    -- Y_PZ = (B_n + C_n)(B_n + D_n)(A_n + C_n)
    --------------------------------------------------------------------
    Y_PZ <= (B_n or C_n) and (B_n or D_n) and (A_n or C_n);
end Behavioral;