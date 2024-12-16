# Get beam.
beam = input()

# Find pivot position.
pos = beam.find("^")

# Variables for storing clockwise and anti-clockwise moments.
anti_clockwise = 0
clockwise = 0

n = int(input())
for i in range(n):
    # Get name and mass.
    box_identifier, mass = input().split()
    weight = float(mass) * 9.81
    if beam.find(box_identifier) < pos:
        anti_clockwise += weight * (pos-beam.find(box_identifier))
    else:
        clockwise +=  weight * (beam.find(box_identifier)-pos)

# Round to 2dp. 
anti_clockwise = round(anti_clockwise , 2)
clockwise = round(clockwise , 2)

# Print direction
if anti_clockwise == clockwise:
    print("BALANCED")
elif anti_clockwise > clockwise:
    print("ANTI-CLOCKWISE")
else:
    print("CLOCKWISE")

# Print moments.
print(f"{abs(anti_clockwise-clockwise):.2f}N")
