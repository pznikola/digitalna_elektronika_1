module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [1:0] A, B;
    logic [3:0] C;

    zadatak UUT (.A(A), .B(B), .C(C));

    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        A = 2'b00;
        B = 2'b00;
        for (int i = 0; i < 4; i++) begin
            for (int j = 0; j < 4; j++) begin
                A = 2'(i);
                B = 2'(j);
                #10ns;
        assert (C === 4'(i * j)) else $fatal(1, "Neocekivan proizvod");
            end
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
