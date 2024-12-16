import java.util.*;
class Solution {

    public static void main(String args[]) {
        // Form Grid.
        Scanner in = new Scanner(System.in);
        int W = in.nextInt();
        int H = in.nextInt();
        ArrayList<ArrayList<Integer>> grid = new ArrayList<>();
        for (int i = 0; i < H; i++) {
            grid.add(new ArrayList<Integer>());
            for (int j = 0; j < W; j++) {
                int v = in.nextInt();
                grid.get(grid.size()-1).add(v);
            }
        }

        // Set directions to check.
        int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}, {1, 1}, {-1, -1}, {-1, 1}, {1, -1}};
        String coords = "0 0";

        // Find treasure.
        for(int i = 0; i < H; i++){
            for(int j = 0; j < W; j++){
                // Storing the sum of obstacles.
                int sum_val = 0;

                // If current is an obstacle, move onto next.
                if (grid.get(i).get(j) != 0){continue;}
            
                // Find amount of obstacles around current position.
                for (int k = 0; k < directions.length; k++){
                    int x = directions[k][0];
                    int y = directions[k][1];
                    if (i+y>=0 && i+y<H && x+j >= 0 && x+j < W){
                        sum_val += grid.get(i+y).get(j+x); 
                    }
                }

                //  Determine is current position is the treasure.
                if (sum_val == 3 && ((i == 0 && j == 0 || j == W-1) || (i == H-1 && j == 0 || j == W-1))){
                    coords = String.format("%s %s",j,i);
                }
                else if (sum_val == 5 && ((i == 0 || i == H-1) || (j == 0 || j == W-1))){
                    coords = String.format("%s %s",j,i);
                }
                else if (sum_val == 8){
                    coords = String.format("%s %s",j,i);
                }

                // If treasure has been found, exit and print.
                if (coords != "0 0"){break;}
            }
        }

        // Print location of treasure otherwise 0 0.
        System.out.println(coords);
        in.close();
    }
}
