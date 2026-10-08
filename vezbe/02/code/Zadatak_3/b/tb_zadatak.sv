module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [3:0] A = 0;
    logic [15:0] Y;

    zadatak uut (.A(A), .Y(Y));

    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        for (int i = 0; i < 16; i++) begin
            A = 4'(i);
            #10ns;
        assert (Y === ~(16'b1 << i)) else $fatal(1, "Neocekivan izlaz dekodera");
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
