module zadatak (
    input logic [5:0] A,
    output logic [63:0] Y
);
    logic [7:0] H;
    // Prvi stepen bira jedan od osam aktivno niskih EN ulaza.
    decoder HIGH (.EN0(1'b1), .EN1_B(1'b0), .EN2_B(1'b0),
                  .A(A[5:3]), .Y(H));
    generate
        for (genvar i = 0; i < 8; i++) begin : grana
            decoder LOW (.EN0(1'b1), .EN1_B(H[i]), .EN2_B(1'b0),
                         .A(A[2:0]), .Y(Y[8*i+:8]));
        end
    endgenerate
endmodule
