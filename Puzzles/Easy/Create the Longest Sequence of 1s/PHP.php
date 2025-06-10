<?php
// Read in value.
$b = stream_get_line(STDIN, 999 + 1, "\n");
$s = explode("0", $b);

// Value of the largest when changing and 0 to 1.
$largest = 0;

// Go through and compare adjacent pairs testing if their sizes added make a new largest.
for ($i = 0; $i < count($s)-1; $i++){
    if (strlen($s[$i]) + strlen($s[$i+1]) + 1 > $largest){
        $largest = strlen($s[$i]) + strlen($s[$i+1]) + 1;
    }
}
// Return the new largest sequence of 1s length.
echo("$largest");
?>
