# Array for storing the first and second value for fizz, buzz and fizzbuzz.
f = [-1,-1]
b = [-1,-1]
fb = [-1,-1]

# Storing the values and the first value seen with its index.
nums = []
first_value = [-1,-1]

# Read in the values storing the first value seen and the first and second fizz, buzz and fizzbuzz.
n = int(input())
i = 1
for _ in range(n):
    line = input()

    # Store the first numeric value and it's position.
    if all(1 if char.isnumeric() else 0 for char in line) and first_value == [-1, -1]:
        first_value = [int(line),i]

    nums += [line]
    if line == "Fizz":
        if f[0] == -1:
            f[0] = i
        elif f[1] == -1:
            f[1] = i
    
    elif line == "Buzz":
        if b[0] == -1:
            b[0] = i
        elif b[1] == -1:
            b[1] = i
    
    elif line == "FizzBuzz":
        if fb[0] == -1:
            fb[0] = i
        elif fb[1] == -1:
            fb[1] = i
    i+=1

# Calculate the values for fizz, buzz and fizzbuzz - if available.
fizz = None
buzz = None
fizzbuzz = None
if f[1] != -1:
    fizz = abs(f[1] - f[0])
elif f[0] != -1:
    fizz = first_value[0] - first_value[1] + nums.index("Fizz") + 1
if b[1] != -1:
    buzz = abs(b[1] - b[0])
elif b[0] != -1:
    buzz = first_value[0] - first_value[1] + nums.index("Buzz") + 1
if fb[1] != -1:
    fizzbuzz = abs(fb[1] - fb[0])

# Calcualte any missing value and print the value for fizz and buzz.
# Fizz and Buzz available
if fizz and buzz:
    print(fizz ,buzz)
# Fizz and FizzBuzz:
elif fizz and fizzbuzz:
    print(fizz , fizzbuzz // fizz)
# Buzz and FizzBuzz:
elif buzz and fizzbuzz:
    print(fizzbuzz // buzz , buzz)
# Only Fizzbuzz:
else:
    print(fizzbuzz, fizzbuzz)
