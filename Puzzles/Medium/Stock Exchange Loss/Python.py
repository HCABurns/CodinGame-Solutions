# Get required input
n = int(input())

# Create array of stock positions
arr = [int(i) for i in input().split()]

# Set required variables.
maxLoss = 0
min1 = arr[0]
for i in range(len(arr)-1):

    #If current value is minimum, find the next minimum.
    if arr[i] == min1:
        min1 = min(arr[i+1:])

    # Calculate the loss.
    v = min1-arr[i]

    # Set new max loss if loss is greater than current loss.
    if v < maxLoss:
        maxLoss = v

# Output the max loss
print(maxLoss)
