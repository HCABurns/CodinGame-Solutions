import java.util.*;
import java.util.stream.*;

class Solution {

    public static void main(String args[]) {
        // Get number of mountains and form a array of the heights.
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(); 
        int[] heights = new int[n];
        for (int i = 0; i < n; i++) {
            int height = in.nextInt();
            heights[i] = height;
        }

        // Get width and height of the grid.
        int width = IntStream.of(heights).sum()*2;
        int height = Arrays.stream(heights).max().getAsInt();
        
        // Form Grid
        ArrayList<char[]> grid = new ArrayList<>();
        for (int i = 0; i < height;i++){
            char[] arr = new char[width];
            for (int j = 0; j<width;j++){
                arr[j] = ' ';
            }
            grid.add(arr);
        }

        // Place mountains in the correct places in the grid.
        int i = height-1;
        int j = 0;
        for (int mountain_height: heights){
            for (int _k = 0; _k < mountain_height ; _k++){
                grid.get(i)[j] = '/';
                i-=1;
                j+=1;
            }
            i+=1;
            for (int _k = 0; _k < mountain_height ; _k++){
                grid.get(i)[j] = '\\';
                i+=1;
                j+=1;
            }
            i-=1;
        }

        // Print grid with rstrip to remove trailing spaces.
        for (char[] arr : grid){
            System.out.println(String.valueOf(arr).stripTrailing());
        }
        in.close();
    }
}
