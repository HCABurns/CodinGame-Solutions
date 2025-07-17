import std;

void main()
{
    auto inputs = readln.split;
    int light_x = inputs[0].to!int; // the X position of the light of power
    int light_y = inputs[1].to!int; // the Y position of the light of power
    int thor_x = inputs[2].to!int; // Thor's starting X position
    int thor_y = inputs[3].to!int; // Thor's starting Y position

    // game loop
    while (1) {
        int remainingTurns = readln.chomp.to!int; // The remaining amount of turns Thor can move. Do not remove this line.

        string[2] o = ["",""];
        // If thor is below light, move north.
        if (light_y < thor_y){
            o[0]="N";
            thor_y-=1;
        }
        // If thor is above light, move south.
        if (light_y > thor_y){
            o[0]="S";
            thor_y+=1;
        }
        // If thor is right of the light, move west.
        if (light_x < thor_x){
            o[1] = "W";
            thor_x+=1;
        }
        // If thor is left of the light, move east.
        if (light_x > thor_x){
            o[1] = "E";
            thor_x-=1;
        }
        // A single line providing the move to be made: N NE E SE S SW W or NW
        writefln("%s%s",o[0],o[1]);
    }
}
