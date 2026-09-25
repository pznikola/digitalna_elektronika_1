entity ckt is
port (A: in BIT:=1; B: in BIT; Y,Z: out BIT);
end ckt;
architecture ckt of ckt is
begin
B <= A and A;
Y<= A and B;
Z<= B after 10 ns;
end ckt;
