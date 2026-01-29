library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity ALU_tb is
end ALU_tb;

architecture behavior of ALU_tb is

    component ALU is
        port(
            a_i   : in  std_logic_vector (7 downto 0);
            b_i   : in  std_logic_vector (7 downto 0);
            opc_i : in  std_logic_vector (1 downto 0);
            res_o : out std_logic_vector (7 downto 0);
            ovf_o : out std_logic;
            zero_o: out std_logic
        );
    end component;

    signal a_w   : std_logic_vector(7 downto 0) := (others => '0');
    signal b_w   : std_logic_vector(7 downto 0) := (others => '0');
    signal opc_w : std_logic_vector(1 downto 0) := (others => '0');
    signal res_w : std_logic_vector(7 downto 0);
    signal ovf_w : std_logic;
    signal zero_w: std_logic;

    constant TDELAY : time := 10 ns;

    -- Function to show 0..255 as decimal string
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
            if x(i) = '0' then bitc := '0';
            elsif x(i) = '1' then bitc := '1';
            elsif x(i) = 'U' then bitc := 'U';
            elsif x(i) = 'X' then bitc := 'X';
            elsif x(i) = 'Z' then bitc := 'Z';
            elsif x(i) = 'W' then bitc := 'W';
            elsif x(i) = 'L' then bitc := 'L';
            elsif x(i) = 'H' then bitc := 'H';
            elsif x(i) = '-' then bitc := '-';
            else bitc := '?';
            end if;
            s(k) := bitc;
            k := k + 1;
        end loop;
        return s;
    end function;

    -- Print opcode as integer 0..3
    function opc_to_int_str(opc : std_logic_vector(1 downto 0)) return string is
    begin
        return integer'image(to_integer(unsigned(opc)));
    end function;

