import java.util.*;

class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        // game loop
        while (true) {
            // Define variables required
            int j = 0;
            int maxVal = 0;

            // Find the index of the max height and store in j.
            for (int i = 0; i < 8; i++) {
                int mountainH = in.nextInt(); // represents the height of one mountain.
                maxVal = Math.max(maxVal,mountainH);
                if (maxVal == mountainH){
                    j = i; 
                }
            }
            // Output the index of the mountain to fire on.
            System.out.println(j); 
        }
    }
}
