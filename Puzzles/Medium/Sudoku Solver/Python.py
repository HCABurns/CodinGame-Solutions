# Get input grid.
n = 9
grid = [[int(x) for x in input()] for i in range(n)]

# Find which numbers are missing in the rows and columns.
left_rows = [set([i for i in range(1,n+1) if i not in row]) for row in grid]
left_columns = []
for col in range(n):
    left_columns.append(set(range(1,n+1)))
    for row in range(n):
        if grid[row][col] != 0:
            left_columns[-1].remove(grid[row][col])

# Check if valid - Only need to check the boxes since left_rows/columns deals with vertical and horizontal.
def isValid(i, j, val):
    startRow = i - (i % 3)
    startCol = j - (j % 3)
    for y in range(3):
        for x in range(3):
            if grid[y + startRow][x + startCol] == val:
                return False

    return True

# Search to find complete graph.
def search(i, j):
    ## Goal state.
    if i == n:
        return True
    if j == n:
        return search(i + 1, 0)
    if grid[i][j] != 0:
        return search(i, j + 1)

    # Check each possible value with backtracking.
    for val in left_rows[i] & left_columns[j]:
        if not isValid(i, j, val):
            continue

        left_rows[i].remove(val)
        left_columns[j].remove(val)
        grid[i][j] = val

        if search(i, j + 1):
            return True

        grid[i][j] = 0
        left_rows[i].add(val)
        left_columns[j].add(val)
    return False
                    
# Find valid state and print.
search(0 ,0)
for row in grid:
    print("".join(str(i) for i in row))
