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
        int n = int.Parse(Console.ReadLine()); // the number of temperatures to analyse
        string[] inputs = Console.ReadLine().Split(' ');

        // Find temp closest to 0 and prioritise positive over negatives if equal.
        int temp = -999999;
        for (int i = 0; i < n; i++){
            int t = int.Parse(inputs[i]);// a temperature expressed as an integer ranging from -273 to 5526
            if (Math.Abs(t) < Math.Abs(temp)){
                temp = t;
            }else if (Math.Abs(t) == Math.Abs(temp)){
                temp = Math.Max(t,temp);
            }
        }
        // Print correct output.
        if (temp != -999999){
            Console.WriteLine(temp);
        }else{
            Console.WriteLine("0");
        }
    }
}
