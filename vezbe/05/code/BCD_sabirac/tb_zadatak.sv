module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [3:0] A, B, S;
    logic C_in, C_out;
    int total;
    zadatak UUT (.A(A), .B(B), .C_in(C_in), .S(S), .C_out(C_out));
    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        for (int i = 0; i < 10; i++) begin
            for (int j = 0; j < 10; j++) begin
                for (int c = 0; c < 2; c++) begin
                    A = 4'(i); B = 4'(j); C_in = 1'(c);
                    total = i+j+c;
                    #10ns;
                    assert (S === 4'(total % 10) && C_out === 1'(total / 10))
                        else $fatal(1, "Pogresan BCD zbir");
                end
            end
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
