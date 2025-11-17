library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity zadatak_4 is
    generic (
        T : time := 1 ns   -- globalni delay parametar
    );
    port (
        A : in  STD_LOGIC;
        B : in  STD_LOGIC;
        C : in  STD_LOGIC;
        D : in  STD_LOGIC;
        Y : out STD_LOGIC
    );
end zadatak_4;

architecture Structural of zadatak_4 is

    -- interni signali
    signal B_inv, I1 : STD_LOGIC;
    signal I2, I3, I4 : STD_LOGIC;
begin

    --------------------------------------------------------------------
    -- Invertori: B_inv = inv B, I1 = inv D
    --------------------------------------------------------------------
    U_INV_B : entity work.INV
        generic map ( T => T )
        port map (
            A => B,
            Y => B_inv
        );

    U_INV_D : entity work.INV
        generic map ( T => T )
        port map (
            A => D,
            Y => I1
        );

    --------------------------------------------------------------------
    -- I2 = A + B_inv
    --------------------------------------------------------------------
    U_I2 : entity work.AND2
        generic map ( T => T )
        port map (
            A => A,
            B => B_inv,
            Y => I2
        );

    --------------------------------------------------------------------
    -- I3 = C D
    --------------------------------------------------------------------
    U_I3 : entity work.AND2
        generic map ( T => T )
        port map (
            A => C,
            B => D,
            Y => I3
        );

    --------------------------------------------------------------------
    -- I4 = A and C and I1   (A C \bar{D})
    --------------------------------------------------------------------
    U_I4 : entity work.AND3
        generic map ( T => T )
        port map (
            A => A,
            B => C,
            C => I1,
            Y => I4
        );

    --------------------------------------------------------------------
    -- Single 3-input OR:
    -- Y = I2 + I3 + I4
    --------------------------------------------------------------------
    U_OR3 : entity work.OR3
        generic map ( T => T )
        port map (
            A => I2,
            B => I3,
            C => I4,
            Y => Y
        );

end Structural;
