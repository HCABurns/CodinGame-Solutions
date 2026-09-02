from collections import deque

# Get buckets and the target.
target = int(input())
containers_count = int(input())
buckets = []
for i in range(containers_count):
    buckets.append(int(input()))

# Perform BFS to find the minimum moves to get the target.
queue = deque([((0,) * len(buckets), 0)])
seen = {(0,) * len(buckets)}
while queue:
    state, moves = queue.popleft()
    ## Goal state.
    if target in state:
        print(moves)
        break

    # Simulate the 3 actions: fill, empty, pour
    for i, capacity in enumerate(buckets):
        # Fill bucket
        new_state = list(state)
        new_state[i] = capacity
        new_state = tuple(new_state)

        if new_state not in seen:
            seen.add(new_state)
            queue.append((new_state, moves + 1))

        # Empty bucket
        new_state = list(state)
        new_state[i] = 0
        new_state = tuple(new_state)
        if new_state not in seen:
            seen.add(new_state)
            queue.append((new_state, moves + 1))

        # Pour bucket i into bucket j
        for j, capacity_j in enumerate(buckets):
            if i == j:
                continue
            amount = min(state[i], capacity_j - state[j])
            new_state = list(state)
            new_state[i] -= amount
            new_state[j] += amount
            new_state = tuple(new_state)
            if new_state not in seen:
                seen.add(new_state)
                queue.append((new_state, moves + 1))
