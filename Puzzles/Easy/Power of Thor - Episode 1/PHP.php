<?php
// $lightX: the X position of the light of power
// $lightY: the Y position of the light of power
// $initialTx: Thor's starting X position
// $initialTy: Thor's starting Y position
fscanf(STDIN, "%d %d %d %d", $lightX, $lightY, $x, $y);

// game loop
while (TRUE)
{
    // $remainingTurns: The remaining amount of turns Thor can move. Do not remove this line.
    fscanf(STDIN, "%d", $remainingTurns);

    // Loop and if thor needs to move a direction, append it to output.
    for ($i=0; $i<$remainingTurns; $i++){
        $leftRight = "";
        $upDown = "";

        // If thor is right of the light, move west.
        if ($lightX < $x){
            $leftRight="W";
            $x-=1;
        }
        // If thor is left of the light, move east.
        else if ($lightX > $x){
            $leftRight="E";
            $x+=1;
        }
        // If thor is below light, move north.
        if ($lightY < $y){
            $upDown = "N";
            $y-=1;
        }
        // If thor is above light, move south.
        else if ($lightY > $y){
            $upDown = "S";
            $y+=1;
        }
        // Output direction to travel.
        printf("%s%s\n",$upDown,$leftRight);
    } 
}

