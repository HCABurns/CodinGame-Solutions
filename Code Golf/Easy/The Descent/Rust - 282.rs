use std::io;
macro_rules!parse_input{($x:expr,$t:ident)=>($x.trim().parse::<$t>().unwrap())}
fn main(){loop{let mut I=0;let mut V=0;for k in 0..8 as usize{let mut i = String::new();io::stdin().read_line(&mut i).unwrap();let H=parse_input!(i,i32);if(H>V){V=H;I=k;}}println!("{}",I)}}
