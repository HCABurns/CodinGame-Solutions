# Build map.
n = int(input())
grid = [list(input()) for i in range(n)]
max_size = len(max(grid, key = len)) + 2
grid = [i+[" "]*(max_size-len(i)+2) for i in grid+[[]]+[[]]]
illegalChars = set([" ","-","`"])

# Build shadows.
placed = set()
for i, row in enumerate(grid[:-2]):
    for j, char in enumerate(row[:-2]):
        if char != " " and (i,j) not in placed:
            s1 = (i+1, j+1)
            s2 = (i+2, j+2)
            if grid[s1[0]][s1[1]] == " ":
                grid[s1[0]][s1[1]] = "-"
                placed.add(s1)
                if grid[s2[0]][s2[1]] == " ":
                    grid[s2[0]][s2[1]] = "`"
                    placed.add(s2)

# Print image with shadows.
for row in grid:
    print("".join(row).rstrip())
