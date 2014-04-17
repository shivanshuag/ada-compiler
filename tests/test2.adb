-- SAXPY computation
procedure test2 is
	arr1 : array(1..20) of Integer;
	arr2 : array(1..20) of Integer;
    space : character := ' ';
    alpha : integer := 2;
  begin
  	for J in 0 .. 19 loop
         arr1(J) := J;
    end loop;

    for J in 0 .. 19 loop
        arr2(J) := 20 - J;
    end loop;

    for J in 0 .. 19 loop
         arr2(J) := alpha*arr1(J) + arr2(J);
    end loop;

    for J in 0 .. 19 loop
         Put(arr2(J));
         Put(space);
    end loop;
    put(newline);
  end;
