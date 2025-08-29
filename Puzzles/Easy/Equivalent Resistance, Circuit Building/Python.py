# Get resistance.
res = {}
n = int(input())
for i in range(n):
    inputs = input().split()
    name = inputs[0]
    r = int(inputs[1])
    res[name] = r

# Create stack and split.
stack = []
circuit = input().split()

# Go through input and backtrack to sum series or parallel
for char in circuit:
    if char.isalpha() and char not in res:continue
    if char not in "])":
        stack.append(char)
    elif char == ")":
        sum_val = 0
        while stack:
            c2 = stack.pop()
            if c2 == "(":break
            if c2 in res:
                sum_val += res[c2]
            else:
                sum_val += c2
        stack.append(sum_val)
    else:
        sum_val = 0
        while stack:
            c2 = stack.pop()
            if c2 == "[":break
            if c2 in res:
                sum_val += 1/res[c2]
            else:
                sum_val += 1/c2
        stack.append(1/sum_val)

# Print circuit resistance.
print(f"{stack[0]:0.1f}")
