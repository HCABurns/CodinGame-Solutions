<?php

fscanf(STDIN, "%d", $surfaceN);
for ($i = 0; $i < $surfaceN; $i++)
{
    // $landX: X coordinate of a surface point. (0 to 6999)
    // $landY: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    fscanf(STDIN, "%d %d", $landX, $landY);
}

// game loop
while (TRUE)
{
    // $hSpeed: the horizontal speed (in m/s), can be negative.
    // $vSpeed: the vertical speed (in m/s), can be negative.
    // $fuel: the quantity of remaining fuel in liters.
    // $rotate: the rotation angle in degrees (-90 to 90).
    // $power: the thrust power (0 to 4).
    fscanf(STDIN, "%d %d %d %d %d %d %d", $X, $Y, $hSpeed, $vSpeed, $fuel, $rotate, $power);

    // If speed larger than landing speed, set power to max.
    if ($vSpeed>-39){
        $power = 0;
    }else{
        $power = 4;
    }
    echo("0 {$power}\n");
}
?>
