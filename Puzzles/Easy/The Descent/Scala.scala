import scala.io.StdIn._

object Player extends App {
    // game loop
    while(true) {
        // Define required variables.
        var max_i = 0
        var max_v = 0

        // Find the index of the max height and store in max_i.
        for(i <- 0 until 8) {
            val mountainH = readLine.toInt // represents the height of one mountain.
            if (mountainH > max_v){
                max_v = mountainH
                max_i = i
            }
        }
        
        // Output the index of the mountain to fire on.
        println(max_i) 
    }
}
