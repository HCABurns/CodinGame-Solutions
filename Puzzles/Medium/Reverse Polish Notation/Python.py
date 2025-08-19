# Function to apply an operation to the popped valuess.
def apply(stack,op):
    v1 = stack.pop()
    v2 = stack.pop()
    return eval(str(v2)+op+str(v1))

# Define stack.
stack = []
n = int(input())
for instruction in input().split():
    try:
        # Check if the next instruction is a number - If so add otherwise perform instruction.
        int(instruction)
        stack.append(instruction)
    except:
        try:
            # Perform correct instruction.
            if instruction == "ADD":
                stack.append(apply(stack,"+"))
            elif instruction == "MUL":
                stack.append(apply(stack,"*"))
            elif instruction == "SUB":
                stack.append(apply(stack,"-"))
            elif instruction == "DIV":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(v2) // int(v1))
            elif instruction == "MOD":
                stack.append(apply(stack, "%"))
            elif instruction == "POP":
                stack.pop()
            elif instruction == "DUP":
                stack.append(stack[-1])
            elif instruction == "SWP":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v1)
                stack.append(v2)
            elif instruction == "ROL":
                val = stack.pop()
                seen = []
                for i in range(int(val)):
                    seen.append(stack.pop())
                seen = [seen[-1]] + seen[:-1]
                while seen:
                    stack.append(seen.pop())
        except:
            # Add an error and quit loop.
            stack.append("ERROR")
            break

# Print the final stack.
print(*[str(i) for i in stack])