begin

    DUT: ALU
        port map (
            a_i    => a_w,
            b_i    => b_w,
            opc_i  => opc_w,
            res_o  => res_w,
            ovf_o  => ovf_w,
            zero_o => zero_w
        );

    stim_proc: process
        variable exp_res  : std_logic_vector(7 downto 0);
        variable exp_ovf  : std_logic;
        variable exp_zero : std_logic;
        variable res_9    : unsigned(8 downto 0);
        variable au, bu   : unsigned(7 downto 0);

        procedure apply_and_check(
            constant a_in   : std_logic_vector(7 downto 0);
            constant b_in   : std_logic_vector(7 downto 0);
            constant opc_in : std_logic_vector(1 downto 0);
            constant tag    : string
        ) is
            variable cin_u9 : unsigned(8 downto 0);
        begin
            a_w   <= a_in;
            b_w   <= b_in;
            opc_w <= opc_in;
            wait for TDELAY;

            au := unsigned(a_in);
            bu := unsigned(b_in);

            -- Expected RESULT and C (C matches add_sub_8.ovf for opcodes 2/3, else 0)
            case opc_in is
                when "00" =>  -- MAX
                    if au >= bu then exp_res := a_in; else exp_res := b_in; end if;
                    exp_ovf := '0';

                when "01" =>  -- MIN
                    if au <= bu then exp_res := a_in; else exp_res := b_in; end if;
                    exp_ovf := '0';
                    
                when "10" =>  -- ADD
                    res_9 := resize(au, 9) + resize(bu, 9);
                    exp_res := std_logic_vector(res_9(7 downto 0));
                    exp_ovf := std_logic(res_9(8));  -- ovf for ADD = carry out

                when "11" =>  -- SUB: A + (~B) + 1 = A - B
                    cin_u9 := to_unsigned(1, 9);
                    res_9 := resize(au, 9) + resize(unsigned(not b_in), 9) + cin_u9;
                    exp_res := std_logic_vector(res_9(7 downto 0));
                    exp_ovf := not std_logic(res_9(8)); -- ovf for SUB = borrow = not cout
                    
                when others =>
                    exp_res := (others => 'X');
                    exp_ovf := '0';
            end case;

            -- Expected Z flag
            if exp_res = x"00" then
                exp_zero := '1';
            else
                exp_zero := '0';
            end if;

            -- Compare with detailed report
            if (res_w /= exp_res) or (ovf_w /= exp_ovf) or (zero_w /= exp_zero) then
                assert false
                    report tag & " FAILED | " &
                           "OPCODE=" & opc_to_int_str(opc_in) & " | " &
                           "A=" & slv_u8_to_dec_str(a_in) & " (0x" & slv_u8_to_hex_str(a_in) & ", " &
                           slv_u8_to_bin_str(a_in) & "), " &
                           "B=" & slv_u8_to_dec_str(b_in) & " (0x" & slv_u8_to_hex_str(b_in) & ", " &
                           slv_u8_to_bin_str(b_in) & ") | " &
                           "Expected RES=" & slv_u8_to_dec_str(exp_res) &
                           " (0x" & slv_u8_to_hex_str(exp_res) & ", " &
                           slv_u8_to_bin_str(exp_res) & "), " &
                           "Expected OVF=" & std_logic'image(exp_ovf) &
                           ", Expected ZERO=" & std_logic'image(exp_zero) & " | " &
                           "Got RES=" & slv_u8_to_dec_str(res_w) &
                           " (0x" & slv_u8_to_hex_str(res_w) & ", " &
                           slv_u8_to_bin_str(res_w) & "), " &
                           "Got OVF=" & std_logic'image(ovf_w) &
                           ", Got ZERO=" & std_logic'image(zero_w)
                    severity error;
            end if;
        end procedure;

    begin
        ----------------------------------------------------------------
        -- Directed tests
        ----------------------------------------------------------------
        -- MAX (opcode 0) (C must be 0)
        apply_and_check(x"00", x"00", "00", "MAX T1 eq (ZERO=1,OVF=0)");
        apply_and_check(x"01", x"02", "00", "MAX T2 b");
        apply_and_check(x"FF", x"00", "00", "MAX T3 a");

        -- MIN (opcode 1) (C must be 0)
        apply_and_check(x"00", x"00", "01", "MIN T1 eq (ZERO=1,OVF=0)");
        apply_and_check(x"01", x"02", "01", "MIN T2 a");
        apply_and_check(x"FF", x"00", "01", "MIN T3 b");
        
        -- ADD (opcode 2)
        apply_and_check(x"00", x"00", "10", "ADD T1");
        apply_and_check(x"05", x"03", "10", "ADD T2");
        apply_and_check(x"FF", x"01", "10", "ADD T3 carry");
        apply_and_check(x"80", x"80", "10", "ADD T4 Z+carry");

        -- SUB (opcode 3)  (C = borrow flag here, matching add_sub_8.ovf)
        apply_and_check(x"07", x"03", "11", "SUB T1 no borrow");
        apply_and_check(x"03", x"07", "11", "SUB T2 borrow");
        apply_and_check(x"00", x"01", "11", "SUB T3 borrow");
        apply_and_check(x"10", x"10", "11", "SUB T4 ZERO=1");


        ----------------------------------------------------------------
        -- Sweep tests (0..15) across all opcodes
        ----------------------------------------------------------------
        for a_i in 0 to 15 loop
            for b_i in 0 to 15 loop
                apply_and_check(std_logic_vector(to_unsigned(a_i, 8)),
                                std_logic_vector(to_unsigned(b_i, 8)),
                                "00", "SWEEP MAX");
                apply_and_check(std_logic_vector(to_unsigned(a_i, 8)),
                                std_logic_vector(to_unsigned(b_i, 8)),
                                "01", "SWEEP MIN");
                apply_and_check(std_logic_vector(to_unsigned(a_i, 8)),
                                std_logic_vector(to_unsigned(b_i, 8)),
                                "10", "SWEEP ADD");
                apply_and_check(std_logic_vector(to_unsigned(a_i, 8)),
                                std_logic_vector(to_unsigned(b_i, 8)),
                                "11", "SWEEP SUB");
            end loop;
        end loop;

        report "All ALU tests passed successfully!" severity failure;
        wait;
    end process;

end behavior;
