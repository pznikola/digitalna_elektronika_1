library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity add_sub_8_tb is
end add_sub_8_tb;

architecture behavior of add_sub_8_tb is

    component add_sub_8 is
        port (
            a    : in  std_logic_vector (7 downto 0);
            b    : in  std_logic_vector (7 downto 0);
            sel  : in  std_logic;  -- 0=ADD, 1=SUB
            sumb : out std_logic_vector (7 downto 0);
            ovf  : out std_logic
        );
    end component;

    signal a_tb    : std_logic_vector(7 downto 0) := (others => '0');
    signal b_tb    : std_logic_vector(7 downto 0) := (others => '0');
    signal sel_tb  : std_logic := '0';
    signal sumb_tb : std_logic_vector(7 downto 0);
    signal ovf_tb  : std_logic;

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

    -- 8-bit vector to binary string like "01010101"
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

    DUT: add_sub_8
        port map (
            a    => a_tb,
            b    => b_tb,
            sel  => sel_tb,
            sumb => sumb_tb,
            ovf  => ovf_tb
        );

    stim_proc: process
        -- Local variables for expected calculation
        variable result9        : unsigned(8 downto 0);
        variable expected_sumb  : std_logic_vector(7 downto 0);
        variable expected_ovf   : std_logic;

        -- Procedure must be declared BEFORE "begin" of the process
        procedure apply_and_check(
            constant a_in   : std_logic_vector(7 downto 0);
            constant b_in   : std_logic_vector(7 downto 0);
            constant sel_in : std_logic;
            constant tag    : string
        ) is
            variable cin_u9 : unsigned(8 downto 0);
            variable opstr  : string(1 to 3);
        begin
            -- Drive inputs
            a_tb   <= a_in;
            b_tb   <= b_in;
            sel_tb <= sel_in;
            wait for TPD;

            -- Compute expected based on your DUT logic
            if sel_in = '0' then
                -- ADD: A + B, ovf = cout
                result9 := resize(unsigned(a_in), 9) + resize(unsigned(b_in), 9);
                expected_sumb := std_logic_vector(result9(7 downto 0));
                expected_ovf  := std_logic(result9(8));
                opstr := "ADD";
            else
                -- SUB: A + (~B) + 1 = A - B, ovf = borrow = not cout
                cin_u9 := to_unsigned(1, 9);
                result9 := resize(unsigned(a_in), 9) + resize(unsigned(not b_in), 9) + cin_u9;
                expected_sumb := std_logic_vector(result9(7 downto 0));
                expected_ovf  := not std_logic(result9(8));
                opstr := "SUB";
            end if;

            -- Compare + detailed failure report
            if (sumb_tb /= expected_sumb) or (ovf_tb /= expected_ovf) then
                assert false
                    report tag & " (" & opstr & ") FAILED | " &
                           "A=" & slv_u8_to_dec_str(a_in) & " (0x" & slv_u8_to_hex_str(a_in) & ", " &
                           slv_u8_to_bin_str(a_in) & "), " &
                           "B=" & slv_u8_to_dec_str(b_in) & " (0x" & slv_u8_to_hex_str(b_in) & ", " &
                           slv_u8_to_bin_str(b_in) & "), " &
                           "SEL=" & std_logic'image(sel_in) & " | " &
                           "Expected SUMB=" & slv_u8_to_dec_str(expected_sumb) &
                           " (0x" & slv_u8_to_hex_str(expected_sumb) & ", " &
                           slv_u8_to_bin_str(expected_sumb) & "), " &
                           "Expected OVF=" & std_logic'image(expected_ovf) & " | " &
                           "Got SUMB=" & slv_u8_to_dec_str(sumb_tb) &
                           " (0x" & slv_u8_to_hex_str(sumb_tb) & ", " &
                           slv_u8_to_bin_str(sumb_tb) & "), " &
                           "Got OVF=" & std_logic'image(ovf_tb)
                    severity error;
            end if;
        end procedure;

    begin
        -- Directed tests (ADD)
        apply_and_check(x"00", x"00", '0', "T1");
        apply_and_check(x"05", x"03", '0', "T2");
        apply_and_check(x"FF", x"01", '0', "T3"); -- carry expected
        apply_and_check(x"AA", x"55", '0', "T4");

        -- Directed tests (SUB)
        apply_and_check(x"07", x"03", '1', "T5"); -- 7-3=4 no borrow
        apply_and_check(x"03", x"07", '1', "T6"); -- 3-7=252 borrow
        apply_and_check(x"00", x"01", '1', "T7"); -- 0-1=255 borrow
        apply_and_check(x"FF", x"FF", '1', "T8"); -- 255-255=0 no borrow

        -- Small sweep (0..15) to increase coverage
        for a_i in 0 to 15 loop
            for b_i in 0 to 15 loop
                apply_and_check(std_logic_vector(to_unsigned(a_i, 8)),
                                std_logic_vector(to_unsigned(b_i, 8)),
                                '0',
                                "SWEEP_ADD a=" & integer'image(a_i) & " b=" & integer'image(b_i));

                apply_and_check(std_logic_vector(to_unsigned(a_i, 8)),
                                std_logic_vector(to_unsigned(b_i, 8)),
                                '1',
                                "SWEEP_SUB a=" & integer'image(a_i) & " b=" & integer'image(b_i));
            end loop;
        end loop;

        report "All add_sub_8 tests passed successfully!" severity failure;
        wait;
    end process;

end behavior;
