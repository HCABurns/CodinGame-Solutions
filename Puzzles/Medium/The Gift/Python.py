# Get number of participants and cost of the gift.
n = int(input())
c = int(input())

# Form an array of each persons budget.
nums = []
for i in range(n):
    b = int(input())
    nums += [b]

# Ensure the gift is not too expensive.
if sum(nums) < c:
    print("IMPOSSIBLE")
    quit()

# Sort from highest to lowest budget and store array for storing contribution.
nums.sort()
contributions = [0 for i in range(n)]

# Take 1 unit from everyone until the gift is paid for.
while c > 0:
    for i in range(n-1,-1,-1):
        if c == 0:
            break
        if nums[i] != 0:
            contributions[i] += 1
            nums[i] -= 1
            c-=1

# Print the contributions.
for i in contributions:
    print(i)
