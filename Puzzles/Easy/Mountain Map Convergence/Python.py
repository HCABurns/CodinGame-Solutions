# Get number of mountains and form a array of the heights.
n = int(input())  
heights = [int(i) for i in input().split()] 

# Get width and height of the grid.
width = 200
height = max(heights)

if len([i for i in heights if i < 0]) > 0:
    height += abs([0,max([i for i in heights if i<0])][any(1 for i in heights if i < 0)])

# Form Grid
grid = [[" " for _ in range(width)] for _ in range(40)]

prev_height = 0
# Place mountains in the correct places in the grid.
i = max(heights)
j = 0

# Store starting location.
s = i

# Print the mountains.
prev_height = 0
for idx, height in enumerate(heights):
    direction = [1,-1][i > s-height+1]
    if direction == 1 and idx !=0:
        i += 1

    value = s-height+1
    equal = value == i
    if not equal:
        if direction == 1 and idx == 0:
            i += 1
        
        if idx == 0 or heights[idx] != heights[idx-1]:
            while i != value:
                grid[i][j] = ["/","\\"][direction == 1]
                j += 1
                i += direction
        else:
            i += direction * -1

    if idx != 0 and direction == 1 and heights[idx] != heights[idx-1] or direction == 1 and idx == 0 and not equal and i != 1:
        grid[i][j] = "\\"
        j += 1

    # Print Peak
    grid[i][j] = "/"
    j += 1
    grid[i][j] = '\\'
    j += 1

# Return to the start location.
while i != s:
    if i > s:
        
        grid[i][j] = "/"  
        i -= 1
    else:
        i += 1
        grid[i][j] = "\\"
        
    j += 1

# Print grid with rstrip to remove trailing spaces.
for row in grid:
    line = "".join(row).rstrip()
    if line:
        print(line)
