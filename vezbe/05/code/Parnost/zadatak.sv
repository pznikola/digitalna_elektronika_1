module zadatak #(parameter int N = 6) (
    input logic [N-1:0] D,
    output logic [N:0] PARNA, NEPARNA
);
    logic P;
    // Redukcioni XOR predstavlja XOR svih informacionih bita.
    assign P = ^D;
    // Bit parnosti dodaje se zdesna, kao u tabeli.
    assign PARNA = {D, P};
    assign NEPARNA = {D, ~P};
endmodule
