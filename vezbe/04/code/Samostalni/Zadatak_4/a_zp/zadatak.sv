module zadatak (
    input logic [1:0] A, B,
    output logic [2:0] S
);
    // Minimizovani zbirovi proizvoda, bez XOR kola.
    assign S[0] = (~A[0] & B[0]) | (A[0] & ~B[0]);
    assign S[1] = (A[1] & ~A[0] & ~B[1])
                | (A[1] & ~B[1] & ~B[0])
                | (~A[1] & ~A[0] & B[1])
                | (~A[1] & B[1] & ~B[0])
                | (~A[1] & A[0] & ~B[1] & B[0])
                | (A[1] & A[0] & B[1] & B[0]);
    assign S[2] = (A[1] & B[1]) | (A[1] & A[0] & B[0])
                | (B[1] & B[0] & A[0]);
endmodule
