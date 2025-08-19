import re

# Get cleaned input.
s = []
n = int(input())
for i in range(n):
    line = re.sub('".*"', "",input())
    s+=[line]
s = "\n".join(s)

# Regular brackets pair checker.
pairing = {"(":")", "{":"}","[":"]"}
stack = []
brackets = False
for char in s:
    if char in ")}]":
        if not stack or pairing.get(stack.pop(),"W") != char:
            stack.append("ERROR")
            break
    elif char in "({[":
        brackets = True
        stack.append(char)

# Correct output.
if stack:
    print("Invalid")
elif brackets:
    print("Valid")
else:
    print("No brackets")
