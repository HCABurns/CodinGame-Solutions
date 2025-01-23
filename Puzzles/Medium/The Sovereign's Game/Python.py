# Required imports.
from math import floor
import heapq

# Create maxheap.
heap = []
k = int(input())
n = int(input())
for i in range(n):
    value, rate = [int(j) for j in input().split()]
    heap += [[-value ,-rate]]
heapq.heapify(heap)

# Create empty heap to store which resources are on cooldown.
replenish = []

# Select largest value k times.
resources = 0
for i in range(k):
    # Get max value.
    value,rate = heapq.heappop(heap) if heap else [0,-100]

    # Increment resources amount.
    resources += value * -1

    # Add item after replenishment cooldown, if exists.
    if replenish and replenish[0][0] == i:
        _,replenished_value, replenished_rate = heapq.heappop(replenish)
        heapq.heappush(heap, [replenished_value, replenished_rate])

    # Add updated value to replenish cooldown heap.
    if value != 0:
        heapq.heappush(replenish, [i+3, -floor(abs(value)*-rate/100),rate])

# Output number of resources collected.
print(resources)
