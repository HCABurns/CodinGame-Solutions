# Read in the height to be achieved.
n = int(input())

# Cache for memoization.
cache = {}
def search(height, next_step):
    # Goal Case
    if height == n:
        return 1

    # End Case
    if height > n:
        return 0
    
    # Check if in cache or not.
    if (height,next_step) in cache:
        return cache[(height,next_step)]

    # Check the next steps.
    ways = 0
    for i in range(next_step+1, n-height+1):
        ways += search(height+i, i)

    # Cache and return the ways to reach n from current positon.
    cache[(height,next_step)] = ways
    return ways

# Find number of ways to built increasing staircase to height n.
ways = search(0,0)

# Print number of ways. (-1 for invalid single brick route)
# Saves O(l) where l is number of ways to build stairs with more than 1 brick.
print(ways - 1)
