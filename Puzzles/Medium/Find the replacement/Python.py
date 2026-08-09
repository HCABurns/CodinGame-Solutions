# Get inputs.
x = input()
y = input()

# Map the changes needed for turning x into y.
hashmap = {}
for i in range(len(x)):
    if (x[i] in hashmap and hashmap[x[i]] != y[i]):
        print("CAN'T")
        quit()
    hashmap[x[i]] = y[i]

# Remove any equals pairs and print required output.
pairs = [a+b for a,b in hashmap.items() if a != b]
if pairs:
    print(*[f"{a}->{b}" for a,b in hashmap.items() if a != b] , sep="\n")
else:
    print("NONE")
