package main

import "fmt"
import "sort"


func main() {
    // Define variables.
    var N int
    fmt.Scan(&N)
    var arr []int
    difference := 10000001

    // Fill array with horse strengths.
    for i := 0; i < N; i++ {
        var pi int
        fmt.Scan(&pi)
        arr = append(arr, pi)
    }

    // Sort array.
    sort.Ints(arr)

    // Check adjacent horses power and store minimum difference.
    for i := 0; i < N-1; i++ {
        val := arr[i+1] - arr[i]
        if val < difference{
            difference = val
        }
    }
    // Output the min difference
    fmt.Println(difference)
}
