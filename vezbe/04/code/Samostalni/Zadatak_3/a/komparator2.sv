module komparator2 (
    input logic [1:0] A, B,
    output logic G, E, L
);
    logic E1, E0;
    assign E1 = ~(A[1] ^ B[1]);
    assign E0 = ~(A[0] ^ B[0]);
    assign G = (A[1] & ~B[1]) | (E1 & A[0] & ~B[0]);
    assign E = E1 & E0;
    assign L = (~A[1] & B[1]) | (E1 & ~A[0] & B[0]);
endmodule
