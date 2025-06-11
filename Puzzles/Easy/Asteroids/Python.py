import math

# Get the inputs.
w, h, t1, t2, t3 = [int(i) for i in input().split()]

# Create array for before, after and empty output.
before = []
after = []
grid = [list("."*w) for _ in range(h)]

# Form the arrays.
for i in range(h):
    first_picture_row, second_picture_row = input().split()#
    before += [first_picture_row]
    after += [second_picture_row]

# Convert to string for searching.
before = "".join(before)
after = "".join(after)

# Form hashamp of asteroids and their position in the string.
pos = {char:pos for pos,char in enumerate(before) if char != "."}

# Move each asteroid to position it should be at t3.
for char,pos in sorted(pos.items(), reverse = True):
    # Convert string positions to 2d grid positions. 
    i1, j1 = pos // w, pos % w
    pos2 = after.index(char)
    i2, j2 = pos2 // w, pos2 % w

    # Find the position at t3.
    d = t2 - t1
    new_i = i1 + math.floor((i2 - i1)*((t3-t1)/d))
    new_j = j1 + math.floor((j2 - j1)*((t3-t1)/d))

    # Add the asteroid at position at t3 if in "sky" region.
    if 0<= new_i < h and 0<= new_j < w:
        grid[new_i][new_j] = char

# Output the grid.
print(*["".join(i) for i in grid], sep = "\n")
