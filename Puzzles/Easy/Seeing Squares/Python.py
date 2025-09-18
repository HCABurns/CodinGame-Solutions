# Form grid of squares.
grid = []
r, c = [int(i) for i in input().split()]
for i in range(r):
    row = input()
    grid.append(row)

# Find out how many squares are in the grid.
seen = set()
squares = 0
for i in range(r):
    for j in range(c):
        if grid[i][j] == "+":
            for y in range(i+1,r):
                if grid[y][j] in "- ":break
                if grid[y][j] == "+" and j+(y-i) < c:
                    for x in range(j+1, c):
                        if grid[i][x] in "| ":break
                        elif grid[y][x] in "| ":break

                        if (y-i+1)*2 - 1 == (x-j+1):
                            if grid[i][x] == "+" and grid[y][x] == "+":
                                # Check right side of square
                                for row in range(i,y+1):
                                    if grid[row][x] in "- ":break
                                    if grid[row][j] in "- ":break
                                else:
                                    squares += 1
                            break
                            
# Print the number of squares in the image.     
print(squares)
