# Get input and split the input on 0s.
b = input()
s = b.split("0")

# Value of the largest when changing and 0 to 1.
largest = 0

# Go through and compare adjacent pairs testing if their sizes added make a new largest.
for i in range(0,len(s)-1):
    if len(s[i]) + len(s[i+1]) + 1 > largest:
        largest = len(s[i]) + len(s[i+1]) + 1

# Return the new largest sequence of 1s length.
print(largest)
