from collections import deque

# Set directions and reverse directions.
dirs = {
    "/":{"N":(0,1),"S":(0,-1), "E":(-1,0),"W":(1,0)},
    "\\":{"N":(0,-1),"S":(0,1), "E":(1,0),"W":(-1,0)},
}
reverse_mirror = {"/":"\\", "\\":"/"}
reverse_dirs = {(0,1):"E", (1,0):"S", (0,-1):"W", (-1,0):"N"}

# Form grid and find laser.
grid = []
laser = []
w, h = [int(i) for i in input().split()]
for i in range(h):
    s = input()
    if "L" in s: laser = [i,s.index("L")]
    grid.append(list(s))

# Set directions.
direction = input()
for d, v in reverse_dirs.items():
    if v == direction:
        direction = d 
        break

# BFS to find a solution.
queue = deque([[*laser,direction, (), ()]])
min_swaps = None
cache = {}
while queue:
    y,x, (dy,dx), seen, swaps = queue.popleft()

    if (y,x,dy,dx, swaps) in cache or min_swaps and len(swaps) > len(min_swaps):
        continue
    cache[(y,x,dy,dx, swaps)] = 1

    if grid[y][x] == "T":
        if not min_swaps: min_swaps = swaps
        min_swaps = min(min_swaps, swaps, key = len)
        continue
    seen += ((y,x))

    ny , nx = dy+y, dx+x
    if 0<=ny<h and 0<=nx<w and (ny,nx, seen, swaps) not in cache:
        if grid[ny][nx] in "\\/":
            word_direction = reverse_dirs[(dy,dx)]
            queue.append([ny,nx, dirs[grid[ny][nx]][word_direction], seen, swaps])            
            queue.append([ny,nx, dirs[reverse_mirror[grid[ny][nx]]][word_direction], seen, swaps + ((nx,ny),)])
        
        elif grid[ny][nx] == "." or grid[ny][nx] == "T" or grid[ny][nx] == "L":
            queue.append([ny,nx, (dy,dx), seen, swaps])
            

# Print the mirrors to swap.
for swap in sorted(list(min_swaps), key = lambda x : (x[1],x[0])):
    print(*swap)
