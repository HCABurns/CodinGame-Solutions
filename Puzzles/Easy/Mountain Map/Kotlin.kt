import java.util.*
import java.io.*
import java.math.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    val n = input.nextInt() // the number of mountains
    var heights = Array<Int>(n){1}
    var width = 0
    var max_height = 0
    for (i in 0 until n) {
        val height = input.nextInt() // height of the mountain
        heights[i] = height
        width += height
        max_height = Math.max(height, max_height)
    }
    
    // Get width and height of the grid.
    width *= 2
    var height = max_height
        
    // Form Grid
    var grid = ArrayList<Array<Char>>()
    for (i in 0..height-1){
        var arr = Array<Char>(width){' '}
        for (j in 0..width-1){
            arr[j] = ' '
        }
        grid.add(arr)
    }

    // Place mountains in the correct places in the grid.
    var i = height-1
    var j = 0
    for (mountain_height in heights){
        for (_k in 0..mountain_height-1){
            grid.get(i)[j] = '/'
            i-=1;
            j+=1;
        }
        i+=1;
        for (_k in 0..mountain_height-1){
            grid.get(i)[j] = '\\'
            i+=1
            j+=1
        }
        i-=1
    }

    // Print grid with rstrip to remove trailing spaces.
    for (arr in grid){
        println(arr.joinToString(separator = "").trimEnd());
    }
}
