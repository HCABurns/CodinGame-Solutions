# Required import.
import math

# Get information.
small_radius, large_radius, glass_height, beer_vol = [float(i) for i in input().split()]

# Set test height and current volume
test_height = 0.001
current_volume = 1e9

while abs(current_volume - beer_vol) > 0.1:
    # Calculate large_radius at the current height h
    test_large_radius = small_radius + (large_radius - small_radius) * (test_height / glass_height)
    
    # Calculate the volume up to height h
    current_volume = (math.pi * test_height / 3) * (small_radius**2 + small_radius * test_large_radius + test_large_radius**2)

    # Increment test height
    test_height += 0.0001

# Print the height of the liquid in the glass.
print(round(test_height,1))
