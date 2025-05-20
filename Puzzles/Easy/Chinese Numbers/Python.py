# Array of numbers in a single string form.
values = [
"*000*0***00***00***0*000*",
"**********00000**********",
"00000***************00000",
"00000******000******00000",
"000000*0*000*000***000000",
"00000**0***0000**0*000000",
"**0****0**00000*0*0*0***0",
"**0****0**00000**0****000",
"*0*0**0*0**0*0**0*0*0***0",
"**0****0**0000**0*0*0**00",
]

# read the input and store each section of the numbers in the correct array.
nums = []
for i in range(5):
    s = input().split(" ")

    if len(nums) == 0:
        for i in range(len(s)):
            nums.append([])
    
    for j, char in enumerate(s):
        nums[j] += [char]

# Combine the sections of the numbers and print the representative value.
for number in nums:
    print(end = str(values.index("".join(number))))
