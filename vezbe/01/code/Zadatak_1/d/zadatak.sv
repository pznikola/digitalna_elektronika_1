module zadatak (
    input logic A, B, C, D,
    output logic Y
);
    logic A_n, B_n, C_n, D_n;
    logic A_p, B_p, C_p, D_p;
    logic I1, I2, I3, I4, I5;
    // Potpun ulazni razvod sa osam invertora, kao na semi.
    assign A_n = ~(A | A);
    assign A_p = ~(A_n | A_n);
    assign B_n = ~(B | B);
    assign B_p = ~(B_n | B_n);
    assign C_n = ~(C | C);
    assign C_p = ~(C_n | C_n);
    assign D_n = ~(D | D);
    assign D_p = ~(D_n | D_n);
    // Svaka dodela predstavlja jedno dvoulazno NILI kolo.
    assign I1 = ~(A_p | D_p);
    assign I2 = ~(A_n | D_n);
    assign I3 = ~(I1 | I2);
    assign I4 = ~(C_p | I3);
    assign I5 = ~(B_p | C_n);
    assign Y = ~(I4 | I5);
endmodule
