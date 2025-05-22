# Get inputs.
number = int(input())
d = int(input())

# Find the largest value divisible by d by removing 0-2 digits.
largest = 0

# Remove 0 digits
if number % d == 0:
    largest = number

num = str(number)
# Remove 1 or 2 digits
for i in range(0,len(num)):
    for j in range(0,len(num)-1):
        new_num = (num[:i] + num[i+1:])
        if int(new_num) % d == 0:
            largest = max(largest, int(new_num))
        new_num = int(new_num[:j] + new_num[j+1:])
        if new_num % d == 0:
            largest = max(largest, new_num)

# Print the largest value.
print(largest)
