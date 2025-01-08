# Form grid and store rows with apples.
grid = [[" " for i in range(100)] for i in range(100)]
n = int(input())
rows = []
for i in range(n):
    inputs = input().split()
    name = inputs[0]
    r = int(inputs[1])
    c = int(inputs[2])
    grid[r][c] = name
    if r not in rows:rows+=[r]

# Sort rows, create output variable and direction variable.
rows.sort()
output = []
direction = 1

# Go along the rows of apples in the correct order and store apples.
for row in rows:
    i = row
    j = 0 if direction == 1 else 99

    while j >= 0 and j <= 99:
        if grid[i][j] != " ":
            output += [grid[i][j]]
        j += direction   
    direction *= -1

# Print the apples the snake will eat.
print(",".join(output))
