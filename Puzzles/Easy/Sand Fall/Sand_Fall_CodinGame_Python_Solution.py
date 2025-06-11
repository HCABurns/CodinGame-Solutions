# Get width and height and form grid.
w, h = [int(i) for i in input().split()]
grid = [[" " for i in range(w)] for i in range(h)]

# Define priority for lowercase and uppercase.
priority = [[1,-1] , [-1,1]]

n = int(input())
for i in range(n):
    # Get input char and column.
    inputs = input().split()
    s = inputs[0]
    j = int(inputs[1])

    # Perform the sand fall until it can't be placed.
    i = 0
    valid = False
    while True:
        # Move down until another character is found or bottom of the glass.
        while i < len(grid) and grid[i][j] == " ":
            i += 1

        # Define the priority for falling.
        if s.islower():
            directions = priority[0]
        else:
            directions = priority[1]
        
        # Attempt to move sideways, if possible shift.
        valid = False
        for x in directions:
            if i < h and 0 <= j+x < w and grid[i][j+x] == " ":
                j += x
                valid = True
                break

        # If moved sideways, continue otherwise add to the glass and move onto next char.
        if valid== True:
            continue
        else:
            grid[i-1][j] = s
            break

# Print the hourglass.
print(*["|"+"".join(i)+"|" for i in grid], sep ="\n")
print("+"+"-"*(w)+"+")
