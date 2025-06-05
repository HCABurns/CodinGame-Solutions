import java.util.*;
import java.io.*;
import java.math.*;
class Solution {

    public static void main(String args[]) {
        // Form Grid.
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] grid = new int[n];
        for (int i = 0; i < n; i++) {
            int x = in.nextInt();
            grid[i] = x;
        }

        // Swaps left most 0 with right most 1 until R < L.
        int swaps = 0;
        int l = 0;
        int r = n-1;
        while (l < r){
            while (l < r && grid[l] != 0){
                l += 1;
            }
            while (l < r && grid[r] != 1){
                r -= 1;
            }
            
            if (l < r){
                swaps += 1;
                l += 1;
                r -= 1;
            }
        }
        // Print the number of swaps required.
        System.out.println(swaps);
        in.close();
    }
}
