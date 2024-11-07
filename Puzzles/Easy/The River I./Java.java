import java.util.*;
class Solution {

    public static void main(String args[]) {
        // Get inputs.
        Scanner in = new Scanner(System.in);
        long r1 = in.nextLong();
        long r2 = in.nextLong();

        // Ensure r1 is the smaller value.
        if (r1 > r2){
            long tmp = r1;
            r1 = r2;
            r2 = tmp;
        }

        // Continue until equal values.
        while (r1 != r2){

            // Compute algorithm until r_1 is larger or equal to r_2.
            String str;
            while (r1 < r2){
                str = String.valueOf(r1);
                for (int i = 0; i < str.length();i++){
                    r1 += Integer.parseInt(str.charAt(i)+"");
                }
            }

            // If r_2 is smaller than r_1, compute the next value.
            if (r2 < r1){
                str = String.valueOf(r2);
                for (int i = 0; i < str.length();i++){
                    r2 += Integer.parseInt(str.charAt(i)+"");
                } 
            }
        }
        // Output the meeting point.
        System.out.println(r1);
        in.close();
    }
}
