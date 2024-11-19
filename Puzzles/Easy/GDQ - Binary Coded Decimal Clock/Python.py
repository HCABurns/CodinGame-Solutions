# Create empty grid.
out = [list(["_____"]*6) for i in range(4)]

# Get times.
timer = input().split(":")
idx = 0
for i in range(4):
    # Get digits if possible.
    t1 = timer[i] if len(timer[i]) == 1 or i == 0 else timer[i][0]
    t2 = timer[i][1] if len(timer[i]) > 1 and i != 0 else None

    # Convert to binary.
    t1 = bin(int(t1))[2:].zfill(4)
    t2 = bin(int(t2))[2:].zfill(4) if t2 else None

    # Convert any 1s to "#####". Use idx to place into correct column.
    for j,val in enumerate(t1):
        if val == "1":
            out[j][idx]="#####"
    idx+=1
    
    if t2:    
        for j,val in enumerate(t2):
            if val == "1":
                out[j][idx]="#####"
        idx+=1
    
# Print Binary Coded Decimal Clock
for i in out:
    print("|"+"|".join(i)+"|")
