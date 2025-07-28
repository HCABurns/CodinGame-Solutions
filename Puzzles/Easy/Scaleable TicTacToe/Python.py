import sys

# Get values and form grid.
n, g = [int(i) for i in input().split()]
grid = [list(input()) for i in range(n)]

# Print the correct values.
def output(out, pos, char):
    for y,x in pos:
        grid[y][x] = char
    finished = True
    for row in grid:
        if " " in row: finished = False
        print("".join(row))
    if len(pos) > 1:
        print(f"The winner is {out[0]}.")
    else:
        if finished:
            print("The game ended in a draw!")
        else:
            print("The game isn't over yet!")
    sys.exit()


required = [["X" for i in range(g)], ["O" for i in range(g)]]

# Check Vertical - Convert to queue and shift?
for row in range(0,n-g+1):
    for j in range(n):
        out = []
        pos = []
        for i in range(g):
            i+=row
            out += [grid[i][j]]
            pos += [[i,j]]
        if out in required:output(out, pos, "|")

# Check Horizontal
for row in range(n):
    for j in range(0,n-g+1):
        out = []
        pos = []
        for jj in range(g):
            out += [grid[row][jj+j]]
            pos += [[row,jj+j]]
        if out in required:output(out, pos, "-")

# Check Dia right
for row in range(0,n-g+1):
    for j in range(0,n-g+1):
        out = []
        pos = []
        for i in range(g):
            out += [grid[row+i][j+i]]
            pos += [[row+i,i+j]]
        if out in required:output(out, pos, "\\")

# Check Dia left
for row in range(0,n-g+1):
    for j in range(n-1, g-2, -1):
        out = []
        pos = []
        for i in range(g):
            out += [grid[row+i][j-i]]
            pos += [[row+i,j-i]]
        if out in required:output(out, pos, "/")

output(grid, [], " ")
