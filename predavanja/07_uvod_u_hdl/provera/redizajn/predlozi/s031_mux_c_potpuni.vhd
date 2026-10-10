PROCESS ( Sel, x1, x2 )
BEGIN
  IF Sel = '1' THEN
    f <= x2;
  ELSE
    f <= x1;
  END IF;
END PROCESS;
