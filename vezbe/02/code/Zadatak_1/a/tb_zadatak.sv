module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [1:0] S = 0;
    logic [3:0] D = 0;
    logic Y;

    zadatak uut (.S(S), .D(D), .Y(Y));

    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        D = 4'b1010;
        S = 2'b00;
        #10ns;
        assert (Y === D[S]) else $fatal(1, "Neocekivan izlaz MUX");
        S = 2'b01;
        #10ns;
        assert (Y === D[S]) else $fatal(1, "Neocekivan izlaz MUX");
        S = 2'b10;
        #10ns;
        assert (Y === D[S]) else $fatal(1, "Neocekivan izlaz MUX");
        S = 2'b11;
        #10ns;
        assert (Y === D[S]) else $fatal(1, "Neocekivan izlaz MUX");
        D = 4'b0101;
        S = 2'b00;
        #10ns;
        assert (Y === D[S]) else $fatal(1, "Neocekivan izlaz MUX");
        S = 2'b01;
        #10ns;
        assert (Y === D[S]) else $fatal(1, "Neocekivan izlaz MUX");
        S = 2'b10;
        #10ns;
        assert (Y === D[S]) else $fatal(1, "Neocekivan izlaz MUX");
        S = 2'b11;
        #10ns;
        assert (Y === D[S]) else $fatal(1, "Neocekivan izlaz MUX");
        $display("PASS: %m");
        $finish;
    end
endmodule
