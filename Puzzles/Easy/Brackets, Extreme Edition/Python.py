# Get input.
expression = input()

# Declare required inputs.
pairs = {"}":"{","]":"[",")":"("}
inputs = {"{":1 , "[":1 , "(":1 , "}":1 , "]":1 , ")":1}
stack = []
valid = True

for char in expression:
    # If char not a bracket -> ({[ then move on to next character
    if char not in inputs :
        continue

    # Check if char is a closing bracket or not.
    if char in pairs:
        # If no character on stack or top of stack doesn't pair with char
        # set valid to false and break loop.
        if len(stack) == 0 or stack.pop() != pairs[char]:
            valid = False
            break
    else:
        # Add open bracket to the stack.
        stack.append(char)

# Output true if valid otherwise false
if len(stack) != 0:
    valid = False
print("true" if valid else "false")
