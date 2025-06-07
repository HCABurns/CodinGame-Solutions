import heapq

# Form the sliding puzzle grid and find where the "empty" slot is.
h, w = 3, 4
grid = []
for i in range(3):
    grid.extend(input().split())
# Define the finished state.
done = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')
grid = tuple(grid)

pos = grid.index("0")
goal_positions = {'0':(0,0),'1':(0,1),'2':(0,2),'3':(0,3),'4':(1,0),'5':(1,1),'6':(1,2),'7':(1,3),'8':(2,0),'9':(2,1),'10':(2,2),'11':(2,3)}
current_position = {0:(0,0),1:(0,1),2:(0,2),3:(0,3),4:(1,0),5:(1,1),6:(1,2),7:(1,3),8:(2,0),9:(2,1),10:(2,2),11:(2,3)}

# Get manhattan distance.
def distance(grid):
    dist = 0
    for idx, char in enumerate(grid):
        if char == "0":continue
        i2, j2 = goal_positions[char]
        i, j = current_position[idx]
        dist += abs(j2-j) + abs(i2-i)
    return dist

# Define the directions and the queue.
directions = [(1,0), (0,1),(-1,0), (0,-1)]
puzzles = [[distance(grid), 0, grid, pos]]

# Complete a BFS to find the completed state in minimal moves.
seen = {grid:0}

# Complete BFS to find the goal state.
came_from = {grid:None}
while puzzles:
    dist, moves, puzzle, pos = heapq.heappop(puzzles)

    i, j = divmod(pos, w)
    for y,x in directions:
        if 0 <= i + y < h and 0 <= j + x < w:
            next_pos = pos + (w*y + x)
            r = list(puzzle)
            r[pos], r[next_pos] = r[next_pos], r[pos]
            r = tuple(r)
            if r not in seen or moves + 1 < seen[r]:
                if r == done:
                    puzzles = []
                    break
                seen[r] = moves + 1
                came_from[r] = [puzzle, [next_pos // w, next_pos % w]]
                heapq.heappush(puzzles, [distance(r) + moves + 1, moves + 1, r, next_pos])

# Print the path from original to goal.
arr = []
while came_from[puzzle]:
    arr += came_from[puzzle][1]
    puzzle = came_from[puzzle][0]

for i in range(len(arr)-1,0,-2):
    print(arr[i-1], arr[i])
print(0,0)
