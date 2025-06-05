using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Player
{
    static void Main(string[] args)
    {
        string[] inputs = Console.ReadLine().Split(' ');
        int light_x = int.Parse(inputs[0]); // the X position of the light of power
        int light_y = int.Parse(inputs[1]); // the Y position of the light of power
        int x = int.Parse(inputs[2]); // Thor's starting X position
        int y = int.Parse(inputs[3]); // Thor's starting Y position

        // Loop and if thor needs to move a direction, append it to output.
        while (true)
        {
            int remainingTurns = int.Parse(Console.ReadLine()); // The remaining amount of turns Thor can move. Do not remove this line.

            string leftRight = "";
            string upDown = "";

            if (light_x < x){
                leftRight="W";
                x-=1;
            }
            // If thor is left of the light, move east.
            else if (light_x > x){
                leftRight="E";
                x+=1;
            }
            // If thor is below light, move north.
            if (light_y < y){
                upDown = "N";
                y-=1;
            }
            // If thor is above light, move south.
            else if (light_y > y){
                upDown = "S";
                y+=1;
            }

            // A single line providing the move to be made: N NE E SE S SW W or NW
            Console.WriteLine(upDown+leftRight);
        }
    }
}
