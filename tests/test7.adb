-- type checking 
procedure test7 is
   input: Integer;
   output: Integer := 0;	
   char : Character := '1';
   bool : Boolean;
begin		
   output := input + 50;	--does not give error if undeclared as in GNAT compiler
   output := char + output;  -- gives error because character + integer
   output := input * bool;   -- gives error
   Put(output);
   Put(newline);
end;			--gives error label do not match
