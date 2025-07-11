# Get requests
n = int(input())
reqs = []
for i in range(n):
    request = input()
    reqs += [request]

# Get crates
crates = []
for i in range(n):
    crate = input()
    crates += [crate] 


# Find which crate corresponds to which request.
for box in reqs:
    for idx,crate in enumerate(crates , start = 1):
        if len(box) != len(crate):continue
        chars1 = {}
        chars2 = {}
        valid = True
        for c1, c2 in zip(crate.lower(),box.lower()):
            if c1 not in chars1 and c2 not in chars2:
                chars1[c1] = c2
                chars2[c2] = c1
            elif c1 not in chars1 or c2 not in chars2:
                valid = False
            else:
                if chars1[c1] != c2 or chars2[c2] != c1:
                    valid = False
        if valid:
            print(idx)
            break
