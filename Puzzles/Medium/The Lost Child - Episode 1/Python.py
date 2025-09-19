from collections import deque

# Form grid and find start and end position.
grid = []
for i in range(10):
    row = input()
    grid.append(row)
    if "M" in row:
        start = [i,row.index("M")]
    if "C" in row:
        end = (i,row.index("C"))

# Standard BFS from start to end.
seen = set(start)
queue = deque([[*start,0]])
while queue:
    i,j,moves = queue.popleft()

    if (i,j) == end:
        break

    for y,x in [[0,1],[-1,0],[0,-1],[1,0]]:
        dy, dx = i+y, j+x
        if (dy,dx) not in seen and 0<=dy<10 and 0<=dx<10 and grid[dy][dx]!="#":
            seen.add((dy,dx))
            queue.append([dy,dx,moves+1])

# Print the distance between.
print(f"{moves*10}km")
