module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [5:0] D;
    logic [6:0] PARNA, NEPARNA;
    logic [7:0] D8;
    logic [6:0] D7;
    logic [8:0] D9;
    logic [8:0] P8, N8;
    logic [7:0] P7, N7;
    logic [9:0] P9, N9;
    int ones;
    zadatak UUT (.D(D), .PARNA(PARNA), .NEPARNA(NEPARNA));
    zadatak #(.N(8)) U8 (.D(D8), .PARNA(P8), .NEPARNA(N8));
    zadatak #(.N(7)) U7 (.D(D7), .PARNA(P7), .NEPARNA(N7));
    zadatak #(.N(9)) U9 (.D(D9), .PARNA(P9), .NEPARNA(N9));
    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        D8 = 8'b10101011;
        D7 = 7'b1101011;
        D9 = 9'b110100101;
        for (int i = 0; i < 64; i++) begin
            D = 6'(i);
            ones = 0;
            for (int j = 0; j < 6; j++) ones += (i >> j) & 1;
            #10ns;
            assert (PARNA === {D, 1'(ones % 2)} &&
                    NEPARNA === {D, 1'(1 - ones % 2)})
                else $fatal(1, "Pogresna parnost");
        end
        D = 6'b100101;
        #10ns;
        assert (PARNA === 7'b1001011 && NEPARNA === 7'b1001010 &&
                P8 === 9'b101010111 && N8 === 9'b101010110 &&
                P7 === 8'b11010111 && N7 === 8'b11010110 &&
                P9 === 10'b1101001011 && N9 === 10'b1101001010)
            else $fatal(1, "Pogresan primer iz tabele");
        $display("PASS: %m");
        $finish;
    end
endmodule
