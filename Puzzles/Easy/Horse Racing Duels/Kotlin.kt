import java.util.Scanner

fun main(args : Array<String>) {
    // Get size of inputs and store in a array.
    val input = Scanner(System.`in`)
    val N = input.nextInt()
    val numbers = IntArray(N)
    for (i in 0 until N) {
        val pi = input.nextInt()
        numbers[i] = pi
    } 
    // Sort array.
    numbers.sort()
    // Define difference variable.
    var maxVal = 10000001

    // Check adjacent horses power and store minimum difference.
    for(i in 0 until N-1){
        if ((numbers[i+1] - numbers[i])<maxVal){
            maxVal = numbers[i+1] - numbers[i]
        }
    }
    // Output minimum difference
    println(maxVal)
}
