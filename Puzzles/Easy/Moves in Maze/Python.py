#NOTE: Coordinates are formed as [y,x] / [Row , column]
w, h = [int(i) for i in input().split()]

#Form grid in 2d array and store position of "S" in start
grid = []
start = []
for i in range(h):
    row = input()
    grid.append([i for i in row])
    if "S" in row:
        start = [i, row.find("S")]
        grid[i][start[1]] = "."

#Iterative BFS changing any . characters to the next in the sequence
to_visit = [start]
val = 0
while to_visit:
    tmp = []
    while to_visit:
        node = to_visit.pop()
        #Wrap the value (Wraps around the grid)
        x = node[1]%w
        y = node[0]%h
        #If spot is empty -> Add to the list and set to current character in sequence
        if grid[y][x] == ".":
            grid[y][x] = str(val) if val < ord("A") else chr(val)
            tmp.append([y+1,x])
            tmp.append([y-1,x])
            tmp.append([y,x-1])
            tmp.append([y,x+1])
    #Update to_visit list and character in the sequence
    to_visit = tmp
    val+=1
    if val == 10:
        val=ord("A")

#Print out the changed grid
for i in grid:
    print("".join(i))
