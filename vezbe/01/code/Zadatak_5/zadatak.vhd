library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity zadatak is
    generic (
        T : time := 1 ns   -- globalni delay parametar
    );
    port (
        A, B, C, D: in  STD_LOGIC;
        Y_min, Y_no_hazard : out STD_LOGIC
    );
end zadatak;

architecture Behavioral of zadatak is
    -- interni signali
    signal A_inv, C_inv : STD_LOGIC;
    signal I1, I2, I3, I4, I5 : STD_LOGIC;
begin
    --------------------------------------------------------------------
    -- Invertovane vrednosti
    A_inv <= (not A) after T;
    C_inv <= (not C) after T;
    --------------------------------------------------------------------
    -- I1 = A_n C_n
    I1 <= (A_inv and C_inv) after T;
    --------------------------------------------------------------------
    -- I2 = C D
    I2 <= (C and D) after T;
    --------------------------------------------------------------------
    -- I3 = B C
    I3 <= (B and C) after T;
    --------------------------------------------------------------------
    -- I4 = A_n B
    I4 <= (A_inv and B) after T;
    --------------------------------------------------------------------
    -- I5 = A_n D
    I5 <= (A_inv and D) after T;
    --------------------------------------------------------------------
    -- Y_min = A_n C_n + C D + BC = I1 + I2 + I3
    Y_min <= (I1 or I2 or I3) after T;
    --------------------------------------------------------------------
    -- Y_no_hazard = A_n C_n + CD + BC + A_nB + A_nD 
    --             = I1 + I2 + I3 + I4 + I5
    Y_no_hazard <= (I1 or I2 or I3 or I4 or I5) after T;

end Behavioral;