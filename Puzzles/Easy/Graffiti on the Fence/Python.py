# Get inputs.
l = int(input())
n = int(input())

# Form invalid ranges.
invalid = []
for i in range(n):
    st, ed = [int(j) for j in input().split()]
    invalid += [[st, ed]]

# Sort and merge if required.
invalid.sort()
merged = []
for interval in invalid:
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])

# Print the correct output.
start = 0
for pair in merged:
    if start != pair[0]:
        print(start,pair[0])
    start = pair[1]

if merged[-1][-1] != l and len(merged) != 0:
    print(start, l)

if len(merged) == 0 or len(merged) == 1 and merged[-1][-1] == l and merged[0][0] == 0:
    print("All painted")
