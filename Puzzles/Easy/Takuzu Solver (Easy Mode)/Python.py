# Get input grid.
out = []
dots = 0
n = int(input())
for i in range(n):
    row = input()
    out += [list(row)]
    dots += row.count(".")

# Complete checks insuring no repeating characters 3 times.
while dots > 0:
    for i in range(n):
        for j in range(n-2):
            tmp = [out[i][j],out[i][j+1],out[i][j+2]]
            if tmp.count("1") == 2 and "." in tmp:
                out[i][j+tmp.index(".")] = "0"
                dots -= 1
            if tmp.count("0") == 2 and "." in tmp:
                out[i][j+tmp.index(".")] = "1"
                dots -= 1

    for i in range(n-2):
        for j in range(n):
            tmp = [out[i][j],out[i+1][j],out[i+2][j]]
            if tmp.count("1") == 2 and "." in tmp:
                out[i+tmp.index(".")][j] = "0"
                dots -= 1
            if tmp.count("0") == 2 and "." in tmp:
                out[i+tmp.index(".")][j] = "1"
                dots -= 1

# Print result.
for i in range(0,n):
    print("".join(out[i]))
