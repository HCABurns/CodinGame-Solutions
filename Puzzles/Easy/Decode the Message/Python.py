# Get inputs.
p = int(input())
c = input()

# Ensure not 0 input.
if p==0:print(c[0]);quit()

# Get base and output.
base = len(c)
out = ""

# Continue until converted from base 10 to base len(c)
while p > 0:
    if out != "":
        p-=1 # Since aa = 4 instead of ba - Minus 1 each loop to set correct.
    
    # Regular base conversion
    rem = p % base
    out += c[rem]
    p //= base
    
# Output the conversion.
print(out)
