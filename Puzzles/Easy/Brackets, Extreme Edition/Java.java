import java.util.*;

class Solution {

    public static void main(String args[]) {
         
        // Define required variables.
        Scanner in = new Scanner(System.in);
        String expression = in.next();
        boolean valid = true;
        Stack<Character> stack = new Stack<>();
        HashMap<Character,Character> pairs = new HashMap<>();
        pairs.put('}', '{');
        pairs.put(']', '[');
        pairs.put(')', '(');

        // Iterate through chars and check char is valid, if opening add it to stack
        // if closing then check if top of stack is a pair.
        for (char c : expression.toCharArray()) {
            if ("(){}[]".contains(String.valueOf(c))){
                if (pairs.containsKey(c)){
                    if (stack.isEmpty() || stack.pop() != pairs.get(c)){
                        valid = false;
                    }
                }
                else{
                    stack.push(c);
                }
            }
        }
        
        // Output true if valid otherwise false
        if (stack.isEmpty() && valid){
            System.out.println("true");
        }else{
            System.out.println("false");
        }
    }
}
