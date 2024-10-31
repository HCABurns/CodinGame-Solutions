using System;

class Solution
{
    static void Main(string[] args)
    {
        // Get inputs.
        int L = int.Parse(Console.ReadLine());
        int N = int.Parse(Console.ReadLine());
        string[] inputs = Console.ReadLine().Split(' ');

        // Form array of bot positons.
        int[] arr = new int[N];
        for (int i = 0; i < N; i++)
        {
            int b = int.Parse(inputs[i]);
            arr[i] = b;
        }

        // Max time is for a furthest box from the end to reach the end.
        Array.Sort(arr);
        int minVal = arr[0];
        int maxVal = arr[arr.Length-1];
        Console.WriteLine(Math.Max(L-minVal , maxVal));
    }
}
