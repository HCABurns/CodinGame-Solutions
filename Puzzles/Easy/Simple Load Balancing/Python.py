# Get inputs and store loads in array. (Sort loads for better efficiency)
n = int(input())
k = int(input())
start = list(map(int,input().split()))
start.sort()

# Define required variables.
idx = 0
additional = 0
remainder = 0

# Continue until all same length or no more to add.
while k > 0 and idx<len(start)-1:
    # Get difference and increment idx.
    diff = start[idx+1] - start[idx]
    idx+=1
    # If all minimums can be incremented to next unique minimum, do it.
    if k > idx * diff:
        for j in range(idx):
            start[j] += diff
            k -= diff
    else:
        # Add 1 to a item if remainder exists.
        additional = k // idx
        if additional!=0 and k % additional > 0:
            start[0] += 1
        # Increment all 
        for j in range(idx):
            start[j] += additional
        k = 0

# Add remainder to first if needed.
additional = k // idx
if additional!=0 and k % additional > 0:
    start[-1] += 1

# Output the minimum difference.
print(max(start) - min(start) + remainder)
