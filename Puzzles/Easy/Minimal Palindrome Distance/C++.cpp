#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int n;
    cin >> n; cin.ignore();
    string s;
    getline(cin, s);

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
    cout << n - longest << endl;
}
