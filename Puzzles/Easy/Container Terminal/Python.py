# Get inputs length.
n = int(input())
for i in range(n):
    # Container for stacks and get order of shipping contains.
    stacks = []
    line = input()

    # Place the containers in stacks - Placing it on top of any that are before it in the order
    # otherwise start a new stack.
    for char in line:
        place = -1
        for i,stack in enumerate(stacks):
            if not stack or ord(stack[-1]) >= ord(char):
                place = i
                break
        
        if place == -1:
            stacks.append([char])
        else:
            stacks[i].append(char)

    # Print the number of stacks required.
    print(len(stacks))
