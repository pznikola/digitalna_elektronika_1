library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tb_zadatak is
end entity tb_zadatak;

architecture sim of tb_zadatak is

    signal A : std_logic := '0';
    signal B : std_logic := '0';
    signal C : std_logic := '0';
    signal Y : std_logic;

begin

    -- Instanciraj Unit Under Test (UUT)
    uut : entity work.zadatak
        generic map (
            T => 20 ns -- Staviti zeljeno kasnjenje
        )
        port map (
            A => A,
            B => B,
            C => C,
            Y => Y
        );

    -- Stimulus + self-checking
    stim_proc : process
    begin
        -- Iteracija svih kombinacija A, B, C (16 ukupno)
        for a_val in 0 to 1 loop
            for b_val in 0 to 1 loop
                for c_val in 0 to 1 loop

                    -- Postavljanje ulaza
                    if a_val = 0 then
                        A <= '0';
                    else
                        A <= '1';
                    end if;

                    if b_val = 0 then
                        B <= '0';
                    else
                        B <= '1';
                    end if;

                    if c_val = 0 then
                        C <= '0';
                    else
                        C <= '1';
                    end if;

                    -- Wait
                    wait for 40 ns;
                end loop;
            end loop;
        end loop;

        -- End simulation
        wait;
    end process;

end architecture sim;
