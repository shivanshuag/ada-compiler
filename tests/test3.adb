-- fibonnaci
function Fib(i : Integer) return Integer is
	begin
		if (i=0) then
			return 0;
		elsif (i=1) then 
			return 1;
		else
			return (Fib(i-1)+Fib(i-2));
		end if;
	end;

procedure test3 is
   input: Integer;
   output: Integer;	
begin		
   input:=6;	
   output:=Fib(input);
   Put(output);
   Put(newline);
end test3;
