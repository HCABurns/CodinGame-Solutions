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
        // Initialise require variables.
        int n = int.Parse(Console.ReadLine());
        long total = 1; // Total count of diagonals (Start at 1 as 1 isn't included)
        int idx = 1; // Value currently on.
        int corner_counter = 0; // Counter for how many corners have been visited.
        int distance_between_corner = n-1; // Distance between corners.
        int counter = 0; // Number of items passed since last corner.
        
        // Continue from 1-N counting only corners. (Corners are diagonals)
        while (idx < n*n+1){
            if (counter == distance_between_corner){
                total += idx;
                corner_counter += 1;
                if (corner_counter == 4){
                    distance_between_corner -= 2;
                    corner_counter=0;
                }
                counter = 0;
            }
            // Increment idx and counter.
            idx += 1;
            counter += 1;
        }
        // Output sum.
        Console.WriteLine(total);
    }
}
