using System;

class Solution
{
    static void Main(string[] args)
    {
        // Get size of array and create array of size N.
        int N = int.Parse(Console.ReadLine());
        int[] arr = new int[N];
        // Fill array with horse strengths.
        for (int i = 0; i < N; i++)
        {
            int pi = int.Parse(Console.ReadLine());
            arr[i] = pi;
        }

        // Sort array.
        Array.Sort(arr);

        // Define difference.
        int difference = 999999999;

        // Check adjacent horses power and store minimum difference.
        for (int i = 0; i < N-1; i++)
        {
            int val = arr[i+1] - arr[i];
            if (val < difference){
                difference = val;
            }
        }
        // Output minimum difference
        Console.WriteLine(difference);
    }
}
