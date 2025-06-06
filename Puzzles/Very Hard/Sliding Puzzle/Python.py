from collections import deque 
import copy

# Form the sliding puzzle grid and find where the "empty" slot is.
h, w = [int(i) for i in input().split()]
grid = []
pos = [0,0]
for i in range(h):
    row = input()
    grid.append([])
    for j,c in enumerate(row.split()):
        if c == ".":
            pos = [i,j]
        grid[-1] += [c]
    
# Define the finished state.
done = [[str(i*w + j) for j in range(1,w+1)] for i in range(h)]
done[-1][-1] = "."

# Define the directions and the queue.
directions = [(1,0), (0,1),(-1,0), (0,-1)]
puzzles = deque([[grid,0, pos]])

# Complete a BFS to find the completed state in minimal moves.
seen = set()
while puzzles:
    puzzle, moves, pos = puzzles.popleft()
    i, j = pos
    
    if all(a==b for a,b in zip(puzzle,done)):
        print(moves)
        break

    for y,x in directions:
        if 0 <= i + y < h and 0 <= j + x < w:
            r = copy.deepcopy(puzzle)

            tmp = r[i][j]
            r[i][j] = r[i+y][j+x]
            r[i+y][j+x] = tmp

            string_grid = "".join(["".join(row) for row in r])
            if string_grid not in seen:
                seen.add(string_grid)
                puzzles.append([r, moves + 1, [i+y,j+x]])
