import std;

void main()
{
    int surfaceN = readln.chomp.to!int; // the number of points used to draw the surface of Mars.
    for (int i = 0; i < surfaceN; i++) {
        auto inputs = readln.split;
        int landX = inputs[0].to!int; // X coordinate of a surface point. (0 to 6999)
        int landY = inputs[1].to!int; // Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    }

    // game loop
    while (1) {
        auto inputs2 = readln.split;
        int X = inputs2[0].to!int;
        int Y = inputs2[1].to!int;
        int hSpeed = inputs2[2].to!int; // the horizontal speed (in m/s), can be negative.
        int vSpeed = inputs2[3].to!int; // the vertical speed (in m/s), can be negative.
        int fuel = inputs2[4].to!int; // the quantity of remaining fuel in liters.
        int rotate = inputs2[5].to!int; // the rotation angle in degrees (-90 to 90).
        int power = inputs2[6].to!int; // the thrust power (0 to 4).

        // If speed larger than landing speed, set power to max.
        if( vSpeed >-39 ) { 
            power = 0;
            writeln("0 0");
        }
        else { 
            power = 4;
            writeln("0 4");
        }
    }
}
