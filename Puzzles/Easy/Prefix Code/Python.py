# From hashmap of prefix codes. Also keep track of sizes for searching through encoded string.
char_map = {}
sizes = []
n = int(input())
for i in range(n):
    inputs = input().split()
    b = inputs[0]
    c = int(inputs[1])
    char_map[b] = chr(c)
    if len(b) not in sizes:
        sizes.append(len(b))

# Get encoded string.
s = input()

# Sort sizes in decreasing order for seaching.
sizes.sort(reverse=True)

# Required variables.
out = ""
i = 0

# Go through the encoded string looking for prefixes from max size to min size.
while i < len(s):
    found = False # Flag indicating if a prefix has been found.
    for size in sizes:
        if s[i:i+size] in char_map:
            out+=char_map[s[i:i+size]]
            found=True
            break
    # No prefix was found, return string and index of failure.
    if not found:
        print("DECODE FAIL AT INDEX",i)
        quit()
    # Increment i to the next position past the prefix.
    i+=size

print(out)
