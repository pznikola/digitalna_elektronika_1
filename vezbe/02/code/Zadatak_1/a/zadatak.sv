module zadatak (
    input logic [1:0] S,
    input logic [3:0] D,
    output logic Y
);
    // Y = S1' S0' D0 + S1' S0 D1 + S1 S0' D2 + S1 S0 D3
    assign Y = (~S[1] & ~S[0] & D[0]) |
         (~S[1] &     S[0] & D[1]) |
         (    S[1] & ~S[0] & D[2]) |
         (    S[1] &     S[0] & D[3]);
endmodule
