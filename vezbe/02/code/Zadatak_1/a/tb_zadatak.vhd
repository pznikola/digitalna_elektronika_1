library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tb_zadatak is
end entity tb_zadatak;

architecture sim of tb_zadatak is

    signal S : std_logic_vector(1 downto 0) := (others => '0');
    signal D : std_logic_vector(3 downto 0) := (others => '0');
    signal Y : std_logic;

begin

    -- Instanciraj Unit Under Test (UUT)
    uut: entity work.zadatak
        port map (
            S => S,
            D => D,
            Y => Y
        );

    -- Stimulus
    stim_proc: process
    begin
        -- Prvi patern: D0..D3 = 0,1,0,1
        D <= "1010";  -- D3=1, D2=0, D1=1, D0=0

        -- Testiramo sve kombinacije
        S <= "00"; wait for 10 ns;  -- S1=0,S0=0 => Y = D0 = 0
        S <= "01"; wait for 10 ns;  -- Y = D1 = 1
        S <= "10"; wait for 10 ns;  -- Y = D2 = 0
        S <= "11"; wait for 10 ns;  -- Y = D3 = 1

        -- Drugi patern: D0..D3 = 1,0,1,0 => D = "0101"
        D <= "0101";  -- D3=0, D2=1, D1=0, D0=1

        S <= "00"; wait for 10 ns;  -- Y = D0 = 1
        S <= "01"; wait for 10 ns;  -- Y = D1 = 0
        S <= "10"; wait for 10 ns;  -- Y = D2 = 1
        S <= "11"; wait for 10 ns;  -- Y = D3 = 0

        wait;
    end process;

end architecture sim;
