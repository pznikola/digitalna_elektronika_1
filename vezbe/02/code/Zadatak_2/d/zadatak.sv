module zadatak #(parameter time T = 10ns) (
    input logic A,
    input logic B,
    input logic C,
    output logic Y
);
    logic I1, I2, I3;
    assign #(T) I1 = (C & B); // I1 = C · B
    assign #(T) I2 = (~B & A); // I2 = ¬B · A
    assign #(T) I3 = (C & A); // I3 = C · A
    assign #(T) Y = (I1 | I2 | I3); // Y = I1 + I2 + I3
endmodule
