// Get inputs.
const n: number = parseInt(readline());
const s: string = readline();

// Find Longest palindrome starting from the back.
var longest = 1;
for (var j = 0; j < n; ++j) {
    var isPalindrome = true;
    for (var k = 0; k <= j; ++k) {
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
console.log(n-longest);

