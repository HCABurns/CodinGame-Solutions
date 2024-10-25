# Set grid to 2D array.
grid = []
n = int(input())
for i in range(n):
    row = input()
    grid.append([j for j in row])


def search(grid, i,j):
    """
    This is a helper function to recursively search the grid to find coast lengths.

    Parameters:
    Grid : 2D Array - Grid to be searched
    i : int - Index of row of grid.
    j : int - Index of column of grid.

    Return: None
    """
    # Check the item to check is valid.
    if i < 0 or i > len(grid) -1 or j < 0 or j > len(grid[0]) - 1:
        return 0
    
    # If water has been found - Add 1 to coast length if it hasn't been added already.
    if grid[i][j] == "~":
        if (i,j) not in checked:
            islands[-1] += 1
        checked.add((i,j))
    
    # If part of island found then recursively search.
    # Set current position to ? to stop endless loop.
    elif grid[i][j] == "#":
        grid[i][j] = "?"
        #Up
        search(grid, i-1 ,j)
        #Down
        search(grid, i+1 ,j)
        #Left
        search(grid, i ,j-1)
        #Right
        search(grid, i ,j+1)
    
# Check for islands and find the coast length.
islands = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            islands.append(0)
            checked = set()
            search(grid, i,j)

# Output the island index and the coast value for the island with the longest coast.
max_val = 0
max_i = 0
for i,val in enumerate(islands):
    if val > max_val:
        max_val = val
        max_i = i
print(max_i + 1 , max_val)
