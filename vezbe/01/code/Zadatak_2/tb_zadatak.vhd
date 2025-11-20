library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;  -- needed for to_unsigned

entity tb_zadatak is
end tb_zadatak;

architecture Behavioral of tb_zadatak is

    -- Testbench signals
    signal ABCD : STD_LOGIC_VECTOR(3 downto 0);
    signal Y_ZP, Y_PZ : STD_LOGIC;

begin

    --------------------------------------------------------------------
    -- Device Under Test (DUT)
    --------------------------------------------------------------------
    UUT : entity work.zadatak
        port map (
            A    => ABCD(3),
            B    => ABCD(2),
            C    => ABCD(1),
            D    => ABCD(0),
            Y_ZP => Y_ZP,
            Y_PZ => Y_PZ
        );

    --------------------------------------------------------------------
    -- Stimulus process
    --------------------------------------------------------------------
    stim_proc : process
    begin
        -- Initialize
        ABCD <= (others => '0');
        wait for 10 ns;

        -- Apply all 4-bit combinations 0000 .. 1111
        for i in 0 to 15 loop
            ABCD <= std_logic_vector(to_unsigned(i, 4));
            wait for 10 ns;
        end loop;

        -- Stop simulation
        wait;
    end process;

end Behavioral;
