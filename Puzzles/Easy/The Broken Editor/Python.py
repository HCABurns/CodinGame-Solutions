#NOTE: Not the best time complexity solution but as input size <= 80 it 
# Get input.
typed_keys = input()

# Create array for storing chars.
stack = []

i = 0
for char in typed_keys:
    # Reset bounds if out-of-bounds.
    if i < 0:
        i=0
    if i > len(stack):
        i = len(stack)
    
    # Place charater in the correct position, or remove correct charater.
    if char not in "<>-":
        stack.insert(i,char)
        i = i + 1
    else:
        if char == "<":
            i-=1
        elif char == ">":
            i+=1
        else:
            if i != 0:
                stack.pop(i-1)
                i-=1

# Output the result.
print("".join(stack))
