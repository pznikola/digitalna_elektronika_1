module zadatak #(parameter time T = 1ns) (
    input logic A,
    input logic B,
    input logic C,
    input logic D,
    output logic Y_min,
    output logic Y_no_hazard
);
    logic A_inv, C_inv;
    logic I1, I2, I3, I4, I5;
    // Invertovane vrednosti
    assign #(T) A_inv = (~A);
    assign #(T) C_inv = (~C);
    // I1 = A_n C_n
    assign #(T) I1 = (A_inv & C_inv);
    // I2 = C D
    assign #(T) I2 = (C & D);
    // I3 = B C
    assign #(T) I3 = (B & C);
    // I4 = A_n B
    assign #(T) I4 = (A_inv & B);
    // I5 = A_n D
    assign #(T) I5 = (A_inv & D);
    // Y_min = A_n C_n + C D + BC = I1 + I2 + I3
    assign #(T) Y_min = (I1 | I2 | I3);
    // Y_no_hazard = A_n C_n + CD + BC + A_nB + A_nD
    // = I1 + I2 + I3 + I4 + I5
    assign #(T) Y_no_hazard = (I1 | I2 | I3 | I4 | I5);
endmodule
