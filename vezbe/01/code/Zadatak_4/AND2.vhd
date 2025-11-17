library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- 2-input AND gate with delay T
entity AND2 is
    generic (
        T : time := 1 ns
    );
    port (
        A : in  STD_LOGIC;
        B : in  STD_LOGIC;
        Y : out STD_LOGIC
    );
end AND2;

architecture Behavioral_AND2 of AND2 is
begin
    Y <= (A and B) after T;
end Behavioral_AND2;
