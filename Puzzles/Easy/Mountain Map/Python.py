# Get number of mountains and form a array of the heights.
n = int(input())  
heights = [int(i) for i in input().split()]

# Get width and height of the grid.
width = sum(heights)*2
height = max(heights)

# Form Grid
grid = [[" "]*width for _ in range(height)]

# Place mountains in the correct places in the grid.
i = height-1
j = 0
for height in heights:
    for _ in range(height):
        grid[i][j] = "/"
        i-=1
        j+=1
    i+=1

    for _ in range(height):
        grid[i][j] = "\\"
        i+=1
        j+=1
    i-=1

# Print grid with rstrip to remove trailing spaces.
for i in grid:
    print("".join(i).rstrip())
