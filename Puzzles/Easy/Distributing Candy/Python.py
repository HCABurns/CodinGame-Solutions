# Get bags of sweets and sort in increasing order.
n, m = map(int,input().split())
sweets = sorted([int(sweet) for sweet in input().split()])

# Output minimum difference between m sweet bags.
print(min([sweets[i+m-1] - sweets[i] for i in range(n-m+1)]))
