import java.util.*;

class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);

        // Get size of shape.
        int a = in.nextInt();
        int b = in.nextInt();
        if (in.hasNextLine()) {
            in.nextLine();
        }

        // Find shape coordinates relative to the first * characters.
        int[] start = {-a-1,-a-1};
        ArrayList<int[]> shape = new ArrayList<>();
        for (int i = 0; i < a; i++) {
            String objectLine = in.nextLine();
            for (int j = 0 ; j < b;j++){
                if (objectLine.charAt(j)=='*'){
                    if (start[0] == -a-1 & start[1] == -a-1){
                        start[0] = i;
                        start[1] = j;
                        shape.add(new int[]{0,0});
                    }
                    else{
                        shape.add(new int[]{i-start[0],j-start[1]});
                    }
                }
            }
        }

        // Form Grid.
        int c = in.nextInt();
        int d = in.nextInt();
        ArrayList<String> grid = new ArrayList<>();
        if (in.hasNextLine()) {
            in.nextLine();
        }
        for (int i = 0; i < c; i++) {
            String gridLine = in.nextLine();
            grid.add(gridLine);
        }

        // Find positions that the shape can fit and store in array.
        ArrayList<int[]> positions = new ArrayList<>();
        for (int i = 0; i < grid.size(); i++){
            for (int j = 0; j < grid.get(0).length();j++){
                if (grid.get(i).charAt(j) == '.'){
                    boolean shape_fits = true;
                    for (int[] pos : shape){
                        int ix = pos[0] + i;
                        int jy = pos[1] + j;
                        if (0>ix || ix>=c || 0>jy || jy>=d || grid.get(ix).charAt(jy) == '#'){
                            shape_fits = false;
                            break;
                        }
                    }
                    if (shape_fits){
                        positions.add(new int[]{i,j});
                    }
                }
            }
        }
        
        // Output number of positions and if only one, place the shape in and print.
        System.out.println(positions.size());
        if (positions.size() == 1){
            for (int[] pos : shape){
                int x = pos[0];
                int y = pos[1];
                int i = positions.get(0)[0];
                int j = positions.get(0)[1];
                int ix = i+x;
                int jy = j+y;
                StringBuilder sb = new StringBuilder(grid.get(ix));
                sb.setCharAt(jy,'*');
                grid.set(ix, sb.toString());
            }
            for (String row : grid){
                System.out.println(row);
            }
        }
    }
}
