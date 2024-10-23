<?php
// game loop
while (TRUE)
{
    // Define required variables.
    $maxVal = 0;
    $maxIndex = 0;

    // Find the index of the max height and store in max_index.
    for ($i = 0; $i < 8; $i++)
    {
        fscanf(STDIN, "%d", $mountainH);
        if ($mountainH > $maxVal){
            $maxVal = $mountainH;
            $maxIndex = $i;
        }
    }
    // Output the index of the mountain to fire on.
    echo $maxIndex . "\n" ;
}
?>
