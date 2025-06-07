import heapq

# Form the sliding puzzle grid and find where the "empty" slot is.
h, w = [int(i) for i in input().split()]
grid = []
pos = [0,0]
for i in range(h):
    row = input()
    for j,c in enumerate(row.split()):
        if c == ".":
            pos = (w*i + j)
        grid.append(c)
    
# Define the finished state.
done = []
for i in range(h):
    [done.append(str(i*w + j)) for j in range(1,w+1)]
done[-1] = "."

done = tuple(done)
grid = tuple(grid)
goal_positions = {char:i for i,char in enumerate(done)}

def distance(grid):
    dist = 0
    for idx, char in enumerate(list(grid)):
        expected = goal_positions[char]
        i = idx // w
        j = idx % w

        i2 = expected // w
        j2 = expected % w
        #dist += ((i-i2)**2 + (j-j2)**2)**0.5
        dist += abs(j-j2) + abs(i-i2)

    return dist

# Define the directions and the queue.
directions = [(1,0), (0,1),(-1,0), (0,-1)]
puzzles = [[distance(grid), 0, grid, pos]]
heapq.heapify(puzzles)

# Complete a BFS to find the completed state in minimal moves.
seen = set()
while puzzles:
    dist, moves, puzzle, pos = heapq.heappop(puzzles)
    i = pos // w
    j = pos % w

    if puzzle == done:
        print(moves)
        break

    for y,x in directions:
        if 0 <= i + y < h and 0 <= j + x < w:
            r = list(puzzle)
            tmp = r[pos]
            r[pos] = r[pos + (w*y + x)]
            r[pos + (w*y + x)] = tmp
            r = tuple(r)

            if r not in seen:
                seen.add(r)
                new_dist = distance(r)
                heapq.heappush(puzzles, [moves + new_dist, moves + 1, r, pos + (w*y + x)])
