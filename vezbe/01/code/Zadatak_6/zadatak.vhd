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
    signal A_inv, B_inv, C_inv, D_inv : STD_LOGIC;
    signal I1, I2, I3, I4, I5, I6 : STD_LOGIC;
begin
    ---------------------------------------------------------------------------
    -- Invertovane vrednosti
    A_inv <= (not A) after T;
    B_inv <= (not B) after T;
    C_inv <= (not C) after T;
    D_inv <= (not D) after T;
    ---------------------------------------------------------------------------
    -- I1 = (B_n + C + D)
    I1 <= (B_inv or C or D) after T;
    ---------------------------------------------------------------------------
    -- I2 = (A + D_n)
    I2 <= (A or D_inv) after T;
    ---------------------------------------------------------------------------
    -- I3 = (A_n + C_n)
    I3 <= (A_inv or C_inv) after T;
    ---------------------------------------------------------------------------
    -- I4 = (C_n + D_n)
    I4 <= (C_inv or D_inv) after T;
    ---------------------------------------------------------------------------
    -- I5 = (A + B_n + C)
    I5 <= (A or B_inv or C) after T;
    ---------------------------------------------------------------------------
    -- I6 = (A_n + B_n + D)
    I6 <= (A_inv or B_inv or D) after T;
    ---------------------------------------------------------------------------
    -- Y_min = (B_n + C + D)(A + D_n)(A_n + C_n) = I1 I2 I3
    Y_min <= (I1 and I2 and I3) after T;
    ---------------------------------------------------------------------------
    -- Y_no_hazard = 
    -- (B_n + C + D)(A + D_n)(A_n + C_n)(C_n + D_n)(A + B_n + C)(A_n + B_n + D)
    -- I1 I2 I3 I4 I4 I6
    Y_no_hazard <= (I1 and I2 and I3 and I4 and I5 and I6) after T;

end Behavioral;