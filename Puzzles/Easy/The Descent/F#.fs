open System

(* game loop *)
while true do
    // Define muatable variables
    let mutable max_i = 0
    let mutable max_v = 0

    // Find max value and set that index to max_i
    for i in 0 .. 8 - 1 do
        let mountainH = int(Console.In.ReadLine()) 
        if (mountainH > max_v) then
            max_v <- mountainH
            max_i <- i
    
    // Convert int to string for output
    let intToString = string max_i
    
    // Output index of mountain to fire on.
    printfn "%s" intToString
