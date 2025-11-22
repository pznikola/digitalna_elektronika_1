library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tb_zadatak is
end entity tb_zadatak;

architecture sim of tb_zadatak is

    -- DUT signali
    signal A : std_logic_vector(2 downto 0) := (others => '0');
    signal Y : std_logic_vector(7 downto 0);

begin

    -- Instanciraj Unit Under Test (UUT)
    uut: entity work.zadatak
        port map (
            A => A,
            Y => Y
        );

    -- Stimulus process
    stim_proc: process
    begin
        -- Testiramo sve ulazne kombinacije

        A <= "000";  -- ocekujemo Y = 00000001
        wait for 10 ns;

        A <= "001";  -- ocekujemo Y = 00000010
        wait for 10 ns;

        A <= "010";  -- ocekujemo Y = 00000100
        wait for 10 ns;

        A <= "011";  -- ocekujemo Y = 00001000
        wait for 10 ns;

        A <= "100";  -- ocekujemo Y = 00010000
        wait for 10 ns;

        A <= "101";  -- ocekujemo Y = 00100000
        wait for 10 ns;

        A <= "110";  -- ocekujemo Y = 01000000
        wait for 10 ns;

        A <= "111";  -- ocekujemo Y = 10000000
        wait for 10 ns;

        -- Kraj simulacije
        wait;
    end process;

end architecture sim;
