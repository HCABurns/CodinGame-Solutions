import java.util.*
import java.io.*
import java.math.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    val n = input.nextInt()
    var remainder = 1

    // Array for storing ints, hashmap for storing index and index.
    var res = StringBuilder();
    var values = HashMap<Int, Int>()
    var idx = 0
    
    // Complete the divison until terminates or repeat found.
    while (remainder != 0){
        // Check for repeated remainder.
        if (values.containsKey(remainder)){
            res.insert( values[remainder]!!, '(')
            res.append(')')
            break;
        }
        values.put(remainder, idx);

        // Complete the division.
        remainder *= 10
        var value = remainder / n
        res.append(value)
        remainder = remainder % n

        // Increment index variable.
        idx += 1
    }

    // Print the value.
    println("0."+res.toString())
}
