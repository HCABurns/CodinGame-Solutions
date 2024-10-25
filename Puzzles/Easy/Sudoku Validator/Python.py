# Form Grid - 2D array.
grid = []
valid = {i:1 for i in range(1,10)}
for i in range(9):
    grid.append([int(j) for j in input().split()])

def is_valid_sudoku(grid):
    """
    Helper function to check if a 9x9 grid is a valid suduko.

    Parameters:
    grid : 2D Array - Grid of numbers to be checked.

    Return: boolean - True if valid otherwise false
    """
    # Check rows are valid
    for col in grid:
        hashmap={i:col.count(i) for i in range(1,10)}
        if hashmap != valid:
            return False

    #Check Columns are valid
    for col in range(9):
        hashmap = {i:0 for i in range(1,10)}
        for row in range(9):
            hashmap[grid[row][col]] += 1
        if hashmap != valid:
            return False

    #Check sub grids are valid
    for sub_grid_row in range(0,9,3):
        for sub_grid_col in range(0,9,3):
            hashmap = {i:0 for i in range(1,10)}
            for i in range(3):
                for j in range(3):
                    hashmap[grid[sub_grid_row+i][sub_grid_col+j]] += 1
            if hashmap != valid:
                return False
    return True

# Return true if valid otherwise false.
print("true" if is_valid_sudoku(grid) else "false")
    
