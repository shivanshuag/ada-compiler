--syntax checking
procedure test8 is
  number : Integer := 15;
  output : Integer;
  begin
    if(number = 1) then
      output := 1;
      put(output);
    else
      if(number < 4) then
        output := 2;
        put(output);
      else
        if(number < 8) then
          output := 4;
          put(output);
        else
          if(number<16) then
          output := 8;
           put(output);
         -- end if;
        end if;
        end if;
    end if;
  end test8;
