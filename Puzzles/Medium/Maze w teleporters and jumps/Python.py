from collections import deque

# Define start, teleporters and input grid.
teleporters_positions = {}
grid = start = []
width = int(input())
height = int(input())
for i in range(height):
    row = input()
    grid.append([])
    for j,char in enumerate(row):
        grid[-1].append(char)
        if char == "S":
            start = (i,j)
        elif char.isalpha() and char not in "SE":
            teleporters_positions[char] = [i,j]

# Define teleporter locations.
teleporters = {}
for char in [i for i in teleporters_positions.keys() if i.islower() and i!="v"]:
    teleporters[char] = teleporters_positions[char.upper()]

# Define jump pods
pods = {"v":[2,0],"<":[0,-2],">":[0,2],"^":[-2,0]}

# BFS to find shortest route to final.
queue = deque([[*start,0]])
shortest_moves = -1
seen = set(start)
while queue:
    i,j,moves  = queue.popleft()
    char = grid[i][j]
    
    if char == "E":
        shortest_moves = moves
        break

    if char in teleporters:
        destination = (teleporters[char][0], teleporters[char][1])
        if destination not in seen:
            queue.append([*destination,moves])
            seen.add(destination)
    elif char in "<>v^":
        destination = (i+pods[char][0], j+pods[char][1])
        if destination not in seen:
            queue.append([*destination,moves])
            seen.add(destination)
    
    for di,dj in [[0,1],[-1,0],[0,-1],[1,0]]:
        if 0<=i+di and i+di<height and 0<=j+dj and j+dj<width and grid[i+di][j+dj] != "#":
            if (i+di,j+dj) not in seen:
                queue.append([i+di,j+dj,moves+1])
                seen.add((i+di, j+dj))

print(shortest_moves)
