size = int(input())
angle = int(input())
grid = []
for i in range(size):
    line = input().replace(" ","")
    grid += [line]

corner = 0
while angle > 0:
    corner = (corner+1)%4
    angle -= 90

new_grid = [[] for j in range(size*2-1)]
if corner == 1:
    for i in range(size):
        for j in range(size-1, -1, -1):
            new_grid[i+(size-1-j)].append(grid[i][j])
elif corner == 0:
    for i in range(size):
        for j in range(size):
            new_grid[i+j].append(grid[j][i])
elif corner == 2:
    for i in range(size-1, -1, -1):
        for j in range(size-1, -1, -1):
            new_grid[size-1-j + size-1-i].append(grid[j][i])

for row in new_grid:
    print(" "*(size-len(row)) +  " ".join(row) + " "*(size-len(row)))
