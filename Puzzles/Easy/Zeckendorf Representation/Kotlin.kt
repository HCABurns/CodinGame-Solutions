import java.util.*
import java.io.*
import java.math.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    var N = input.nextLong()

    // Generate Fibonacci sequence
    var fib = ArrayList<Long>()
    fib.add(1)
    fib.add(1)
    while (N > fib.get(fib.size-1) + fib.get(fib.size-2)){
        fib.add(fib.get(fib.size-1) + fib.get(fib.size-2))
    }

    // Find Zeckendorf representation by picking largest available number until sum is n.
    var sb = StringBuilder();
    var i = fib.size-1;
    while (N > 0){
        if (N - fib.get(i) >= 0){
            N -= fib.get(i)
            sb.append(fib.get(i))
            sb.append("+")
        }
        i-=1;
    }

    // Output the representation.
    sb.setLength(sb.length - 1)
    println(sb.toString())
    input.close()
}
