module zadatak #(parameter time T = 1ns) (
    input logic A,
    input logic B,
    input logic C,
    input logic D,
    output logic Y_min,
    output logic Y_no_hazard
);
    logic A_inv, B_inv, C_inv, D_inv;
    logic I1, I2, I3, I4, I5, I6;
    // Invertovane vrednosti
    assign #(T) A_inv = (~A);
    assign #(T) B_inv = (~B);
    assign #(T) C_inv = (~C);
    assign #(T) D_inv = (~D);
    // I1 = (B_n + C + D)
    assign #(T) I1 = (B_inv | C | D);
    // I2 = (A + D_n)
    assign #(T) I2 = (A | D_inv);
    // I3 = (A_n + C_n)
    assign #(T) I3 = (A_inv | C_inv);
    // I4 = (C_n + D_n)
    assign #(T) I4 = (C_inv | D_inv);
    // I5 = (A + B_n + C)
    assign #(T) I5 = (A | B_inv | C);
    // I6 = (A_n + B_n + D)
    assign #(T) I6 = (A_inv | B_inv | D);
    // Y_min = (B_n + C + D)(A + D_n)(A_n + C_n) = I1 I2 I3
    assign #(T) Y_min = (I1 & I2 & I3);
    // Y_no_hazard =
    // (B_n + C + D)(A + D_n)(A_n + C_n)(C_n + D_n)(A + B_n + C)(A_n + B_n + D)
    // I1 I2 I3 I4 I5 I6
    assign #(T) Y_no_hazard = (I1 & I2 & I3 & I4 & I5 & I6);
endmodule
