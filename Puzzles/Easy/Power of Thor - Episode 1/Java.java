import java.util.*;
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int lightX = in.nextInt(); // the X position of the light of power
        int lightY = in.nextInt(); // the Y position of the light of power
        int x = in.nextInt(); // Thor's starting X position
        int y = in.nextInt(); // Thor's starting Y position

        // game loop
        while (true) {
            int remainingTurns = in.nextInt();

            // Loop and if thor needs to move a direction, append it to output.
            for (int i= 0 ; i < remainingTurns;i++){
                String leftRight = "";
                String upDown = "";

                // If thor is right of the light, move west.
                if (lightX < x){
                    leftRight="W";
                    x-=1;
                }
                // If thor is left of the light, move east.
                else if (lightX > x){
                    leftRight="E";
                    x+=1;
                }
                // If thor is below light, move north.
                if (lightY < y){
                    upDown = "N";
                    y-=1;
                }
                // If thor is above light, move south.
                else if (lightY > y){
                    upDown = "S";
                    y+=1;
                }

                // Output direction to travel.
                System.out.println(upDown + leftRight);
            }
        }
    }
}
