module zadatak (
    input logic D, C, B, A,
    output logic a, b, c, d, e, f, g
);
    logic D_n, C_n, B_n, A_n;
    logic a1, a2;
    logic b1, b2, b3, b4;
    logic c1, d1;
    logic e1, e2, e3;
    logic f1, f2, f3;
    logic g1;

    // Invertori: NILI kola sa vezanim ulazima.
    assign D_n = ~(D | D);
    assign C_n = ~(C | C);
    assign B_n = ~(B | B);
    assign A_n = ~(A | A);

    // Segment a.
    assign a1 = ~(D | C_n | B | A);
    assign a2 = ~(D | C | B | A_n);
    assign a = ~(a1 | a2);

    // Segment b; b1 i b2 koriste se i za segment c.
    assign b1 = ~(D_n | B_n);
    assign b2 = ~(D_n | C_n);
    assign b3 = ~(C_n | B_n | A);
    assign b4 = ~(C_n | B | A_n);
    assign b = ~(b1 | b2 | b3 | b4);

    // Segment c.
    assign c1 = ~(C | B_n | A);
    assign c = ~(b1 | b2 | c1);

    // Segment d; a1 i a2 su zajednicki sa segmentom a.
    assign d1 = ~(D | C_n | B_n | A_n);
    assign d = ~(a1 | a2 | d1);

    // Segment e.
    assign e1 = ~(D | A_n);
    assign e2 = ~(C | B | A_n);
    assign e3 = ~(D | C_n | B);
    assign e = ~(e1 | e2 | e3);

    // Segment f.
    assign f1 = ~(D | C | A_n);
    assign f2 = ~(D | C | B_n);
    assign f3 = ~(D | B_n | A_n);
    assign f = ~(f1 | f2 | f3);

    // Segment g; d1 je zajednicki sa segmentom d.
    assign g1 = ~(D | C | B);
    assign g = ~(g1 | d1);
endmodule
