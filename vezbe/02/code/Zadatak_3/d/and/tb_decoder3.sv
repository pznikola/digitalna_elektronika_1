module tb_decoder3;
    timeunit 1ns;
    timeprecision 1ps;

    logic [2:0] A = 0;
    logic [7:0] Y;

    decoder3 uut (.A(A), .Y(Y));

    initial begin
        $dumpfile("tb_decoder3.vcd");
        $dumpvars(0, tb_decoder3);
        for (int i = 0; i < 8; i++) begin
            A = 3'(i);
            #10ns;
            assert (Y === (8'b1 << i)) else $fatal(1, "Neocekivan izlaz dekodera");
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
