module mreza_pz (
    input logic C, B, A,
    output logic F
);
    logic C_n, C_p, B_n, B_p, A_n, A_p;
    logic Z0, Z1, Z2, Z4, Z7;
    // Pravi i komplementni vodovi.
    assign C_n = ~C, C_p = ~C_n;
    assign B_n = ~B, B_p = ~B_n;
    assign A_n = ~A, A_p = ~A_n;
    // ILI gejtovi i zavrsno I kolo.
    assign Z0 = C_p | B_p | A_p;
    assign Z1 = C_p | B_p | A_n;
    assign Z2 = C_p | B_n | A_p;
    assign Z4 = C_n | B_p | A_p;
    assign Z7 = C_n | B_n | A_n;
    assign F = Z0 & Z1 & Z2 & Z4 & Z7;
endmodule
