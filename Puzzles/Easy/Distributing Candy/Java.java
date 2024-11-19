import java.util.*;
class Solution {
    public static void main(String args[]) {
        // Get sweets and create array.
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        ArrayList<Integer> sweets = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            sweets.add(in.nextInt());
        }

        // Sort the list.
        Collections.sort(sweets);

        int minDifference = 999;
        for (int i = 0; i < n-m+1; i++) {
            minDifference = Math.min(sweets.get(i+m-1) - sweets.get(i) , minDifference);
        }

        // Output minimum difference between m sweet bags.
        System.out.println(minDifference);
        in.close();
    }
}
