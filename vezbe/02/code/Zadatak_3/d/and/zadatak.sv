module zadatak (
    input logic [5:0] A,
    output logic [63:0] Y
);
    logic [7:0] H, L;
    decoder3 HIGH (.A(A[5:3]), .Y(H));
    decoder3 LOW (.A(A[2:0]), .Y(L));
    // Svaka iteracija stvara jedno zasebno dvoulazno I kolo.
    generate
        for (genvar i = 0; i < 8; i++) begin : grana
            for (genvar j = 0; j < 8; j++) begin : izlaz
                assign Y[8*i+j] = H[i] & L[j];
            end
        end
    endgenerate
endmodule
