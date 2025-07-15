// Get positions.
var inputs: string[] = readline().split(' ');
let light_x: number = parseInt(inputs[0]); // the X position of the light of power
let light_y: number = parseInt(inputs[1]); // the Y position of the light of power
let thor_x: number = parseInt(inputs[2]); // Thor's starting X position
let thor_y: number = parseInt(inputs[3]); // Thor's starting Y position

// game loop
while (true) {
    const remainingTurns: number = parseInt(readline()); // The remaining amount of turns Thor can move. Do not remove this line.

    let output : string ="";
    // If thor is below light, move north.
    if (light_y < thor_y){
        output="N"
        thor_y-=1
    }
    // If thor is above light, move south.
    if (light_y > thor_y){
        output="S"
        thor_y+=1
    }
    // If thor is right of the light, move west.
    if (light_x < thor_x){
        output+="W"
        thor_x+=1
    }
    // If thor is left of the light, move east.
    if (light_x > thor_x){
        output+="E"
        thor_x-=1
    }
    // A single line providing the move to be made: N NE E SE S SW W or NW
    console.log(output);
}
