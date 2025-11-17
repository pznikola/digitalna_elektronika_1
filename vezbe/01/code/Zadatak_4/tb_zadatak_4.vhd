library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tb_zadatak_4 is
end tb_zadatak_4;

architecture Behavioral of tb_zadatak_4 is

    -- DUT signals
    signal A, B, C, D : STD_LOGIC := '0';
    signal Y          : STD_LOGIC;

begin

    -- Instantiate the Device Under Test (DUT)
    UUT : entity work.zadatak_4
        generic map (
            T => 10 ns        -- choose any delay you like
        )
        port map (
            A => A,
            B => B,
            C => C,
            D => D,
            Y => Y
        );

    -- Stimulus process
    stim_proc : process
    begin
        -- Initial values: ABCD = 1111
        A <= '1';
        B <= '1';
        C <= '1';
        D <= '1';
        wait for 50 ns;

        -- Change to ABCD = 1110
        D <= '0';
        wait for 50 ns;

        -- End simulation
        wait;
    end process;

end Behavioral;
