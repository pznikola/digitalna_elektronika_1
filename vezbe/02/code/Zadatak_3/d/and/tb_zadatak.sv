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
        A = 6'bx00000;
        #10ns;
        for (int i = 0; i < 64; i++) begin
            assert (Y[i] === ((i % 8 == 0) ? 1'bx : 1'b0))
                else $fatal(1, "AND: neispravan X odziv");
        end
        A = 6'b00000z;
        #10ns;
        assert (Y === {56'b0, 8'bxxxxxxxx})
            else $fatal(1, "AND: neispravan Z odziv");
`endif
        $display("PASS: %m");
        $finish;
    end
endmodule
