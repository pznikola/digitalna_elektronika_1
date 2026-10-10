module mreza_sa_hazardom #(
    parameter time T = 5
) (
    input logic C, B, A,
    output logic F
);
    logic B_n, C_B_n, BA;

    // Samo invertor ima kasnjenje T.
    assign #(T) B_n = ~B;

    // Ostali gejtovi su idealno brzi.
    assign C_B_n = C & B_n;
    assign BA = B & A;
    assign F = C_B_n | BA;
endmodule
