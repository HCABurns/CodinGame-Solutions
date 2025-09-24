from collections import defaultdict
from collections import deque

# Form grid and find starting positions.
grid = defaultdict(list)
l, r, c = [int(i) for i in input().split()]
ln = int(input())
idx = val = 0
start = [0,0,0]
end = [0,0,0]
for i in range(ln):
    line = input()
    if not line:
        continue
    
    if "S" in line: start = [idx, val%r, line.index("S")]
    if "A" in line: end = [idx, val%r, line.index("A")]
    
    grid[idx].append(list(line))
    
    val += 1
    if val % r == 0:
        idx += 1

# Find if the move goes beyond the grid or barrier blocking move.
def valid(dz,dy,dx):
    if 0>dz or dz>=l:return False
    if 0>dy or dy>=r:return False
    if 0>dx or dx>=c:return False
    if grid[dz][dy][dx] == "#":return False
    return True

# Complete 3D BFS from starting location to the end
queue = deque([[*start,0,[]]])
directions = [[0,0,1],[0,-1,0],[0,0,-1],[0,1,0], [1,0,0], [-1,0,0]]
seen = set((start[0],start[1],start[2]))
found = False
while queue:
    k,i,j,moves, path = queue.popleft()
    
    if [k,i,j] == end:
        found = True
        break

    for z,y,x in directions:
        dz = z+k
        dy = y+i
        dx = x+j
        if valid(dz,dy,dx) and (dz,dy,dx) not in seen:
            queue.append([dz,dy,dx,moves+1, path+[[dz,dy,dx]]])
            seen.add((dz,dy,dx))

# Print the distance between S and A or "NO PATH" if not path exists.
if found:
    print(moves)
else:
    print("NO PATH")
