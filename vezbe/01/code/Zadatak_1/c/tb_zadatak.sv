module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic A, B, C, D, Y;
    zadatak UUT (.A(A), .B(B), .C(C), .D(D), .Y(Y));
    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        for (int i = 0; i < 16; i++) begin
            {A, B, C, D} = 4'(i);
            #10ns;
            assert (Y === ((~A & ~C & D) | (A & ~C & ~D) | (B & C)))
                else $fatal(1, "Pogresna NI/NILI realizacija, ABCD=%b", {A,B,C,D});
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
