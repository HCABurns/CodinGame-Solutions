import sys
from collections import deque
import time

# Form 1D grid representation and store idx of starting nodes.
grid = []
colour_nodes = {} # Int : [int, int]
h, w = [int(i) for i in input().split()]
for i in range(h):
    row = input()
    s = time.time()
    for j in range(w):
        if row[j] != ".":
            grid.append(row[j])
            colour_nodes.setdefault(int(row[j]) , []).append(i*w+j)
        else:
            grid.append('')

def proximity(y,x):
    prox = 0
    for i,j in [[0,1],[1,0],[0,-1],[1,0]]:
        newidx = y+i*w+x+j
        if 0<=y+i<h and 0<=x+j<w and grid[newidx] == '':
            prox+=1
    return prox 

def manhattan(v1,v2):
    """
    Manhattan distance between two nodes used for searching closest to furtherest.
    """
    return abs(v1-v2)

def scoring(idx, idx2):
    i,j = divmod(idx, w)
    y,x = divmod(idx2, w)
    return [proximity(i,j) + proximity(y,x) , -(manhattan(i,y) + manhattan(j,x))]

# Get the colours in increasing manhattan distance.
colours = sorted(colour_nodes.keys(),key = lambda k : scoring(*colour_nodes[k])) # int[]
N = len(colours)

# Set the starting bitmask and endmask.
starting_bitmask = 0
for colour in colours:
    for idx in colour_nodes[colour]:
        starting_bitmask |= (1 << idx)

print(bin(starting_bitmask)[2:][::-1], file = sys.stderr)

# Backtracking to find a solution.
colour_paths = {}
solution_found = [False]
def find_paths(colour_idx, current_bitmask):
    # Solution already found so exit.
    if solution_found[0]:
        return True

    # Goal state - All colour have been added and all tiles used.
    if colour_idx == N:
        goal_mask = (1 << (h * w)) - 1
        if current_bitmask == goal_mask:
            solution_found[0] = True
            return True
        return False

    def find_colour_path(y,x, path_mask):
        if solution_found[0]:
            return
        
        current_path.append((y,x))
        
        if y * w + x == end_idx:
            if find_paths(colour_idx+1, current_bitmask | path_mask):
                colour_paths[colour] = list(current_path)
                solution_found[0] = True
            current_path.pop()
            return

        for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]:
        #for dy, dx in [(0,1), (-1,0), (0,-1), (1,0)]:
        #for dy, dx in [(-1,0), (0,-1),(1,0), (0,1)]:
        #for dy, dx in [(0,-1),(1,0), (0,1), (-1,0)]:
            ny, nx = y + dy, x + dx
            nidx = ny * w + nx
            # Check for valid moves: within bounds and not occupied by other paths
            if 0 <= ny < h and 0 <= nx < w:
                is_endpoint = nidx == end_idx
                is_empty = not ((current_bitmask >> nidx) & 1)
                
                if not ((path_mask >> nidx) & 1): # Avoid self-intersections
                    if is_empty or is_endpoint:
                        # Recurse to extend the path
                        find_colour_path(ny, nx, path_mask | (1 << nidx))
                        if solution_found[0]:
                            return
        current_path.pop()
    
    # Get information of current path.
    colour = colours[colour_idx]
    start_idx, end_idx = colour_nodes[colour]
    start_y, start_x = divmod(start_idx, w)
    current_path = []

    def is_path(start_idx, end_idx, mask):
        # BFS from start to end
        queue = deque([start_idx])
        visited = {start_idx}
        while queue:
            new_idx = queue.popleft()
            if new_idx == end_idx:
                return True
            visited.add(new_idx)
            y ,x = divmod(new_idx, w)
            for dy, dx in [[0,1],[-1,0],[0,-1],[1,0]]:
                ny, nx = dy+y, dx+x
                new_idx = ny*w + nx
                if 0<=ny<h and 0<=nx<w:
                    if new_idx not in visited and (new_idx == end_idx or not ((mask >> new_idx) & 1)):
                        queue.append(new_idx)
        return False

    def can_connect_colours(mask, colour_idx):
        """Check if the remaining colours can be connected or not - Not blocked by paths"""
        for colour in colours[colour_idx:]:
            start_idx, end_idx = colour_nodes[colour]
            if not is_path(start_idx, end_idx, mask):
                return False
        return True

    if not can_connect_colours(current_bitmask, colour_idx):
        return False

    find_colour_path(start_y, start_x, (1 << start_idx)) 
    return solution_found[0]
    
# Initial call to the solver
if not find_paths(0, starting_bitmask):
    raise AssertionError("No valid full-covering path combination found")

# --- Print the Solution ---
print(colours, file = sys.stderr)
print(colour_paths, file = sys.stderr)
for colour in colours:
    path = colour_paths[colour]
    for i in range(len(path) - 1):
        y1, x1 = path[i]
        y2, x2 = path[i+1]
        print(x1, y1, x2, y2, colour)


# Need in a function for the use of nonlocal
print(f"Execution time: {time.time()-s:.2f}s", file = sys.stderr)
