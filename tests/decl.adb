with Text_IO;
with Gnat.Io; use Gnat.Io;
procedure Example is
	type Day_Type is (Sun, Mon, Tue, Wed, Thu, Fri, Sat);
	Work_Hours : array(Day_Type) of Natural;
	function Adjust_Overtime
		(Day : Day_Type; Hours : Natural) return Natural is
		procedure abc is
		begin
			Put("123");
		end abc;
	begin
		Work_Hours(Day) := 12;
	end Adjust_Overtime;
begin
	Work_Hours := (0, 8, 8, 8, 8, 0);
	for Day in Day_Type loop
		Work_Hours(Day) := Adjust_Overtime(Day, Work_Hours(Day));
	end loop;
end Example;