from collections import defaultdict

# Array for storing order and hashmap for storing quantity.
order = []
seen = defaultdict(int)

# Get input and append + if required.
expression = input().replace(" ","")
if expression[0].isnumeric():
    expression = "+"+expression

# Store order and quanity from input.
for i in range(0,len(expression),2):
    op = expression[i:i+2]
    if op not in order:
        order.append(op)
    seen[op] += 1

# Print the instructions in order.
for op in order:
    if seen[op] > 1:
        print("REPEAT" , seen[op])
    prefix = "ADD" if op[0]=="+" else "SUB"
    print(prefix,"cgx",op[1])
print("EXIT")
