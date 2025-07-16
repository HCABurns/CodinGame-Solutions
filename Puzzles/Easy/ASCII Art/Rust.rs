use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let l = parse_input!(input_line, i32);
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let h = parse_input!(input_line, i32);
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let t = input_line.trim_matches('\n').to_string().to_ascii_uppercase();

    // Get each row and print each characters ascii art with no newline until all characters have been printed
    for row_index in 0..h as usize {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let row = input_line.to_string();

        for c in t.chars() {
            let mut j: usize = c as usize - 'A' as usize;
            if j < 0 || j > 25 {
                j = 26;
            }
            let start = j * l as usize;
            let slice: String = row.chars().skip(start).take(l as usize).collect();
            print!("{}", slice);

        }
        println!(); // Newline after each row
    }
}
