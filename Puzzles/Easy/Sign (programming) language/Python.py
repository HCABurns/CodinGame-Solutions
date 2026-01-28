"""
Apply an operation to the register using the given value.

Return int - The value in the register.
"""
def process(register, operation, value):
    if operation == "/$":
        register += value
    elif operation == "//":
        register -= value
    elif operation == "/**":
        register *= (value+1)
    elif operation == "/*/":
        register *= (-1*value)
    return register

operations = set(["/$","//","/*/","/**"])
program = input()
stack = []
operation = None
instructions_count_required = 0
instructions_count = 0
register = 0
for char in program:
    # End the operation and apply the value.
    if char == "/" and operation:
        register = process(register, operation, len(stack))
        if instructions_count_required == 1:
            instructions_count += 1
        operation = None
        stack = []
        continue
    
    # Special case operation.
    if not operation and not stack and char == "$":
        if instructions_count_required == 1:
            register += instructions_count
        instructions_count = 0
        instructions_count_required ^= 1
        continue
    
    # Add to stack and check for operations.
    stack.append(char)
    stack_str = "".join(stack)
    if stack_str == "/*$":
        instructions_count += 1
        stack = []
    elif stack_str in operations:
        operation = stack_str 
        stack = []

# Print the value in the register.
print(register)
