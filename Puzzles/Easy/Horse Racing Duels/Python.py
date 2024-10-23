# Get inputs
n = int(input())
arr = [int(input()) for i in range(n)]
# Sort array on horse power.
arr.sort()

# Define min difference.
diff = 99999999999999
# Check adjacent horses power and store minimum difference.
for i in range(len(arr)-1):
    diff = min(arr[i+1]-arr[i],diff)

# Output minimum distance
print(diff)
