#NOTE: Coordinates in the form [y,x] / [i,j] / [row,column]
# From array of array. Each array will store items position and direction.
# Also store amount of starting items.
directions = {">":[0,1],"<":[0,-1],"^":[-1,0],"v":[1,0]}
h, w = [int(i) for i in input().split()]
items = []
for i in range(h):
    for j,char in enumerate(input()):
        if char != ".":
            items.append([[i,j],directions[char]])
items_count = len(items)

# Simulation loop.
time = 0
while items_count > 0:
    # Move all items in correct direction - Including wrapping.
    for item in items:
        if item != "":
            item[0][1] += item[1][1]
            item[0][0] += item[1][0]
            item[0][1] %= w
            item[0][0] %= h

    # Check for matches and remove (Just set to "" for better efficiency).
    items_to_remove = {}
    for i,item in enumerate(items):
        if item == "":
            continue
        pos = (item[0][0],item[0][1])
        if pos not in items_to_remove:
            items_to_remove[pos] = i
        else:
            items[i] = ""
            items_count -= 1
            if items[items_to_remove[pos]] != "":
                items[items_to_remove[pos]] = ""
                items_count -= 1
    
    # Increment time counter.
    time+=1

# Output total running time.
print(time)
