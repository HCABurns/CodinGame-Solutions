# Store the circles in an array.
circles = []
for i in range(int(input())):
    x, y, z, r = [int(j) for j in input().split()]
    circles += [[x,y,z,r]]

# Increase size in order read in until it touches another circle.
radius_cubed = 0
for i,c in enumerate(circles):
    x,y,z,r = c
    smallest_change = 1e6
    for j,circle in enumerate(circles):
        # Ensure not checking with own circle.
        if i==j:continue
        
        # Find distance remaining between circles.
        x2, y2, z2, r2 = circle
        remaining_distance = ((x-x2)**2 + (y-y2)**2 + (z-z2)**2) ** 0.5 - r - r2

        # Store the smallest change in radius required.
        if remaining_distance < smallest_change:
            smallest_change = remaining_distance

    # Update radius and store the cubed of the radius.
    circles[i][-1] += smallest_change
    radius_cubed += circles[i][-1] ** 3

# Print sum of radii cubed.
print(round(radius_cubed))
