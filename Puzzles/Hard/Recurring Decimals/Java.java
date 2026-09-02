import java.util.*;
class Solution {

    public static void main(String args[]) {
        // Get the value and set the remainder.
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int remainder = 1;

        // Array for storing ints, hashmap for storing index and index.
        StringBuilder res = new StringBuilder();
        HashMap<Integer, Integer> values = new HashMap<>();
        int idx = 0;

        // Complete the divison until terminates or repeat found.
        while (remainder != 0){
            // Check for repeated remainder.
            if (values.containsKey(remainder)){
                res.insert((int)values.get(remainder), '(');
                res.append(')');
                break;
            }
            values.put(remainder, idx);

            // Complete the division.
            remainder *= 10;
            int value = remainder / n;
            res.append(String.valueOf(value));
            remainder = remainder % n;

            // Increment index variable.
            idx += 1;
        }
        // Print the value.
        System.out.println("0."+res.toString());
        in.close();
    }
}
