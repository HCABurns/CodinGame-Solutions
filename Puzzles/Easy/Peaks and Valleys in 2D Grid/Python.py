# Form grid.
grid = []
h = int(input())
for i in range(h):
    line = input()
    grid.append([*map(int,line.split(" "))])
w = len(grid[0])

# Define neighbours
neighbours = {}
for i in range(h):
    for j in range(w):
        for dy,dx in [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1], [1,-1], [-1,1]]:
            ny, nx, = dy+i, dx+j
            if 0<=ny<h and 0<=nx<w:
                neighbours.setdefault((i,j), [])
                neighbours[(i,j)].append(grid[ny][nx])

# Find peak and valleys.
peaks = []
valley = []
for i in range(h):
    for j in range(w):
        larger = 0
        smaller = 0
        for val in neighbours[(i,j)]:
            if val > grid[i][j]:
                larger+=1
            elif val < grid[i][j]:
                smaller+=1
               
        if smaller == len(neighbours[(i,j)]):
            peaks.append(f"({j}, {i})")
        if larger == len(neighbours[(i,j)]):
            valley.append(f"({j}, {i})")

# Print the peaks and valley coordiantes.
print(", ".join(peaks) if peaks else "NONE")
print(", ".join(valley) if valley else "NONE")
