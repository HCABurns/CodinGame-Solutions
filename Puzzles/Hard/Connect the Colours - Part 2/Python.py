from collections import deque
from functools import lru_cache

# Form 1D grid representation and store idx of starting nodes.
grid = []
colour_nodes = {} # Int : [int, int]
all_nodes = {}
h, w = [int(i) for i in input().split()]
for i in range(h):
    row = input()
    for j in range(w):
        if row[j] != ".":
            grid.append(row[j])
            colour_nodes.setdefault(int(row[j]) , []).append(i*w+j)
            all_nodes[i*w+j] = int(row[j])
        else:
            grid.append('')

# Set the starting bitmask and endmask.
starting_bitmask = 0
for colour in colour_nodes.keys():
    for idx in colour_nodes[colour]:
        starting_bitmask |= (1 << idx)

def proximity(y,x, bitmask):
    prox = 0
    for i,j in [[0,1],[-1,0],[0,-1],[1,0]]:
        newidx = (y+i)*w+x+j
        if 0<=y+i<h and 0<=x+j<w and (bitmask << newidx) & 0:
            prox+=1
    return prox 

def manhattan_idx(v,v2):
    #Manhattan distance between two nodes used for searching closest to furtherest.
    i,j = divmod(v, w)
    y,x = divmod(v2, w)
    return abs(i-y) + abs(j-x)

def manhattan(v1,v2):
    #Manhattan distance between two nodes used for searching closest to furtherest.
    return abs(v1-v2)

def scoring(idx, idx2, current_mask):
    i,j = divmod(idx, w)
    y,x = divmod(idx2, w)
    return [proximity(i,j, current_mask) + proximity(y,x,current_mask) , -(manhattan(i,y) + manhattan(j,x))]

# Neighbor lookup precomputed
neighbours = [[] for _ in range(h * w)]
for idx in range(h * w):
    y, x = divmod(idx, w)
    for dy, dx in [(1, 0), (0, -1), (0, 1), (-1, 0)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < h and 0 <= nx < w:
            neighbours[idx].append(ny * w + nx)

sorted_neighbours = {}
for idx in range(h*w):
    for target in range(h*w):
        sorted_neighbours[(idx, target)] = sorted(neighbours[idx],key=lambda n: manhattan_idx(n, target)) 

# Get the colours in increasing manhattan distance.
colours = sorted(colour_nodes.keys(),key = lambda k : scoring(*colour_nodes[k],starting_bitmask)) # int[]
N = len(colours)

# Backtracking to find a solution.
colour_paths = {}
solution_found = [False]
failed = set()
t = [0]

invalid = set()

@lru_cache(None)
def is_path_cached(start_idx, end_idx, mask):
    # BFS from start to end
    queue = deque([start_idx])
    visited = 1 << start_idx
    while queue:
        new_idx = queue.popleft()
        if new_idx == end_idx:
            return True
        visited |= (1 << new_idx)
        for new_idx in neighbours[new_idx]:
            if not ((visited >> new_idx) & 1) and (new_idx == end_idx or not ((mask >> new_idx) & 1)):
                queue.append(new_idx)
    return False

@lru_cache(None)
def is_locked_cached(mask):
    visited = mask

    for start in range(h * w):
        if (visited >> start) & 1:
            continue

        queue = deque([start])
        visited |= (1 << start)
        endpoint_count = 0
        while queue:
            idx = queue.popleft()
            for n in neighbours[idx]:
                if ((visited >> n) & 1) == 0:
                    visited |= (1 << n)
                    queue.append(n)
                else:
                    if n in all_nodes:
                        endpoint_count += 1
        if endpoint_count < 2:
            return True
    return False


@lru_cache(None)
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

    @lru_cache(None)
    def find_colour_path(idx, path_mask):
        if solution_found[0]:
            return
        
        current_path.append((divmod(idx,w)))
        if idx == end_idx:
            if find_paths(colour_idx+1, current_bitmask | path_mask):
                colour_paths[colour] = list(current_path)
                solution_found[0] = True
            current_path.pop()
            return

        for nidx in sorted_neighbours[(idx, end_idx)]:
            is_endpoint = nidx == end_idx
            is_empty = not ((current_bitmask >> nidx) & 1)
            
            
            if not ((path_mask >> nidx) & 1):
                if is_empty or is_endpoint:
                    new_mask = path_mask | (1 << nidx)
                    # New prune attempt here
                    temp_mask = current_bitmask | new_mask

                    for c in remaining[1:]: 
                        s_idx, e_idx = colour_nodes[c]
                        if not is_path_cached(s_idx, e_idx, temp_mask):
                            break 
                    else:
                        find_colour_path(nidx, new_mask)
                        if solution_found[0]:
                            return
        current_path.pop()

    # Get information of current path.
    # Determine remaining colours and sort them each time
    remaining = colours[colour_idx:]
    remaining = sorted(remaining,key=lambda c: scoring(*colour_nodes[c], current_bitmask))
    
    colour = remaining[0]
    start_idx, end_idx = colour_nodes[colour]
    current_path = []

    if is_locked_cached(current_bitmask):
        return False

    find_colour_path(start_idx, (1 << start_idx)) 
    return solution_found[0]
    
if not find_paths(0, starting_bitmask):
    raise AssertionError("No valid full-covering path combination found")

# Print the Solution
for colour in colours:
    path = colour_paths[colour]
    for i in range(len(path) - 1):
        y1, x1 = path[i]
        y2, x2 = path[i+1]
        print(x1, y1, x2, y2, colour)
