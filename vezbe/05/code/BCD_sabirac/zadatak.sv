module zadatak (
    input logic [3:0] A, B,
    input logic C_in,
    output logic [3:0] S,
    output logic C_out
);
    logic [4:0] Z, R;
    logic K;
    // Prvi binarni sabirac: svi operandi imaju pet bita.
    assign Z = {1'b0, A} + {1'b0, B} + {4'b0000, C_in};
    // Korekcija je potrebna za binarni zbir veci od devet.
    assign K = Z[4] | (Z[3] & (Z[2] | Z[1]));
    // Drugi sabirac dodaje 00110 kada je K=1, inace 00000.
    assign R = Z + {2'b00, K, K, 1'b0};
    assign S = R[3:0];
    assign C_out = K;
endmodule
