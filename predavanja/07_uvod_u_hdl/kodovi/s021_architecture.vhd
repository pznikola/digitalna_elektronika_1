ARCHITECTURE LogicFunc OF example1 IS
BEGIN
  f <= (x1 AND x2) OR (NOT x2 AND x3);
END LogicFunc;
