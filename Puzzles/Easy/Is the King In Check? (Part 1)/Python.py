# Get board and store position of pieces that aren't the king.
pieces = []
board = []
for i in range(8):
    board += [[]]
    chess_row = input().replace(" ", "")
    for j,char in enumerate(chess_row):
        if char in set("BNRQ"):
            pieces.append((char,i,j))
        board[-1] += [char]

def is_check(start_i, start_j, directions):
    """
    Function to check if the king piece is in check.

    Parameters:
    start_i : int - Integer for row of the piece.
    start_j : int - Integer for column of the piece.
    directions : array - Array of array of directions to be checked. 

    Returns : boolean - True if the king is in check, otherwise false.
    """
    if board[start_i][start_j] == "K":return True
    for di, dj in directions:
        i = start_i
        j = start_j
        while i + di >= 0 and i + di < 8 and j + dj >= 0 and j + dj < 8:
            i += di
            j += dj
            if board[i][j] == "K":return True
            if abs(di) == 2 or abs(dj) == 2:break
    return False

# Check each piece for if the king is in check.
check = False
for char, i, j in pieces:
    if char == "Q":
        if is_check(i,j,[[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,1],[1,-1],[-1,1]]):check=True;break
    elif char == "R":
        if is_check(i,j,[[-1,0],[1,0],[0,-1],[0,1]]):check=True;break
    elif char == "B":
        if is_check(i,j,[[-1,-1],[1,1],[1,-1],[-1,1]]):check=True;break
    elif char == "N":
        if is_check(i,j,[[-2,1],[-2,-1],[-1,2],[-1,-2],[1,2],[1,-2],[2,-2],[2,-2]]):check=True;break

# Print if the king is in check or not.
print(["No Check","Check"][check])
