module zadatak #(parameter time T = 1) (
    input logic A, B, C, D,
    output logic Y
);
    logic B_inv, I2, I3, I4;
    assign #(T) B_inv = ~B;
    assign #(T) I2 = A & B_inv;
    assign #(T) I3 = C & D;
    // Clan AC pokriva oba kraja prelaza D: 1 <-> 0.
    assign #(T) I4 = A & C;
    assign #(T) Y = I2 | I3 | I4;
endmodule
