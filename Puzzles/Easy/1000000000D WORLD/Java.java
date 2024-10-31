import java.util.*;
import java.util.stream.*;

class Solution {

    public static void main(String args[]) {
        // Convert input into long array.
        Scanner in = new Scanner(System.in);
        String a = in.nextLine();
        String b = in.nextLine();
        long[] arr1 = Stream.of(a.split(" ")).mapToLong(Long::parseLong).toArray();
        long[] arr2 = Stream.of(b.split(" ")).mapToLong(Long::parseLong).toArray();

        // Set up total and two pointers.
        int i = 0;
        int j = 0;
        long total = 0;

        // Dot Product Loop.
        while (i<arr1.length && j<arr2.length){
            
            // Get value and amount of the next values.
            long a_val = arr1[i+1];
            long a_count = arr1[i];
            
            long b_val = arr2[j+1];
            long b_count = arr2[j];

            // Increment the total by the dot product of a and b.
            // Multiply the dot product by the minumum count of a and b.
            // E.g. a = [4, 4, 4] b = [5, 5, 5] A•B = 4*5+4*5+4*5 ≡ (4*5)*3
            long min_count = Math.min(a_count,b_count);
            total += (a_val * b_val) * min_count;

            // Adjust counts.
            arr1[i] -= min_count;
            arr2[j] -= min_count;

            // Move onto next value pair if required.
            if (arr1[i] == 0){
                i+=2;
            }
            if (arr2[j] == 0){
                j+=2;
            }

        }
        // Output the total of the  dot product.
        System.out.println(total);
        in.close();
    }
}
