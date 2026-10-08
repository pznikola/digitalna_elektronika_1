module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic A = 0, B = 0;
    logic [1:0] C = 0, Y;
    logic [1:0] expY;
    logic axb;

    zadatak uut (.A(A), .B(B), .C(C), .Y(Y));

    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        // Sve kombinacije A, B, C: 16 ukupno.
        for (int a_val = 0; a_val < 2; a_val++) begin
            for (int b_val = 0; b_val < 2; b_val++) begin
                for (int c_val = 0; c_val < 4; c_val++) begin
                    A = 1'(a_val);
                    B = 1'(b_val);
                    C = 2'(c_val);
                    #10ns;
                    axb = A ^ B;
                    case (C)
                        2'b00: expY = {~axb, axb};
                        2'b01: expY = {axb, ~axb};
                        2'b10: expY = {~A & ~B, ~A & B};
                        2'b11: expY = {A & B, A & ~B};
                    endcase
        assert (Y === expY) else $fatal(1, "Neocekivani izlazi dva MUX");
                end
            end
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
