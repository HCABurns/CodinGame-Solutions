# Directions array and current direction.
directions = [(-1,0),(0,-1,),(1,0),(0,1)]
current_direction = 0

# Form Grid
n = int(input())
grid_size = n
grid =  [[" "for j in range(n)] for i in range(n)]

# Index of the grid.
i = j = n-1

# Value of bottom left
n **=2

# Check Ulam spiral for primes.
while n > 1:
    # Determine if prime.
    prime = True
    test_n = n
    for k in range(2,(test_n+1)//2+1):
        if test_n % k == 0:
            prime = False
            break
    
    # Set as prime or seen.
    if prime:
        grid[i][j] = "#"
    else:
        grid[i][j] = "X"

    # If next is OOB or already visited then change direction.
    x, y = directions[current_direction]
    if j+x < 0 or j+x>=grid_size or i+y<0 or i+y>=grid_size or grid[i+y][j+x] != " ":
        current_direction = (current_direction+1)%4
        x, y = directions[current_direction]
    i += y
    j += x
    n -= 1

# Print grid - Replace seen with space character.
for row in grid:
    print(" ".join([i if i != "X" else " " for i in row]))
