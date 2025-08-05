from collections import deque

# Form the map.
food = []
w, h = [int(i) for i in input().split()]
for i in range(h):
    food.append([*map(int,input().split())])

# Find max food path across the pond.
queue = deque([[0,0, 0]])
max_score = 0
seen = {}
while queue:
    i, j, score = queue.popleft()
    score += food[i][j]
    
    # Checking if faster way to reach the same tile.
    if (i,j) in seen and score <= seen[(i,j)]:
        continue
    seen[(i,j)] = score

    if score > max_score:
        max_score = score

    if i+1 < h:
        queue.append([i+1,j,score])
    if j+1 < w:
        queue.append([i,j+1,score])

# Print the max score.
print(max_score)
