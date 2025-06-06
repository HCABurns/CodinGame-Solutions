import java.util.*
import java.io.*
import java.math.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    val typedKeys = input.nextLine()

    // Create array.
    var arr = ArrayList<Char>();

    // Place charaters in the correct position, or remove charater if required.
    var i = 0;
    for (j in 0..typedKeys.length-1){
        var c = typedKeys[j];

        // Ensure i is in bounds.
        if (i < 0){
            i = 0;
        }else if (i>arr.size){
            i = arr.size
        }

        // Check character and perform correct operation.
        if (c == '<'){
            i -= 1
        }else if (c == '>'){
            i +=1
        }else if (c == '-'){
            i -= 1
            if (i != -1){
                arr.removeAt(i)
            }
        }else{
            arr.add(i, c)
            i+=1
        }
    }

    // Output the new string.
    println(arr.joinToString(separator = ""))
}
