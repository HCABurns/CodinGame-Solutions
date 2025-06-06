import java.util.*
import java.io.*
import java.math.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    val n = input.nextInt()
    if (input.hasNextLine()) {
        input.nextLine()
    }
    for (i in 0 until n) {
        // Get card number,remove spaces and convert to integer array.
        var arr = Array<Int>(16){1}
        val card = input.nextLine()
        var idx = 0
        for (j in 0..card.length-1){
            if (card[j] != ' '){
                arr[idx] = (Character.getNumericValue(card[j]))
                idx+=1;
                }
        }

        // Step 1 and 2
        var sum_val = 0;
        for (j in 0..arr.size-1 step 2){
            if (j%2 == 0){
                if (arr[j] * 2 < 10){
                    sum_val += arr[j] * 2
                }else{
                    sum_val += arr[j] * 2 - 9
                }
            }
        }

        // Step 3 - Add odd place values.
        var odd_value = 0;
        for (j in 1..arr.size-1 step 2){
            odd_value += arr[j]
        }

        // Step 4 - Output YES if card is valid otherwise NO.
        if ((odd_value + sum_val) % 10 == 0){
            println("YES")
        }else{
            println("NO")
        }
    }
    input.close()
}
