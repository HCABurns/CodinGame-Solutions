# Get value to be checked.
n = int(input())

# Create Fibonacci sequence until next value is larger than n.
fib = [1 ,1]
while fib[-1] + fib[-2] < n:
    fib.append(fib[-1] + fib[-2])

# Find Zeckendorf representation by picking largest available number until sum is n.
out = []
i = len(fib)-1
while n > 0:
    if n - fib[i] >= 0:
        n -= fib[i]
        out.append(str(fib[i]))
    i-=1

# Output the representation.
print("+".join(out))
