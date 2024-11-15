# Form hashmap of hashmaps using given ranges and values.
maps = {}
n = int(input())
for i in range(n):
    r , vals = input().split("=")
    idx , ra = r.split("[")
    ra , _ = ra.split("]")
    lb , _ , rb = ra.split(".") 
    vals = vals.strip().split(" ")
    maps[idx] = {}
    for j,val in zip(range(int(lb), int(rb)+1),vals):
        maps[idx][str(j)] = val

# Get inputs and convert to only useful information. Val is starting index, stack is order of searching.
stack = input()
val = "".join(i for i in stack if i.isnumeric() or i == "-")
stack=stack.replace(val,"").split("[")[:-1][::-1]

# Find and print value using maps.
for idx in stack:
    val = maps[idx][val]
print(val)
