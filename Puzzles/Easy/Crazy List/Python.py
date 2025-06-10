# Get inputs list.
crazylist = list(map(int,input().split(" ")))

# Find the difference between them.
a = [i-j for i,j in zip(crazylist[1:],crazylist)]

if len(a) > 1 and a[0] != a[1]:
    # Multiplication sequence. 
    d = a[1] // a[0]
    print(crazylist[-1] + a[-1]*d)
else:
    # Add/Subtract - a+(n)*d
    print(crazylist[0] + (len(crazylist))*a[0])
