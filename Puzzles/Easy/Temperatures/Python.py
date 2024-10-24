# Get size and print and return if size is 0.
if input() == "0":
    print(0)
    quit()

# Map value to integer and append a tuple of (x*-x , x)
# x*-x is used as it will make the smallest numbers the largest.
# i.e -1*1 = -1, 4*-4 = -16. Thus we can use this to find the value
# that are closest to 0. A tuple is used to store it's original state to
# differentiate between positive and negatives.
arr = []
for i in map(int,input().split()):
    arr.append((i*-i,i))

# Sort array using .sort(): .sort on tuple defaults by sorting first value then second value.
# This will ensure that positive values are chosen over negative values.
arr.sort(reverse = True)

# Print correct output.
print(arr[0][1])
