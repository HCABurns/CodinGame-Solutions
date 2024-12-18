while true do
    (* Variables to be used to store heighest mountain value and position*)
    let max_i = ref 0 in
    let max_v = ref 0 in
    for i = 0 to 7 do
        let mountainh = int_of_string (input_line stdin) in
        (* Store the index and value of heighest mountain*)
        if mountainh > !max_v then max_v := mountainh;
        if mountainh == !max_v then max_i := i;
        ();
    done;
    (* Print index to be shot *) 
    print_endline (string_of_int !max_i);
    ();
done;
