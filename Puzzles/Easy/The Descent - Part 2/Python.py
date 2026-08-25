# Form Grid.
w, h = [int(i) for i in input().split()]
grid = [[*map(int,input().split())] for _ in range(h)]
a, b = [int(i) for i in input().split()]
t = int(input())

# Find landing area.
best = 1e9
for i in range(0,h):
    for j in range(0,w):
        for a1,b1 in [[a,b], [b,a]]:
            if i+a1>h or j+b1>w:continue
            landing_zone = [grid[i+dy][j+dj] for dj in range(b1) for dy in range(a1)]
            val = sum([v-min(landing_zone) for v in landing_zone])
            if val <= t and val < best:
                best = val

# Print result.
print(best if best != 1e9 else "Not Possible")
