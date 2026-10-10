module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [5:0] G, B;
    zadatak UUT (.G(G), .B(B));
    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        // Sve binarne reci kodujemo u TB-u i nezavisno dekodiramo u DUT-u.
        for (int i = 0; i < 64; i++) begin
            G = 6'(i ^ (i >> 1));
            #10ns;
            assert (B === 6'(i)) else $fatal(1, "Pogresno Grej dekodiranje");
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
