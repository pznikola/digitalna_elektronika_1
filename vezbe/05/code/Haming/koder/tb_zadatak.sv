module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [3:0] D;
    logic [7:1] KOD;
    logic [7:0] PROSIRENI;
    logic [7:1] words [0:15];
    logic [7:0] extended [0:15];
    int syndrome, ones, distance;
    zadatak UUT (.D(D), .KOD(KOD), .PROSIRENI(PROSIRENI));
    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        for (int i = 0; i < 16; i++) begin
            D = 4'(i);
            #10ns;
            assert ((^KOD !== 1'bx) && (^PROSIRENI !== 1'bx))
                else $fatal(1, "Nepoznati biti kodne reci");
            syndrome = 0;
            ones = 0;
            for (int p = 1; p <= 7; p++) begin
                if (KOD[p]) syndrome ^= p;
                ones += int'(KOD[p]);
            end
            assert (syndrome == 0 && {KOD[7],KOD[6],KOD[5],KOD[3]} === D)
                else $fatal(1, "Pogresan Haming kod");
            assert (PROSIRENI === {KOD, 1'(ones % 2)})
                else $fatal(1, "Pogresna prosirena rec");
            words[i] = KOD;
            extended[i] = PROSIRENI;
        end
        for (int i = 0; i < 16; i++) begin
            for (int j = i+1; j < 16; j++) begin
                distance = $countones(words[i] ^ words[j]);
                assert (distance >= 3) else $fatal(1, "Rastojanje osnovnog koda");
                distance = $countones(extended[i] ^ extended[j]);
                assert (distance >= 4) else $fatal(1, "Rastojanje prosirenog koda");
            end
        end
        D = 4'b1001;
        #10ns;
        assert (KOD === 7'b1001100 && PROSIRENI === 8'b10011001)
            else $fatal(1, "Pogresna rec iz zadatka");
        $display("PASS: %m");
        $finish;
    end
endmodule
