module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [3:0] A, B;
    logic G, E, L;
    zadatak UUT (.A(A), .B(B), .G(G), .E(E), .L(L));
    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        for (int i = 0; i < 16; i++) begin
            for (int j = 0; j < 16; j++) begin
                A = 4'(i);
                B = 4'(j);
                #10ns;
                assert ({G,E,L} === {i > j, i == j, i < j})
                    else $fatal(1, "Pogresan komparator");
            end
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
