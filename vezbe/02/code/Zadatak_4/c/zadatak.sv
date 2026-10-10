module zadatak (
    input logic [3:0] BCD3, BCD2, BCD1, BCD0,
    output logic [6:0] SEG3, SEG2, SEG1, SEG0
);
    logic R3, R2, R1, R0, G;
    logic LZ3, LZ2;
    logic C0_mod, D0_mod;

    // Greska jedinica: izvorni ulaz, pre nametanja slova E.
    assign R0 = BCD0[3] & (BCD0[2] | BCD0[1]);
    assign G = R3 | R2 | R1 | R0;

    // Ako postoji greska, jedinice dobijaju kod 11xx (E).
    assign C0_mod = BCD0[2] | G;
    assign D0_mod = BCD0[3] | G;

    // SEG[6:0] = {a, b, c, d, e, f, g}; BCD[3:0] = DCBA.
    bcd_cifra CIFRA3 (
        .D(BCD3[3]), .C(BCD3[2]), .B(BCD3[1]), .A(BCD3[0]),
        .OFF(G), .LZ_IN(1'b1), .ERROR(R3), .LZ_OUT(LZ3),
        .a(SEG3[6]), .b(SEG3[5]), .c(SEG3[4]), .d(SEG3[3]),
        .e(SEG3[2]), .f(SEG3[1]), .g(SEG3[0])
    );

    bcd_cifra CIFRA2 (
        .D(BCD2[3]), .C(BCD2[2]), .B(BCD2[1]), .A(BCD2[0]),
        .OFF(G), .LZ_IN(LZ3), .ERROR(R2), .LZ_OUT(LZ2),
        .a(SEG2[6]), .b(SEG2[5]), .c(SEG2[4]), .d(SEG2[3]),
        .e(SEG2[2]), .f(SEG2[1]), .g(SEG2[0])
    );

    // LZ_OUT cifre 1 nije potreban: jedinice se ne gase zbog nule.
    bcd_cifra CIFRA1 (
        .D(BCD1[3]), .C(BCD1[2]), .B(BCD1[1]), .A(BCD1[0]),
        .OFF(G), .LZ_IN(LZ2), .ERROR(R1), .LZ_OUT(),
        .a(SEG1[6]), .b(SEG1[5]), .c(SEG1[4]), .d(SEG1[3]),
        .e(SEG1[2]), .f(SEG1[1]), .g(SEG1[0])
    );

    // ERROR sa izmenjenog ulaza jedinica ne ulazi u racunanje G.
    bcd_cifra CIFRA0 (
        .D(D0_mod), .C(C0_mod), .B(BCD0[1]), .A(BCD0[0]),
        .OFF(1'b0), .LZ_IN(1'b0), .ERROR(), .LZ_OUT(),
        .a(SEG0[6]), .b(SEG0[5]), .c(SEG0[4]), .d(SEG0[3]),
        .e(SEG0[2]), .f(SEG0[1]), .g(SEG0[0])
    );
endmodule
