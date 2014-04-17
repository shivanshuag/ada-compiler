--nested conditional
procedure test4 is
  number : Integer := 3;
  output : Integer;
  begin
    if(number = 1) then
      output := 1;
      put(output);
    else
      if(number < 4) then
        output := 2;
        put(output);
        if(number = 3) then
          output := 3;
          put(output);
        end if;
      else
        if(number < 8) then
          output := 4;
          put(output);
        else
          if(number<16) then
          output := 8;
           put(output);
          end if;
        end if;
        end if;
    end if;
  end test4;
