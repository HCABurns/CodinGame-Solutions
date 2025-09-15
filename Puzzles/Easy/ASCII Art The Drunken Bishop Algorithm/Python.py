# Define starting grid.
height = 9
width = 17
grid = [[0 for i in range(width)] for i in range(height)] 

# Define the moves, mapper, moves and the output swapper.
fingerprint = input().split(":")
mapper = {ord(str(i)):i for i in range(10)} | {ord(c):ord(c)-ord("a")+10 for c in "abcdef"}
moves = {"00":[-1,-1],"01":[-1,1],"10":[1,-1], "11":[1,1]}
swapper = {i:c for i,c in zip(range(15)," .o+=*BOX@%&#/^")}

# Starting location.
i = 4
j = 8

# Simulate the moves.
for chars in fingerprint:
    for char in chars[::-1]:
        value = bin(mapper[ord(char)])[2:].zfill(4)

        c1 = value[:2]
        c2 = value[2:]
        
        for (y,x) in [moves[c2], moves[c1]]:
            if 0<=i+y<height and 0<=j+x<width:
                grid[i+y][j+x] += 1
                i += y
                j += x
            elif 0<=i+y<height:
                grid[i+y][j] += 1
                i += y
            elif 0<=j+x<width:
                grid[i][j+x] += 1
                j += x
            else:
                grid[i][j] += 1

# Print the grid.
grid[4][8] = "S"
grid[i][j] = "E"
print("+---[CODINGAME]---+")
for row in grid:
    print("|"+"".join([swapper[char%15] if type(char) == int else char for char in row ]) +"|")
print("+-----------------+")

