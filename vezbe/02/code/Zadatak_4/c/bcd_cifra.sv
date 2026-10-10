module bcd_cifra (
    input logic D, C, B, A,
    input logic OFF, LZ_IN,
    output logic a, b, c, d, e, f, g,
    output logic ERROR, LZ_OUT
);
    logic off_int;
    logic D_n, C_n, B_n, A_n;
    logic a1, a2;
    logic b1, b2, b3, b4;
    logic c1, d1;
    logic e1, e2, e3;
    logic f1, f2, f3;
    logic g1;

    // Detekcija greske ne zavisi od signala za gasenje.
    assign ERROR = D & (C | B);
    assign LZ_OUT = LZ_IN & ~D & ~C & ~B & ~A;
    assign off_int = OFF | LZ_OUT;

    // Invertori: NILI kola sa vezanim ulazima.
    assign D_n = ~(D | D);
    assign C_n = ~(C | C);
    assign B_n = ~(B | B);
    assign A_n = ~(A | A);

    // Segment a sa kontrolom gasenja.
    assign a1 = ~(D | C_n | B | A);
    assign a2 = ~(D | C | B | A_n);
    assign a = ~(a1 | a2 | off_int);

    // Segment b; b1 i b2 koriste se i za segment c.
    assign b1 = ~(D_n | B_n);
    assign b2 = ~(D_n | C_n);
    assign b3 = ~(C_n | B_n | A);
    assign b4 = ~(C_n | B | A_n);
    assign b = ~(b1 | b2 | b3 | b4 | off_int);

    // Segment c.
    assign c1 = ~(C | B_n | A);
    assign c = ~(b1 | b2 | c1 | off_int);

    // Segment d; zajednicki clanovi sa segmentom a.
    assign d1 = ~(D | C_n | B_n | A_n);
    assign d = ~(a1 | a2 | d1 | off_int);

    // Segment e.
    assign e1 = ~(D | A_n);
    assign e2 = ~(C | B | A_n);
    assign e3 = ~(D | C_n | B);
    assign e = ~(e1 | e2 | e3 | off_int);

    // Segment f.
    assign f1 = ~(D | C | A_n);
    assign f2 = ~(D | C | B_n);
    assign f3 = ~(D | B_n | A_n);
    assign f = ~(f1 | f2 | f3 | off_int);

    // Segment g; zajednicki clan sa segmentom d.
    assign g1 = ~(D | C | B);
    assign g = ~(g1 | d1 | off_int);
endmodule
