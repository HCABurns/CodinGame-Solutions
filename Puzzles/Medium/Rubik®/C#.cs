using System;
class Solution
{
    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());

        if (n == 1){
            Console.WriteLine("1");
        }else{
            Console.WriteLine((6*(n-2)*(n-2) + 12 * (n-2) + 8));
        }
    }
}
