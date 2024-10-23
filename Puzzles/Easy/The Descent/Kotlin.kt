import java.util.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)

    // game loop
    while (true) {
        // Define required variables
        var max_i = 0
        var max_v = 0

        // Find the index of the max height and store in max_index.
        for (i in 0 until 8) {
            val mountainH = input.nextInt()
            if (mountainH > max_v){
                max_v = mountainH
                max_i = i
            }
        }
        
        // Output the index of the mountain to fire on.
        println(max_i)
    }
}
