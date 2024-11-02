# Get coordinates of the cities.
coords = []
n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    coords.append([x,y])

# Get required variables.
start = coords[0]
visited = 0
current = 0
seen = set()
sum_val = 0

# Calculate shortest distance to a city and move to that position.
# Continue until only one city is left. (Will be made to return to start)
while visited <= n-2:
    local_min = 999999
    local_min_i = -1
    x,y = coords[current]
    for j in range(1,n):
        if current!=j and j not in seen:
            x2,y2 = coords[j]
            dist = ((x2-x)**2 + (y2-y)**2)**0.5
            if dist < local_min:
                local_min, local_min_i = dist, j
               
    # Adjust variables.
    seen.add(current)
    sum_val += local_min
    coords[current] = "X"
    current = local_min_i
    visited+=1

# Calculate back to the start.
x2 , y2 = coords[current]
x,y = start
dist_to_start = ((x2-x)**2 + (y2-y)**2)**0.5

# Output total distance between cities.
print(round(sum_val + dist_to_start))
