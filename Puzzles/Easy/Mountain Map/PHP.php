<?php
// $n: the number of mountains
fscanf(STDIN, "%d", $n);
$heights = [];
$inputs = explode(" ", fgets(STDIN));
for ($i = 0; $i < $n; $i++)
{
    $height = intval($inputs[$i]); // height of the mountain
    $heights[$i] = $height;
}

// Get width and height of the grid.
$width = array_sum($heights)*2;
$height = max($heights);

// Form Grid
$grid = [];
for ($i = 0; $i < $height;$i++){
    $arr = [];
    for ($j = 0; $j<$width;$j++){
        $arr[$j] = ' ';
    }
    array_push($grid,$arr);
}

// Place mountains in the correct places in the grid.
$i = $height-1;
$j = 0;
foreach ($heights as  $mountain_height){
    for ($k = 0; $k < $mountain_height ; $k++){
        $grid[$i][$j] = '/';
        $i-=1;
        $j+=1;
    }
    $i+=1;
    for ($k = 0; $k < $mountain_height ; $k++){
        $grid[$i][$j] = '\\';
        $i+=1;
        $j+=1;
    }
    $i-=1;
}
// Print grid with rstrip to remove trailing spaces.
for ($i = 0; $i < $height; $i++){
    echo (rtrim(implode("",$grid[$i])) . "\n");
}
