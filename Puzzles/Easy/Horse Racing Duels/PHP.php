<?php
// Read in array.
fscanf(STDIN, "%d", $N);
$arr = [];
for ($i = 0; $i < $N; $i++)
{
    fscanf(STDIN, "%d", $pi);
    $arr[$i] = $pi;
}

// Sort.
sort($arr);

// Find minimum difference.
$diff = PHP_INT_MAX;
for ($i = 0; $i < $N-1; $i++)
{
    if ($arr[$i+1] - $arr[$i] < $diff)
    {
        $diff = $arr[$i+1] - $arr[$i];
    }
}

// Print minimum difference.
print($diff."\n");
?>
