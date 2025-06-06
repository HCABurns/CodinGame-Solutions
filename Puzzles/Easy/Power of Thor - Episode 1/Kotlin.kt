import java.util.*
import java.io.*
import java.math.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    val lightX = input.nextInt() // the X position of the light of power
    val lightY = input.nextInt() // the Y position of the light of power
    var x = input.nextInt() // Thor's starting X position
    var y = input.nextInt() // Thor's starting Y position

    // game loop
    while (true) {
        val remainingTurns = input.nextInt() // The remaining amount of turns Thor can move. Do not remove this line.

        // Loop and if thor needs to move a direction, append it to output.
        for (i in 0..remainingTurns){
            var leftRight = "";
            var upDown = "";

            // If thor is right of the light, move west.
            if (lightX < x){
                leftRight="W";
                x-=1;
            }
            // If thor is left of the light, move east.
            else if (lightX > x){
                leftRight="E";
                x+=1;
            }
            // If thor is below light, move north.
            if (lightY < y){
                upDown = "N";
                y-=1;
            }
            // If thor is above light, move south.
            else if (lightY > y){
                upDown = "S";
                y+=1;
            }
            // Output direction to travel.
            println(upDown+leftRight);
        } 
    }
}
