# Get inputs.
l = int(input())
n = int(input())

# Get bot positions.
val = [int(i) for i in input().split()]

#Max time is for a furthest box from the end to reach the end.
print(max(l-min(val), max(val)))
