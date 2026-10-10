module komparator4 (
    input logic [3:0] A, B,
    output logic G, E, L
);
    logic G_H, E_H, L_H, G_L, E_L, L_L;
    logic I1, I2;
    komparator2 HIGH (.A(A[3:2]), .B(B[3:2]), .G(G_H), .E(E_H), .L(L_H));
    komparator2 LOW (.A(A[1:0]), .B(B[1:0]), .G(G_L), .E(E_L), .L(L_L));
    assign I1 = E_H & G_L;
    assign G = G_H | I1;
    assign E = E_H & E_L;
    assign I2 = G | E;
    // Inverzija preko NI kola sa vezanim ulazima.
    assign L = ~(I2 & I2);
endmodule
