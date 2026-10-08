module zadatak #(parameter time T = 20ns) (
    input logic A, B, C,
    output logic Y
);
    logic [1:0] S;
    logic [3:0] D;
    assign S[1] = A;
    assign S[0] = B;
    assign D = {C, 1'b1, C, 1'b0};
    // Prosledi parametar spoljasnjeg kola.
    mux4 #(.T(T)) UMUX (.S(S), .D(D), .Y(Y));
endmodule
