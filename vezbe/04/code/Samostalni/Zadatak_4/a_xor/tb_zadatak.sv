module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [1:0] A, B;
    logic [2:0] S;
    zadatak UUT (.A(A), .B(B), .S(S));
    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        for (int i = 0; i < 4; i++) begin
            for (int j = 0; j < 4; j++) begin
                A = 2'(i); B = 2'(j);
                #10ns;
                assert (S === 3'(i+j)) else $fatal(1, "Pogresan zbir");
            end
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
