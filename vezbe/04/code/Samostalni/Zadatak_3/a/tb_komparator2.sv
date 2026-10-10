module tb_komparator2;
    timeunit 1ns;
    timeprecision 1ps;

    logic [1:0] A, B;
    logic G, E, L;
    komparator2 UUT (.A(A), .B(B), .G(G), .E(E), .L(L));
    initial begin
        $dumpfile("tb_komparator2.vcd");
        $dumpvars(0, tb_komparator2);
        for (int i = 0; i < 4; i++) begin
            for (int j = 0; j < 4; j++) begin
                A = 2'(i);
                B = 2'(j);
                #10ns;
                assert ({G,E,L} === {i > j, i == j, i < j})
                    else $fatal(1, "Pogresan komparator");
            end
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
