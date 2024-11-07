# Get dimensions and form grid.
height, width = [int(i) for i in input().split()]
grid = [input().split(" ") for i in range(height)]

# Get values from the grid.
nodes = []
for i in range(height):
    line = input().split(" ")
    for j, char in enumerate(line):
        if char == "X":
            nodes.append(int(grid[i][j]))

# Check pairing nodes are opposite signs.
valid = True
for i in range(0,len(nodes)-1,2):
    if nodes[i]>0 and nodes[i+1]>0 or nodes[i]<0 and nodes[i+1]<0:
        valid = False

# Output if valid or not.
print("true" if valid else "false")
