library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity max_8_tb is
end max_8_tb;

architecture behavior of max_8_tb is

    component max_8 is
        port(
            num_a   : in  std_logic_vector(7 downto 0);
            num_b   : in  std_logic_vector(7 downto 0);
            num_max : out std_logic_vector(7 downto 0)
        );
    end component;

    signal num_a_tb   : std_logic_vector(7 downto 0) := (others => '0');
    signal num_b_tb   : std_logic_vector(7 downto 0) := (others => '0');
    signal num_max_tb : std_logic_vector(7 downto 0);

    constant TPD : time := 10 ns;

    -- 0..255 as decimal string
    function slv_u8_to_dec_str(x : std_logic_vector(7 downto 0)) return string is
    begin
        return integer'image(to_integer(unsigned(x)));
    end function;

    -- 8-bit vector to 2-digit hex string
    function slv_u8_to_hex_str(x : std_logic_vector(7 downto 0)) return string is
        constant HEX : string := "0123456789ABCDEF";
        variable hi  : integer;
        variable lo  : integer;
        variable s   : string(1 to 2);
    begin
        hi := to_integer(unsigned(x(7 downto 4)));
        lo := to_integer(unsigned(x(3 downto 0)));
        s(1) := HEX(hi + 1);
        s(2) := HEX(lo + 1);
        return s;
    end function;

    -- 8-bit vector to binary string "01010101" (MSB..LSB)
    function slv_u8_to_bin_str(x : std_logic_vector(7 downto 0)) return string is
        variable s : string(1 to 8);
        variable k : integer := 1;
        variable bitc : character;
    begin
        for i in x'range loop
            if x(i) = '0' then
                bitc := '0';
            elsif x(i) = '1' then
                bitc := '1';
            elsif x(i) = 'U' then
                bitc := 'U';
            elsif x(i) = 'X' then
                bitc := 'X';
            elsif x(i) = 'Z' then
                bitc := 'Z';
            elsif x(i) = 'W' then
                bitc := 'W';
            elsif x(i) = 'L' then
                bitc := 'L';
            elsif x(i) = 'H' then
                bitc := 'H';
            elsif x(i) = '-' then
                bitc := '-';
            else
                bitc := '?';
            end if;

            s(k) := bitc;
            k := k + 1;
        end loop;
        return s;
    end function;

begin

    DUT: max_8
        port map (
            num_a   => num_a_tb,
            num_b   => num_b_tb,
            num_max => num_max_tb
        );

    stim_proc: process
        variable expected_max : std_logic_vector(7 downto 0);

        procedure apply_and_check(
            constant a_in : std_logic_vector(7 downto 0);
            constant b_in : std_logic_vector(7 downto 0);
            constant tag  : string
        ) is
        begin
            num_a_tb <= a_in;
            num_b_tb <= b_in;
            wait for TPD;

            -- Expected: max of a and b (unsigned compare)
            if unsigned(a_in) >= unsigned(b_in) then
                expected_max := a_in;
            else
                expected_max := b_in;
            end if;

            if num_max_tb /= expected_max then
                assert false
                    report tag & " FAILED | " &
                           "A=" & slv_u8_to_dec_str(a_in) & " (0x" & slv_u8_to_hex_str(a_in) & ", " &
                           slv_u8_to_bin_str(a_in) & "), " &
                           "B=" & slv_u8_to_dec_str(b_in) & " (0x" & slv_u8_to_hex_str(b_in) & ", " &
                           slv_u8_to_bin_str(b_in) & ") | " &
                           "Expected MAX=" & slv_u8_to_dec_str(expected_max) &
                           " (0x" & slv_u8_to_hex_str(expected_max) & ", " &
                           slv_u8_to_bin_str(expected_max) & ") | " &
                           "Got MAX=" & slv_u8_to_dec_str(num_max_tb) &
                           " (0x" & slv_u8_to_hex_str(num_max_tb) & ", " &
                           slv_u8_to_bin_str(num_max_tb) & ")"
                    severity error;
            end if;
        end procedure;

    begin
        -- Directed tests
        apply_and_check(x"00", x"00", "T1 eq");
        apply_and_check(x"00", x"01", "T2 b bigger");
        apply_and_check(x"01", x"00", "T3 a bigger");
        apply_and_check(x"7F", x"80", "T4 boundary b bigger");
        apply_and_check(x"80", x"7F", "T5 boundary a bigger");
        apply_and_check(x"FF", x"00", "T6 a bigger");
        apply_and_check(x"00", x"FF", "T7 b bigger");
        apply_and_check(x"AB", x"AB", "T8 eq");

        -- Sweep small range for coverage (0..31)
        for a_i in 0 to 31 loop
            for b_i in 0 to 31 loop
                apply_and_check(std_logic_vector(to_unsigned(a_i, 8)),
                                std_logic_vector(to_unsigned(b_i, 8)),
                                "SWEEP a=" & integer'image(a_i) & " b=" & integer'image(b_i));
            end loop;
        end loop;

        report "All max_8 tests passed successfully!" severity failure;
        wait;
    end process;

end behavior;
