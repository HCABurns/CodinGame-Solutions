package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func absInt(x int64) int64 {
    return absDiffInt(x, 0)
}


func absDiffInt(x, y int64) int64 {
    if x < y {
        return y - x
    }
    return x - y
}

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Buffer(make([]byte, 1000000), 1000000)
    var inputs [] string

    // Find temp closest to 0 and prioritise positive over negatives if equal.
    var temp int64 = 999999
    // n: the number of temperatures to analyse
    var n int
    scanner.Scan()
    fmt.Sscan(scanner.Text(),&n)
    
    scanner.Scan()
    inputs = strings.Split(scanner.Text()," ")
    for i := 0; i < n; i++ {
        // t: a temperature expressed as an integer ranging from -273 to 5526
        t,_ := strconv.ParseInt(inputs[i],10,32)
        _ = t
        if absInt(t) < absInt(temp) {
            temp = t;
        }else if (absInt(t) == absInt(temp)){
            temp = int64(math.Max(float64(t), float64(temp)));
        }

    }
    
    // Print smallest temp.
    if temp != 999999{
        fmt.Println(temp);
    }
    if temp == 999999{
        fmt.Println("0");
    }
}
