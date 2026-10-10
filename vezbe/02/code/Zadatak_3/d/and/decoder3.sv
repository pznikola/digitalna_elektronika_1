module decoder3 (
    input logic [2:0] A,
    output logic [7:0] Y
);
    always_comb begin
        case (A)
            3'b000: Y = 8'b00000001; // Y0
            3'b001: Y = 8'b00000010; // Y1
            3'b010: Y = 8'b00000100; // Y2
            3'b011: Y = 8'b00001000; // Y3
            3'b100: Y = 8'b00010000; // Y4
            3'b101: Y = 8'b00100000; // Y5
            3'b110: Y = 8'b01000000; // Y6
            3'b111: Y = 8'b10000000; // Y7
            default: Y = 'x; // Nebinarna adresa.
        endcase
    end
endmodule
