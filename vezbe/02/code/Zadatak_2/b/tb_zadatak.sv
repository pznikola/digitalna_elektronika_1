module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic A = 0, B = 0, C = 0;
    logic Y;

    zadatak #(.T(10ns)) uut (.A(A), .B(B), .C(C), .Y(Y));

    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        for (int a_val = 0; a_val < 2; a_val++) begin
            for (int b_val = 0; b_val < 2; b_val++) begin
                for (int c_val = 0; c_val < 2; c_val++) begin
                    A = 1'(a_val);
                    B = 1'(b_val);
                    C = 1'(c_val);
                    #40ns;
        assert (Y === ((C & B) | (~B & A))) else $fatal(1, "Neocekivan izlaz");
                end
            end
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
