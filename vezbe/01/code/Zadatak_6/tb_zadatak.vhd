library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tb_zadatak is
end tb_zadatak;

architecture Behavioral of tb_zadatak is

    -- Testbench signals
    signal ABCD : STD_LOGIC_VECTOR(3 downto 0);
    signal Y_min, Y_no_hazard : STD_LOGIC;

begin

    -- Device Under Test (DUT)
    UUT : entity work.zadatak
        generic map (
            T => 10 ns        -- Staviti zeljeno kasnjenje
        )
        port map (
            A           => ABCD(3),
            B           => ABCD(2),
            C           => ABCD(1),
            D           => ABCD(0),
            Y_min       => Y_min,
            Y_no_hazard => Y_no_hazard
        );

    -- Stimulus
    stim_proc : process
    begin
        ABCD <= "0101";
        wait for 50 ns;

        ABCD <= "0100";
        wait for 50 ns;

        ABCD <= "0101";
        wait for 50 ns;

        ABCD <= "0001";
        wait for 50 ns;

        ABCD <= "0011";
        wait for 50 ns;

        ABCD <= "1011";
        wait for 50 ns;

        ABCD <= "0011";
        wait for 50 ns;

        ABCD <= "0111";
        wait for 50 ns;

        ABCD <= "1111";
        wait for 50 ns;

        ABCD <= "0111";
        wait for 50 ns;

        ABCD <= "1111";
        wait for 50 ns;

        ABCD <= "1110";
        wait for 50 ns;

        ABCD <= "1100";
        wait for 50 ns;

        ABCD <= "1110";
        wait for 50 ns;

        -- Kraj simulacije
        wait;
    end process;

end Behavioral;
