library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- 3-input OR gate with delay T
entity OR3 is
    generic (
        T : time := 1 ns
    );
    port (
        A : in  STD_LOGIC;
        B : in  STD_LOGIC;
        C : in  STD_LOGIC;
        Y : out STD_LOGIC
    );
end OR3;

architecture Behavioral_OR3 of OR3 is
begin
    Y <= (A or B or C) after T;
end Behavioral_OR3;
