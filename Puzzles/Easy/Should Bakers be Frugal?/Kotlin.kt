import java.util.*
import java.io.*
import java.math.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    var side = input.nextFloat()
    val diameter = input.nextFloat()
    
    // Calculate wasteful bakers amount.
    var wasteful =  Math.pow(Math.floor(side.toDouble() / diameter),2.0)

    // Calculate frugal bakers amount.
    var frugal = 0
    var area = side*side
    while (side > diameter){
        // Calculate amount possible to be cut.
        var amount = (Math.floor(side.toDouble() / diameter)).toInt()
        amount *= amount
        // Convert wasted into a new dough rectangle.
        frugal += amount
        area -= amount * (Math.PI*Math.pow((diameter.toDouble()/2),2.0)).toFloat()
        side = Math.sqrt(area.toDouble()).toFloat()
     }

    // Output the correct number of biscuits.
    println((frugal - wasteful).toInt())
}
