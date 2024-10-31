# Form grid.
width, height = [int(i) for i in input().split()]
grid = [[j for j in input()] for _ in range(height)]

def search(grid, i , j ,visited):
    """
    Recursive helper function used to find number of neighbors for a given path.

    Parameter:
    grid : 2D array - Array to be searched.  
    i : int - Row index of current search.
    j : int - Column index of current search.
    visited : set - Set of coordinates that has already been searched.

    Returns: int - Return 1 if valid square (not wall) otherwise 0.
    """
    # Return 0 if square is a wall square.
    if grid[i][j] == "#":
        return 0
    
    # Find number of neighbors.
    neighbours = 0
    for y,x in [[1,0],[-1,0],[0,1],[0,-1]]:
        visited.add((i,j))
        if i+y < 0 or i+y >= len(grid) or j+x < 0 or j+x >= len(grid[0]):
            continue
        val = 1 if (i+y,j+x) in visited else search(grid, i+y, j+x , visited)
        neighbours += val
    grid[i][j] = str(neighbours)
    # Return 1 indicating a valid square.
    return 1

# Traverse grid.
for i in range(height):
    for j in range(width):
        if grid[i][j] == "0":
            search(grid, i , j , set())

# Output the ammended graph.
for i in grid:
    print("".join(i))
