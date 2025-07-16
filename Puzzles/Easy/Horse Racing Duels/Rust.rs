use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}


fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32);
    
    // Populate vector with horse strengths.
    let mut arr = vec![];
    //let mut arr = [0; n];
    for i in 0..n as usize {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let pi = parse_input!(input_line, i32);
        arr.push(pi);
    }

    arr.sort();

    // Define difference variable.
    let mut closestStrength: i32 = 10000001;

    // Check adjacent horses power and store minimum difference.
    for i in 0..(n-1) as usize {
        if (arr[i+1]-arr[i])<closestStrength{
            closestStrength = arr[i+1]-arr[i];
        }
    }

    // Print the closest strength between horses.
    println!("{}",closestStrength);
}
