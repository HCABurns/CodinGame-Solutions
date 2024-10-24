# Get required inputs.
n = int(input())
s = input().split(" ")

# Check if the number is positive or negative. Also check if the number is a float or integer.
negative = False
decimal = False
if "-" in s:
    negative = True
if "." in s:
    decimal = True

#Sort numbers only smallest to largest.
vals = sorted([i for i in s if i.isnumeric()])

# If all values are 0 then print and quit.
if all(1 if i == "0" else 0 for i in vals):
    print(0)
    quit()

# If deciaml add deciaml.
if decimal:
    vals.insert(1,".")

# If negative add minus sign otherwise reverse the array.
if negative:
    vals = ["-"] + vals
else:
    vals = vals[::-1]
    
# Output the value.
x = float(''.join(vals))
print(int(x) if int(x) == x else x)
