# arrays for storing coordinates and custom order.
coordinates = []
custom_order = []

# Get custom order.
d = int(input())
n = int(input())
for i in input().split():
    _ord = int(i)
    custom_order += [_ord - 1]

# Order coordinates based on custom order in index_order.
for i in range(n):
    # Get coordinates in original position.
    vals = []
    for j in input().split():
        coord = int(j)
        vals += [coord]

    # Change order based on custom order.
    perm = []
    for j in custom_order:
        perm += [vals[j]]
    coordinates.append((perm, i))

# Sort.
coordinates.sort()

# Print indexes of topology space sorted in custom order.
print(" ".join([str(i+1) for _,i in coordinates]))
