#Import pi constant.
from math import pi

# Get length of dough and size of circle.
side, diameter = [float(i) for i in input().split()]

# Calculate wasteful bakers amount.
wasteful = (side // diameter) ** 2

# Calculate frugal bakers amount.
frugal = 0
area = side**2
while side > diameter:
    # Calculate amount possible to be cut.
    amount = ((side//diameter)**2)//1
    frugal += amount
    # Convert wasted into a new dough rectangle.
    area -= amount * (pi*(diameter/2)**2)
    side = area**0.5

# Output the difference between frugal and wasteful.
print(int(frugal - wasteful))
