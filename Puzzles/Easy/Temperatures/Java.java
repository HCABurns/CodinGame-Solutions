import java.util.*;

class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        // Declare closest variable.
        int closest = 0;

        // If size if 0 don't set closest so the output will be 0.
        if (n!=0){
            closest = 9999;
        }

        // Go thorugh each value and compare with closest. If it is smaller than closest, set new closest.
        // If equal with closest then select the positive value if available.
        for (int i = 0; i < n; i++) {
            int t = in.nextInt(); // a temperature expressed as an integer ranging from -273 to 5526
            if (Math.abs(t) <= Math.abs(closest)){
                if (Math.abs(t) == Math.abs(closest) && !(t<0 && closest<0)){
                    closest = Math.abs(closest);
                }else{
                    closest = t;
                }
            }
        }
        // Output the closest value to 0.
        System.out.println(closest);
    }
}
