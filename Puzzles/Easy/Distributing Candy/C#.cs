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
        // Read inputs and form array.
        string[] inputs;
        inputs = Console.ReadLine().Split(' ');
        int n = int.Parse(inputs[0]);
        int m = int.Parse(inputs[1]);
        inputs = Console.ReadLine().Split(' ');
        int[] sweets = new int[n];
        for (int i = 0; i < n; i++)
        {
            int x = int.Parse(inputs[i]);
            sweets[i] = x;
        }

        // Sort array.
        Array.Sort(sweets);

        // Find the minimum difference.
        int minDifference = 999;
        for (int i = 0; i < n-m+1; i++) {
            minDifference = Math.Min(sweets[i+m-1] - sweets[i] , minDifference);
        }

        // Print the minimum difference
        Console.WriteLine(minDifference);
    }
}
