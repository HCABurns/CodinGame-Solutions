# Get the input value.
n = input()

# Find the date by reversing the encryption.
for i in range(1, len(str(n))):
    # Split into a and b.
    v1 , v2 = int(n[:i]), int(n[i:])
    
    # Calculate v2 * v2
    val = int(v1)*int(v2)

    # Ensure that val translates to a valid date.
    val2 = str(val)
    d = val2[-2:].zfill(2)
    m = val2[len(val2)-4:len(val2)-2].zfill(2)
    y = val2[:len(val2)-len(m)-len(d)].zfill(4)
    if int(d) > 31 or int(m) > 12 or val == 0:
        continue
    
    # Find the closest factores of val.
    # Set flag to false if there exists closer factors than v1 and v2.
    closest_factors = True
    for i in range(int(val**0.5), 1, -1):
        if val % i == 0:
            if i not in {v1,v2}:
                closest_factors = False
            break

    # If v1 and v2 are the closest factors, print the formated date.
    if closest_factors == True:
        print(f"{y}-{m}-{d}")
