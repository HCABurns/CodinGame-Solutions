# Get inputs
n = int(input())
g = int(input())
grids = []
max_infected = 0
max_index = 0
max_grid = []

# Get grids
for grid_index in range(g):
    grid = []
    infected = 0
    for j in range(n):
        row = input()
        grid.append(list(row))
        infected += row.count("C")

    # Spread disease until can't be spread anymore.
    spreading = True
    while spreading:
        spreading = False

        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if col == "C":
                    for dy,dx in [[1,1],[-1,-1],[-1,1],[1,-1]]:
                        ny, nx = i+dy, j+dx
                        if 0<=ny<n and 0<=nx<len(row) and grid[ny][nx] == ".":
                            spreading = True
                            grid[ny][nx] = "C"
                            infected += 1
    
    # Store maximum infected grid. 
    if infected > max_infected:
        max_infected = infected
        max_index = grid_index
        max_grid = grid

# Print result.  
print(max_index)
for row in max_grid:
    print("".join(row))
