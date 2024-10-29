# Get value to be checked.
n = gets.to_i

# Create Fibonacci sequence until next value is larger than n.
fib = [1 , 1]
while n>fib[-1] + fib[-2]
    fib << fib[-1] + fib[-2]
end

# Find Zeckendorf representation by picking largest available number until sum is n.
out = []
i = fib.size-1
while n > 0
    if n - fib[i] >= 0
        out << fib[i]
        n -= fib[i]
    end
    i-=1
end

# Output the representation.
puts out.join("+")
