use std::io;

macro_rules! print_err {
    ($($arg:tt)*) => (
        {
            use std::io::Write;
            writeln!(&mut ::std::io::stderr(), $($arg)*);
        }
    )
}

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let inputs = input_line.split(" ").collect::<Vec<_>>();
    let light_x = parse_input!(inputs[0], i32); // the X position of the light of power
    let light_y = parse_input!(inputs[1], i32); // the Y position of the light of power
    let initial_tx = parse_input!(inputs[2], i32); // Thor's starting X position
    let initial_ty = parse_input!(inputs[3], i32); // Thor's starting Y position

    let mut thor_x = initial_tx;
    let mut thor_y = initial_ty;

    // game loop
    loop {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let remaining_turns = parse_input!(input_line, i32); // The remaining amount of turns Thor can move. Do not remove this line.

    	let mut direction_x = "";
    	let mut direction_y = "";
    
    	if thor_y > light_y {
    		direction_y = "N";
    		thor_y = thor_y - 1;
    	} else if thor_y < light_y {
    		direction_y = "S";
    		thor_y = thor_y + 1;
    	}
    	
    	if thor_x > light_x {
    		direction_x = "W";
    		thor_x = thor_x - 1;
    	} else if thor_x < light_x {
    		direction_x = "E";
    		thor_x = thor_x + 1;
    	}
    	
    	println!("{}{}", direction_y, direction_x);
    }
}
