module tb_mreza_zp;
    timeunit 1ns;
    timeprecision 1ps;

    logic C, B, A, F;
    logic ocekuje_se;
    mreza_zp UUT (.C(C), .B(B), .A(A), .F(F));

    initial begin
        $dumpfile("tb_mreza_zp.vcd");
        $dumpvars(0, tb_mreza_zp);
        // Tabela: F=1 samo za indekse 3, 5 i 6.
        for (int i = 0; i < 8; i++) begin
            {C, B, A} = 3'(i);
            case (i)
                3, 5, 6: ocekuje_se = 1'b1;
                default: ocekuje_se = 1'b0;
            endcase
            #10ns;
            assert (F === ocekuje_se)
                else $fatal(1, "Pogresno F za CBA=%b", {C, B, A});
        end
        $display("PASS: %m, svih 8 redova funkcionalne tabele");
        $finish;
    end
endmodule
