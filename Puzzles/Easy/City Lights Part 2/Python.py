from collections import defaultdict

grids = defaultdict(list)
swapper = {c:v for v,c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ",start = 10)} | {v:c for v,c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ",start = 10)} | {".":0}
sources = []

w = int(input())
h = int(input())
l = int(input())
n = int(input())

idx = 0
i = 0
for _ in range(n):
    s = input()
    w = len(s)
    if w < 1:
        idx+=1
        i = 0
        continue
    for j,char in enumerate(s):
        if char != ".":
            sources.append([idx,i,j, int(char) if char.isdigit() else ord(char) - ord("A") + 10])
    grids[idx].append(list([swapper[c] if not c.isnumeric() else int(c) for c in s]))
    i += 1
    
# Define new brightness.
for k in range(l):
    for i in range(h):
        for j in range(w):
            for z,y,x,radius in sources:
                if y==i and j==x and k == z:continue
                #print(k,i,j)
                grids[k][i][j] += max(0, radius - round(((i-y)**2 + (j-x)**2 + (k-z)**2)**0.5))

# Output new brightness grid.
outputs = []
for grid in grids:
    outputs += [[]]
    for row in grids[grid]:
        outputs[-1] += ["".join([str(char) if char < 10 else min(chr(ord("A")+char-10),"Z") for char in row])+"\n"]
    outputs[-1] = "".join(outputs[-1])
print("\n".join(outputs).strip())
