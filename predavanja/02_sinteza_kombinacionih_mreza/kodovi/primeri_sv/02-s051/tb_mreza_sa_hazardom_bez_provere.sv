module tb_mreza_sa_hazardom_bez_provere;
    timeunit 1ns;
    timeprecision 1ps;

    localparam time T = 5ns;
    logic C, B, A, F;
    mreza_sa_hazardom #(.T(T)) UUT (.C(C), .B(B), .A(A), .F(F));

    initial begin
        $dumpfile("tb_mreza_sa_hazardom_bez_provere.vcd");
        $dumpvars(0, tb_mreza_sa_hazardom_bez_provere);

        // Menjajte ulaze i trajanje svake pobude.
        {C, B, A} = 3'b111; #20ns;
        B = 1'b0;          #20ns;
        B = 1'b1;          #20ns;
        {C, B, A} = 3'b100; #20ns;

        $finish;
    end
endmodule
