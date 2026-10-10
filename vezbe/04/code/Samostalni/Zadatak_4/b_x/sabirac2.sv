module sabirac2 (
    input logic [1:0] A, B,
    output logic [2:0] S
);
    logic C1, P1, G1, I1;
    assign S[0] = A[0] ^ B[0];
    assign C1 = A[0] & B[0];
    assign P1 = A[1] ^ B[1];
    assign S[1] = P1 ^ C1;
    assign G1 = A[1] & B[1];
    assign I1 = C1 & P1;
    assign S[2] = G1 | I1;
endmodule
