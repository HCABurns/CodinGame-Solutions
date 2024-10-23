input = new Scanner(System.in);

// game loop
while (true) {
    // Declare required variables
    int max_i = 0
    int max_v = 0

    // Find the index of the max height and store in max_i.
    for (i = 0; i < 8; ++i) {
        mountainH = input.nextInt() 
        
        if (mountainH > max_v){
            max_v = mountainH
            max_i = i
        }
    }
    // Output the index of the mountain to fire on.
    println Integer.toString(max_i)
}
