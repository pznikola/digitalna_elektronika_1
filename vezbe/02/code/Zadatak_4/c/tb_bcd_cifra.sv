module tb_bcd_cifra;
    timeunit 1ns;
    timeprecision 1ps;

    logic D, C, B, A, OFF, LZ_IN;
    logic a, b, c, d, e, f, g, ERROR, LZ_OUT;
    logic [6:0] ocekivano;
    bcd_cifra UUT (.D(D), .C(C), .B(B), .A(A), .OFF(OFF),
                   .LZ_IN(LZ_IN), .ERROR(ERROR), .LZ_OUT(LZ_OUT),
                   .a(a), .b(b), .c(c), .d(d), .e(e), .f(f), .g(g));

    function automatic logic [6:0] cifra(input int n);
        case (n)
            0: cifra = 7'b1111110;
            1: cifra = 7'b0110000;
            2: cifra = 7'b1101101;
            3: cifra = 7'b1111001;
            4: cifra = 7'b0110011;
            5: cifra = 7'b1011011;
            6: cifra = 7'b1011111;
            7: cifra = 7'b1110000;
            8: cifra = 7'b1111111;
            9: cifra = 7'b1111011;
            default: cifra = 7'b1001111;
        endcase
    endfunction

    initial begin
        $dumpfile("tb_bcd_cifra.vcd");
        $dumpvars(0, tb_bcd_cifra);
        for (int n = 0; n < 16; n++) begin
            for (int kontrola = 0; kontrola < 4; kontrola++) begin
                {D, C, B, A} = 4'(n);
                {OFF, LZ_IN} = 2'(kontrola);
                ocekivano = (OFF || (LZ_IN && n == 0)) ? 7'b0 : cifra(n);
                #10ns;
                assert ({a, b, c, d, e, f, g} === ocekivano)
                    else $fatal(1, "Cifra: n=%0d, OFF=%b, LZ_IN=%b",
                                n, OFF, LZ_IN);
                assert (ERROR === (n > 9))
                    else $fatal(1, "ERROR mora biti nezavisan od gasenja");
                assert (LZ_OUT === (LZ_IN && n == 0))
                    else $fatal(1, "Pogresan LZ_OUT");
            end
        end
`ifdef FOUR_STATE
        OFF = 1'b1;
        // OFF=1 mora gasiti sve segmente i za nepoznate ulaze.
        for (int stanje = 0; stanje < 2; stanje++) begin
            for (int pozicija = 0; pozicija < 4; pozicija++) begin
                for (int lz = 0; lz < 2; lz++) begin
                    {D, C, B, A} = 4'b0000;
                    LZ_IN = 1'(lz);
                    case (pozicija)
                        0: A = stanje == 0 ? 1'bx : 1'bz;
                        1: B = stanje == 0 ? 1'bx : 1'bz;
                        2: C = stanje == 0 ? 1'bx : 1'bz;
                        3: D = stanje == 0 ? 1'bx : 1'bz;
                    endcase
                    #10ns;
                    assert ({a, b, c, d, e, f, g} === 7'b0)
                        else $fatal(1, "OFF nije ugasio X/Z podatak");
                end
            end
        end
        {D, C, B, A} = 4'bxxxx;
        LZ_IN = 1'bx;
        #10ns;
        assert ({a, b, c, d, e, f, g} === 7'b0)
            else $fatal(1, "OFF nije ugasio nepoznat LZ_IN");
`endif
        $display("PASS: %m, 64 binarna ulaza i Icarus X/Z gasenje");
        $finish;
    end
endmodule
