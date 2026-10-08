module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [2:0] ABC = 0;
    logic Y_comb, Y_dekoder;

    zadatak uut (.A(ABC[0]), .B(ABC[1]), .C(ABC[2]),
                 .Y_comb(Y_comb), .Y_dekoder(Y_dekoder));

    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        for (int i = 0; i < 8; i++) begin
            ABC = 3'(i);
            #10ns;
        assert ((Y_comb === Y_dekoder) && (Y_comb === ((ABC != 0) && (ABC != 2) && (ABC != 7)))) else $fatal(1, "Neocekivan izlaz funkcije dekodera");
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
