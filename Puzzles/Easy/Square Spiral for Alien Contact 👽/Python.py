# Get the relevant information from the input.
size, start, direction, a, b = input().split(" ")
size = int(size)
grid = [[" " for i in range(size)] for i in range(size)]
start = {"topRight":[0,size-1],"topLeft":[0,0],"bottomLeft":[size-1,0],"bottomRight":[size-1,size-1]}[start]

directions = [
    [[0,1],[1,0],[0,-1],[-1,0]], #clock - RDLU
    [[0,-1],[1,0],[0,1],[-1,0]]][direction == "counter-clockwise"]
direction = 0 if start in [[0,size-1],[0,0]] else 2

a_char, a_quantity = a[0], int("".join([str(i) for i in a if i.isnumeric()]))
b_char, b_quantity = b[0], int("".join([str(i) for i in b if i.isnumeric()]))

diff = b_quantity - a_quantity
char_diff = ord(b_char) - ord(a_char)

# Create stack of characters and quantity.
stack = [a_char for i in range(a_quantity)]

chars = 0
i , j = start
invalid = 0
corners = 0
while True:
    # If invalid of current and previous turn, no valid move so end loop.     
    if invalid == 2:
        break

    # Find the next direction to go and check for completed loop.
    y,x = directions[direction]
    check_x , check_y = x * 2, y * 2
    
    # If 2 moves ahead if a non space character, need to rotate!
    if i+check_y < size and i+check_y >= 0 and j+check_x < size and j+check_x >= 0 and grid[i+check_y][j+check_x] != " ":
        invalid += 1
        direction = (direction+1) % 4
        continue
    
    # If current position plus next is invalid, need to turn.
    if i+y >= size or i+y < 0 or j+x >= size or j+x < 0:
        direction = (direction+1) % 4
        continue

    # Valid move is possible, get the next character, or update stack if required.
    invalid = 0
    if len(stack) == 0:
        chars += 1
        next_char = chr(ord(a_char) + char_diff*chars)
        if next_char > "Z" or next_char < "A":
            break
        stack = [next_char for _ in range(a_quantity + (diff * chars))]
    char = stack.pop(0)

    # Update character and move position.
    grid[i][j] = char
    i += y
    j += x

# Add the final character if possible.
if len(stack) > 0:
    next_char = stack.pop(0)
else:
    chars += 1
    next_char = chr(ord(a_char) + char_diff*chars)
grid[i][j] = next_char if next_char <= "Z" and next_char >= "A" else " "

# Print the grid.
for row in grid[:min(31,size)]:
    print("".join(row[:min(31, size)]))
