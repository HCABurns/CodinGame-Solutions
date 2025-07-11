import sys
sys.setrecursionlimit(100000)

# Memorization and counter for ways to reach r.
memo = {}
total = [0]

# Get the value.
r = int(input())

# DFS with memorization to find ways to reach r.
def dfs(v):
    
    if v in memo:
        total[0] += memo[v]
        return memo[v]
    
    if total[0] > 1:
        return True
    
    if v == r:
        total[0] += 1
        return True
    
    if v > r:
        return False
    
    res = dfs(v + sum([int(i) for i in str(v)]))
    memo[v] = res
    return res

# Complete rivers until ended or 2 different ways to reach r are found.
for i in range(1,r):
    if total[0] == 2:break
    dfs(i)

# Output YES if more than 1 way to reach r, otherwise NO.
print("NO" if total[0] < 2 else "YES")
