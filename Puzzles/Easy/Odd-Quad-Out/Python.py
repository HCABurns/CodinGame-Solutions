# Get dimension of grid.
side_size = int(input())
mid = side_size // 2

# Get sums of the four quadrants.
sums = [0,0,0,0]
placement = 0
for i in range(side_size):
    if i==mid:
        placement+=2
    row = input()
    sums[placement] += sum([int(val) for val in row[:mid] if val.isnumeric()])
    sums[placement+1] += sum([int(val) for val in row[mid:] if val.isnumeric()])
    
# Form hashmap and sort based on count.
numbers = sorted({val:sums.count(val) for val in sums}.items(),key=lambda x:x[1])

# Output the correct values.
print(f"Quad-{sums.index(numbers[0][0])+1} is Odd-Quad-Out\nIt has value of {numbers[0][0]}\nOthers have value of {numbers[1][0]}")
