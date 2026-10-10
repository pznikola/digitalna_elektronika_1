module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic A, B, C, D;
    logic Y, Y_7, Y_hazard, Y_hazard_7;
    zadatak UUT (.A(A), .B(B), .C(C), .D(D), .Y(Y));
    zadatak #(.T(7ns)) UUT7 (.A(A), .B(B), .C(C), .D(D), .Y(Y_7));
    sa_hazardom OLD (.A(A), .B(B), .C(C), .D(D), .Y(Y_hazard));
    sa_hazardom #(.T(7ns)) OLD7 (.A(A), .B(B), .C(C), .D(D), .Y(Y_hazard_7));
    bit proveri_prelaz = 1'b0;
    always @(Y or Y_7)
        if (proveri_prelaz)
            assert ({Y, Y_7} === 2'b11)
                else $fatal(1, "Hazard u prosirenoj realizaciji");

    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        for (int i = 0; i < 16; i++) begin
            {A, B, C, D} = 4'(i);
            #30ns;
            assert ({Y, Y_7, Y_hazard, Y_hazard_7} ===
                    {4{(A & ~B) | (C & D) | (A & C)}})
                else $fatal(1, "Pogresna stacionarna vrednost");
        end
        // 1111 -> 1110: izvorni izlaz ima laznu nulu [2T,3T).
        {A, B, C, D} = 4'b1111;
        #30ns;
        proveri_prelaz = 1'b1;
        D = 1'b0;
        #2.5ns;
        assert (Y_hazard === 1'b0 && Y === 1'b1)
            else $fatal(1, "Neispravan odziv za T=1ns");
        #12ns;
        assert (Y_hazard_7 === 1'b0 && Y_7 === 1'b1)
            else $fatal(1, "Neispravan odziv za T=7ns");
        #10ns;
        // Obrnuti smer nema impuls u ovom modelu jednakih kasnjenja.
        D = 1'b1;
        repeat (60) begin
            #0.5ns;
            assert ({Y, Y_7, Y_hazard, Y_hazard_7} === 4'b1111)
                else $fatal(1, "Impuls pri obrnutom prelazu");
        end
        $display("PASS: %m");
        $finish;
    end
endmodule
