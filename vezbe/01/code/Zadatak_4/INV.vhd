library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- NOT gate with delay T
entity INV is
    generic (
        T : time := 1 ns
    );
    port (
        A : in  STD_LOGIC;
        Y : out STD_LOGIC
    );
end INV;

architecture Behavioral_NOT of INV is
begin
    Y <= not A after T;
end Behavioral_NOT;
