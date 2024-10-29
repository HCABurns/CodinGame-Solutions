# Get width and hight of shape to fit
a, b = [int(i) for i in input().split()]

# Find shape coordinates relative to the first * character.
shape = []
start = []
for i in range(a):
    object_line = input()
    for j,char in enumerate(object_line):
        if char == "*":
            if start == []: #Set first position values
                start = [i,j]
                shape.append([0,0])
            else:
                shape.append([i-start[0],j-start[1]])

# From Grid
c, d = [int(i) for i in input().split()]
grid = [list(input()) for _ in range(c)]


def shape_can_fit(i,j):
    """
    Helper function to determine if the shape can fit when placed at i,j

    Parameters:
    i : int - Row index of start position.
    j : int - Column index of start position.

    Returns: boolean - True if the shape can fit otherwise False.
    """
    for x,y in shape:
        ix = i + x
        jy = j + y
        if 0>ix or ix>=c or 0>jy or jy>=d or grid[ix][jy] != ".":
            return False
    return True

# Find positions that the shape can fit and store in array.
positions = []
for i,row in enumerate(grid):
    for j,col in enumerate(row):
        if col == ".":
            if shape_can_fit(i,j):
                positions.append([i,j])

# Output number of positions and if only one, place the shape in and print.
print(len(positions))
if len(positions)==1:
    for x,y in shape:
        grid[positions[0][0] + x][positions[0][1] + y] = "*"

    for row in grid:
        print("".join(row))
        
