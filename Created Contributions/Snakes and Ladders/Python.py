#Actual code.
from collections import deque

# For hashmap of serpents and vines.
snakes = {}
ladders = {}
width, height = [int(i) for i in input().split()]
n = int(input())
snake_amount, ladder_amount = [int(i) for i in input().split()]
for i in range(snake_amount):
    head, tail = [int(j) for j in input().split()]
    snakes[head] = tail
for i in range(ladder_amount):
    top, bottom = [int(j) for j in input().split()]
    ladders[bottom] = top

# Define starting tile and goal tile.
pos, goal= 1, height*width

# Complete BFS to find the shorted number of die throws to reach the final tile.
queue = deque([[pos,0]])
visited = set()
moves = -1
while queue:
    pos,moves = queue.popleft()
    if pos == goal:
        break

    if pos in visited:
        continue
    visited.add(pos)

    for i in range(1,n+1):
        new_pos = pos+i
        if new_pos > goal:
            continue
        if new_pos in snakes:
            queue.append([snakes[new_pos],moves+1])
        elif new_pos in ladders:
            queue.append([ladders[new_pos],moves+1])
        else:
            queue.append([new_pos, moves+1])

# Print shortest die throws to reach the final tile.
print(moves)
