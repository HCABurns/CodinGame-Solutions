# Dictionary for converting direction to character.
chars = {"right":">", "left":"<"}

# Get input information.
direction, *info = input().split()
amount, height, width, spacing, indent = map(int,info)

# Print the 'turn here sign'.
for i in range(*[[height],[height//2, height+height//2]][direction=="left"]):
    print((" "*indent * (i if i<height/2 else abs(height - i - 1))) + (" "*spacing).join([chars[direction]*width for _ in range(amount)]))
