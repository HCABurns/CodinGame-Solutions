# Import math for ceilling division.
import math

# Get required inputs.
value_to_reach = int(input())
n = int(input())

# Get coins and put into a sorted array in increasing order. 
coins = [[float(value),int(count)] for count,value in zip(input().split(),input().split())]
coins.sort()

# Find the minimum coins required to reach value_to_reach.
#To do this go from the least value coins increasing until value is met or no more coins left.
total = 0
for value, count in coins:
    # Value is too large and needs only a proportion of the coins left.
    if value_to_reach - count*value < 0:
        total += math.ceil(value_to_reach/value)
        value_to_reach = -1
    else:
        #Value is too big still so add all the coins with this value
        value_to_reach -= count*value 
        total += count

# Print correct output.
if total>0 and value_to_reach<0:
    print(total)
else:
    print("-1")
