PROCESS ( Sel, x1, x2 )
BEGIN
  IF Sel = '0' THEN
    f <= x1 ;
  ELSE
    f <= x2 ;
  END IF ;
END PROCESS ;
