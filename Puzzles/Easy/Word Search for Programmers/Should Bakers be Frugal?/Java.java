import java.util.*;

class Solution {

    public static void main(String args[]) {
        // Get length of dough and size of circle.
        Scanner in = new Scanner(System.in);
        double side = in.nextDouble();
        double diameter = in.nextDouble();

        // Calculate wasteful bakers amount.
        int wasteful = (int) Math.pow(Math.floor(side / diameter),2);
        
        // Calculate frugal bakers amount.
        int frugal = 0;
        double area = side*side;
        while (side > diameter){
            // Calculate amount possible to be cut.
            int amount = (int) Math.floor(side / diameter);
            amount *= amount;
            // Convert wasted into a new dough rectangle.
            frugal += amount;
            area -= amount * (Math.PI*Math.pow((diameter/2),2));
            side = Math.sqrt(area);
        }
        // Output the correct 
        System.out.println((int) (frugal - wasteful));
        in.close();
    }
}
