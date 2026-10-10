module proizvod (
    input logic [1:0] A, B,
    output logic [4:0] X
);
    logic [2:0] S;
    logic [4:0] D0, D1, D2, D3;
    sabirac2 ADD (.A(A), .B(2'b01), .S(S));
    // Pomeranje predstavlja samo drugacije povezivanje bita.
    assign D0 = {2'b00, S};
    assign D1 = {1'b0, S, 1'b0};
    assign D2 = {1'b0, A[1], A[0], ~A[1], ~A[0]};
    assign D3 = {S, 2'b00};
    // Petobitni multiplekser 4/1 bira S, 2S, 3S ili 4S.
    assign X = ({5{~B[1] & ~B[0]}} & D0)
             | ({5{~B[1] & B[0]}} & D1)
             | ({5{B[1] & ~B[0]}} & D2)
             | ({5{B[1] & B[0]}} & D3);
endmodule
