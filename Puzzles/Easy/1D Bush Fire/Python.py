# Get the number of bush fires.
n = int(input())
for i in range(n):
    # Get bush fire.
    line = input()

    # Add empty trees at the end.
    grid = list(line) + [".","."]

    # Start at i = 2 and with 0 water used.
    i = 2
    water = 0

    # Go through the array and find fires to put out.
    while i < len(grid):
        if grid[i-2] == "f":
            water += 1
            grid[i-2:i+1] = [".",".","."]
        i += 1
    
    # Print the number of water used to put out the fires.
    print(water)
