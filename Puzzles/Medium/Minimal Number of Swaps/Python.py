# Form the grid.
grid = []
n = int(input())
for i in input().split():
    grid += [int(i)]

# Swaps left most 0 with right most 1 until R < L.
swaps, l, r = 0, 0, n-1
while l < r:
    while l < r and grid[l] != 0:
        l += 1
    while l < r and grid[r] != 1:
        r -= 1
    
    if l < r:
        swaps += 1
        l += 1
        r -= 1

# Print the number of swaps required.
print(swaps)
