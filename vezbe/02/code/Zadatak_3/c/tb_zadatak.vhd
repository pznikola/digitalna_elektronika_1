library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity tb_zadatak is
end entity tb_zadatak;

architecture sim of tb_zadatak is

    -- DUT signals
    signal ABC : std_logic_vector(2 downto 0) := (others => '0');
    signal Y_comb, Y_dekoder : std_logic;

begin

    -- Instantiate the Unit Under Test (UUT)
    uut : entity work.zadatak
        port map (
            A         => ABC(0),
            B         => ABC(1),
            C         => ABC(2),
            Y_comb    => Y_comb,
            Y_dekoder => Y_dekoder
        );

    -- Stimulus
    stim_proc : process
    begin

        for i in 0 to 7 loop
            ABC <= std_logic_vector(to_unsigned(i, 3));
            wait for 10 ns;
        end loop;

        -- End simulation
        wait;
    end process;

end architecture sim;
