# Get input grid.
grid = [[int(x) for x in input()] for i in range(4)]

left_rows = [set([i for i in range(1,5) if i not in row]) for row in grid]
left_columns = []
for col in range(4):
    left_columns.append(set(range(1,5)))
    for row in range(4):
        if grid[row][col] != 0:
            left_columns[-1].remove(grid[row][col])

# Check if valid.
def isValid():
    for i in range(0,4,2):
        for j in range(0,4,2):
            s = set([grid[i][j], grid[i][j+1], grid[i+1][j], grid[i+1][j+1]])
            if s != set(range(1,5)):
                return False
    return True

# Search to find complete graph.
def search():
    if isValid():
        for row in grid:
            print("".join(str(i) for i in row))
        quit()

    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                for val in [i for i in left_rows[i] if i in left_columns[j]]:
                    left_rows[i].remove(val)
                    left_columns[j].remove(val)
                    before = grid[i][j]
                    grid[i][j] = val
                    search()
                    grid[i][j] = before
                    left_rows[i].add(val)
                    left_columns[j].add(val)

search()
