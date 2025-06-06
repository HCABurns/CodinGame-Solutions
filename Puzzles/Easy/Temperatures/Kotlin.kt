import java.util.*
import java.io.*
import java.math.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    val n = input.nextInt() // the number of temperatures to analyse

    var closest = 0;
    // If size if 0 don't set closest so the output will be 0.
    if (n!=0){
        closest = 9999;
    }

    // Go thorugh each value and compare with closest. If it is smaller than closest, set new closest.
    // If equal with closest then select the positive value if available.
    for (i in 0 until n) {
        val t = input.nextInt() // a temperature expressed as an integer ranging from -273 to 5526
        if (Math.abs(t) <= Math.abs(closest)){
            if (Math.abs(t) == Math.abs(closest) && !(t<0 && closest<0)){
                closest = Math.abs(closest);
            }else{
                closest = t;
            }
        }
    }
    // Output the closest value to 0.
    println(closest)
}
