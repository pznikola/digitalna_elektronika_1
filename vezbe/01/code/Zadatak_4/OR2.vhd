library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- 2-input OR gate with delay T
entity OR2 is
    generic (
        T : time := 1 ns
    );
    port (
        A : in  STD_LOGIC;
        B : in  STD_LOGIC;
        Y : out STD_LOGIC
    );
end OR2;

architecture Behavioral_OR2 of OR2 is
begin
    Y <= (A or B) after T;
end Behavioral_OR2;
