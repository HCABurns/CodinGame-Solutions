# Get inputs and store loads in array. (Sort loads for better efficiency)
n = int(input())
k = int(input())
servers = list(map(int,input().split()))
servers.sort()

# Define required variables.
idx = 0
additional = 0
remainder = 0

# Continue until all same length or no more to add.
while k > 0 and idx<len(servers)-1:
    # Get difference and increment idx.
    diff = servers[idx+1] - servers[idx]
    idx+=1
    # If all minimums can be incremented to next unique minimum, do it.
    if k > idx * diff:
        for j in range(idx):
            servers[j] += diff
            k -= diff
    else:
        # Add 1 to a item if remainder exists.
        additional = k // idx
        if additional!=0 and k % additional > 0:
            servers[0] += 1
        # Increment all 
        for j in range(idx):
            servers[j] += additional
        k = 0

# Add remainder to first if needed.
additional = k // idx
if additional!=0 and k % additional > 0:
    servers[-1] += 1

# Output the minimum difference.
print(max(servers) - min(servers) + remainder)
