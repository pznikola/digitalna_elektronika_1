module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [3:0] ABCD;
    logic Y_min, Y_no_hazard;

    // Isto kasnjenje kao u izvornom testbenchu.
    zadatak #(.T(10ns)) UUT (
        .A(ABCD[3]), .B(ABCD[2]), .C(ABCD[1]), .D(ABCD[0]),
        .Y_min(Y_min), .Y_no_hazard(Y_no_hazard)
    );

    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        ABCD = 4'b0101;
        #50ns;
        assert ((Y_min === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0]))) && (Y_no_hazard === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0])))) else $fatal(1, "Neocekivani ustaljeni izlazi");
        ABCD = 4'b0100;
        #50ns;
        assert ((Y_min === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0]))) && (Y_no_hazard === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0])))) else $fatal(1, "Neocekivani ustaljeni izlazi");
        ABCD = 4'b0101;
        #50ns;
        assert ((Y_min === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0]))) && (Y_no_hazard === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0])))) else $fatal(1, "Neocekivani ustaljeni izlazi");
        ABCD = 4'b0001;
        #50ns;
        assert ((Y_min === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0]))) && (Y_no_hazard === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0])))) else $fatal(1, "Neocekivani ustaljeni izlazi");
        ABCD = 4'b0011;
        #50ns;
        assert ((Y_min === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0]))) && (Y_no_hazard === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0])))) else $fatal(1, "Neocekivani ustaljeni izlazi");
        ABCD = 4'b1011;
        #50ns;
        assert ((Y_min === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0]))) && (Y_no_hazard === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0])))) else $fatal(1, "Neocekivani ustaljeni izlazi");
        ABCD = 4'b0011;
        #50ns;
        assert ((Y_min === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0]))) && (Y_no_hazard === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0])))) else $fatal(1, "Neocekivani ustaljeni izlazi");
        ABCD = 4'b0111;
        #50ns;
        assert ((Y_min === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0]))) && (Y_no_hazard === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0])))) else $fatal(1, "Neocekivani ustaljeni izlazi");
        ABCD = 4'b1111;
        #50ns;
        assert ((Y_min === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0]))) && (Y_no_hazard === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0])))) else $fatal(1, "Neocekivani ustaljeni izlazi");
        ABCD = 4'b0111;
        #50ns;
        assert ((Y_min === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0]))) && (Y_no_hazard === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0])))) else $fatal(1, "Neocekivani ustaljeni izlazi");
        ABCD = 4'b1111;
        #50ns;
        assert ((Y_min === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0]))) && (Y_no_hazard === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0])))) else $fatal(1, "Neocekivani ustaljeni izlazi");
        ABCD = 4'b1110;
        #50ns;
        assert ((Y_min === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0]))) && (Y_no_hazard === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0])))) else $fatal(1, "Neocekivani ustaljeni izlazi");
        ABCD = 4'b1100;
        #50ns;
        assert ((Y_min === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0]))) && (Y_no_hazard === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0])))) else $fatal(1, "Neocekivani ustaljeni izlazi");
        ABCD = 4'b1110;
        #50ns;
        assert ((Y_min === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0]))) && (Y_no_hazard === ((~ABCD[2] & ~ABCD[1] & ~ABCD[0]) | (ABCD[3] & ~ABCD[1] & ABCD[0]) | (~ABCD[3] & ABCD[1] & ~ABCD[0])))) else $fatal(1, "Neocekivani ustaljeni izlazi");
        $display("PASS: %m");
        $finish;
    end
endmodule
