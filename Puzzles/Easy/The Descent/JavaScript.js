// game loop
while (true) {
    // Declare required variables.
    let maxVal = 0;
    let maxIndex = 0;

    // Find the index of the max height and store in max_index.
    for (let i = 0; i < 8; i++) {
        const mountainH = parseInt(readline());
        if (mountainH > maxVal){
            maxVal = mountainH;
            maxIndex = i;
        }
    }
    // Output the index of the mountain to fire on.
    console.log(maxIndex);
}
