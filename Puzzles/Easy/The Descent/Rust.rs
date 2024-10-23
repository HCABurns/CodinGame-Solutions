use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn main() {

    // game loop
    loop {
        // Declare required variables.
        let mut max_i = 0;
        let mut max_v = 0;

        // Find the index of the max height and store in max_index.
        for i in 0..8 as usize {
            let mut input_line = String::new();
            io::stdin().read_line(&mut input_line).unwrap();
            let mountain_h = parse_input!(input_line, i32); // represents the height of one mountain.
            if (mountain_h > max_v){
                max_v = mountain_h;
                max_i = i;
            }
        }

        // Ourput the index of the mountain to fire on.
        println!("{}",max_i); 
    }
}
