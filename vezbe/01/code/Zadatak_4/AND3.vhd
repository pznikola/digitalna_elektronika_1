library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- 3-input AND gate with delay T
entity AND3 is
    generic (
        T : time := 1 ns
    );
    port (
        A : in  STD_LOGIC;
        B : in  STD_LOGIC;
        C : in  STD_LOGIC;
        Y : out STD_LOGIC
    );
end AND3;

architecture Behavioral_AND3 of AND3 is
begin
    Y <= (A and B and C) after T;
end Behavioral_AND3;
