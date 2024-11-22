# Get counts of number of # per column.
width, height = [int(i) for i in input().split()]
counts = [0 for i in range(width)]
for i in range(height):
    line = input()
    for j,char in enumerate(line):
        if char == "#":
            counts[j] += 1

# Print each row after gravity effects.
for i in range(height, 0, -1):
    print("".join(["#" if c >= i else "." for c in counts]))
