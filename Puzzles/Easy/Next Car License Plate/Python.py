# Get inputs.
x = input()
n = int(input())

# Parse input.
a,b,c = x.split("-")
b = int(b)
a = list(a)
c = list(c)

# Complete the sequence to find the next plate.
while n > 0:
    # If b not 999, increment to 999 otherwise max.
    if b != 999:
        d = min(999-b, n)
        b += d
        n -= d
    else:
        # Set middle to 001 and increment C.
        b = 1
        if c != ["Z","Z"]:
            if c[-1] != "Z":
                c[-1] = chr(ord(c[-1])+1)
            else:
                c[-1] = "A"
                c[0] = chr(ord(c[0])+1)
        else:
            # Set C to AA and increment A.
            c[0] , c[-1] = "A", "A"
            if a[-1] != "Z":
                a[-1] = chr(ord(a[-1])+1)
            else:
                a[-1] = "A"
                a[0] = chr(ord(a[0])+1)
        n-=1

# Print the plate.
print(f'{"".join(a)}-{str(b).zfill(3)}-{"".join(c)}')
