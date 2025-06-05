using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{
    static void Main(string[] args)
    {
        string[] inputs = Console.ReadLine().Split(' ');
        double side = double.Parse(inputs[0]);
        double diameter = double.Parse(inputs[1]);

        // Calculate wasteful bakers amount.
        int wasteful = (int) Math.Pow(Math.Floor(side / diameter),2);
            
        // Calculate frugal bakers amount.
        int frugal = 0;
        double area = side*side;
        while (side > diameter){
            // Calculate amount possible to be cut.
            int amount = (int) Math.Floor(side / diameter);
            amount *= amount;
            // Convert wasted into a new dough rectangle.
            frugal += amount;
            area -= amount * (Math.PI*Math.Pow((diameter/2),2));
            side = Math.Sqrt(area);
        }
        // Output the correct number.
        Console.WriteLine((int) (frugal - wasteful));
    }
}
