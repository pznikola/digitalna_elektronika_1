PROCESS ( Sel, x1, x2 )
BEGIN
  f <= x1 ;
  IF Sel = 1 THEN
    f <= x2 ;
  END IF ;
END PROCESS ;
