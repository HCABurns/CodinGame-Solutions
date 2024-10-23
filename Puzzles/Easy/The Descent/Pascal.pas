program Answer;
{$H+}
uses sysutils, classes, math;

// Helper to read a line and split tokens
procedure ParseIn(Inputs: TStrings) ;
var Line : string;
begin
    readln(Line);
    Inputs.Clear;
    Inputs.Delimiter := ' ';
    Inputs.DelimitedText := Line;
end;

var
    mountainH : Int32; // represents the height of one mountain.
    i : Int32;
    Inputs: TStringList;
    // Declare required variables
    max_i : Int32;
    max_v : Int32;
begin
    Inputs := TStringList.Create;

    // game loop
    while true do
    begin
        // Declare required variables values.
        max_i := 0;
        max_v := 0;

        // Find the index of the max height and store in max_index.
        for i := 0 to 7 do
        begin
            ParseIn(Inputs);
            mountainH := StrToInt(Inputs[0]);

            if (mountainH > max_v) then
            begin
                max_v := mountainH;
                max_i := i;
            end;

        end;

        // Output the index of the mountain to fire on.
        writeln(max_i); 
        flush(StdErr); flush(output); // DO NOT REMOVE
    end;
end.
