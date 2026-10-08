module decoder (
    input logic EN0, EN1_B, EN2_B,
    input logic [2:0] A,
    output logic [7:0] Y
);
    logic E;
    assign E = EN0 & ~EN1_B & ~EN2_B;

    always_comb begin
        if (E === 1'b0)
            Y = '1; // Sigurno iskljucen dekoder.
        else if (E === 1'b1) begin
            case (A)
                3'b000: Y = 8'b11111110; // Y0 aktivan
                3'b001: Y = 8'b11111101; // Y1 aktivan
                3'b010: Y = 8'b11111011; // Y2 aktivan
                3'b011: Y = 8'b11110111; // Y3 aktivan
                3'b100: Y = 8'b11101111; // Y4 aktivan
                3'b101: Y = 8'b11011111; // Y5 aktivan
                3'b110: Y = 8'b10111111; // Y6 aktivan
                3'b111: Y = 8'b01111111; // Y7 aktivan
                default: Y = 'x;
            endcase
        end else
            Y = 'x; // Neodredjena dozvola rada.
    end
endmodule
