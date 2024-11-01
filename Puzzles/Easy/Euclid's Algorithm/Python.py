# Get values to be used to find GCD.
a, b = [int(i) for i in input().split()]
a_start , b_start = a,b

# Continue until remainder is 0.
while b!=0:
    print(f"{a}={b}*{a//b}+{a%b}")
    a , b = b , a%b

# Output the GCD of a and b.
print(f"GCD({a_start},{b_start})={a}")
