module zadatak (
    input logic [5:0] A,
    output logic [63:0] Y
);
    logic [7:0] H, L;
    decoder3 HIGH (.A(A[5:3]), .Y(H));
    decoder3 LOW (.A(A[2:0]), .Y(L));
    // Y3 dekodera sa adresom 0pq predstavlja proizvod pq.
    generate
        for (genvar i = 0; i < 8; i++) begin : grana
            for (genvar j = 0; j < 8; j++) begin : izlaz
                logic [7:0] P;
                decoder3 PRODUCT (.A({1'b0, H[i], L[j]}), .Y(P));
                assign Y[8*i+j] = P[3];
            end
        end
    endgenerate
endmodule
