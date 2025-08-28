# Get input data.
n = int(input())
vert_pos, hor_pos = input().split()
order, direction = input().split()

# Get information from data.
i = 0 if vert_pos == "t" else n-1
j = 0 if hor_pos == "l" else n-1
values = range(1,n**2+1) if order == "+" else range(n**2,0,-1)
out = [["" for _ in range(n)] for _ in range(n)]
directions = [[0,1],[1,0],[0,-1],[-1,0]] if direction == "c" else [[0,-1],[1,0],[0,1],[-1,0]]
direction = 0 if i == 0 else 1

# Fill spiral.
for val in values:
    out[i][j] = str(val)
    if val == values[-1]:break
    y,x = directions[direction]
    while not (0<=y+i<n and 0<=x+j<n and out[y+i][x+j] == ""):
        direction = (direction+1)%4
        y,x = directions[direction]
    i += y
    j += x

# Print sprial.
for row in out:
    print("\t".join(row))
