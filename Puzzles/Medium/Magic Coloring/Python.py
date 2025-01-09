# Form Grid.
valid = False
grid = []
x, y = [int(i) for i in input().split()]
for i in range(y):
    line = input()
    if any(1 for i in line if i != "0"):valid = True 
    grid += [[i for i in line]]

# If no colouring positions, print and quit.
if not valid:print("No coloring today");quit()

# Define search directions.
directions = [(1,0),(-1,0),(0,1),(0,-1)]

# Fill all connectect "val" with "0"
def fill(i, j, val):
    if i<0 or i>=y or j<0 or j>=x or grid[i][j] != val:
        return
    
    grid[i][j] = "0"
    for iy, jx in directions:
        fill(iy+i,jx+j,val)
    return 

# Find the sections, count sections and fill with 0s. 
total = {}
for i in range(y):
    for j in range(x):
        if grid[i][j] != "0":
            val = grid[i][j]
            fill(i, j, val)
        
            if val not in total:
                total[str(val)] = 0
            total[str(val)] += 1

# Print out the number of segments of each colour.
for i,j in sorted(total.items()):
    print(f"{i} -> {j}")
