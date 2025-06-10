<?php
fscanf(STDIN, "%d", $N);

// Generate Fibonacci sequence
$fib = array(1,1);
while ($N > $fib[count($fib)-1] + $fib[count($fib)-2]){
    array_push($fib, $fib[count($fib)-1] + $fib[count($fib)-2]);
}

// Find Zeckendorf representation by picking largest available number until sum is n.
$i = count($fib)-1;
$out = [];
while ($N > 0){
    if ($N - $fib[$i] >= 0){
        $N -= $fib[$i];
        array_push($out, $fib[$i]);
    }
    $i-=1;
}

// Output the representation.
echo(implode("+", $out));
?>
