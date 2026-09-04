# Get input size and grid.
w, h = [int(i) for i in input().split()]
k = int(input())
grid = [list(input()) for i in range(h)]

# Create set for the obstacles.
obstacles = set(str(i) for i in range(1,10))

# Block solar panels that fall in shadow of a obstacle.
for i in range(h):
    for j in range(w):
        if grid[i][j] in obstacles:
            for ni in range(1, 1+k*int(grid[i][j])):
                if 0<=i-ni:
                    grid[i-ni][j] = "."

# Count total number of solar panels left.
total = 0
for row in grid:
    for char in row:
        if char == "P":
            total+=100
print(total)

