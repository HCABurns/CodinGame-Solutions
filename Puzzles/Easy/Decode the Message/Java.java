import java.util.*;
class Solution {
    public static void main(String args[]) {
        // Get inputs.
        Scanner in = new Scanner(System.in);
        long P = in.nextLong();
        if (in.hasNextLine()) {
            in.nextLine();
        }
        String C = in.nextLine();

        // Set output string builder.
        StringBuilder out = new StringBuilder();
        // Ensure not 0 input.
        if (P == 0){
            System.out.println(C.charAt(0));
        }else{
            // Set base.
            int base = C.length();
            // Continue until converted from base 10 to base len(c).
            while (P > 0){
                if (out.length() != 0){
                    P -= 1;
                }
                // Regular base conversion.
                int rem = Math.floorMod(P, base);
                out.append(String.valueOf(C.charAt(rem)));
                P = Math.floorDiv(P , base);
            }
        }
        System.out.println(out.toString());
    }
}
