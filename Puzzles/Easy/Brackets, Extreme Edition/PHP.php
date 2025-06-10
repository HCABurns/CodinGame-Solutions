<?php

fscanf(STDIN, "%s", $expression);

// Declare required inputs.
$stack = [];
$pairs = array("}"=>"{","]"=>"[",")"=>"(");
$inputs = ['{' , '[', '(' , '}' , ']' , ')'];
$valid = True;

foreach (str_split($expression) as $char){
    if (in_array($char, $inputs) == false){
        continue;
    }
    // Check if char is a closing bracket or not.
    if (array_key_exists($char, $pairs)){
        // If no character on stack or top of stack doesn't pair with char
        // set valid to false and break loop.
        if (count($stack) == 0){
            $valid = false;
            break;
        }
        if (array_pop($stack) != $pairs[$char]){
            $valid = false;
            break;
        }
    }else{
        // Add open bracket to the stack.
        array_push($stack,$char);
    }

}

// Output true if valid bracket pairs, otherwise false.
if (count($stack) != 0){
    $valid = False;
}

if ($valid == true){echo "true";}
else{echo "false";}

?>
