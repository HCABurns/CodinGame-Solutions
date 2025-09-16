# Get number of networks.
m = int(input())
for i in range(m):
    # Parse network.
    b,s = input().split("/")
    s = int(s)
    a,b,c,d = map(lambda x : bin(int(x))[2:].zfill(8),b.split("."))
    address = a+b+c+d

    # Find if valid or not.
    valid = False if any(True if i=="1" else False for i in address[s:]) else True

    # Print result.
    if valid:
        print("valid",2**(32-s))
    else:
        print(f"invalid {int(a,2)}.{int(b,2)}.{int(c,2)}.{int(d,2)}/{32-address[::-1].index('1')} {2**(address[::-1].index('1'))}")

