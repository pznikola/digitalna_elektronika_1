library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity zadatak is
    port (
        A : in  STD_LOGIC_VECTOR(2 downto 0);  -- A(2)=MSB, A(0)=LSB
        Y : out STD_LOGIC_VECTOR(7 downto 0)   -- Y(7) ... Y(0)
    );
end entity zadatak;

architecture Behavioral of zadatak is
begin

    process (A) is
    begin
        case A is
            when "000" =>
                Y <= "00000001";  -- Y0
            when "001" =>
                Y <= "00000010";  -- Y1
            when "010" =>
                Y <= "00000100";  -- Y2
            when "011" =>
                Y <= "00001000";  -- Y3
            when "100" =>
                Y <= "00010000";  -- Y4
            when "101" =>
                Y <= "00100000";  -- Y5
            when "110" =>
                Y <= "01000000";  -- Y6
            when "111" =>
                Y <= "10000000";  -- Y7
            when others =>
                -- Ne bi trebalo da se desi nikad
                Y <= (others => '0');
        end case;
    end process;

end architecture Behavioral;
