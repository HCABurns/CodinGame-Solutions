import java.util.*
import java.io.*
import java.math.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    val expression = input.next()

    var valid = true
    var stack = ArrayDeque(listOf("("))
    stack.pop()
    val pairs = HashMap<String, String>()
    pairs.put("}", "{")
    pairs.put("]", "[")
    pairs.put(")", "(")

    // Iterate through chars and check char is valid, if opening add it to stack
    // if closing then check if top of stack is a pair.
    for (c in expression.toCharArray()) {
        if ("(){}[]".contains(c)){
            if (pairs.containsKey(c.toString())){
                if (stack.isEmpty() || stack.pop() != pairs.get(c.toString())){
                    valid = false
                }
            }
            else{
                stack.push(c.toString())
            }
        }
    }
    // Output true if valid otherwise false
    if (stack.isEmpty() && valid){
        println("true")
    }else{
        println("false")
    }
    
}
