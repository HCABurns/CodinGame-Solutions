# Get number.
n = int(input())

# Set values.
t = 5
pk = 2
k = 3

# Find combinations.
combs = set()
for a in range(n // t + 1): 
    for b in range(min(n // pk + 1, a+1)): 
        for c in range(n // k + 1):
            total = a*t + b*pk + c*k
            if total > n:
                break
            if total == n:
                combs.add((a, b, c))
# Sort and display results
for comb in sorted(combs):
    print(*comb)

"""
# All combinations recursive approach
combs = []
cache = set()
def combs(vals):
    a,b,c = vals
    if a*t + b * pk + c * k > n or vals in cache or b > a:
        return 
    elif (a*t + b * pk + c * k) == n:
        cache.add(vals)
    else:
        combs((a+1,b,c))
        combs((a,b+1,c))
        combs((a,b,c+1))
combs((0,0,0))
cache = sorted(list(cache))
for i in cache:
    print(*i)
"""
