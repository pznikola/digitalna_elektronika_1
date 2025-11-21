library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity zadatak is
    port (
        A, B : in  STD_LOGIC;
        C    : in  STD_LOGIC_VECTOR(1 downto 0); -- C(1)=C1, C(0)=C0
        Y    : out STD_LOGIC_VECTOR(1 downto 0)  -- Y(1)=Y1, Y(0)=Y0
    );
end entity zadatak;

architecture Structural of zadatak is
    signal D_Y1 : STD_LOGIC_VECTOR(3 downto 0);  -- D ulazi za MUX 1
    signal D_Y0 : STD_LOGIC_VECTOR(3 downto 0);  -- D ulazi za MUX 0
    signal axb  : STD_LOGIC;                     -- A xor B
begin
    axb <= A xor B;
    --------------------------------------------------------------------
    -- C1C0 = 00 : Y0 =  A xor B    -> D_Y0(0)
    -- C1C0 = 01 : Y0 = ¬(A xor B)  -> D_Y0(1)
    -- C1C0 = 10 : Y0 = ¬A · B      -> D_Y0(2)
    -- C1C0 = 11 : Y0 =  A · ¬B     -> D_Y0(3)
    D_Y0(0) <= axb;
    D_Y0(1) <= not axb;
    D_Y0(2) <= (not A) and B;
    D_Y0(3) <= A and (not B);
    --------------------------------------------------------------------
    -- C1C0 = 00 : Y1 = ¬(A xor B)  -> D_Y1(0)
    -- C1C0 = 01 : Y1 =  A xor B    -> D_Y1(1)
    -- C1C0 = 10 : Y1 = ¬A · ¬B     -> D_Y1(2)
    -- C1C0 = 11 : Y1 =  A · B      -> D_Y1(3)
    D_Y1(0) <= not axb;
    D_Y1(1) <= axb;
    D_Y1(2) <= (not A) and (not B);
    D_Y1(3) <= A and B;
    --------------------------------------------------------------------
    -- Instanciranje dva multipleksera
    mux_Y1 : entity work.mux4
        port map (
            S => C,
            D => D_Y1,
            Y => Y(1)
        );

    mux_Y0 : entity work.mux4
        port map (
            S => C,
            D => D_Y0,
            Y => Y(0)
        );

end architecture Structural;
