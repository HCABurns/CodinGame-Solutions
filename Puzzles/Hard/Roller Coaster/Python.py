from collections import deque

# Populate queue
queue = deque([])
l, c, n = [int(i) for i in input().split()]
for i in range(n):
    pi = int(input())
    queue.append([pi,i])

# Form required variables.
cache = {}
total = 0
rounds = 0
found = False
totals = {0:0}
start_idx = 0

# Perform Simulation.
while c > 0:
    
    # Check cache for cycle detected
    if start_idx in cache:
        # If first time finding, simulate loops as many times as possible.
        if not found:
            cycle_len = rounds - cache[start_idx][2]
            cycle_amount = c // cycle_len
            cycle_gain = total - totals[cache[start_idx][2]]
            total += cycle_gain * cycle_amount
            c %= cycle_len
            found = True
        # Perform remaining cached simulations
        if c > 0:
            c -= 1
            total += cache[start_idx][0]
            start_idx = cache[start_idx][1]
        
    else:
        # Add to the ride until full or can't add again and cache result.
        ride_capacity = 0
        idxs = []
        local = 0
        while queue[0][0] + ride_capacity <= l and queue[0][1] not in idxs:
            val, idx = queue.popleft()
            ride_capacity += val
            queue.append([val,idx])
            local += val
            idxs += [idx]
        total += local
        cache[start_idx] = [local, (idxs[-1]+1) % n, rounds]
        start_idx = (idxs[-1]+1) % n
        rounds += 1
        totals[rounds] = total
        c -= 1

print(total)

