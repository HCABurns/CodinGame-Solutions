#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    int n;
    scanf("%d", &n); fgetc(stdin);
    char s[n + 1];
    scanf("%[^\n]", s);

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
    printf("%d\n",(n-longest));
    return 0;
}
