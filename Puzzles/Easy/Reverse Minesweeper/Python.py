# Get dimensions and form grid. Keep track of mines positions to be used.
grid = []
mines = []
directions = [(1,0),(-1,0),(0,-1),(0,1),(-1,-1),(1,1),(1,-1),(-1,1)]
w = int(input())
h = int(input())
for i in range(h):
    grid.append([])
    line = input()
    for j,char in enumerate(line):
        grid[-1].append(char)
        if char == "x":
            mines.append((i,j))
            grid[i][j] = "x"

# Set +1 for all available squares around a bomb.
for i,j in mines:
    for x , y in directions:
        iy = i + y
        jx = j + x
        if 0<=iy<len(grid) and 0<=jx<len(grid[0]):
            if grid[iy][jx] != "x":
                if grid[iy][jx] == ".":
                    grid[iy][jx] = 0
                grid[iy][jx] += 1

# Output the changed grid.
for row in grid:
    print("".join([str(char) if char != "x" else "." for char in row]))
