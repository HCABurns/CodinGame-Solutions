import java.util.*;
class Solution {
    public static void main(String args[]) {
        // Get grid dimensions and starting position.
        Scanner in = new Scanner(System.in);
        int w = in.nextInt();
        int h = in.nextInt();
        int startRow = in.nextInt();
        int startCol = in.nextInt();

        // Set directions hashmap and set minimum path size and idx.
        //HashMap<String,ArrayList<Integer>> directions = new HashMap<>();
        HashMap<Character,Integer[]> directions = new HashMap<>();
        directions.put('<', new Integer[]{0,-1});
        directions.put('>', new Integer[]{0,1});
        directions.put('^', new Integer[]{-1,0});
        directions.put('v', new Integer[]{1,0});
        int min_path = w*h+1;
        int min_path_idx = -1;

        // Get number of grid to check.
        int n = in.nextInt();
        if (in.hasNextLine()) {
            in.nextLine();
        }

        // Check all grids for valid path and select idx of shortest.
        for (int idx = 0; idx < n; idx++) {
            // From grid.
            ArrayList<String> grid = new ArrayList<>();
            for (int j = 0; j < h; j++) {
                String mapRow = in.nextLine();
                grid.add(mapRow);
            }

            // Traverse grid and find path length - If loops then quit loop.
            int i = startRow;
            int j = startCol;
            int path = 0;
            ArrayList<String> visited = new ArrayList<>();
            while (directions.containsKey(grid.get(i).charAt(j)) && !visited.contains(i + " " + j)){
                visited.add(i + " " + j);
                int iy = directions.get(grid.get(i).charAt(j))[0];
                int jx = directions.get(grid.get(i).charAt(j))[1];
                // Ensure next move is valid
                if (i+iy<0 || i+iy>=h || j+jx<0 || j+jx>=w){
                    break;
                }
                i += iy;
                j += jx;
                path += 1;
            }

            // Change minimum if required.
            if (grid.get(i).charAt(j) == 'T'){
                min_path = Math.min(min_path , path);
            }
            if (min_path == path){
                min_path_idx = idx;
            }
        }
        
        // Output the id of the map with the shortest path or TRAP if no route.
        if (min_path_idx != -1){
            System.out.println(min_path_idx);
        }else{
            System.out.println("TRAP");
        }
        in.close();
    }
}
