module zadatak (
    input logic A, B, C,
    output logic Y_comb, Y_dekoder
);
    logic [2:0] A_dec;
    logic [7:0] Y_dec;
    assign A_dec = {C, B, A};
    decoder udec (.EN0(1'b1), .EN1_B(1'b0), .EN2_B(1'b0),
                  .A(A_dec), .Y(Y_dec));
    // Potpuni zbirovi i odgovarajuci aktivno niski izlazi dekodera.
    assign Y_comb = (C | B | A) & (C | ~B | A) & (~C | ~B | ~A);
    assign Y_dekoder = Y_dec[0] & Y_dec[2] & Y_dec[7];
endmodule
