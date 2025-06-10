<?php
# Hashmap for storing values, array for storing order of keys.
$keys = array();
$order = [];

fscanf(STDIN, "%d", $N);
for ($i = 0; $i < $N; $i++)
{
    # Get inputs.
    $s = explode(" ",stream_get_line(STDIN, 100 + 1, "\n"));
    
    # Perfrom the correct operation.
    if ($s[0] == "SET"){
        foreach (array_splice($s, 1, count($s)-1) as $item){
            $item = explode("=",$item);
            $name = $item[0];
            $value = $item[1];
            
            if (!array_key_exists($name, $keys)){
                $order[count($order)] = $name;
            }
            $keys[$name] = $value;

        }
    }
    else if ($s[0] == "GET"){
        $res = [];
        foreach (array_splice($s, 1, count($s)-1) as $name){
            if (array_key_exists($name, $keys)){
                $str = $keys[$name];
            }else{$str = "null";}
            $res[count($res)] = $str;
        }
        echo (implode(" ",$res) . "\n");
    }
    else if ($s[0] == "KEYS"){
        $res = [];
        if (count($keys) > 0){
            foreach ($order as $name){
                $res[count($res)] = $name;
            }
            echo (implode(" ",$res). "\n");
        }
        else{
            echo ("EMPTY" . "\n");
        }
    }
    else if ($s[0] == "EXISTS"){
        $res = [];
        foreach (array_splice($s, 1, count($s)-1) as $name){
            if (array_key_exists($name, $keys)){
                $str = "true";
            }else{
                $str = "false";
            }
            $res[count($res)] = $str;
        }
        echo (implode(" ",$res) . "\n");   
    }
    
}
