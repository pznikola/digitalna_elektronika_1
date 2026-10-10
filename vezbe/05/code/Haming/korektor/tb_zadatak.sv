module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [3:0] message, D;
    logic [7:1] original, R, KOD;
    logic [7:0] extended;
    logic [2:0] S;
    haming_koder ENC (.D(message), .KOD(original), .PROSIRENI(extended));
    zadatak UUT (.R(R), .S(S), .KOD(KOD), .D(D));
    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        for (int i = 0; i < 16; i++) begin
            message = 4'(i);
            #10ns;
            for (int p = 0; p <= 7; p++) begin
                R = original;
                if (p != 0) R[p] = ~R[p];
                #10ns;
                assert (S === 3'(p) && KOD === original && D === message)
                    else $fatal(1, "Neispravna korekcija pozicije %0d", p);
            end
        end
        R = 7'b1011100;
        #10ns;
        assert (S === 3'd5 && KOD === 7'b1001100 && D === 4'b1001)
            else $fatal(1, "Pogresna korekcija primera iz zadatka");
        $display("PASS: %m");
        $finish;
    end
endmodule
