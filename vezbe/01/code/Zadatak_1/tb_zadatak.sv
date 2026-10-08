module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [3:0] ABCD;
    logic Y_ZP, Y_PZ;

    zadatak UUT (.A(ABCD[3]), .B(ABCD[2]), .C(ABCD[1]),
                 .D(ABCD[0]), .Y_ZP(Y_ZP), .Y_PZ(Y_PZ));

    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        ABCD = 4'b0000;
        #10ns;
        for (int i = 0; i < 16; i++) begin
            ABCD = 4'(i);
            #10ns;
        assert ((Y_ZP === ((ABCD[3] | ABCD[1] | ABCD[0]) & (~ABCD[3] | ABCD[1] | ~ABCD[0]) & (ABCD[2] | ~ABCD[1]))) && (Y_PZ === ((ABCD[3] | ABCD[1] | ABCD[0]) & (~ABCD[3] | ABCD[1] | ~ABCD[0]) & (ABCD[2] | ~ABCD[1])))) else $fatal(1, "Neocekivan ZP/PZ izlaz");
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
