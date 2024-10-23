input = new Scanner(System.in);

surfaceN = input.nextInt() // the number of points used to draw the surface of Mars.
for (i = 0; i < surfaceN; ++i) {
    landX = input.nextInt() // X coordinate of a surface point. (0 to 6999)
    landY = input.nextInt() // Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
}

// game loop
while (true) {
    X = input.nextInt()
    Y = input.nextInt()
    hSpeed = input.nextInt() // the horizontal speed (in m/s), can be negative.
    vSpeed = input.nextInt() // the vertical speed (in m/s), can be negative.
    fuel = input.nextInt() // the quantity of remaining fuel in liters.
    rotate = input.nextInt() // the rotation angle in degrees (-90 to 90).
    power = input.nextInt() // the thrust power (0 to 4).

    // If speed larger than landing speed, set power to max.
    if (vSpeed > -39){
        power = 0
        println "0 0"
    }
    else{
        power = 4
        println "0 4"
    }
}
