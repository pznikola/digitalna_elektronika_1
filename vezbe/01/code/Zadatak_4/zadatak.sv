module zadatak #(parameter time T = 1ns) (
    input logic A,
    input logic B,
    input logic C,
    input logic D,
    output logic Y
);
    logic B_inv, I1;
    logic I2, I3, I4;
    // B_inv = inv B, I1 = inv D
    assign #(T) B_inv = (~B);
    assign #(T) I1 = (~D);
    // I2 = A B_inv
    assign #(T) I2 = (A & B_inv);
    // I3 = C D
    assign #(T) I3 = (C & D);
    // I4 = A and C and I1   (A C \bar{D})
    assign #(T) I4 = (A & C & I1);
    // Y = I2 + I3 + I4
    assign #(T) Y = (I2 | I3 | I4);
endmodule
