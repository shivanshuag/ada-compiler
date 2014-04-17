-- Case Statement
procedure test11 is
   a, b, c: Integer;
begin
   a := 10;
   b := 3;

   case b is
      when 1 =>
         c := a * 1;
      when 2 =>
         c := a * 2;
      when 3 =>
         c := a * 3; 
      when others =>
         c := a * 4;     
   end case;
   Put(c);
end test11;
