s = input()

def palindrome(i,j):
    """
    Function to test if string from index i to index j is a palindrome.

    Parameters:
    int i - Index of left most character.
    int j - Index of right most character.

    Return:
    String - String of max palindrome between i and j.
    """
    while i >= 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i+1:j]

strs = []
maxVal = 1
for i in range(len(s)):
    #Get palindromes - Including odd and even lengths.
    odd = palindrome(i,i)
    even = palindrome(i,i+1)
    odd_length = len(odd)
    even_length = len(even)

    #Test if either palindrome is larger than current largest.
    if even_length > maxVal  or maxVal < odd_length:
        strs = []
    maxVal = max(maxVal , odd_length ,even_length)

    #Add palindrome to list if equals max length.
    if maxVal == odd_length:
        strs.append(odd)
    if maxVal==even_length:
        strs.append(even)

#Print all palindromes of max length
for i in strs:
    print(i)
