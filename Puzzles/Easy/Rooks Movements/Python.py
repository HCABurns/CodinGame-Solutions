# Create hashmap to store pieces positions.
pieces = {}

# Hashmaps for converting alpha representation to position and visa versa.
position = {chr(char):value for char,value in zip(range(97,108),range(8,0,-1))}
position_reversed = {value:chr(char) for char,value in zip(range(97,108),range(7,-1,-1))}

# Get starting location and convert from alphabetical representation to position.
starting_pos = input()
x,y = map(lambda x : int(position.get(x,x))-1,starting_pos)

# Get pieces and fill grid.
nb_pieces = int(input())
for i in range(nb_pieces):
    inputs = input().split()
    colour = int(inputs[0])
    x1 , y1 = map(lambda x : int(position.get(x,x))-1,inputs[1])
    #grid[y1][x1] = colour
    pieces[(y1,x1)] = colour

# Store starting position in tmp variables and create array to store moves.
tmp_x, tmp_y = x, y
moves = []

# Direction pairs for vertical and horizontal moves.
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# Check in all directions for valid moves, store in moves array if valid.
for dx, dy in directions:
    x, y = tmp_x + dx, tmp_y + dy
    while 0 <= x < 8 and 0 <= y < 8:
        if pieces.get((y,x),None) == 1:
            moves.append(f"R{starting_pos}x{position_reversed[x]}{y + 1}")
            break
        elif pieces.get((y,x),None) == 0:
            break
        else:
            moves.append(f"R{starting_pos}-{position_reversed[x]}{y + 1}")
        x += dx
        y += dy

# Print moves in lexicographical ASCII order.
for i in sorted(moves):
    print(i)
