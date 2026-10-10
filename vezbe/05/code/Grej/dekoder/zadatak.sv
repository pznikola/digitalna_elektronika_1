module zadatak (
    input logic [5:0] G,
    output logic [5:0] B
);
    // Svaki sledeci bit koristi vec dekodirani visi bit.
    assign B[5] = G[5];
    assign B[4] = B[5] ^ G[4];
    assign B[3] = B[4] ^ G[3];
    assign B[2] = B[3] ^ G[2];
    assign B[1] = B[2] ^ G[1];
    assign B[0] = B[1] ^ G[0];
endmodule
