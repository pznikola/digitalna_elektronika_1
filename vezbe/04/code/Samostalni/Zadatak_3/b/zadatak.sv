module zadatak (
    input logic [3:0] A, B, C,
    output logic [4:0] RES
);
    logic [3:0] X, Y, M;
    logic [4:0] Z;
    logic G1, E1, L1, G2, E2, L2, S;
    assign X = A;
    assign Y = {1'b0, C[3:1]};
    assign Z = {B, 1'b0};
    komparator4 CMP1 (.A(X), .B(Y), .G(G1), .E(E1), .L(L1));
    // Multiplekser bira vecu od X i Y.
    assign M = ({4{G1}} & X) | ({4{~G1}} & Y);
    komparator4 CMP2 (.A(Z[3:0]), .B(M), .G(G2), .E(E2), .L(L2));
    // Visoki bit 2B ima prednost nad cetvorobitnim poredjenjem.
    assign S = Z[4] | G2;
    assign RES = ({5{S}} & Z) | ({5{~S}} & {1'b0, M});
endmodule
