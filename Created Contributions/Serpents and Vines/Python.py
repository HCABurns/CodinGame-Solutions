from collections import deque

serpents = {}
vines = {}

height, width = [int(i) for i in input().split()]
n = int(input())
serpent_amount, vine_amount = [int(i) for i in input().split()]
for i in range(serpent_amount):
    top, bottom = [int(j) for j in input().split()]
    vines[top] = bottom
for i in range(vine_amount):
    head, tail = [int(j) for j in input().split()]
    serpents[head] = tail

pos = 1
goal = height*width

queue = deque([[pos,0,()]])
cache = {}
checked = 0
while queue:
    checked += 1
    pos,moves,route = queue.popleft()
    if pos in cache and cache[pos] <= moves:
        continue
    cache[pos] = moves

    if pos == goal:
        #print(route)
        continue

    for i in range(1,n+1):
        new_pos = pos+i
        if new_pos > goal:
            continue
        if new_pos in serpents:
            queue.append([serpents[new_pos],moves+1,route+(i,)])
        elif new_pos in vines:
            queue.append([vines[new_pos],moves+1,route+(i,)])
        else:
            queue.append([new_pos, moves+1,route+(i,)])

print(cache[goal])
