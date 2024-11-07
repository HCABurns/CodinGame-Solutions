# Set grid, get starting position, set controlling variable.
grid = []
pos = (-1,-1)
color = input()[0]
for i in range(8):
    line = input()
    grid.append(line)
    if "Q" in line:
        pos = (i,line.index("Q"))
controlling = 0

# Testing vertical
for vertical_range in [range(pos[0]-1,-1,-1), range(pos[0]+1,len(grid))]:
    for i in vertical_range:
        if grid[i][pos[1]] == ".":
            controlling += 1
        else:
            if grid[i][pos[1]] != color:
                controlling+=1
            break

# Testing Horizontal
for horizontal_range in [range(pos[1]-1,-1,-1), range(pos[1]+1,len(grid[0]))]:
    for j in horizontal_range:
        if grid[pos[0]][j] == ".":
            controlling += 1
        else:
            if grid[pos[0]][j] != color:
                controlling+=1
            break

# Top Diagonals
for diagonal_range in [[range(1,pos[0]+1),1], [range(1,pos[0]+1),-1]]:
    diagonal_range, sign = diagonal_range
    for diag in diagonal_range:
        if pos[1]+diag*sign < 0 or pos[1]+diag*sign >= len(grid[0]) or pos[0]-diag < 0 or pos[0]-diag >= len(grid):

            break
        if grid[pos[0]-diag][pos[1]+diag*sign] == ".":
            controlling += 1
        else:
            if grid[pos[0]-diag][pos[1]+diag*sign] != color:
                controlling+=1
            break

# Bottom Diagonals
for diagonal_range in [[range(1,len(grid)-pos[0]),1], [range(1,len(grid)-pos[0]),-1]]:
    diagonal_range, sign = diagonal_range
    for diag in diagonal_range:
        if pos[1]+diag*sign < 0 or pos[1]+diag*sign >= len(grid[0]) or pos[0]+diag < 0 or pos[0]+diag >= len(grid):
            break
        if grid[pos[0]+diag][pos[1]+diag*sign] == ".":
            controlling += 1
        else:
            if grid[pos[0]+diag][pos[1]+diag*sign] != color:
                controlling+=1
            break

# Output number of squares the queen controls.
print(controlling)
