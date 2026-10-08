module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [2:0] A = 0;
    logic [7:0] Y;

    zadatak uut (.A(A), .Y(Y));

    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        for (int i = 0; i < 8; i++) begin
            A = 3'(i);
            #10ns;
        assert (Y === (8'b1 << i)) else $fatal(1, "Neocekivan izlaz dekodera");
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
