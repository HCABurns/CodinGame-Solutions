# Parse times.
times = []
n = int(input())
for i in range(n):
    h,m,s = map(int,input().split(":"))
    times.append([h,m,s])

# Sort times.
times.sort()

# Print shortest time.
print(":".join([str(i).zfill(2) for i in times[0]]))
