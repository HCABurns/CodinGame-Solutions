# Get inputs and build array of bar sizes.
m = int(input())
n = int(input())
arr = []
for i in input().split():
    bar = int(i)
    arr += [bar]

# Variable to store information. (Note in array to be mutable in the function.)
max_size = [0]
max_path = [[]]

# DFS to find the longest length of bars < m with < n bars.
def search(i, sumVal, path):
    if len(path) > n:
        return

    if sumVal > m:
        return

    if sumVal > max_size[0] or max_size[0] == sumVal and len(path) < len(max_path[0]):
        max_size[0] = sumVal
        max_path[0] = path

    for j,val in enumerate(arr[i:],start = i):
        search(j+1, sumVal + val, path+[val])

# Search and print.
search(0,0,[])
print(*max_path[0])
