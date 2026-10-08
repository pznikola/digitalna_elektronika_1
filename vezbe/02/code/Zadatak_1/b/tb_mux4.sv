module tb_mux4;
    timeunit 1ns;
    timeprecision 1ps;

    logic [1:0] S;
    logic [3:0] D;
    logic Y;

    mux4 uut (.S(S), .D(D), .Y(Y));

    initial begin
        $dumpfile("tb_mux4.vcd");
        $dumpvars(0, tb_mux4);
        for (int s = 0; s < 4; s++) begin
            for (int d = 0; d < 16; d++) begin
                S = 2'(s);
                D = 4'(d);
                #10ns;
        assert (Y === D[S]) else $fatal(1, "Neocekivan pomocni MUX izlaz");
            end
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
