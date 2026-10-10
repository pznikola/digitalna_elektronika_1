module tb_mreza_sa_hazardom;
    timeunit 1ns;
    timeprecision 1ps;

    logic C, B, A, F, F_7;
    logic ocekuje_se;
    mreza_sa_hazardom UUT (.C(C), .B(B), .A(A), .F(F));
    mreza_sa_hazardom #(.T(7ns)) UUT7 (.C(C), .B(B), .A(A), .F(F_7));

    initial begin
        $dumpfile("tb_mreza_sa_hazardom.vcd");
        $dumpvars(0, tb_mreza_sa_hazardom);
        // F bira C pri B=0, odnosno A pri B=1.
        for (int i = 0; i < 8; i++) begin
            {C, B, A} = 3'(i);
            ocekuje_se = B ? A : C;
            #20ns;
            assert ({F, F_7} === {2{ocekuje_se}})
                else $fatal(1, "Pogresno stacionarno F za CBA=%b", {C, B, A});
        end

        {C, B, A} = 3'b111;
        #20ns;
        assert ({F, F_7} === 2'b11)
            else $fatal(1, "Neispravno pocetno stanje");
        B = 1'b0;
        // Posle 2ns oba invertora jos zadrzavaju B_n=0.
        #2ns;
        assert ({F, F_7} === 2'b00)
            else $fatal(1, "Lazna nula nije uocena");
        // Posle 6ns oporavio se samo invertor sa T=5ns.
        #4ns;
        assert ({F, F_7} === 2'b10)
            else $fatal(1, "Pogresno trajanje lazne nule");
        // Posle 8ns obe mreze daju konacnu jedinicu.
        #2ns;
        assert ({F, F_7} === 2'b11)
            else $fatal(1, "Izlaz se nije oporavio");

        // Obrnuti prelaz pri A=C=1 ne pravi laznu nulu.
        B = 1'b1;
        #2ns;
        assert ({F, F_7} === 2'b11)
            else $fatal(1, "Neispravan obrnuti prelaz");
        #8ns;
        assert ({F, F_7} === 2'b11)
            else $fatal(1, "Neispravno zavrsno stanje");
        $display("PASS: %m, tabela i lazna nula za T=5ns i T=7ns");
        $finish;
    end
endmodule
