from math import ceil
# Form Grid
grid = [["{}" for i in range(19)]for i in range(25)]

# Perform the instructions of mowing, plating or plant and mowing on the grid.
for instruction in input().split():
    # Determine values from the instruction.
    radii = int("".join([i for i in instruction if i.isnumeric()]))/2
    j,i = [ord(c) - ord("a") for c in instruction if c.isalpha()][-2:]
    symbol = None
    if "PLANTMOW" in instruction:
        symbol = None
    elif "PLANT" in instruction:
        symbol = "{}"
    else:
        symbol = "  "

    # Complete operation on any value inside the given circle.
    rounded_radii = ceil(radii)
    for y in range(max(0,i-rounded_radii) , min(len(grid),i+rounded_radii)):
        for x in range(max(0,j-rounded_radii) , min(len(grid[0]),j+rounded_radii)):
            dist = ((y-i)**2 + (x-j)**2)**0.5
            if dist <= radii:
                if symbol:
                    grid[y][x] = symbol
                else:
                    grid[y][x] = ["{}","  "][grid[y][x] == "{}"]

# Output the crop circle.
for row in grid:
    print("".join(row))
