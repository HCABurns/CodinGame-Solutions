from collections import deque

# Get inputs.
a = input().split(" ")

# Find direction for males and females
f = -1 if a[0] == "m" else 1
m = -1 if a[0] == "f" else 1

# Form the goal state.
w = len(a)
goal = [i for i in a[::-1]]

queue = deque([[a, [" ".join(a)]]])
while queue:
    board, moves = queue.popleft()
    ## Goal state.
    if board == goal:
        print(*moves,sep="\n")
        break

    # Simulate jumps, ensuring the female jump is first.
    for i in range(w):
        if board[i] == "s":continue
        if board[i] == "m" and len(moves) > 1:
            if i+m >= 0 and i+m < w and board[i+m] == "s":
                new = [x for x in board]
                new[i], new[i+m] = new[i+m] , new[i]
                queue.append([new, moves+[" ".join(new)]])
            elif i+m+m >= 0 and i+m+m < w and board[i+m+m] == "s":
                new = [x for x in board]
                new[i], new[i+m+m] = new[i+m+m], new[i] 
                queue.append([new, moves+[" ".join(new)]])
        else:
            if i+f >= 0 and i+f<w and board[i+f] == "s":
                new = [x for x in board]
                new[i], new[i+f] = new[i+f] , new[i]
                queue.append([new, moves+[" ".join(new)]])
            elif i+f+f >= 0 and i+f+f < w and board[i+f+f] == "s":
                new = [x for x in board]
                new[i], new[i+f+f] = new[i+f+f], new[i] 
                queue.append([new, moves+[" ".join(new)]])


