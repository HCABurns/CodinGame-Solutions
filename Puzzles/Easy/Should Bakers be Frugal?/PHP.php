<?php
// Get inputs.
fscanf(STDIN, "%f %f", $side, $diameter);

// Calculate wasteful bakers amount.
$wasteful = intval(pow(floor($side / $diameter),2));
        
// Calculate frugal bakers amount.
$frugal = 0;
$area = $side*$side;
while ($side > $diameter){
    // Calculate amount possible to be cut.
    $amount = intval(floor($side / $diameter));
    $amount *= $amount;
    // Convert wasted into a new dough rectangle.
    $frugal += $amount;
    $area -= $amount * (pi()*pow(($diameter/2),2));
    $side = sqrt($area);
}
// Output the correct 
echo (intval($frugal - $wasteful));

?>
