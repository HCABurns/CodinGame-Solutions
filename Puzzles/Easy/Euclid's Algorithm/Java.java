import java.util.*;

class Solution {

    public static void main(String args[]) {
        //  Get values to be used to find GCD.
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int a_start = a;
        int b_start = b;

        // Continue until remainder is 0.
        while (b != 0){
            System.out.println(String.format("%d=%d*%d+%d",a,b,a/b,a%b));
            int tmp = a%b;
            a = b;
            b = tmp;
        }

        // Output the GCD of a and b.
        System.out.println(String.format("GCD(%d,%d)=%d",a_start,b_start,a));
        in.close();
    }
}
