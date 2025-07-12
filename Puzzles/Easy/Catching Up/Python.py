from collections import deque

# From grid and get positions.
grid = []
pos = sus = [0,0]
k = int(input())  # representing after how many turns the sus man will make another move
for i in range(10):
    s = input()  # the map
    if "P" in s:
        pos = [i,s.find("P")]
    if "E" in s:
        sus = [i,s.find("E")]
    grid += [s.replace("EP","--")]

# Define directions
d = {0:"D",1:"R",2:"U",3:"L"} | {"D":(1,0),"R":(0,1),"U":(-1,0),"L":(0,-1)}
directions = [(1,0),(0,1),(-1,0),(0,-1)]

# Complete full BFS with rotating directions to stop loops.
def bfs(y,x,goal_y, goal_x, limit,route):
    visited = set()
    queue = deque([[y,x, limit, route]])
    finished = []
    rotate = 0

    while queue:
        rotate = (rotate + 1) % 4
        y,x,limit,route = queue.popleft()
        visited.add((y,x))
        if y==goal_y and x==goal_x:
            return route
            
        for pos, (i,j) in enumerate(directions[rotate:4] + directions[:rotate]):
            ny = y + i
            nx = j + x
            if (ny,nx) not in visited and 0<=ny<10 and 0<=nx<10 and grid[ny][nx] != "*":
                queue.append([ny,nx,limit-1, route + [d[(rotate + pos) % 4]]])
    return finished

# Print initial directions movement.
res = bfs(pos[0], pos[1], sus[0], sus[1], k, [])
for r in res:
    y,x = d[r]
    pos[0] += y
    pos[1] += x
    print(r)


# game loop
while True:
    # Get sus mans position.
    ene_y, ene_x = [int(i) for i in input().split()]

    # Complete BFS to reach.
    res = bfs(pos[0], pos[1], ene_y, ene_x , k, [])

    # Print the movements.
    for r in res:
        y,x = d[r]
        pos[0] += y
        pos[1] += x
        print(r)
