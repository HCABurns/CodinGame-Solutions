# Get inputs.
n = int(input())
l = int(input())

# Form grid and store candle top left positions.
grid = []
candles = []
for i in range(n):
    grid.append([])
    for j,cell in enumerate(input().split()):
        grid[-1].append(cell)
        if cell == "C":
            TLI = i-l+1
            TLJ = j-l+1
            candles.append([TLI,TLJ])

# Change spots from X to light if within range of a candle.
total = n*n - len(candles)
for i,j in candles:
    for light_reach_i in range(l*2-1):
        for light_reach_j in range(l*2-1):
            if i+light_reach_i>=0 and j+light_reach_j>=0 and i+light_reach_i<len(grid) and j+light_reach_j<len(grid[0]) and grid[i+light_reach_i][j+light_reach_j] == "X":
                grid[i+light_reach_i][j+light_reach_j] = "1"
                total -= 1

# Print total of spots in darkness.
print(total)
