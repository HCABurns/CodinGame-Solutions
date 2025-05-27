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
        // Get the value and set the remainder.
        int n = int.Parse(Console.ReadLine());
        int remainder = 1;

        // Array for storing ints, hashmap for storing index and index.
        string res = "";
        int idx = 0;
        Dictionary<int, int> values = new Dictionary<int, int>();
        
        // Complete the divison until terminates or repeat found.
        while (remainder != 0){
            // Check for repeated remainder.
            if (values.ContainsKey(remainder)){
                string left = res[0..values[remainder]];
                string right = res[values[remainder]..res.Length];
                res = left + "(" + right + ")";
                break;
            }
            values[remainder] = idx;

            // Complete the division.
            remainder *= 10;
            int val = remainder / n;
            res += val.ToString();
            remainder = remainder % n;
            
            // Increment index variable.
            idx += 1;
        }
        // Print the value.
        Console.WriteLine("0."+res);
    }
}
