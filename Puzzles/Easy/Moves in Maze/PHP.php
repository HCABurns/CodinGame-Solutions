<?php
//NOTE: Coordinates are formed as [y,x] / [Row , column]
// Form grid in 2d array and store position of "S" in start
fscanf(STDIN, "%d %d", $w, $h);
$grid = [];
$start = [0,0];
for ($i = 0; $i < $h; $i++)
{
    $ROW = stream_get_line(STDIN, 255 + 1, "\n");
    $grid[$i] = str_split($ROW);
    $j = 0;
    foreach ($grid[$i] as $char)
    {
        if ($char == "S")
        {
            $grid[$i][$j] = ".";
            $start = [$i,$j];
        }
        $j += 1;
    }
}


// Iterative BFS changing any . characters to the next in the sequence.
$to_visit = [$start];
$val = 0;
while ($to_visit)
{
    $tmp = [];
    while ($to_visit)
    {
        $node = $to_visit[0];
        array_shift($to_visit);
        // Wrap the value (Wraps around the grid)
        $x = ($node[1]+$w) % $w;
        $y = ($node[0]+$h) % $h;
        // If spot is empty -> Add to the list and set to current character in sequence
        if ($grid[$y][$x] == ".")
        {
            if ($val < 10) {
                $grid[$y][$x] = strval($val);
            } else {
                $grid[$y][$x] = chr($val);
            }
            array_push($tmp,[$y+1,$x]);
            array_push($tmp,[$y-1,$x]);
            array_push($tmp,[$y,$x-1]);
            array_push($tmp,[$y,$x+1]);
        }
        
    }
    // Update to_visit list and character in the sequence
    $to_visit = $tmp;
    $val+=1;
    if ($val == 10)
    {
        $val=ord("A");
    }

}

// Output the changed grid.
for ($i = 0; $i < $h; $i++) {
    echo implode('', $grid[$i]);
    if ($i !== $h - 1) {
        echo "\n";
    }
}
?>
