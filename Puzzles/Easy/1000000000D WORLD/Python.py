# Convert input into integers.
a = list(map(int,input().split(" ")))
b = list(map(int,input().split(" ")))

# Set up total and two pointers.
i = 0
j = 0
total = 0

# Dot Product Loop.
while i<len(a) and j <len(b):
    # Get value and amount of the next values.
    a_val = a[i+1]
    a_count = a[i]

    b_val = b[j+1]
    b_count = b[j]

    # Increment the total by the dot product of a and b.
    # Multiply the dot product by the minumum count of a and b.
    # E.g. a = [4, 4, 4] b = [5, 5, 5] A•B = 4*5+4*5+4*5 ≡ (4*5)*3
    min_count = min(a_count , b_count)
    total += a_val * b_val * min_count

    # Adjust counts.
    a[i] -= min_count
    b[j] -= min_count

    # Move onto next value pair if required.
    if a_count == 0:
        i+=2
    if b_count == 0:
        j+=2

# Output the total dot product.
print(total)
