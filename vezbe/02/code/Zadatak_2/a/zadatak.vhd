library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity zadatak is
    generic (
        T : time := 20 ns   -- globalni delay parametar
    );
    port (
        A, B, C : in  STD_LOGIC;
        Y       : out STD_LOGIC
    );
end entity zadatak;

architecture Structural of zadatak is

  signal S: STD_LOGIC_VECTOR(1 downto 0);
  signal D: STD_LOGIC_VECTOR(3 downto 0);

begin

  S(1) <= A;
  S(0) <= B;
  D    <= (C, '1', C, '0');

    -- Instanciranje multipleksera
    UMUX : entity work.mux4
        generic map (
            T => 20 ns -- Staviti zeljeno kasnjenje
        )
        port map (
            S => S,
            D => D,
            Y => Y
        );

end architecture Structural;
