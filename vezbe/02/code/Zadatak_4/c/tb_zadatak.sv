module tb_zadatak;
    timeunit 1ns;
    timeprecision 1ps;

    logic [3:0] BCD3, BCD2, BCD1, BCD0;
    logic [6:0] SEG3, SEG2, SEG1, SEG0;
    zadatak UUT (.BCD3(BCD3), .BCD2(BCD2), .BCD1(BCD1), .BCD0(BCD0),
                 .SEG3(SEG3), .SEG2(SEG2), .SEG1(SEG1), .SEG0(SEG0));

    // Nezavisna tabela prikaza; redosled segmenata je abcdefg.
    function automatic logic [6:0] cifra(input int unsigned n);
        case (n)
            0: cifra = 7'b1111110;
            1: cifra = 7'b0110000;
            2: cifra = 7'b1101101;
            3: cifra = 7'b1111001;
            4: cifra = 7'b0110011;
            5: cifra = 7'b1011011;
            6: cifra = 7'b1011111;
            7: cifra = 7'b1110000;
            8: cifra = 7'b1111111;
            9: cifra = 7'b1111011;
            default: cifra = 7'b1001111;
        endcase
    endfunction

    // Referenca koristi decimalnu vrednost i tabelu, bez RTL izraza.
    function automatic logic [27:0] prikaz(input logic [15:0] word);
        int unsigned n;
        if (word[15:12] > 9 || word[11:8] > 9 ||
            word[7:4] > 9 || word[3:0] > 9)
            return {21'b0, 7'b1001111};
        n = 1000 * int'(word[15:12]) + 100 * int'(word[11:8]) +
            10 * int'(word[7:4]) + int'(word[3:0]);
        return {n >= 1000 ? cifra(n / 1000) : 7'b0,
                n >= 100 ? cifra((n / 100) % 10) : 7'b0,
                n >= 10 ? cifra((n / 10) % 10) : 7'b0,
                cifra(n % 10)};
    endfunction

    task automatic proveri(input logic [15:0] word);
        {BCD3, BCD2, BCD1, BCD0} = word;
        #10ns;
        assert ({SEG3, SEG2, SEG1, SEG0} === prikaz(word))
            else $fatal(1, "Prikaz: BCD=%h, SEG=%b %b %b %b",
                        word, SEG3, SEG2, SEG1, SEG0);
    endtask

    initial begin
        $dumpfile("tb_zadatak.vcd");
        $dumpvars(0, tb_zadatak);
        proveri(16'h0231);
        proveri(16'h00A5);
        proveri(16'h0504); // E mora nestati bez resetovanja.
        proveri(16'h0000);
        proveri(16'h1000);
        proveri(16'hFFFF);
        proveri(16'h0009);
        // Svaki nedozvoljeni kod na svakoj poziciji, pa ispravan broj.
        for (int pozicija = 0; pozicija < 4; pozicija++) begin
            for (int greska = 10; greska < 16; greska++) begin
                proveri((16'h1234 & ~(16'hF << (4 * pozicija))) |
                        (16'(greska) << (4 * pozicija)));
                proveri(16'h0504);
            end
        end
        for (int word = 0; word < 65536; word++)
            proveri(16'(word));
        $display("PASS: %m, 65536 ulaza i prelazi bez resetovanja");
        $finish;
    end
endmodule
