module zadatak (
    input logic A, B, C, D,
    output logic Y
);
    logic A_n, B_n, C_n, D_n;
    logic A_p, B_p, C_p, D_p;
    logic I1, I2, I3;
    // Potpun ulazni razvod sa osam invertora, kao na semi.
    assign A_n = ~(A & A);
    assign A_p = ~(A_n & A_n);
    assign B_n = ~(B & B);
    assign B_p = ~(B_n & B_n);
    assign C_n = ~(C & C);
    assign C_p = ~(C_n & C_n);
    assign D_n = ~(D & D);
    assign D_p = ~(D_n & D_n);
    // Tri komplementirana proizvoda sa seme.
    assign I1 = ~(A_n & C_n & D_p);
    assign I2 = ~(A_p & C_n & D_n);
    assign I3 = ~(B_p & C_p);
    assign Y = ~(I1 & I2 & I3);
endmodule
