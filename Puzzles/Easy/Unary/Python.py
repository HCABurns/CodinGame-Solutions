# Required variable. H[2]...H[-1] will also be used for an output.
h=["00","0"]
b=""
# Convert input to binary with exactly 7 characters (as required).
for c in input():
    b+=bin(ord(c))[2:].zfill(7)

# Iterate over binary string and add correct value to array.
for i in range(len(b)):
    # If first value or current value is not equal to the previous (i.e previous was 1 and val is 0) add correct identifier.
    if i==0 or b[i]!=previous:
        previous=b[i]
        h+=[h[int(previous)]]+[""]
    
    # Increment count by 1
    h[-1]+='0'

# Output the correct
print(" ".join(h[2:]))
