// Read in the inputs.
var inputs = readline().split(' ');
const lightX = parseInt(inputs[0]); // the X position of the light of power
const lightY = parseInt(inputs[1]); // the Y position of the light of power
var x = parseInt(inputs[2]); // Thor's starting X position
var y = parseInt(inputs[3]); // Thor's starting Y position

while (true) {
    const remainingTurns = parseInt(readline());

    // Loop and if thor needs to move a direction, append it to output.
    for (let i = 0 ; i < remainingTurns;i++){
        var leftRight = "";
        var upDown = "";

        // If thor is right of the light, move west.
        if (lightX < x){
            leftRight="W";
            x-=1;
        }
        // If thor is left of the light, move east.
        else if (lightX > x){
            leftRight="E";
            x+=1;
        }
        // If thor is below light, move north.
        if (lightY < y){
            upDown = "N";
            y-=1;
        }
        // If thor is above light, move south.
        else if (lightY > y){
            upDown = "S";
            y+=1;
        }

        // Output direction to travel.
        console.log(upDown + leftRight);
    }
}
