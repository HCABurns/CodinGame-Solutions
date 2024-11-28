# Form grid.
grid = []
height = int(input())
for i in range(height):
    grid+=[[*map(int,[c for c in input()])]]

# Get prizes.
prizes = [int(input()) for i in range(height+1)]

# Cache for efficiency.
cache = {}
def search(i , j, multiplier):
    """
    Function for DFS to find max path.

    Parameters:
    i : int - Row in the grid.
    j : int - Column in the row.
    multiplier : int - Multiplier achieved from traversing down the board.

    Return : int - Integer of the max score achievable.
    """
    # Goal case, return multiplier * prize amount.
    if i == height:
        return multiplier * prizes[j]
    
    # If in cache, return result.
    if (i,j,multiplier) in cache:
        return cache[(i,j,multiplier)]

    # Get max of left and right.
    max_score = max(search(i+1, j, multiplier+int(grid[i][j])) , search(i+1, j+1,multiplier+int(grid[i][j])))
    
    # Cache score and return.
    cache[(i,j,multiplier)] = max_score
    return max_score

# Output the max score.
print(search(0 , 0, 0))
