# Get the value and set the remainder.
n = int(input())
remainder = 1

# Array for storing ints, hashmap for storing index and index.
res = []
values = {}
idx = 0

# Complete the divison until terminates or repeat found.
while remainder != 0:
    # Check for repeating remainder.
    if remainder in values:
        res.insert(values[remainder], "(")
        res.append(')')
        break
    values[remainder] = idx

    # Complete the division.
    remainder *= 10
    val = remainder // n
    res.append(str(val))
    remainder = remainder % n

    # Increment index variable.
    idx += 1

# Print the value.
print(f"0.{''.join(res)}")
