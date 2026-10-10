module zadatak (
    input logic [1:0] A, B,
    output logic [5:0] Y
);
    logic [4:0] X;
    logic [5:0] T;
    logic G, E, L, E_n;
    proizvod PROD (.A(A), .B(B), .X(X));
    komparator2 CMP (.A(A), .B(B), .G(G), .E(E), .L(L));
    // G bira 2X umesto X; pri jednakosti svi biti se gase.
    assign T = ({6{G}} & {X, 1'b0})
             | ({6{~G}} & {1'b0, X});
    assign E_n = ~E;
    assign Y = {6{E_n}} & T;
endmodule
