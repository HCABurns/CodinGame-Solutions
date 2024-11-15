# Get size.
n = int(input())

# Print top half 
for i in range(1,n+1):
    if i == 1:
        print("." + " "*(2*n-i-1) + "*"*(2*i-1))
    else:
        print(" "*(2*n-i) + "*"*(2*i-1))

# Print bottom half
for i in range(1,n+1):
    left = " "*(n-i) + "*"*(2*i-1)
    right = "*"*(2*i-1)
    print(left + " "*(2*(n-i)+1) + right)
