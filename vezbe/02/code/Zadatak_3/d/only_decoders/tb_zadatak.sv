module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [5:0] A;
    logic [63:0] Y;
    zadatak UUT (.A(A), .Y(Y));
    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        for (int i = 0; i < 64; i++) begin
            A = 6'(i);
            #10ns;
            assert (Y === (64'b1 << i))
                else $fatal(1, "Pogresan izlaz 6/64, A=%b", A);
        end
`ifdef FOUR_STATE
        // Obican case ne dekodira adresu koja sadrzi X ili Z.
        A = 6'bx00000;
        #10ns;
        assert (Y === {64{1'bx}})
            else $fatal(1, "66 dekodera: neispravan X odziv");
        A = 6'b00000z;
        #10ns;
        assert (Y === {64{1'bx}})
            else $fatal(1, "66 dekodera: neispravan Z odziv");
`endif
        $display("PASS: %m");
        $finish;
    end
endmodule
