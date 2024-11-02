# From Grid.
grid = [list(input()) for row in range(3)]

winning = False
# Check rows for a winning move
for i in range(3):
    if grid[i].count("O") == 2 and grid[i].count('.') == 1:
        grid[i][grid[i].index('.')] = "O"
        for row in grid:print("".join(row))
        quit()

# Check columns for a winning move
for j in range(3):
    col = [grid[i][j] for i in range(3)]
    if col.count("O") == 2 and col.count('.') == 1:
        grid[col.index('.')][j]  = "O"
        for row in grid:print("".join(row))
        quit()

# Check the main diagonal for a winning move
diag = [grid[i][i] for i in range(3)]
if diag.count("O") == 2 and diag.count('.') == 1:
    idx = diag.index('.')
    grid[idx][idx] = "O"
    for row in grid:print("".join(row))
    quit()

# Check the anti-diagonal for a winning move
opposite_diag = [grid[i][2 - i] for i in range(3)]
if opposite_diag.count("O") == 2 and opposite_diag.count('.') == 1:
    idx = opposite_diag.index('.')
    grid[idx][2 - idx] = "O"
    for row in grid:print("".join(row))
    quit()

print("false")
