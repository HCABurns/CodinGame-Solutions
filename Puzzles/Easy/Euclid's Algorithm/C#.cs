using System;
class Solution
{
    static void Main(string[] args)
    {
        //  Get values to be used to find GCD.
        string[] inputs = Console.ReadLine().Split(' ');
        int a = int.Parse(inputs[0]);
        int b = int.Parse(inputs[1]);
        int a_start = a;
        int b_start = b;

        // Continue until remainder is 0.
        while (b!=0){
            Console.WriteLine(a+"="+b+"*"+a/b+"+"+a%b);
            int tmp = a%b;
            a=b;
            b=tmp;
        }

        //  Output the GCD of a and b.
        Console.WriteLine("GCD("+a_start+","+b_start+")="+a);
    }
}
