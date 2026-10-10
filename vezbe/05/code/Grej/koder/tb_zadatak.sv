module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [5:0] B, G;
    zadatak UUT (.B(B), .G(G));
    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        for (int i = 0; i < 64; i++) begin
            B = 6'(i);
            #10ns;
            assert (G === 6'(i ^ (i >> 1))) else $fatal(1, "Pogresan Grej kod");
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
