module tb_sabirac2;
    timeunit 1ns;
    timeprecision 1ps;

    logic [1:0] A, B;
    logic [2:0] S;
    sabirac2 UUT (.A(A), .B(B), .S(S));
    initial begin
        $dumpfile("tb_sabirac2.vcd");
        $dumpvars(0, tb_sabirac2);
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
