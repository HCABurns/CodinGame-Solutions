# Get number of tasks and tasks. Store start and end date.
n = int(input())
tasks = []
for i in range(1,n+1):
    j, d = [int(j) for j in input().split(" ")]
    tasks.append([j,j+d-1])

# Sort based on start and end date.
tasks.sort(key = lambda x : (-x[1],-x[0]))

# Count how many tasks are completed after itself.
seen = set()
after = 0
t2 = []
for s,e in tasks:
    if e not in seen:
        after+=1
    seen.add(e)
    t2.append([after,s,e])

# Find the maxiumum number of tasks and print result.
tasks = sorted(t2,key = lambda x : (-x[0],-x[1],-x[2]))
day = 0
counter = 0
for _,s,e in tasks:
    if s > day:
        day = e
        counter += 1
print(counter)
