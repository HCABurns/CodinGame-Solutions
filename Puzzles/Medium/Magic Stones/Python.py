# Get numbers.
n = int(input())
nums = sorted([int(i) for i in input().split()])

# Perfrom greedy algorithm until no more magic used.
stack = []
magic_used = True
while magic_used:
    magic_used = False
    for level in nums:
        if stack and stack[-1] == level:
            stack.pop()
            stack.append(level+1)
            magic_used = True
        else:
            stack.append(level)
    nums = sorted(stack)
    stack = []

# Print smallest number of stones possible.
print(len(nums))
