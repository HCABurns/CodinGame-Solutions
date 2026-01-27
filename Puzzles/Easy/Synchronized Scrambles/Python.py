# Get offset and split to be hours and minutes.
offset1, offset2 = input().split()
h1,m1 = int(offset1[1:3]), int(offset1[3:])
h2,m2 = int(offset2[1:3]), int(offset2[3:])

# Convert to standard time.
if offset1[0] == "-":
    time1 = [([-h1- [0,1][m1 > 0],-1][h1 == 0])%24, (60-m1)%60]
else:
    time1 = [h1%24,m1]

if offset2[0] == "-":
    time2 = [([-h2 - [0,1][m2 > 0],-1][h2 == 0])%24, (60-m2)%60]
else:
    time2 = [h2%24,m2]

# Find all valid synchronized scrambles.
valid = []
seen = 0
max_seen = 60*24-1
while seen != max_seen:
    v1 = sorted([i for i in f"{time1[0]:02d}" + f"{time1[1]:02d}"])
    v2 = sorted([i for i in f"{time2[0]:02d}" + f"{time2[1]:02d}"])
    if v1 == v2:
        valid.append(", ".join(([f"{time1[0]:02d}" + f"{time1[1]:02d}" , f"{time2[0]:02d}" + f"{time2[1]:02d}"])))

    # Increment timer.
    time1[1]+=1
    time2[1]+=1
    if time1[1] == 60:
        time1[0] = (time1[0]+1) % 24
        time1[1] = 0
    if time2[1] == 60:
        time2[0] = (time2[0]+1) % 24
        time2[1] = 0
    seen += 1

# Print valid pairs.
for pair in sorted(valid):
    print(pair)
