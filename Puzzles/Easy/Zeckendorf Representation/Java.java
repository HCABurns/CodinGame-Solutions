import java.util.*;
class Solution {

    public static void main(String args[]) {
        // Get value to be checked.
        Scanner in = new Scanner(System.in);
        long n = in.nextLong();

        // Generate Fibonacci sequence
        ArrayList<Long> fib = new ArrayList<>();
        fib.add((long)1);
        fib.add((long)1);
        while (n > fib.get(fib.size()-1) + fib.get(fib.size()-2)){
            fib.add(fib.get(fib.size()-1) + fib.get(fib.size()-2));
        }

        // Find Zeckendorf representation by picking largest available number until sum is n.
        StringBuilder sb = new StringBuilder();
        int i = fib.size()-1;
        while (n > 0){
            if (n - fib.get(i) >= 0){
                n -= fib.get(i);
                sb.append(fib.get(i) + "+");
            }
            i-=1;
        }

        // Output the representation.
        sb.setLength(sb.length() - 1);
        System.out.println(sb.toString());
        in.close();
    }
}
