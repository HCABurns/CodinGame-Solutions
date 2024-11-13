# Get counters and store in array as 2D array.
counters = []
l, h = [int(i) for i in input().split()]
for val in range(h):
    numeral = input()
    for j in range(0,len(numeral),l):
        if len(counters) != len(numeral)//l:
            counters.append([])
        counters[j//l].append((numeral[j:j+l]))

# Get input Mayan numbers and convert Mayan to decimal (base 10).
s1 = int(input())
number1 = 0
for val in range(s1//l , 0 , -1):
    number1 += (counters.index([input() for _ in range(h)]))* (20**(val-1))

s2 = int(input())
number2 = 0
for val in range(s2//l , 0 , -1):
    number2 += (counters.index([input() for _ in range(h)]))* (20**(val-1))

# Compute result using given operator.
operator = input()
result = int(eval(f"{number1}{operator}{number2}"))

# Convert decimal back to base 20.
mayan_number = []
if result == 0:
    mayan_number = [0]
else:
    while result > 0:
        mayan_number = [result % 20] + mayan_number
        result //= 20 

# Output the Mayan representation of the output.
for val in mayan_number:
    print(*[value for value in counters[val]],sep="\n")
