module haming_koder (
    input logic [3:0] D,
    output logic [7:1] KOD,
    output logic [7:0] PROSIRENI
);
    // Informacioni biti zauzimaju pozicije 3, 5, 6 i 7.
    assign KOD[3] = D[0];
    assign KOD[5] = D[1];
    assign KOD[6] = D[2];
    assign KOD[7] = D[3];
    // Kontrolni biti za parnu parnost svake grupe.
    assign KOD[1] = KOD[3] ^ KOD[5] ^ KOD[7];
    assign KOD[2] = KOD[3] ^ KOD[6] ^ KOD[7];
    assign KOD[4] = KOD[5] ^ KOD[6] ^ KOD[7];
    // Dodatni bit p0 ne menja numeraciju prvih sedam pozicija.
    assign PROSIRENI = {KOD, ^KOD};
endmodule
