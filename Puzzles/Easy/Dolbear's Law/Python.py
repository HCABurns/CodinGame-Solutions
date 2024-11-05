# Get inputs.
t = 0
together = []
m = float(input())

# Calculate N60
for i in range(int(m)):
    line = list(map(float,input().split(" ")))
    secs = len(line)*4
    t += (10 + (sum(line) - 40) / 7 )
    [together.append(i) for i in line]

# Print N60 average.
print(f"{t/m:.1f}")

# If 5<N60<30, print N8 avarage.
if 5<t/m<30:
    t = j = 0
    while j < len(together) - 1:
        t += together[j] + together[j+1] + 5
        j += 2
    print(f"{(t/(len(together)//2)):.1f}")
