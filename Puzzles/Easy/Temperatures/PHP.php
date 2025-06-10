<?php

// $n: the number of temperatures to analyse
fscanf(STDIN, "%d", $n);
$inputs = explode(" ", fgets(STDIN));
// Go thorugh each value and compare with closest. If it is smaller than closest, set new closest.
// If equal with closest then select the positive value if available.
$temp = 999999;
for ($i = 0; $i < $n; $i++)
{
    $t = intval($inputs[$i]); // a temperature expressed as an integer ranging from -273 to 5526
    if (abs($t) < abs($temp)){
        $temp = $t;
    }else if (abs($t) == abs($temp)){
        $temp = max($t,$temp);
    }
}
// Print closest to zero.
if ($temp != 999999){
    echo "$temp\n";
}else{
    echo("0\n");
}
?>
