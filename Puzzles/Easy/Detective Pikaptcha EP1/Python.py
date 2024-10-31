# Form grid.
width, height = [int(i) for i in input().split()]
grid = [[j for j in input()] for _ in range(height)]

# Traverse grid.
for i in range(height):
    for j in range(width):
        if grid[i][j] == "0":
            neighbors = 0
            for y,x in [[1,0],[-1,0],[0,1],[0,-1]]:
                if i+y >= 0 and i+y < len(grid) and j+x >= 0 and j+x < len(grid[0]) and grid[i+y][j+x]!="#":
                    neighbors += 1
            grid[i][j] = str(neighbors)

# Output the ammended grid.
for i in grid:
    print("".join(i))
