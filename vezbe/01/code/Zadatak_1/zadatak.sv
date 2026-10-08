module zadatak (
    input logic A,
    input logic B,
    input logic C,
    input logic D,
    output logic Y_ZP,
    output logic Y_PZ
);
    logic A_n, C_n, D_n;
    // Invertovane vrednosti signala
    assign A_n = ~A;
    assign C_n = ~C;
    assign D_n = ~D;
    // Y_ZP = A_n C_n D + A C_n D_n + BC
    assign Y_ZP = (A_n & C_n & D) | (A & C_n & D_n) | (B & C);
    // Y_PZ = (A + C + D)(A_n + C + D_n)(B + C_n)
    assign Y_PZ = (A | C | D) & (A_n | C | D_n) & (B | C_n);
endmodule
