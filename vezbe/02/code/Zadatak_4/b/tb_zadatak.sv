module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic D, C, B, A;
    logic a, b, c, d, e, f, g;
    zadatak UUT (.D(D), .C(C), .B(B), .A(A),
                 .a(a), .b(b), .c(c), .d(d), .e(e), .f(f), .g(g));

    // Nezavisna tabela prikaza, redosled abcdefg.
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
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        for (int n = 0; n < 10; n++) begin
            {D, C, B, A} = 4'(n);
            #10ns;
            assert ({a, b, c, d, e, f, g} === cifra(n))
                else $fatal(1, "BCD=%0d: abcdefg=%b", n, {a,b,c,d,e,f,g});
        end
        $display("PASS: %m, 10 ulaza, svi segmenti");
        $finish;
    end
endmodule
