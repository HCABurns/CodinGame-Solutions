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
        // Form Grid.
        int n = int.Parse(Console.ReadLine());
        string[] inputs = Console.ReadLine().Split(' ');
        int[] grid = new int[n];
        for (int i = 0; i < n; i++)
        {
            int x = int.Parse(inputs[i]);
            grid[i] = x;
        }

        // Swaps left most 0 with right most 1 until R < L.
        int swaps = 0;
        int l = 0;
        int r = n-1;
        while (l < r){
            while (l < r && grid[l] != 0){
                l += 1;
            }
            while (l < r && grid[r] != 1){
                r -= 1;
            }
            
            if (l < r){
                swaps += 1;
                l += 1;
                r -= 1;
            }
        }
        // Print the number of swaps required.
        Console.WriteLine(swaps);
    }
}
