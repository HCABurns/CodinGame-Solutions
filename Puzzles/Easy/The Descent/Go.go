package main
import "fmt"

func main() {
    for {
        // Declare required variables
        max_i := 0
        max_v := 0

        // Find the index of the max height and store in max_index.
        for i := 0; i < 8; i++ {
            var mountainH int
            fmt.Scan(&mountainH)
            if mountainH > max_v{
                max_v = mountainH
                max_i = i
            }
        }
        
        // Output the index of the mountain to fire on.
        fmt.Println(max_i) 
    }
}
