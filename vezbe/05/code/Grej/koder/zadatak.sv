module zadatak (
    input logic [5:0] B,
    output logic [5:0] G
);
    // MSB se prepisuje, ostali biti su XOR susednih bita.
    assign G[5] = B[5];
    assign G[4] = B[5] ^ B[4];
    assign G[3] = B[4] ^ B[3];
    assign G[2] = B[3] ^ B[2];
    assign G[1] = B[2] ^ B[1];
    assign G[0] = B[1] ^ B[0];
endmodule
