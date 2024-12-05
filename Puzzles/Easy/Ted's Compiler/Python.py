# Get input.
line = input()

# Define stack and int variable to hold number of matching (prefix only)
stack = []
longest_valid = 0

# Count pairs and end if invalid.
for char in line:
    if char == "<":
        stack += ["<"]
    else:
        if len(stack) == 0:
            break
        else:
            if stack.pop() == "<":
                longest_valid += 2

# Output longest valid prefix length. 
print(longest_valid)
