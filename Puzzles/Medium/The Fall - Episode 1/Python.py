# Form Grid.
w, h = [int(i) for i in input().split()]
grid = []
for i in range(h):
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    grid += [line.split(" ")]
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# Define Direction and their associated words.
directions = [(1,0),(0,1),(0,-1)]
direction_words = "DOWN RIGHT LEFT".split()
direction = "DOWN"

# Define the move direction of the rooms.
rooms = {f"{i}":{} for i in range(0,14)}
rooms["1"] = {"DOWN":(1,0),"LEFT":(1,0),"RIGHT":(1,0)}
rooms["2"] = {"LEFT":(0,-1),"RIGHT":(0,1)}
rooms["3"] = {"DOWN":(1,0)}
rooms["4"] = {"DOWN":(0,-1), "LEFT":(1,0)}
rooms["5"] = {"DOWN":(0,1), "RIGHT":(1,0)}
rooms["6"] = {"LEFT":(0,-1),"RIGHT":(0,1)}

rooms["7"] = {"LEFT":(1,0),"DOWN":(1,0)}
rooms["8"] = {"LEFT":(1,0),"RIGHT":(1,0)}
rooms["9"] = {"RIGHT":(1,0),"DOWN":(1,0)}
rooms["10"] = {"DOWN":(0,-1)}
rooms["11"] = {"DOWN":(0,1)}
rooms["12"] = {"LEFT":(1,0)}
rooms["13"] = {"RIGHT":(1,0)}

# Move until the end goal.
while True:
    # Get current coords.
    inputs = input().split()
    xi = int(inputs[0])
    yi = int(inputs[1])
    pos = inputs[2]

    # Find the room value.
    room = grid[yi][xi]
    
    # Find the direction to go and change direction if needed.
    y,x = rooms[room][direction]
    direction = direction_words[directions.index((y,x))]

    # Coordinates to move to.
    print(xi+x, yi+y)
