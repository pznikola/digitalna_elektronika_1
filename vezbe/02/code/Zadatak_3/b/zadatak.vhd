library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity zadatak is
    port (
        A : in  STD_LOGIC_VECTOR(3 downto 0);   -- A(3)=MSB, A(0)=LSB
        Y : out STD_LOGIC_VECTOR(15 downto 0)   -- active LOW outputs
    );
end entity zadatak;

architecture Structural of zadatak is
    signal Y_low  : STD_LOGIC_VECTOR(7 downto 0);
    signal Y_high : STD_LOGIC_VECTOR(7 downto 0);
begin
    dec_low : entity work.decoder -- dekoder za donjih 8 bita
        port map (
            EN0   => '1',
            EN1_B => A(3),
            EN2_B => '0',
            A     => A(2 downto 0),
            Y     => Y_low
        );
    dec_high : entity work.decoder -- dekoder za gornjih 8 bita
        port map (
            EN0   => A(3),
            EN1_B => '0',
            EN2_B => '0',
            A     => A(2 downto 0),
            Y     => Y_high
        );
    -- Povezivanje izlaza
    Y( 7 downto 0) <= Y_low;
    Y(15 downto 8) <= Y_high;
    
end architecture Structural;
