# Required import
from math import pi

# Arrays for sotring information.
planets = []
alice = []

# Get all inputs, calculate density and store required information.
n = int(input())
for i in range(n):
    # Get inputs.
    name, r, m, c = input().split()

    # Convert to float. (removes e)
    r = float(r)
    m = float(m)
    c = float(c)

    # Set planet details to correct location.
    if name == "Alice":
        alice = [r , (m/((4/3)*pi*r**3))]
    else:
        planets.append([c, r, (m/((4/3)*pi*r**3)), name])

# Sort based on distance.
planets.sort(key = lambda x:x[0])

# Print the closest planet name that will not be disintergrated by Alice.
for i in planets:
    roche = alice[0] * (2 * alice[1] / i[2])**(1/3)
    if i[0] >= roche:
        print(i[-1])
        break
