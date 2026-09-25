entity latch is
port (s,r : in bit;
      q, nq : out bit);
end latch;
architecture dataflow of latch is
begin
q<=r nor nq;
nq<=s nor q;
end dataflow;
