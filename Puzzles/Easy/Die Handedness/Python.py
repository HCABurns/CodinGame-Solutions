# Form grid.
grid = []
for i in range(3):
    grid.append(input().strip())

# Determine which pairs are in the middle given 1,2,3 at the top or bottom.
# If 1,2,3 at the bottom, then reverse middle.
right_handed = {"1":"23","2":"31","3":"12"}
if grid[0][0] not in "123":
    key = grid[2][0]
    grid[1] = grid[1][::-1]
else:
    key=grid[0][0]

# Output one of "right-handed", "left-handed" and "degenerate".
pairs = [[grid[0][0],grid[2][0]] , [grid[1][0],grid[1][2]], [grid[1][1],grid[1][3]]]
if any(1 for pair in pairs if sum(map(int,pair)) != 7):
    print("degenerate")
elif right_handed[key] in grid[1]*2:
    print("right-handed")
else:
    print("left-handed")
