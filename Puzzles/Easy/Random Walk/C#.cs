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
        // Get starting position, starting direction and hashmap of available moves.
        int a = int.Parse(Console.ReadLine());
        int b = int.Parse(Console.ReadLine());
        int m = int.Parse(Console.ReadLine());
        Dictionary<int,int[]> directions = new Dictionary<int,int[]>();
        directions.Add(0, new int[]{-1,0});
        directions.Add(1, new int[]{1,0});
        directions.Add(2, new int[]{0,-1});
        directions.Add(3, new int[]{0,1});
        int moves = 0;
        int d = 0;
        int[] pos = new int[]{0,0};

        // Loop until position returns to [0,0]
        while(true){
            // Increment moves and change direction.
            d = ((a*d)+b)%m;
            moves += 1;

            // Move position.
            pos[0] += directions[d%4][0];
            pos[1] += directions[d%4][1];

            //  Check if returned to start position.
            if (pos[0] == 0 && pos[1]==0){
                break;
            }
        }

         // Output number of moves to return to start.
        Console.WriteLine(moves);
    }
}
