module zadatak (
    input logic [7:1] R,
    output logic [2:0] S,
    output logic [7:1] KOD,
    output logic [3:0] D
);
    // S={s4,s2,s1}; broj sindroma daje poziciju jedne greske.
    assign S[0] = R[1] ^ R[3] ^ R[5] ^ R[7];
    assign S[1] = R[2] ^ R[3] ^ R[6] ^ R[7];
    assign S[2] = R[4] ^ R[5] ^ R[6] ^ R[7];
    // Svaki bit ima svoje XOR kolo za korekciju.
    assign KOD[1] = R[1] ^ (S == 3'd1);
    assign KOD[2] = R[2] ^ (S == 3'd2);
    assign KOD[3] = R[3] ^ (S == 3'd3);
    assign KOD[4] = R[4] ^ (S == 3'd4);
    assign KOD[5] = R[5] ^ (S == 3'd5);
    assign KOD[6] = R[6] ^ (S == 3'd6);
    assign KOD[7] = R[7] ^ (S == 3'd7);
    assign D = {KOD[7], KOD[6], KOD[5], KOD[3]};
endmodule
