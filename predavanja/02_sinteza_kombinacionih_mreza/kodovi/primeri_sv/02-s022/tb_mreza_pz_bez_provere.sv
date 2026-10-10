module tb_mreza_pz_bez_provere;
    timeunit 1ns;
    timeprecision 1ps;

    logic C, B, A, F;
    mreza_pz UUT (.C(C), .B(B), .A(A), .F(F));

    initial begin
        $dumpfile("tb_mreza_pz_bez_provere.vcd");
        $dumpvars(0, tb_mreza_pz_bez_provere);

        // Menjajte ulaze i trajanje svake pobude.
        {C, B, A} = 3'b000; #10ns;
        {C, B, A} = 3'b011; #10ns;
        {C, B, A} = 3'b101; #10ns;
        {C, B, A} = 3'b110; #10ns;
        {C, B, A} = 3'b111; #10ns;

        $finish;
    end
endmodule
