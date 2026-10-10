module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [3:0] A, B, C;
    logic [4:0] RES;
    int expected;
    zadatak UUT (.A(A), .B(B), .C(C), .RES(RES));
    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        for (int i = 0; i < 16; i++) begin
            for (int j = 0; j < 16; j++) begin
                for (int k = 0; k < 16; k++) begin
                    A = 4'(i); B = 4'(j); C = 4'(k);
                    expected = i;
                    if (2*j > expected) expected = 2*j;
                    if (k/2 > expected) expected = k/2;
                    #10ns;
                    assert (RES === 5'(expected))
                        else $fatal(1, "Pogresan maksimum");
                end
            end
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
