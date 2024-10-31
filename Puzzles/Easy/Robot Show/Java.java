import java.util.*;

class Solution {

    public static void main(String args[]) {
        // Get inputs.
        Scanner in = new Scanner(System.in);
        int L = in.nextInt();
        int N = in.nextInt();
        
        // Create array of bots positions.
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            int b = in.nextInt();
            arr.add(b);
        }

        // Max time is for a furthest box from the end to reach the end.
        int maxVal = Collections.max(arr);
        int minVal = Collections.min(arr);
        System.out.println(Math.max(L-minVal, maxVal));
        in.close();
    }
}
