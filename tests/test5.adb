-- scoping
--gives error because z is declared in an enclosed block
procedure test5 is
	x, y : Integer;
	z : Integer := 12;
	begin
	block1:
     declare
		begin
			z:=10;			
			put(z);
			x := 5;
	end block1;
	goto block1;
	x := 10;
	y := 10;
	put(z);
	end test5;	
