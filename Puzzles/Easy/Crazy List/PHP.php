<?php
// Get inputs list.
$crazylist = stream_get_line(STDIN, 100 + 1, "\n");
$crazylist = explode(" ",$crazylist);
for($i = 0; $i < count($crazylist); $i++){
    $crazylist[$i] = intval($crazylist[$i]);
}

// Find the difference between them.
$a = [];
for($i = 1; $i < count($crazylist); $i++){
    $a[$i-1] = $crazylist[$i] - $crazylist[$i-1];
}

if (count($a) > 1 && $a[0] != $a[1]){
    // Multiplication sequence. 
    $d = floor($a[1] / $a[0]);
    printf("%d", ($crazylist[count($crazylist)-1] + $a[count($a)-1]*$d));
}
else{
    // Add/Subtract - a+(n)*d
    printf("%d", ($crazylist[0] + (count($crazylist))*$a[0]));
}
