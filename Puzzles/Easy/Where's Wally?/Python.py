# Get starting position of wally and coordinates of other wally characters relative to the first.
wally_width, wally_height = [int(i) for i in input().split()]
shape = []
start = [-1,-1]
start_char = ""
for i in range(wally_height):
    for j,char in enumerate(input()):
        if char != " ":
            if start == [-1,-1]:
                start = [i, j]
                start_char = char
            else:
                shape.append([(i-start[0], j-start[1]), char])

# Form Grid.
_, picture_height = [int(i) for i in input().split()]
grid = [[i for i in input()] for _ in range(picture_height)]

# Find Wally.
for i,row in enumerate(grid):
    for j, char in enumerate(row):
        if char == start_char:
            found_wally = True
            for coords,wally_char in shape:
                y , x = coords
                if i+y<0 or i+y>=len(grid) or j+x<0 or j+x>=len(grid[0]) or grid[i+y][j+x] != wally_char:
                    found_wally = False
                    break
            # Output and quit - Only one wally.
            if found_wally:
                print(j-start[1], i-start[0])
                quit()
