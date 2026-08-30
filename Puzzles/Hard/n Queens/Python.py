# Get size of the board.
n = int(input())

def validQueen(row, col, board):
    min_val = min(row, col)
    nr = row - min_val
    nc = col - min_val
    count = 0
    for pos in range(nr*n+nc, n*n, n+1):
        count += board & (1 << pos) != 0

    min_val = min(n-col-1, row)
    nr = row - min_val
    nc = col + min_val
    for pos in range(nr*n+nc, n*n, max(1,n-1)):
        count += board & (1 << pos) != 0
    return count <= 2


# DFS to find possible solutions - with bitmask for the grid
def solve(board, row, columns): 
    
    if row == n:
        return 1

    solutions = 0
    for col in [i for i in range(n) if columns & (1 << i) == 0]:
        pos = row*n + col
        board ^= (1 << (pos))
        if validQueen(row, col, board):
            solutions += solve(board, row+1, columns | 1 << col)
        board ^= (1 << (pos))
    return solutions

# Print number of possilbe combinations.
print(solve(0, 0, 0))
