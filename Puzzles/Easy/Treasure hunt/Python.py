# Copy required as python passes by reference.
import copy
# Form grid and find starting position.
h, w = [int(i) for i in input().split()]
grid = []
start = [-1,-1]
for i in range(h):
    row = input()
    grid.append(row)
    for j in range(w):
        if grid[i][j] == "X" and start==[-1,-1]:
            start = [i,j]

def search(grid, i , j, current_gold , visited):
    # End case.
    if  i < 0 or i >= len(grid) or j < 0 or j>=len(grid[0]) or grid[i][j]=="#":
        return 0

    # Goal case.
    if grid[i][j].isnumeric():
        current_gold += int(grid[i][j])
        global max_gold
        if current_gold > max_gold:
            max_gold = current_gold

    # Search case.
    for y,x in [(1,0),(-1,0),(0,1),(0,-1)]:
        if (i+y , j+x) not in visited:
            visited.append((i+y , j+x))
            search(grid , i+y , j+x, current_gold, copy.copy(visited))  

# Search for max gold. 
max_gold = 0
search(grid , start[0] , start[1], 0 , [(start[0],start[1])])

# Print max gold count.
print(max_gold if max_gold != 0 else 0)
