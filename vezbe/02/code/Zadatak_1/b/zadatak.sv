module zadatak (
    input logic A, B,
    input logic [1:0] C,
    output logic [1:0] Y
);
    logic [3:0] D_Y1, D_Y0;
    logic axb;
    assign axb = (A & ~B) | (~A & B);
    // Ulazi MUX 0 za C = 00, 01, 10, 11.
    assign D_Y0[0] = axb;
    assign D_Y0[1] = ~axb;
    assign D_Y0[2] = ~A & B;
    assign D_Y0[3] = A & ~B;
    // Ulazi MUX 1 za C = 00, 01, 10, 11.
    assign D_Y1[0] = ~axb;
    assign D_Y1[1] = axb;
    assign D_Y1[2] = ~A & ~B;
    assign D_Y1[3] = A & B;
    mux4 mux_Y1 (.S(C), .D(D_Y1), .Y(Y[1]));
    mux4 mux_Y0 (.S(C), .D(D_Y0), .Y(Y[0]));
endmodule
