import java.util.*;
class Solution {
    public static void main(String args[]) {
        // Get inputs.
        Scanner in = new Scanner(System.in);
        int HEIGHT = in.nextInt();
        int WIDTH = in.nextInt();
        int THRESHOLD = in.nextInt();

        // Create visited set.
        Set<String> visited = new HashSet<>();

        // Check each position and ensure value is below threshold and the cell is reachable from other valid cells.
        for (int i = 0; i<HEIGHT;i++){
            for (int j = 0; j < WIDTH; j++){
                if (i==0 || visited.contains(String.valueOf(i-1) + " " + String.valueOf(j)) ||
                    visited.contains(String.valueOf(i) + " " + String.valueOf(j-1))){
                    int sum_val = ("" + i + j).chars().map(Character::getNumericValue).sum();
                    if (sum_val <= THRESHOLD){
                        visited.add(String.valueOf(i) + " " + String.valueOf(j));
                    }
                }
            }
        }

        // Print number of valid cells.
        System.out.println(visited.size());
        in.close();
    }
}
