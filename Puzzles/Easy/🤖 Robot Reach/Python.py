# Get inputs.
height = int(input())
width = int(input())
threshold = int(input())

# Create visited set.
visited = set()

# Check each position and ensure value is below threshold and the cell is reachable from other valid cells.
for i in range(height):
    for j in range(width):
        if i==0 or (i-1,j) in visited or (i,j-1) in visited:
            sum_val = sum([int(v) for v in str(i)] + [int(v) for v in str(j)])
            if sum_val <= threshold:
                visited.add((i,j))
# Print number of valid cells.
print(len(visited))
