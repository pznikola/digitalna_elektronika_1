module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [3:0] ABCD;
    logic Y;

    zadatak #(.T(10ns)) UUT (
        .A(ABCD[3]), .B(ABCD[2]), .C(ABCD[1]), .D(ABCD[0]),
        .Y(Y)
    );

    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        ABCD = 4'b1111;
        #50ns;
        assert (Y === 1'b1) else $fatal(1, "Pocetni izlaz");
        ABCD = 4'b1110;
        #15ns;
        assert (Y === 1'b1) else $fatal(1, "Izlaz pre hazarda");
        #10ns;
        assert (Y === 1'b0) else $fatal(1, "Ocekivani hazard od 2T do 3T");
        #10ns;
        assert (Y === 1'b1) else $fatal(1, "Izlaz posle hazarda");
        #15ns;
        $display("PASS: %m");
        $finish;
    end
endmodule
