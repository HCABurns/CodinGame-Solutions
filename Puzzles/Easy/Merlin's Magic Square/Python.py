# Get inputs and form grid.
row_1 = input().split()
row_2 = input().split()
row_3 = input().split()
all_buttons_pressed = input()

grid = [row_1, row_2, row_3]

# Define the swap hashmap and the moves when a button is pressed.
swap = {"~":"*","*":"~"}
coords = {"1":[[0,0],[0,1],[1,0],[1,1]],
"2": [[0,0],[0,1],[0,2]],
"3": [[0,2],[0,1],[1,2],[1,1]],
"4": [[0,0],[1,0],[2,0]],
"5": [[0,1],[1,1],[1,0],[1,2],[2,1]],
"6": [[2,2],[1,2],[0,2]],
"7": [[2,0],[2,1],[1,0],[1,1]],
"8": [[2,2],[2,1],[2,0]],
"9": [[2,2],[2,1],[1,2],[1,1]]}

def press(button):
    for i,j in coords[button]:
        grid[i][j] = swap[grid[i][j]]

# Perform the already pressed buttons.
for char in all_buttons_pressed:
    press(char)

# Try all the buttons and check which button cause the goal state.
# Note: Pressing the same button twice will revert to previous state.
for char in "123456789":
    press(char)
    if grid == [["*","*","*"],["*","~","*"],["*","*","*"]]:
        print(char)
    press(char)
