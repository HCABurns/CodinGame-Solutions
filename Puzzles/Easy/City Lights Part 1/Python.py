h = int(input())
w = int(input())
grid = []
sources = []
for i in range(h):
    row = input()
    grid_row = []
    for j, char in enumerate(row):
        if char == ".":
            grid_row.append(0)
        else:
            value = int(char) if char.isdigit() else ord(char) - ord("A") + 10
            grid_row.append(value)
            sources.append([i, j, value])
    grid.append(grid_row)

# Define new brightness.
for i in range(h):
    for j in range(w):
        for y,x,radius in sources:
            if y==i and j==x:continue
            grid[i][j] += max(0, radius - round(((i-y)**2 + (j-x)**2)**0.5))

# Output new brightness grid.
for row in grid:
    print("".join([str(char) if char < 10 else min(chr(ord("A")+char-10),"Z") for char in row]))
