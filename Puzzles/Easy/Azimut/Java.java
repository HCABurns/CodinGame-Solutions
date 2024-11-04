import java.util.*;
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);

        // Get Hashmap of angles and directions.
        HashMap<String,Integer> angles = new HashMap<>();
        angles.put("N",0);
        angles.put("NE",45);
        angles.put("E",90);
        angles.put("SE",135);
        angles.put("S",180);
        angles.put("SW",225);
        angles.put("W",270);
        angles.put("NW",315);

        HashMap<String,Integer> directions = new HashMap<>();
        directions.put("RIGHT", 45);
        directions.put("LEFT", -45);
        directions.put("FORWARD", 0);
        directions.put("BACK", 180);

        // Get starting direction.
        String startDirection = in.next();
        int direction = angles.get(startDirection);

        // Simulate moves.
        int N = in.nextInt();
        for (int i = 0; i < N; i++) {
            String turn = in.next();
            direction = (direction + directions.get(turn) + 360) % 360;
        }

        // Output the angle the person is facing.
        for (Map.Entry<String, Integer> entry : angles.entrySet()) {
            Integer value = entry.getValue();
            if (value == direction){
                System.out.println(entry.getKey());
                break;
            }
        }
        in.close();
    }
}
