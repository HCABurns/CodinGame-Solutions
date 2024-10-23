// game loop
while (true) {
    // Declare required variables
    let max_i : number = 0;
    let max_v : number = 0;

    // Find the index of the max height and store in max_index.
    for (let i = 0; i < 8; i++) {
        const mountainH: number = parseInt(readline()); // represents the height of one mountain.
        if (mountainH > max_v){
            max_v = mountainH;
            max_i = i;
        }
    }
    // Output the index of the mountain to fire on.
    console.log(max_i);
}
