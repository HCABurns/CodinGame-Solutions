# Get width, height and encoding values.
w = int(input())
h = int(input())
t = [int(i) for i in input().split()]

# Form Grid.
grid = [[" "]*w for i in [1]*h]

# Declare required variables.
draw = 1
i = 0
j=0

# Use wrapping idx and swapping flag with XOR to place * in correct places.
while i < h*w:
    if draw:
        for _ in range(t[j]):
            grid[i//w][i%w] = "*"
            i+=1
    else:
        i+=int(t[j])
    j+=1
    draw ^= 1

# Output the new grid.
for row in grid:
    print("|"+"".join(row)+"|")
