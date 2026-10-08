with Ada.Text_IO;
with Greeting;
procedure Consumer is
begin
   Ada.Text_IO.Put_Line (Greeting.Message);
end Consumer;
