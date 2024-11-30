# Required imports.
import math
import heapq

# Create maxheap.
nums = []
k = int(input())
n = int(input())
for i in range(n):
    value, rate = [int(j) for j in input().split()]
    nums += [[-value ,rate]]

# Create variables to store which resources are on cooldown.
to_add = []
wait = []
wait2 = []

# Select largest value k times.
resources = 0
for i in range(k):
    nums.sort(reverse=True)
    # Get max value.
    value,rate = nums.pop() if nums else [0,-100]

    # Increment resources amount.
    resources += value * -1

    # Add available item after replenishment.
    for value , rate in to_add:
        nums.append([value, rate])

    # Move collect resources down a stage.
    to_add, wait, wait2 = wait, wait2, []

    # Add updated value to waitlist.
    if value != 0:
        wait2 = [[-math.floor(abs(value)/100*rate),rate]]

# Output max resources amount.
print(resources)
