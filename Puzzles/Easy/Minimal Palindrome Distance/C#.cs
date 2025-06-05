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
        int n = int.Parse(Console.ReadLine());
        string s = Console.ReadLine();

        // Find Longest palindrome starting from the back.
        int longest = 1;
        for (int j = 0; j < n; ++j) {
            bool isPalindrome = true;
            for (int k = 0; k <= j; ++k) {
                if (s[n - j - 1 + k] != s[n - 1 - k]) {
                    isPalindrome = false;
                    break;
                }
            }
            if (isPalindrome && j + 1 > longest) {
                longest = j + 1;
            }
        }
        // Print number of chars to be added to the end.
        Console.WriteLine(n-longest);
    }
}
