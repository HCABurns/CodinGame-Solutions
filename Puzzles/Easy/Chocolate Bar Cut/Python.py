import math

# Get inputs.
n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]

    # Find GCD.
    gcd = math.gcd(x,y)
    x //= gcd
    y //= gcd

    # Apply formula and print.
    print((x+y-1) * gcd)
