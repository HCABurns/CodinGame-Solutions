# Get number of inputs.
n = int(input())

# Create array of house positions in a tuple.
arr = []
for i in range(n):
    x, y = [int(j) for j in input().split()]
    arr.append((x,y))

# Get median position of houses in Y-axis.
main_cableY = sorted(arr,key= lambda x:x[1])[len(arr)//2][1]

# Find length of cable in X-Axis. (difference between max and min of X-Axis)
cable_length = max([i for i,_ in arr]) - min([i for i,j in arr])

# Calculate the extra cable needed to connect the house from the main cable.
for i,vals in enumerate(arr):
    cable_length += abs(main_cableY - vals[1])

# Print output.
print(cable_length)
