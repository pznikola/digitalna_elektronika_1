module zadatak #(parameter time T = 10ns) (
    input logic A,
    input logic B,
    input logic C,
    output logic Y
);
    logic I1, I2, I3;
    // I1 = ¬(C · B)
    assign #(T) I1 = ~(C & B);
    // I2 = ¬(B · B)
    assign #(T) I2 = ~(B & B);
    // I3 = ¬(A · I2)
    assign #(T) I3 = ~(A & I2);
    // Y = ¬(I1 · I3)
    assign #(T) Y = ~(I1 & I3);
endmodule
