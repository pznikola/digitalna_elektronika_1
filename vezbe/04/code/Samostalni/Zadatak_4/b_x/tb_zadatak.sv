module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [1:0] A, B;
    logic [4:0] X;
    zadatak UUT (.A(A), .B(B), .X(X));
    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        for (int i = 0; i < 4; i++) begin
            for (int j = 0; j < 4; j++) begin
                A = 2'(i); B = 2'(j);
                #10ns;
                assert (X === 5'((i+1)*(j+1))) else $fatal(1, "Pogresan proizvod");
            end
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
