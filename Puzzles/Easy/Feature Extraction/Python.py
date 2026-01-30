# Read in input image.
grid = []
r, c = [int(i) for i in input().split()]
for i in range(r):
    grid.append([*map(int,input().split())])

# Read in weight matrix.
weights = []
m, n = [int(i) for i in input().split()]
for i in range(m):
    weights.append([*map(int,input().split())])

# Dot product to produce output.
output = [[0 for _ in range(c-n+1)] for _ in range(r-m+1)]
for i in range(r-m+1):
    for j in range(c-n+1):
        for y in range(m):
            for x in range(n):
                ny, nx = i+y, j+x
                output[i][j] += grid[ny][nx] * weights[y][x]

# Output the matrix.
for row in output:
    print(*row)
