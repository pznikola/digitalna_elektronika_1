module zadatak (
    input logic A,
    input logic B,
    input logic C,
    input logic D,
    output logic Y_ZP,
    output logic Y_PZ
);
    logic A_n, B_n, C_n, D_n;
    // Invertovane vrednosti signala
    assign A_n = ~A;
    assign B_n = ~B;
    assign C_n = ~C;
    assign D_n = ~D;
    // Y_ZP = C_n D_n + A_n B_n + B_n C_n
    assign Y_ZP = (C_n & D_n) | (A_n & B_n) | (B_n & C_n);
    // Y_PZ = (B_n + C_n)(B_n + D_n)(A_n + C_n)
    assign Y_PZ = (B_n | C_n) & (B_n | D_n) & (A_n | C_n);
endmodule
