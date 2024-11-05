# Get input string.
n = int(input())
s = input()

#Find Longest palindrome starting from the back.
longest = 1
for j in range(len(s)-1,-1,-1):
    if s[n-1-j:n] == s[n-1-j:n][::-1] and j>longest:
        longest = j+1

# Print number of chars that need to be added from the front to make a palindrome.
print(len(s) - longest)
