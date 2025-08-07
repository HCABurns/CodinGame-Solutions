import sys

def solve():
    # Form 1D grid representation and store idx of starting nodes.
    grid = []
    colour_nodes = {} # Int : [int, int]
    h, w = [int(i) for i in input().split()]
    for i in range(h):
        row = input()
        global s
        s = time.time()
        for j in range(w):
            if row[j] != ".":
                grid.append(row[j])
                colour_nodes.setdefault(int(row[j]) , []).append(i*w+j)
            else:
                grid.append('')

    def score(y,x):
        score = 0
        for i,j in [[0,1],[1,0],[0,-1],[1,0]]:
            newidx = y+i*w+x+j
            if 0<=y+i<h and 0<=x+j<w and grid[newidx] == '':
                score+=1
        return score    
    
    def manhattan(idx, idx2):
        """
        Manhattan distance between two nodes used for searching closest to furtherest.
        """
        i,j = divmod(idx, w)
        y,x = divmod(idx2, w)
        return score(i,j) + score(y,x)

    # Get the colours in increasing manhattan distance.
    colours = sorted(colour_nodes.keys(),key = lambda k : manhattan(*colour_nodes[k])) # int[]
    N = len(colours)

    # Set the starting bitmask and endmask.
    starting_bitmask = 0
    for colour in colours:
        for idx in colour_nodes[colour]:
            starting_bitmask |= (1 << idx)

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
            nonlocal solution_found
            nonlocal colour_paths
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
                ny, nx = y + dy, x + dx
                nidx = ny * w + nx
                if 0 <= ny < h and 0 <= nx < w:
                    is_endpoint = nidx == end_idx
                    is_empty = not ((current_bitmask >> nidx) & 1)
                    
                    if not ((path_mask >> nidx) & 1):
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
        find_colour_path(start_y, start_x, (1 << start_idx)) 
        return solution_found[0]
        
    # Find all the paths and raise error if no path possible.
    if not find_paths(0, starting_bitmask):
        raise AssertionError("No valid full-covering path combination found")

    # Print the Solution
    for colour in colours:
        path = colour_paths[colour]
        for i in range(len(path) - 1):
            y1, x1 = path[i]
            y2, x2 = path[i+1]
            print(x1, y1, x2, y2, colour)

import time
global s
# Need in a function for the use of nonlocal
solve()
print(f"Execution time: {time.time()-s:.2f}s", file = sys.stderr)
