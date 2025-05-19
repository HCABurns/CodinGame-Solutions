# Required import.
import copy

# Get number of inequalities.
n = int(input())

# Creat empty Graph and hashmap for converting chars to values..
bigger = [[] for i in range(26)]
converter = {}
val = 0
for i in range(n):
    # Read in and convert inquality.
    a,b = input().split(" > ")
    if a not in converter:
        converter[a] = val
        val+=1
    if b not in converter:
        converter[b] = val
        val+=1
    a, b = converter[a], converter[b]
    
    # Verify the inequality is true or not.
    valid = False
    if len(bigger[a]) > 0 or len(bigger[b]) > 0: 
        to_check = copy.deepcopy(bigger[a])
        checked = set()
        while to_check:
            val = to_check.pop()
            if val == b:
                valid=True
                break
            else:
                if val not in checked:
                    to_check.extend(bigger[val])
            checked.add(val)

        # Print if not valid.
        if not valid:
            print("contradiction")
            quit()

    # Add to the inequality
    if b not in bigger[a]:
        bigger[a].append(b)

# Print if all inequalities are valid.
print("consistent")
