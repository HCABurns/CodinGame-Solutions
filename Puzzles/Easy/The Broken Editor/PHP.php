<?php

$typedKeys = stream_get_line(STDIN, 80 + 1, "\n");

// Create array.
$arr = [];

// Place charaters in the correct position, or remove charater if required.
$i = 0;
for ($j = 0; $j<strlen($typedKeys);$j++){
    $c = $typedKeys[$j];

    // Ensure i is in bounds.
    if ($i < 0){
        $i = 0;
    } else if ($i>count($arr)){
        $i = count($arr);
    }

    // Check character and perform correct operation.
    if ($i < 0) {
        $i = 0;
    } elseif ($i > count($arr)) {
        $i = count($arr);
    }

    if ($c == '<') {
        $i--;
    } elseif ($c == '>') {
        $i++;
    } elseif ($c == '-') {
        if ($i > 0) {
            $i--;
            array_splice($arr, $i, 1);
        }
    } else {
        $arr = array_merge(
            array_slice($arr, 0, $i),
            [$c],
            array_slice($arr, $i)
        );
        $i++;
    }
}

// Output the new string.
echo(implode("",$arr));
?>
