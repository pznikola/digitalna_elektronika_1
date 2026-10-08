module zadatak (
    input logic [3:0] A,
    output logic [15:0] Y
);
    logic [7:0] Y_low, Y_high;
    // Dekoder za donjih osam izlaza.
    decoder dec_low (.EN0(1'b1), .EN1_B(A[3]), .EN2_B(1'b0),
                     .A(A[2:0]), .Y(Y_low));
    // Dekoder za gornjih osam izlaza.
    decoder dec_high (.EN0(A[3]), .EN1_B(1'b0), .EN2_B(1'b0),
                      .A(A[2:0]), .Y(Y_high));
    assign Y[7:0] = Y_low;
    assign Y[15:8] = Y_high;
endmodule
