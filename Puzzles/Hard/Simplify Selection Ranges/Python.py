# Get numbers and find ranges.
n = sorted(map(int,input()[1:-1].split(",")))
ranges = []
idx = 0
while idx < len(n):
    min_val = n[idx]
    max_val = 0
    while idx != len(n)-1 and n[idx]+1 == n[idx+1]:
        max_val = n[idx+1]
        idx+=1
    if max_val != 0 and max_val - min_val > 1:
        ranges.append([range(min_val,max_val+1) , f"{min_val}-{max_val}"])
    idx += 1

# Find the largest 3 ranges.
ranges = sorted(ranges , key = lambda x : -len(x[0]))[:3]
f = set()
for r in ranges:
    for i in r[0]:f.add(i)

# Build the output.
ignore = set()
out = []
for i in n:
    if i in ignore:continue
    if i not in f:
        out.append(str(i))
    else:
        for r in ranges:
            if i in r[0]:
                out.append(r[-1])
                for k in r[0]:
                    ignore.add(k)
                break

# Print.
print(",".join(out))
