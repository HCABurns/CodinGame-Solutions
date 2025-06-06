import java.util.*
import java.io.*
import java.math.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    val b = input.nextLine()

    // Split the array on 1s.
    var arr = b.split("0");

    // Get max size of two adjacent sets of 1s.
    var  max_size = 0;
    var size = 0;
    for (i in 0..(arr.size-2)){
        size = arr[i].length + arr[i+1].length;
        if (size > max_size){
            max_size = arr[i].length + arr[i+1].length;
        }
    }
    // Return output + 1 for the flip bit.
    println(max_size + 1)
}
