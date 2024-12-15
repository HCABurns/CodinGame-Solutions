# Required imports.
from math import floor
import heapq

# Create maxheap.
heap = []
k = int(input())
assert k>=1 and k<=999999, f"{k}: K is out of range"
n = int(input())
assert n>=1 and n<=1500, f"{n}: N is out of range"
for i in range(n):
    value, rate = [int(j) for j in input().split()]
    assert value>=1 and value<=10000, f"{value}: Value is out of range"
    assert rate>=0 and rate<=100, f"{rate}: Rate is out of range"
    heap += [[-value ,-rate]]
heapq.heapify(heap)

# Test to ensure all rows have been read (check n is the correct number)
while True:
    try:
        input()
        raise AssertionError
    except AssertionError:
        assert False, f"More than {n} rows in the input"
    except:
        break

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
        heapq.heappush(replenish, [i+3, -floor(abs(value)/100*-rate),rate])

# Output number of resources collected.
print(resources)
