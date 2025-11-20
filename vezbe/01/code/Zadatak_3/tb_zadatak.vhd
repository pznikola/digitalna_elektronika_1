library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;  -- needed for to_unsigned

entity tb_zadatak is
end tb_zadatak;

architecture Behavioral of tb_zadatak is

    -- Testbench signals
    signal A, B : STD_LOGIC_VECTOR(1 downto 0);
    signal C    : STD_LOGIC_VECTOR(3 downto 0);

begin

    --------------------------------------------------------------------
    -- Device Under Test (DUT)
    --------------------------------------------------------------------
    UUT : entity work.zadatak
        port map (
            A => A,
            B => B,
            C => C
        );

    --------------------------------------------------------------------
    -- Stimulus process
    --------------------------------------------------------------------
    stim_proc : process
    begin
        -- Initialize
        A <= (others => '0');
        B <= (others => '0');

        -- Apply all 4-bit combinations 0000 .. 1111
        for i in 0 to 3 loop
          for j in 0 to 3 loop
            A <= std_logic_vector(to_unsigned(i, 2));
            B <= std_logic_vector(to_unsigned(j, 2));
            wait for 10 ns;
          end loop;
        end loop;

        -- Stop simulation
        wait;
    end process;

end Behavioral;
