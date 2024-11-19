# Get heights of the segments.
n = int(input())
height = [int(i) for i in input().split()]

# Left and right pointers.
l = 0
r = len(height) - 1

# Max size variable.
max_area = 0

# Shift left and right pointers to find max area.
while l < r:
    size = min(height[l],height[r]) * (r - l)
    max_area = max(max_area , size)
    if height[l] > height[r]:
        r -= 1
    else:
        l += 1

# Output the max area.
print(max_area)
