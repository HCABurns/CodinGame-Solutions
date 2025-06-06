# Get the inputs.
r = input()
l = int(input())

# Define the sequence.
seq = [[r]]

# Complete Conway Sequence to line L.
for i in range(l-1):
    out = []
    prev = seq[-1][0]
    count = 0
    for c in seq[-1]:
        if c == prev:
            count += 1
        else:
            out.append(str(count))
            out.append(prev)
            count = 1
        prev = c

    if count > 0:
        out.append(str(count))
        out.append(seq[-1][-1])
    seq += [out]
            
# Print the Lth line.
print(" ".join(seq[-1]))
