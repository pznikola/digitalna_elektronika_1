library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity decoder is
    port (
        EN0, EN1_B, EN2_B : in STD_LOGIC;      -- enable
        A : in  STD_LOGIC_VECTOR(2 downto 0);  -- A(2)=MSB, A(0)=LSB
        Y : out STD_LOGIC_VECTOR(7 downto 0)   -- active LOW outputs
    );
end entity decoder;

architecture Behavioral of decoder is
  signal E: STD_LOGIC;
begin

    E <= EN0 and (not EN1_B) and (not EN2_B);

    process (E, A) is
    begin
        if E = '0' then
            -- When disabled: all outputs are 1
            Y <= (others => '1');
        else
            -- When enabled: active-low one-hot decoding
            case A is
                when "000" =>
                    Y <= "11111110";  -- Y0 active (0)
                when "001" =>
                    Y <= "11111101";  -- Y1 active
                when "010" =>
                    Y <= "11111011";  -- Y2 active
                when "011" =>
                    Y <= "11110111";  -- Y3 active
                when "100" =>
                    Y <= "11101111";  -- Y4 active
                when "101" =>
                    Y <= "11011111";  -- Y5 active
                when "110" =>
                    Y <= "10111111";  -- Y6 active
                when others =>
                    Y <= "01111111";  -- Y7 active
            end case;
        end if;
    end process;

end architecture Behavioral;
