library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity zadatak is
    port (
        A, B, C : in  STD_LOGIC;
        Y_comb, Y_dekoder : out STD_LOGIC
    );
end entity zadatak;

architecture Structural of zadatak is

    signal A_dec: STD_LOGIC_VECTOR(2 downto 0);
    signal Y_dec: STD_LOGIC_VECTOR(7 downto 0);

begin
    A_dec <= C & B & A;

    -- decoder
    udec : entity work.decoder
        port map (
            EN0   => '1',
            EN1_B => '0',
            EN2_B => '0',
            A     => A_dec,
            Y     => Y_dec
        );

    --------------------------------------------------------------------------------------
    -- Y_comb    = (C + B + A)(C + ¬B + A)(¬C + ¬B + ¬A)
    -- Y_dekoder = ¬Y0 ¬Y2 ¬Y7 (ovi izlazi vec imaju komplement zbog dekodera)
    Y_comb    <= (C or B or A) and (C or not B or A) and (not C or not B or not A);
    Y_dekoder <= Y_dec(0) and Y_dec(2) and Y_dec(7);

end architecture Structural;
