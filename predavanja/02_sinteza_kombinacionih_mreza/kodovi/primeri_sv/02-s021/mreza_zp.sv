module mreza_zp (
    input logic C, B, A,
    output logic F
);
    logic C_n, C_p, B_n, B_p, A_n, A_p;
    logic P1, P2, P3;
    // Pravi i komplementni vodovi.
    assign C_n = ~C, C_p = ~C_n;
    assign B_n = ~B, B_p = ~B_n;
    assign A_n = ~A, A_p = ~A_n;
    // I gejtovi i zavrsno ILI kolo.
    assign P1 = C_n & B_p & A_p;
    assign P2 = C_p & B_n & A_p;
    assign P3 = C_p & B_p & A_n;
    assign F = P1 | P2 | P3;
endmodule
