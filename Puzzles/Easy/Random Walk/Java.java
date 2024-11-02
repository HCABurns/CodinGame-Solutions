import java.util.*;
class Solution {

    public static void main(String args[]) {
        // Get inputs.
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int m = in.nextInt();

        // Get starting position, starting direction and hashmap of available moves.
        HashMap<Integer,int[]> directions = new HashMap<>();
        directions.put(0, new int[]{-1,0});
        directions.put(1, new int[]{1,0});
        directions.put(2, new int[]{0,-1});
        directions.put(3, new int[]{0,1});
        int moves = 0;
        int d = 0;
        int[] pos = new int[]{0,0};

        // Loop until position returns to [0,0]
        while(true){
            // Increment moves and change direction.
            d = ((a*d)+b)%m;
            moves += 1;

            // Move position.
            pos[0] += directions.get(d%4)[0];
            pos[1] += directions.get(d%4)[1];

            //  Check if returned to start position.
            if (pos[0] == 0 && pos[1]==0){
                break;
            }
        }
        // Output number of moves to return to start.
        System.out.println(moves);
    }
}
