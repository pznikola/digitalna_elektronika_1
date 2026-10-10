module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [1:0] A, B;
    logic [5:0] Y;
    int expected;
    zadatak UUT (.A(A), .B(B), .Y(Y));
    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        for (int i = 0; i < 4; i++) begin
            for (int j = 0; j < 4; j++) begin
                A = 2'(i); B = 2'(j);
                expected = (i == j) ? 0 : (i+1)*(j+1)*((i > j) ? 2 : 1);
                #10ns;
                assert (Y === 6'(expected) && Y[5] === 1'b0)
                    else $fatal(1, "Pogresna funkcija Y");
            end
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
