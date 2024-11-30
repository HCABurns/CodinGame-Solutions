# Required imports.
import math
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

# Create variables to store which resources are on cooldown.
to_add = []
wait = []
wait2 = []

# Select largest value k times.
resources = 0
for i in range(k):
    # Get max value.
    value,rate = heapq.heappop(heap) if heap else [0,-100]

    # Increment resources amount.
    resources += value * -1

    # Add available item after replenishment.
    for replenished_value, replenished_rate in to_add:
        heapq.heappush(heap, [replenished_value, replenished_rate])

    # Move collect resources down a stage.
    to_add, wait, wait2 = wait, wait2, []

    # Add updated value to waitlist.
    if value != 0:
        wait2 = [[-math.floor(abs(value)/100*-rate),rate]]

# Output max resources amount.
print(resources)
