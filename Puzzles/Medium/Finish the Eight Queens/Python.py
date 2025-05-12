def valid(start_i, start_j , grid):
    """
    Function to check if moves are valid and set invalid squares to X if flag is set.
    """
    for di, dj in moves:
        i = start_i
        j = start_j
        while i + di >= 0 and i + di < 8 and j + dj >= 0 and j + dj < 8:
            i += di
            j += dj
            if grid[i][j] == "Q":
                return False
    return True

# Define directions a queen can move.
moves = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,1],[1,-1],[-1,1]]

# Form a grid and store queen positions.
queens = set()
grid = []
for i in range(8):
    row = input()
    grid.append([])
    for j,char in enumerate(row):
        grid[-1].append(char)
        if char == "Q":
            queens.add((i,j))

# Set squares a queen can move to, to be invalid.
for i, j in queens:
    valid(i,j, grid)

# Find the open spaces for the new queens.
open_spaces = set()
for i,row in enumerate(grid):
    for j, char in enumerate(row):
        if char == ".":
            open_spaces.add((i,j))

# Complete a search with backtracking to find the valid positions.
import copy
def search(open_spaces, queens, gr):
    # Goal Case - Print the grid.
    if queens == 8:
        for row in gr:
            print("".join(row))
        return True

    for space in open_spaces:
        y, x = space

        if valid(y, x, gr):
            new_grid = copy.deepcopy(gr)
            new_open_spaces = copy.deepcopy(open_spaces)
            new_open_spaces.remove(space)

            valid(y, x, new_grid)
            new_grid[y][x] = "Q"
            if search(new_open_spaces, queens + 1, new_grid):
                return True
    return False
search(open_spaces, len(queens), grid)
