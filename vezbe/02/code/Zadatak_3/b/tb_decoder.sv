module tb_decoder;
    timeunit 1ns;
    timeprecision 1ps;

    logic [2:0] EN, A;
    logic [7:0] Y, expected;

    decoder uut (.EN0(EN[2]), .EN1_B(EN[1]), .EN2_B(EN[0]),
                 .A(A), .Y(Y));

    initial begin
        $dumpfile("tb_decoder.vcd");
        $dumpvars(0, tb_decoder);
        for (int en = 0; en < 8; en++) begin
            for (int a = 0; a < 8; a++) begin
                EN = 3'(en);
                A = 3'(a);
                #10ns;
                expected = (en == 4) ? ~(8'b1 << a) : 8'hff;
        assert (Y === expected) else $fatal(1, "Neocekivan pomocni dekoder izlaz");
            end
        end
`ifdef FOUR_STATE
        // Verilator pretezno simulira 0/1; ove provere pokrece Icarus.
        EN = 3'b100; A = 3'bxxx; #10ns;
        assert (Y === 8'hxx) else $fatal(1, "Nepoznata adresa");
        EN = 3'b100; A = 3'bzzz; #10ns;
        assert (Y === 8'hxx) else $fatal(1, "Z adresa");
        EN = 3'b000; A = 3'bxxx; #10ns;
        assert (Y === 8'hff) else $fatal(1, "Sigurno iskljucenje");
        EN = 3'bx00; A = 3'b000; #10ns;
        assert (Y === 8'hxx) else $fatal(1, "Nepoznata dozvola");
        EN = 3'bz00; A = 3'b000; #10ns;
        assert (Y === 8'hxx) else $fatal(1, "Z dozvola");
        EN = 3'b111; A = 3'bzzz; #10ns;
        assert (Y === 8'hff) else $fatal(1, "Iskljucenje uz Z adresu");
`endif
        $display("PASS: %m");
        $finish;
    end
endmodule
