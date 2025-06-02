# Hashmap for storing values, array for storing order of keys.
keys = {}
order = []

n = int(input())
for i in range(n):
    # Get inputs.
    s = input().split()

    # Perfrom the correct operation.
    if s[0] == "SET":
        for item in s[1:]:
            name,value = item.split("=")
            
            if name not in keys:
                order += [name]
            keys[name] = value
    
    elif s[0] == "GET":
        res = []
        print(" ".join([keys.get(name,"null") for name in s[1:]]))

    elif s[0] == "KEYS":
        if len(keys) > 0:
            print(" ".join([name for name in order]))
        else:
            print("EMPTY")
    elif s[0] == "EXISTS":
        print(" ".join(["true" if name in keys else "false" for name in s[1:]]))
