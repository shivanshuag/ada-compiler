--Type Checking
function Fib(i : in Integer) return Integer is
	begin
		if (i=0) then
			return 0;
		elsif (i=1) then 
			return 1;
		else
			return (Fib(i-1)+Fib(i-2));
		end if;
	end;

procedure test6 is
   input: Integer;
   output: Integer;	
   char : Character := '1';
begin		
   input:=50;	
   --output:=Fib(char);   --gives error for type of parameter
   --output:=Fib(input, output); -- gives error for number of parameters
   Put(output);
   Put(newline);
end test6;
