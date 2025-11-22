library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux4 is
    generic (
        T : time := 20 ns   -- globalni delay parametar
    );
    port (
        S : in  STD_LOGIC_VECTOR(1 downto 0);  -- S(1)=S1, S(0)=S0
        D : in  STD_LOGIC_VECTOR(3 downto 0);  -- D(0)=D0 ... D(3)=D3
        Y : out STD_LOGIC
    );
end entity mux4;

architecture Behavioral of mux4 is
begin
    -- Y = S1' S0' D0 + S1' S0 D1 + S1 S0' D2 + S1 S0 D3
    Y <= ((not S(1) and not S(0) and D(0)) or
          (not S(1) and     S(0) and D(1)) or
          (    S(1) and not S(0) and D(2)) or
          (    S(1) and     S(0) and D(3))) after T;

end architecture Behavioral;
