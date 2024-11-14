# Get input and convert \n to new lines, and convert to list for malleable strings.
s = [list(i) for i in input().split("\\n")]

# Hashmap for checking new inserts are in correct location.
added = {}

# Get number of changes to make.
change_count = int(input())
for i in range(change_count):
    # Get change and convert ints. 
    line, idx, change = input().split("|")
    line , idx = map(int, [line, idx])       

    # Find out how many additions have been made before current id to ensure added to correct location.
    to_change = sum([1 if val < idx else 0 for val in added.get(line,[])])
    
    # Insert string correct location.
    s[line].insert(idx+to_change,change)

    # Update hashamp but new additons index on the correct line.
    if line not in added:
        added[line] = []
    added[line]+=[idx]

# Output the new string with the inserts.
print(*"\n".join(["".join(j) for j in s]).split('\\n'),sep="\n")
