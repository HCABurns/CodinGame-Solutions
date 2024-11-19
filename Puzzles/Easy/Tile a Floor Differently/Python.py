# Get grid size and form grid.
quarter_size = int(input())
grid = []
for row in range(quarter_size):
    row = input()
    grid.append(row)

def swapper(string,direction):
    """
    Helper function to convert a quadrant of the tile.

    Parameters:
    string : str - String to be transformed.
    direction : int - 0 indicates horizontal transformation, 1 indicates vertical transformation.

    Return: string - Transformed string with required swaps.
    """
    if direction == 0:
        chars = {"/":"\\","b":"d","p":"q", "d":"b","q":"p" , "\\":"/"}
    else:  
        chars = {"/":"\\","b":"p","d":"q","p":"b","q":"d" ,"\\":"/" }
    chars = {ord(i):chars[i] for i in chars.keys()}
    return string.translate(chars)

# Print border.
print("+"+ "-"*len(grid[0]*2) + "+" + "-"*len(grid[0]*2) + "+")

# Create the top half and then the bottom half.
for _ in range(2):
    
    # Leave the TOP LEFT and horizontally flip the row for TOP RIGHT.
    new_grid = []
    for row in grid:
        TL = "".join(row)
        TR = "".join(swapper(row,0)[::-1])
        new_row = TL+TR
        new_grid += ["|"+ new_row +"|" + swapper(new_row[::-1],0)+"|"]

    # Vertical flip for BOTTOM LEFT and Vertical and Horizontal flip for BOTTOM RIGHT.
    for row in grid[::-1]:
        BL = "".join(swapper(row,1))
        BR = "".join(swapper(swapper(row,0),1)[::-1])
        new_row = BL + BR
        new_grid += ["|"+new_row+"|" +swapper(new_row[::-1],0)+"|"]

    # Print the half of the grid that has been formed.
    for row in new_grid:
        print(row)
    
    # Print splitter.
    print("+"+ "-"*len(grid[0]*2) + "+" + "-"*len(grid[0]*2) + "+")
