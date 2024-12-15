# Get plank.
plank = input()

# Find pivot position.
pos = plank.find("^")

# Variables for storing clockwise and anti-clockwise moments.
anti_clockwise = 0
clockwise = 0

n = int(input())
for i in range(n):
    # Get name and mass.
    box_name, mass = input().split()
    weight = float(mass) * 9.81
    if plank.find(box_name) < pos:
        anti_clockwise += weight * (pos-plank.find(box_name)+1)
    else:
        clockwise +=  weight * (plank.find(box_name)-pos+1)

# Round to 2dp. 
anti_clockwise = round(anti_clockwise , 2)
clockwise = round(clockwise , 2)

# Print direction
if anti_clockwise == clockwise:
    print("BALANCED")
elif anti_clockwise < clockwise:
    print("ANTI-CLOCKWISE")
else:
    print("CLOCKWISE")

# Print moments.
print(f"{abs(anti_clockwise-clockwise):.2f}N")
