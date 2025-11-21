library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tb_zadatak is
end entity tb_zadatak;

architecture sim of tb_zadatak is

    signal A : std_logic := '0';
    signal B : std_logic := '0';
    signal C : std_logic_vector(1 downto 0) := (others => '0');
    signal Y : std_logic_vector(1 downto 0);

begin

    -- Instanciraj Unit Under Test (UUT)
    uut : entity work.zadatak
        port map (
            A => A,
            B => B,
            C => C,
            Y => Y
        );

    -- Stimulus + self-checking
    stim_proc : process
        variable expY : std_logic_vector(1 downto 0);
        variable axb  : std_logic;
    begin
        -- Iteracija svih kombinacija A, B, C (16 ukupno)
        for a_val in 0 to 1 loop
            for b_val in 0 to 1 loop
                for c_val in 0 to 3 loop

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

                    case c_val is
                        when 0 => C <= "00";
                        when 1 => C <= "01";
                        when 2 => C <= "10";
                        when 3 => C <= "11";
                        when others => C <= "00";
                    end case;

                    -- Wait
                    wait for 10 ns;

                    -- Racunanje vrednosti date tabelom iz zadatka:
                    -- C = 00 : Y1 = ¬(A xor B), Y0 =  A xor B
                    -- C = 01 : Y1 =  A xor B,   Y0 = ¬(A xor B)
                    -- C = 10 : Y1 = ¬A ¬B,      Y0 = ¬A B
                    -- C = 11 : Y1 =  A B,       Y0 = A ¬B
                    axb := A xor B;

                    case C is
                        when "00" =>
                            expY(1) := not axb;
                            expY(0) := axb;
                        when "01" =>
                            expY(1) := axb;
                            expY(0) := not axb;
                        when "10" =>
                            expY(1) := (not A) and (not B);
                            expY(0) := (not A) and B;
                        when "11" =>
                            expY(1) := A and B;
                            expY(0) := A and (not B);
                        when others =>
                            expY := "00";
                    end case;

                    -- Provera rezultata
                    assert Y = expY
                        report "Mismatch: A=" & std_logic'image(A) &
                               " B=" & std_logic'image(B) &
                               " C=" & std_logic'image(C(1)) & std_logic'image(C(0)) &
                               " Y=" & std_logic'image(Y(1)) & std_logic'image(Y(0)) &
                               " expY=" & std_logic'image(expY(1)) & std_logic'image(expY(0))
                        severity error;

                end loop;
            end loop;
        end loop;

        -- End simulation
        wait;
    end process;

end architecture sim;
