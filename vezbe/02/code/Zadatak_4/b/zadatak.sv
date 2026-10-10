module zadatak (
    input logic D, C, B, A,
    output logic a, b, c, d, e, f, g
);
    // Ulaz je dozvoljena BCD cifra (0-9).
    // Segment a: EXNILI iz nacrtane realizacije.
    assign a = D | B | ~(C ^ A);

    // Segment b.
    assign b = ~C | (A & B) | (~A & ~B);

    // Segment c.
    assign c = C | ~B | A;

    // Segment d.
    assign d = D | (B & ~A) | (B & ~C) |
               (~C & ~A) | (C & ~B & A);

    // Segment e.
    assign e = (B & ~A) | (~C & ~A);

    // Segment f.
    assign f = D | (C & ~A) | (C & ~B) | (~A & ~B);

    // Segment g.
    assign g = D | (B & ~C) | (C & ~A) | (C & ~B);
endmodule
