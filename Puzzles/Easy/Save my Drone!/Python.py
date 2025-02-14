# Hashmap for storing parts of the ship.
ship_components = {"#":"Block","^":"Thruster","@":"Gyroscope","+":"Fuel","§":"Core"}

# Get ship dimension and rotation.
x = int(input())
y = int(input())
r = int(input())

# Form ship - Only relevant components.
ship = ""
for _ in range(y):
    ship += "".join([i for i in input() if i in ship_components])

# Rotate ship if required.
if r == 1:
    ship = ship[::-1]

# Variable required.
out = []
prev = ""
j = 0

# Perform RLE on the data with only interest in the ship components
while j < len(ship):
    count = 1
    prev = ship[j]
    j+=1
    while j < len(ship) and ship[j] == prev:
        if ship[j] == prev:
            count+=1
        j += 1

    if prev in ship_components:
        out += [" ".join([str(count) , ship_components[prev] + ["","s"][count > 1]])]
   

# Print the ship contents if a ship if found, otherwise 'Nothing'.
if len(out):
    print(", ".join(out))
else:
    print("Nothing")
