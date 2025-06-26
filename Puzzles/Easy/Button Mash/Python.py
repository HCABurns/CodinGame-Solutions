from collections import deque

# Get target value.
n = int(input())

# Complete a BFS until target is found.
queue = deque([[1,1]])
seen = set()
while queue:
    value, presses = queue.popleft()

    # Print number of pressed if target reached.
    if value == n:
        print(presses)
        quit()

    # Prune useless branches.
    if value > n+10 or value < 0:
        continue

    # Add to the queue.
    for val in [value-1, value*2, value+1]:
        if val not in seen:
            queue.append([val,presses+1])
            seen.add(val)
