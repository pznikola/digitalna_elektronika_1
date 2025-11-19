library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tb_zadatak is
end tb_zadatak;

architecture Behavioral of tb_zadatak is

    -- Testbench signals
    signal ABCD : STD_LOGIC_VECTOR(3 downto 0);
    signal Y : STD_LOGIC;

begin

    -- Device Under Test (DUT)
    UUT : entity work.zadatak
        generic map (
            T => 10 ns        -- Staviti zeljeno kasnjenje
        )
        port map (
            A => ABCD(3),
            B => ABCD(2),
            C => ABCD(1),
            D => ABCD(0),
            Y => Y
        );

    -- Stimulus
    stim_proc : process
    begin
        -- Pocetne vrednosti: ABCD = 1111
        ABCD <= "1111";
        wait for 50 ns;

        -- Promena na ABCD = 1110
        ABCD <= "1110";
        wait for 50 ns;

        -- Kraj simulacije
        wait;
    end process;

end Behavioral;
