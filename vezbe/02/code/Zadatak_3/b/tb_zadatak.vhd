library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity tb_zadatak is
end entity tb_zadatak;

architecture sim of tb_zadatak is

    -- DUT signals
    signal A : std_logic_vector(3 downto 0) := (others => '0');
    signal Y : std_logic_vector(15 downto 0);

begin

    -- Instantiate the Unit Under Test (UUT)
    uut : entity work.zadatak
        port map (
            A => A,
            Y => Y
        );

    -- Stimulus
    stim_proc : process
    begin

        for i in 0 to 15 loop
            A <= std_logic_vector(to_unsigned(i, 4));
            wait for 10 ns;
        end loop;

        -- End simulation
        wait;
    end process;

end architecture sim;
