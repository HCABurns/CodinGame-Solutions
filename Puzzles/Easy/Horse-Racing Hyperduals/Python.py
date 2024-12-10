# Array for horses.
horses = []

# Store horses.
n = int(input())
for i in range(n):
    horses.append([int(j) for j in input().split()])

# Find minimum difference.
min_val = 1e9
for i in range(0, len(horses)-1):
    for j in range(i+1, len(horses)):
        min_val = min(min_val,abs(horses[i][0] - horses[j][0]) + abs(horses[i][1] - horses[j][1]))

# Print min difference.
print(min_val)
