module zadatak (
    input logic [1:0] A,
    input logic [1:0] B,
    output logic [3:0] C
);
    // C0 = A0 B0
    assign C[0] = A[0] & B[0];
    // C1 = (A1 B0) xor (A0 B1)
    assign C[1] = (A[1] & B[0]) ^ (A[0] & B[1]);
    // C2 = (A1 B1) (A0 nand B0)
    assign C[2] = (A[1] & B[1]) & ~(A[0] & B[0]);
    // C3 = A1 A0 B1 B0
    assign C[3] = A[1] & A[0] & B[1] & B[0];
endmodule
