import java.util.*;
import java.math.*;

class Solution {

    // Plane Comparator to compare plane based on plates.
    static class PlaneComparator implements Comparator<Plane>{
        public int compare(Plane p1, Plane p2){
         return p1.getPlate().compareTo(p2.getPlate());
        }
    }

    public static void main(String args[]) {

        // Declare required variables.
        Scanner in = new Scanner(System.in);
        HashMap<String, Long> hashmap = new HashMap<String,Long>();
        ArrayList<Plane> arr = new ArrayList<Plane>();
        int N = in.nextInt();

        for (int i = 0; i < N; i++) {
            // Get required information.
            String plate = in.next();
            in.next();// Redundant input.
            long timestamp = in.nextLong();
            
            // If plane passes second checkpoint, calculate speed and store if over 130km/h.
            if (hashmap.containsKey(plate)){
                long time = timestamp - hashmap.get(plate);
                double time_diference = time / 1000.0/60/60;
                double speed = Math.floor(13/time_diference);
                if (speed > 130){
                    arr.add(new Plane(plate, speed));
                }
            }else{
                // If plane has not been found yet then add to hashmap with timestamp.
                hashmap.put(plate, timestamp);
            }
        }

        // Sort array on speed using comparator
        Collections.sort(arr, new PlaneComparator());

        // Output the plate and speed of planes over 130km/h.
        for (Plane plane : arr){
            System.out.println(plane.getPlate() + " " + (int)plane.getSpeed());
        }
    }
}

// Helper class to store plate and speed
class Plane {
    private String plate;
    private double speed;

    public Plane(String plate, double speed) {
        this.plate = plate;
        this.speed = speed;
    }

    public String getPlate() {
        return plate;
    }

    public double getSpeed() {
        return speed;
    }
}
